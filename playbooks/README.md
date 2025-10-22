# VIA - Virtual Industry Automation: Projektbeschreibung

**Autor**: Benjamin Probst
**Institution**: Technische Universität Dresden, Fakultät Informatik
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya

---

## 1. Einleitung und Motivation

Nach ausführlicher Recherche des Asset Administration Shell (AAS) Projekts, insbesondere des Repositories von Santiago Soler Perez Olaya, wurde eine fundamentale Erkenntnis gewonnen: Die AAS-Architektur repräsentiert eine vollständige Compiler-Architektur mit Metamodell-Phasen (M3/M2/M1), vergleichbar mit den Arbeiten von Prof. Castrillon an der TU Dresden. Während die ursprüngliche Zielsetzung von AAS die Unterstützung der Industrie bei der Erfassung und Verarbeitung von Messdaten war, offenbart die Architektur das Potenzial für einen produktionsreifen Compiler.

Die derzeitige Implementierung in Form von Python-Skripten simuliert lediglich Compiler-Funktionalität, erreicht jedoch nicht den Status eines vollständigen, externen Übersetzerprogramms mit den etablierten Schichten eines Compilers. Das Projekt befindet sich auf Forschungslevel und bietet die Grundlage für eine produktionsreife Implementierung.

**VIA (Virtual Industry Automation)** adressiert diese Lücke durch die Entwicklung einer mehrstufigen Compiler-Kette, die automatisch wartbare Software für heterogene Industriesysteme generiert, deployed und orchestriert.

---

## 2. VIA-Architektur: Mehrstufige Compiler-Kette

Das VIA-System besteht aus drei Hauptphasen, die eine vollständige Compiler-Kette bilden:

### 2.1 VIA-M3-Compiler: Metamodell → SDK

**Zielsetzung**: Definition einer zweckgebundenen Programmiersprache aus AAS-Elementen (https://github.com/aas-core-works) und Erstellung eines vollständigen Compilers als statisches C++-Programm.

**Input**:
- AAS M3 Definitionen (Metamodell-Objekte und -Klassen)
- Benutzerbeschreibung des gewünschten Systems
- VIA-Extensions für Prozesskommunikation

**Verarbeitung**:
- C++20/C++23 Metaprogramming zur Laufzeitauswertung von M3-Modellen
- Template-Engine für Code-Generierung
- Constraint-Validation für Typensicherheit
- Vollständiges Testframework für alle Module

**Output**:
- VIA-M2-SDK in C++ (fokussiert, andere Sprachen optional)
- OPC UA NodeSet XML für Protokollimplementierung
- Protobuf-Definitionen für Microservice-Kommunikation
- Wartbare, versionierte Dokumentation

**Vorteile von C++**:
C++ wird als primäre Ausgabesprache gewählt, da C++20/23 eine umfassende Metaprogrammierebene bietet, die es ermöglicht, M3-Modelle statisch im Code zu definieren und zur Laufzeit effizient auszuwerten. Die generierten SDKs sind in Objekte und Klassen strukturiert, wartbar und vermeiden das "Spaghetti-Code"-Problem bisheriger Code-Generierungsansätze.

**Ausführung**:
```bash
./VIA-M3-Compiler --lang C++ --output ./output-sdk
```

Die Tests werden über Pipes in ein externes Testframework geleitet und auf Erfolg der Einzeltests und Schritte geparst.

---

### 2.2 VIA-M2-SDK-Compiler: SDK → Kundensystemprojekt

**Zielsetzung**: Die M2-SDK fungiert als erneuter Compiler, der die Syntax des Benutzerprojekts prüft, validiert und in ein vollständiges C++-Systemprojekt transformiert.

**Input**:
- Kundenprojekt in M3-Syntax (definiert durch VIA-M2-SDK)
- Netzwerk-Topologie
- Deployment-Ziele (Architekturen, Betriebssysteme)

**Verarbeitung**:

#### 2.2.1 Syntax-Prüfung und Tests
Durch die deterministisch begrenzten Einsatzkombinationen industrieller Anlagen können zur Kompilationszeit statische Tests implementiert werden, die die Features von M3 implementieren und perfekt testen. Das Testframework kann aufwendiger sein als die eigentliche Compiler-Implementierung.

#### 2.2.2 Network Discovery System
Ein innovatives Feature des M2-Compilers ist die automatische Netzwerkkartografie. Mit Erlaubnis des Kunden wird das Netzwerk gescannt, um:
- Edge-Geräte mit Messwertwandlern zu erkennen (SNMP, OPC UA, Modbus, MQTT, RPC)
- Angebotene und notwendige Schnittstellen auszulesen
- Geräteeigenschaften als Objekte für das Projekt anzubieten
- Vorschläge für die Implementierung zu unterbreiten

Diese Funktion unterstützt Kunden beim Einrichten, Ändern, Erweitern oder Löschen von Systemteilen.

#### 2.2.3 Prozesskommunikations-Optimierung
Der M2-SDK-Compiler analysiert Prozessabhängigkeiten und optimiert automatisch:
- **IPC-Mechanismus-Auswahl**: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging
- **Service-Positionierung**: Gleicher Container, gleicher Host oder Remote
- **Statische vs. Dynamische Entscheidung**: Compile-Time-Ranking mit optionaler Runtime-Entscheidung

**Output**:
- Vollständiges C++-Systemprojekt mit allen Gerätedefinitionen, Verbindungen und Gruppen
- Kubernetes-Manifests für Deployment
- Edge-Modules für verteilte Systeme
- Netzwerkprotokollimplementierungen
- Generierte Tests

**Modi**:
- **Release-Modus**: C++-Output-Stream wird über Memory-Filesystem (RAM) direkt in g++ mit Pipe kompiliert (Performance-Optimierung)
- **Debug-Modus**: Projektdateien mit überführter Dokumentation aus Kundenbeschreibung und M2-SDK

**Komplexität**:
Der Entwicklungsprozess ist vergleichbar mit dem Kompilieren von Xilinx FPGAs, da die Transformation der einzelnen Phasen hochgradig vielschichtig ist. Ein Dateiformat definiert, welcher C++-Code und welche Ausführungsprogramme bzw. Shared Libraries in welche Geräte deployed werden müssen.

---

### 2.3 VIA-M1-System-Deployer: Deployment und Orchestrierung

**Zielsetzung**: Das M1-Systemprojekt wird auf einen Kubernetes-Cluster und die Edge-Module ("Horses") deployed.

**Input**:
- M2-Systemprojekt
- Deployment-Targets (Architecture Map)
- Kundendefinierte Systemtests (grobe Vordefinition)

**Verarbeitung**:

#### 2.3.1 Distributed Compilation
- GitHub Runners werden für parallele Kompilation aller Module instanziiert
- Module, die skalieren (mehrfach deployed, einmal implementiert), werden nur einmal kompiliert, wenn Container- und Host-Betriebssystem identisch sind
- Cross-Compilation für heterogene Architekturen: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc
- Unterstützung für Linux, Windows, Mac

**Begründung Multi-Architektur-Support**:
Industriesysteme sind extrem heterogen. Die Unterstützung reicht von billigsten Edge-Minicomputern bis zu ausgefeilten Verarbeitungs-Servern. VIA muss sowohl die Industrie der Zukunft als auch Legacy-Systeme der Vergangenheit unterstützen.

#### 2.3.2 Horse-Rider-Deployment
Ein innovatives Deployment-Modell, bei dem:
- **Horse-Service**: Deployment-Service als Container läuft
- **Rider-Service**: Fachlogik-Programm wird vom Horse-Service als Prozess ausgeführt
- **Hot-Reload**: C++23 Modules mit stabilen ABIs ermöglichen Canary Deployment
- **Redundanz (Digital Twin)**: Mindestens 2 parallele Mikroservices pro Edge-Gerät für Ausfallsicherheit
- **Rollback**: Sekundenbruchteile bei Fehler durch Vorhalten der alten Version

Vorteil: Systemmodule können aus Arbeitsspeicher, Festplatte oder Remote-System geladen und im laufenden Betrieb ersetzt werden.

#### 2.3.3 Generierte Systemtests
Das System wird darauf getestet, dass:
- Alle Protokolle in ihrer Konstellation Befehle senden und empfangen können
- Zustandsbasiertes Verhalten korrekt ist
- Einzelapplikationen nach Kundenspezifikationen funktionieren
- Alle öffentlichen Interfaces getestet sind (Verpflichtung für Kunden)
- Prozessketten der Module und Netzwerk-Services korrekt funktionieren

Tests werden über das Deploy-Protocol orchestriert, um Gegenstellen auf Testläufe vorzubereiten. Die sicherste Variante sind Tests unter echten Betriebsbedingungen. Optional kann ein Deployment-Service in normale Microservices einkompiliert werden, um erweiterte Prozesskommunikation zu testen.

**Output**:
- Deployed System für >50.000 Edge-Geräte
- Digital Twin mit Monitoring und Logging
- Master Active Management für Orchestrierung

---

## 3. Protokoll-Architektur: Sub-Protokolle unter OPC UA

Die gemeinsame Sprache des Systems ist OPC UA (IEC 62541, https://de.wikipedia.org/wiki/OPC_Unified_Architecture). VIA erweitert OPC UA durch drei Sub-Protokolle, die verschiedene Kommunikationsebenen trennen:

### 3.1 Edge-Group-Protocol
- **Funktion**: Virtuelle Netzwerkgruppen für Edgegeräte
- **Vorteil**: Vermeidung einzelner Koordination, Gruppierung von Zielen
- **Sicherheit**: Hardcoded Messages für Effizienz (kein Runtime-Code-Change)
- **Performance**: Kein virtueller Router notwendig (Zeitkritikalität gewahrt)

Gruppeneigenschaften werden in das fertige System kompiliert, Binary ABIs werden stabil gehalten, sodass jedes Edge-Gerät selbst weiß, wohin es gehört.

### 3.2 Deploy-Protocol
- **Funktion**: Verwaltung, Versionierung, Systemupdates, Rejuvenation
- **Separation**: Metadaten und Messdaten der Computer getrennt von Anlagendaten (Kapselung)
- **Logging**: Netzwerk-Logs für Fehleranalyse
- **Horse-Rider-Integration**: Protokollverwaltung durch Deployment-Service

### 3.3 Process-Group-Protocol
- **Funktion**: Transparente Prozesskommunikation zwischen Services
- **IPC-Mechanismen**: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging
- **Automatisierung**: M2-SDK-Compiler erstellt automatisch Prozessketten von Mikroservices
- **Optimierung**: Auswahl des IPC-Mechanismus basiert auf M3-Objektmodellen und deren Kombination
- **Cluster-Verteilung**: Virtuelle Weiterverarbeitung oder Gliederung in Unteraufgaben auf anderen Containern/Maschinen

**Windows-Limitation**: Auf Windows sind die IPC-Möglichkeiten begrenzter.

### 3.4 MMB-Integration (Multi-Message Broker)
Die Sub-Protokolle können nach dem MMB-Ansatz von Dr. Soler Perez Olaya betrieben werden:
- Many-to-Many Broadcast im Netzwerk
- Definierte Sicherheitsstufen
- Paket-Ankunftssicherheit

---

## 4. Master Active Management

**Zielsetzung**: Redundante Deployment-Orchestrierung analog zu Kubernetes, speziell für VIA-Edge-Services.

**Architektur**:
- **Active/Active-Redundanz**: Analog zu Active Directory Domäne
- **Konfiguration**: Redundanz-Levels, Service-Verteilung
- **Zugriffskontrolle**: Rollen und Benutzer für Administratoren
- **Integration**: Eigene Lösung oder Samba/Microsoft Active Directory

Der Master-Service muss konfigurierbar sein bezüglich Redundanz-Häufigkeit und Positionierung.

---

## 5. Kubernetes-Integration und Deployment-Strategie

**Verhältnis zu Kubernetes**:
- **Kubernetes**: Deployed einfache Services (Standard-Container, Docker)
- **VIA**: Deployed C++23 Modules für Edge-Geräte, Protokollübersetzungen, spezielle Speicher- und Netzwerk-Services

**Socket-Kommunikation**:
Kubernetes-Container kommunizieren über Sockets, wenn deployte Systemanwendung vom Update-/Deployprogramm getrennt ist.

**Service-Trennung**:
Deployment-Service (Horse) ist optional:
- **Mit Deployment-Service**: Horse-Service startet mit Grundmodul, erhält Rider-Service von Master Active Management, startet Rider-Service
- **Ohne Deployment-Service**: Microservice wird als Startservice im paketierten Betriebssystem registriert

**Cluster-Übergreifend**:
OPC UA wird auch zwischen Kubernetes-Clustern verwendet (z.B. VPN zwischen Standorten), um komponentenbasierte Aufgliederung der Services zu ermöglichen.

---

## 6. Skalierbarkeit und Performance

**Zielsystem**: >50.000 Edge-Geräte

**Performance-Optimierungen**:
- **Hardcoded Messages**: Effizienter als dynamische Routing-Entscheidungen
- **Compile-Time-Entscheidungen**: Statisches Ranking der IPC-Mechanismen
- **Optional Runtime-Entscheidung**: Dynamische Methodenauswahl bei Bedarf
- **Keine virtuellen Router**: Vermeidung von Performance-Overhead bei Zeitkritikalität
- **Binary ABI-Stabilität**: C++23 Modules mit stabilen Schnittstellen
- **Distributed Compilation**: Parallele Builds aller Module
- **Sicherheit durch Statik**: Quellcode kann zur Laufzeit nicht verändert werden (Fokus auf Deployment-Server-Sicherheit)

**Speicher-Effizienz**:
- Memory-Filesystem (RAM) für Release-Modus
- Direkte Pipe zu g++ (Performance-Steigerung)

---

## 7. Vision: Industrie 5.0 und KI-Integration

Zukünftig wird die Industrie 5.0 durch KI-gesteuerte Systembeschreibung charakterisiert:

1. **Natürlichsprachliche Beschreibung**: Kunde beschreibt System per Spracheingabe oder Text
2. **KI-Modell**: Übersetzt Beschreibung in M3-Compiler-Anforderungen
3. **Compiler-Kette**: M3 → M2 → M1 generiert vollständiges System
4. **Software-in-the-Loop**: Iterative Fehlerkorrektur gegen Kundenspezifikation bis System funktioniert
5. **Vollautomatisches Deployment**: Von Beschreibung bis zum laufenden System

**Demonstration**:
Das Konzept wird demonstriert durch manuelle Testservices, die zufällige Daten generieren, welche vom VIA-System automatisch abgefangen werden. Das System setzt Anforderungen über ein KI-Modell um und iteriert den Projektprozess, bis das gewünschte Debugergebnis auf der Konsole erscheint.

**Meilenstein**:
"M3 mit sich selbst definieren" – Ähnlich wie KI-Modelle heute noch manuell aufgebaut, trainiert und zusammengesteckt werden, schließt VIA den Kreis durch automatische M3-Definition über M3. Dies ist ein Meilenstein in der Forschung.

---

## 8. Technische Spezifikationen

### 8.1 Programmiersprachen und Frameworks
- **C++20/23**: Metaprogramming, Modules, stable ABIs
- **gRPC + Protobuf**: Microservice-Kommunikation (Contract-First, Binary Serialization)
- **OPC UA**: IEC 62541, open62541 (C99 Implementation)
- **Kubernetes**: Container-Orchestrierung
- **CMake**: Build-System, Multi-Architektur-Konfiguration

### 8.2 Unterstützte Architekturen
- **CPU**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc
- **OS**: Linux, Windows, Mac
- **Edge-Devices**: Billigste Minicomputer bis High-End-Server

### 8.3 Protokolle
- **Industrial**: SNMP, OPC UA, Modbus, MQTT, RPC
- **IPC**: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging
- **VIA-Sub-Protocols**: Edge-Group, Deploy, Process-Group

---

## 9. Forschungsfokus für TU Dresden

Während VIA als Gesamtsystem alle beschriebenen Komponenten umfasst, konzentriert sich die Forschungsarbeit an der TU Dresden auf das **Process-Group-Protocol-Subsystem**:

**Forschungsfrage**:
> Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC) bei der Kompilation optimiert wird?

**Teilfragen**:
1. Welche M3-Modellelemente sind notwendig, um Prozesskommunikation zu beschreiben?
2. Wie kann der M2-SDK-Compiler aus Prozessabhängigkeiten optimale IPC-Mechanismen ableiten?
3. Welche Metriken bestimmen die Positionierung (gleicher Container, gleicher Host, Remote)?
4. Wie verhält sich das Process-Group-Protocol unter OPC UA bei >50.000 Geräten?

**Hypothesen**:
- **H1**: Compiler-basierte IPC-Optimierung reduziert Latenz um >30% gegenüber Runtime-Service-Mesh
- **H2**: Statische Positionierungsentscheidung (Compile-Time) erreicht 90% der Effizienz dynamischer Orchestrierung
- **H3**: Process-Group-Protocol skaliert linear bis 100.000 Services bei hierarchischer Gruppierung
- **H4**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um 60%

Die M3/M2/M1-Architektur dient als theoretischer Kontext und Rahmen, innerhalb dessen das Prozesskommunikations-Subsystem entwickelt und evaluiert wird.

---

## 10. Projektstruktur

```
playbooks/
├── README.md (dieses Dokument)
├── TODO.md
├── Analyse_eines_Forschungsthemas_Expose.md
├── phase1_research/ (✅ Abgeschlossen: AAS, OPC UA, CMFM)
├── phase2_research/ (✅ Abgeschlossen: GitHub-Repositories)
├── VIA-M3-Compiler/
│   ├── implementation/
│   └── testsystem/
├── VIA-M2-SDK/
│   ├── implementation/
│   └── testsystem/
└── VIA-M1-System-Deploy/
    ├── implementation/
    └── testsystem/
```

---

## 11. Literatur und Quellen

### Standards
- IEC 63278 (2024): Asset Administration Shell
- IEC 62541 (2020): OPC Unified Architecture
- ISO/IEC 20922 (2016): MQTT Protocol

### Open-Source Projekte
- aas-core-works: https://github.com/aas-core-works
- open62541: https://github.com/open62541/open62541
- OPC Foundation UA-Nodeset: https://github.com/OPCFoundation/UA-Nodeset

### Forschungsarbeiten
- Soler Perez Olaya, S. & Wollschlaeger, M. (2022): CMFM Generality Hierarchy
- Soler Perez Olaya, S. et al. (2019): CMFM for Heterogeneous Industrial Networks
- Soler Perez Olaya, S. (2019): Role of CMFM in Network Management. PhD Thesis, TU Dresden

---

## 12. Status und nächste Schritte

**Status**:
- ✅ Phase 1: Research & Analyse (AAS, OPC UA, IPC) abgeschlossen
- ⏳ Phase 2: Playbook-Erstellung & M3-Metamodell-Design in Arbeit
- 📋 Phase 3: M2-SDK-Compiler Prototyp mit IPC-Optimizer
- 📋 Phase 4: Benchmark-Suite & Use-Case-Implementierung
- 📋 Phase 5: Evaluation & Vergleichsmessungen
- 📋 Phase 6: Dokumentation & Publikation

**Nächste Schritte**:
1. Finalisierung der Playbook-Struktur
2. M3-Modellelemente für Prozesskommunikation definieren (AAS-Extension)
3. Graph-basierter Optimierungsalgorithmus für IPC-Mechanismus-Auswahl
4. Prototypische Implementierung des M2-SDK-Compilers mit IPC-Optimizer

---

**Letzte Aktualisierung**: Oktober 2025
