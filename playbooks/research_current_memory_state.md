# Research Memory State - Live Snapshot

**Zeitpunkt**: 2025-10-22, Token-Stand: ~84K/200K (42%)
**Status**: Option A - Weitermachen mit Papers 8+9

---

## Vollständig gelesene Dokumente (7 von 12)

### ✅ Bereits gelesen und analysiert:

1. **doc1_20251015_antrag.txt** (27 Absätze)
   - Forschungsantrag Prozesskommunikation
   - Erkenntnisse: Implizit in Zusammenfassung

2. **doc3_d1-02.txt** (475 Absätze)
   - SOA Communication Management in Automotive
   - Erkenntnisse: research_doc3_erkenntnisse.md

3. **doc5_cmfm_1.txt** (6 Seiten, 563 Zeilen)
   - CMFM Generality & Workflow (Santiago 2022)
   - Erkenntnisse: research_doc5_erkenntnisse.md

4. **doc6_cmfm_2.txt** (6 Seiten, 360 Zeilen)
   - CMFM Applied to HetIndNets (Santiago 2019)
   - Erkenntnisse: research_doc6_erkenntnisse.md

5. **doc_chatgpt_1.txt** (7 Seiten)
   - OPC UA Funktionsweise
   - Erkenntnisse: research_doc_opcua_1_erkenntnisse.md

6. **doc_chatgpt_2.txt** (6 Seiten)
   - SCADA, MES, OPC UA Server + SNMP
   - Erkenntnisse: research_doc_scada_mes_erkenntnisse.md

7. **doc_santiago_7.txt** (8 Seiten)
   - Dynamic Multi-Message Broker (IEEE 2024)
   - Erkenntnisse: research_santiago_7_mmb_erkenntnisse.md

---

## Aktuell in Bearbeitung (TODO Status)

### ⏳ JETZT: Santiago Papers 8+9
- **doc_santiago_8.txt** (6 Seiten) - SOA for I4.0 Digital Twins
- **doc_santiago_9.txt** (4 Seiten) - Role of CMFM (frühe Version)

### ⏭️ Übersprungen (Redundanz):
- **doc_chatgpt_3.txt** (508 Zeilen) - SNMP Industrie 4.0
- **doc_chatgpt_4.txt** (315 Zeilen) - SNMP MIB Objekte
- **Grund**: SNMP bereits umfassend in doc_chatgpt_2 behandelt

---

## Noch ausstehende Aufgaben (nach Papers 8+9)

1. ⏳ open62541 GitHub Repository analysieren
2. ⏳ UA-Nodeset GitHub Repository analysieren
3. ⏳ VIA OPC UA M3 Mapping erarbeiten
4. ⏳ OPC UA Research Playbook erstellen (Synthese)

---

## Erkenntnisse-Dateien bisher erstellt (7 Dateien)

1. research_doc3_erkenntnisse.md - SOA Communication
2. research_doc5_erkenntnisse.md - CMFM Generality
3. research_doc6_erkenntnisse.md - CMFM HetIndNets
4. research_doc_opcua_1_erkenntnisse.md - OPC UA Funktionsweise
5. research_doc_scada_mes_erkenntnisse.md - SCADA/MES/OPC UA/SNMP
6. research_santiago_7_mmb_erkenntnisse.md - Multi-Message Broker
7. research_step1_zusammenfassung.md - Gesamtübersicht (erste 4 Docs)

---

## Meta-Dateien erstellt (5 Dateien)

1. research_step1_progress.md - Fortschrittstracking
2. research_memory_reconstruction.md - Benjamins Anfragen rekonstruiert
3. research_step1_remaining_docs.md - Liste fehlender Dokumente
4. research_step1_final_status.md - Status nach erstem Durchlauf
5. research_current_memory_state.md - DIESER SNAPSHOT (Live)

---

## Kernerkenntnisse akkumuliert

### 1. OPC UA (docs 1, 5, 6)
- M3/M2/M1 Architektur = VIA Compiler-Basis
- Address Space, ModelCompiler, Companion Specs
- open62541 (C99), Unified Automation (C++)
- Multi-Language: python-opcua, .NET, Java

### 2. CMFM (docs 5, 6)
- Manager-Centric Paradigm
- Generality Hierarchy: Implementation → User → Domain
- VIA = Domain, VIA Services = CMFs
- Catalog vs Core (Promotion)

### 3. Control Plane (doc 3)
- Data Plane: IPC Mechanisms
- Control Plane: Registry, Orchestration, Scheduling
- Management Plane: CMFM

### 4. ISA-95 Levels (doc 2)
- Level 2 (SCADA): VIA Core
- Level 3 (MES): VIA Orchestrator
- OPC UA als Vermittler

### 5. MMB Konzept (doc 7) **NEU!**
- Northbound (NB): I4.0 Ecosystem (OPC UA HTTP API)
- Southbound (SB): Legacy Assets (Multi-Protocol)
- AID/AIMC Submodels für Mapping
- Sync/Async Translation
- VIA = MMB Architecture!

---

## VIA Mapping Stand

### VIA ↔ OPC UA
- VIA Services = OPC UA Servers
- VIA Registry = OPC UA Discovery
- VIA Router = OPC UA Aggregation Server
- VIA Informationsmodell = OPC UA M2 Layer
- VIA Compiler = OPC UA ModelCompiler

### VIA ↔ MMB **NEU!**
- VIA = Multi-Message Broker
- VIA Processes = Legacy Assets (Brownfield)
- VIA Registry = AAS Storage
- VIA IPC = Southbound Protocols
- VIA OPC UA API = Northbound Interface
- VIA Mapping Layer = Data Transformation

### VIA ↔ CMFM
- VIA = Domain
- VIA Services = CMFs
- M3/M2/M1 = Generality Hierarchy
- VIA Vocabulary: Process, Service, Registry, Scheduler, Router

---

## Nächste Schritte (JETZT)

1. ✅ Memory State gesichert (diese Datei)
2. ⏳ TODO.md aktualisieren
3. ⏳ Santiago Paper 8 lesen (6 Seiten)
4. ⏳ Santiago Paper 9 lesen (4 Seiten)
5. ⏳ Erkenntnisse dokumentieren
6. ⏳ Finalen Status updaten

**Danach**: Token-Check → falls genug: SNMP Docs, sonst: Stoppen für Repository-Analyse

---

## Token-Management Strategie

- **Aktuell**: ~84K/200K (42%)
- **Paper 8**: ~15K Tokens geschätzt
- **Paper 9**: ~10K Tokens geschätzt
- **Erkenntnisse**: ~5K Tokens geschätzt
- **Total erwartet nach Papers 8+9**: ~114K/200K (57%)

**Verbleibend nach Papers 8+9**: ~86K Tokens
- **Genug für**: SNMP Docs (2x ~15K = 30K) → Total ~144K (72%)
- **NICHT genug für**: Repository-Analyse (geschätzt 50-80K pro Repo)

**Plan**: Nach Papers 8+9 + SNMP Docs → STOPPEN für neuen Token-Reset vor Repository-Analyse
