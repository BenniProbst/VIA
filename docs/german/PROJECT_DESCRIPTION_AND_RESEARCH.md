# Exposé: Analyse eines Forschungsthemas - Prozesskommunikation

**Titel**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Autor**: Benjamin-Elias Probst
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Fakultät Informatik
**Datum**: Oktober 2025

---

[Das vollständige Exposé wurde aus playbooks/Analyse_eines_Forschungsthemas_Expose.md übernommen]

Für den vollständigen Inhalt siehe: `playbooks/Analyse_eines_Forschungsthemas_Expose.md`

Dieses Dokument beschreibt die VIA-Architektur als mehrstufige Compiler-Kette (M3→M2→M1) für heterogene Industriesysteme mit automatischer Orchestrierung von mehr als 50.000 Edge-Devices.

## Forschungsfokus

Der Fokus dieser Forschungsarbeit liegt auf dem **Process-Group-Protocol-Subsystem**:

> Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?

## Kernkomponenten

1. **VIA-M3-Compiler**: Metamodell → SDK
2. **VIA-M2-SDK-Compiler**: SDK → Kundensystem (mit IPC-Optimizer)
3. **VIA-M1-System-Deployer**: System → Produktion
4. **Sub-Protokolle unter OPC UA**: Edge-Group, Deploy, Process-Group

Siehe das vollständige Exposé in `playbooks/Analyse_eines_Forschungsthemas_Expose.md` für Details.
