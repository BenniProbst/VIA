# PHASE 2: Repository-Analyse - Memory State

**Start**: 2025-10-22
**Vorherige Phase**: Phase 1 Research & Dokumentenanalyse ABGESCHLOSSEN
**Kontext**: Siehe `phase1_research/PHASE1_SUMMARY.md`

---

## Aufgabe für PHASE 2

Vollständige Analyse von 3 GitHub Repositories für:
1. OPC UA Research Playbook
2. AAS Research Playbook
3. Integration in VIA M3/M2/M1 Architektur

---

## Repositories zu analysieren

### 1. open62541 (C99 OPC UA Implementation)
- **URL**: https://github.com/open62541/open62541
- **Fokus**:
  - Architektur und API-Struktur
  - Client/Server Implementation
  - NodeSet Integration
  - Code-Beispiele für VIA

### 2. UA-Nodeset (OPC UA Standard NodeSets)
- **URL**: https://github.com/OPCFoundation/UA-Nodeset
- **Fokus**:
  - Standard NodeSet Definitionen
  - Companion Specifications
  - AAS NodeSet (für VIA relevant)
  - Custom NodeSet Creation

### 3. aas-core-works (AAS SDK & Tools)
- **URL**: https://github.com/aas-core-works
- **Fokus**:
  - AAS Metamodell M3 Definitionen
  - Python SDK (aas-core3.0-python)
  - C++ SDK (aas-core3.0-cpp)
  - Code-Generator (aas-core-codegen)

---

## Aus Phase 1: Kernerkenntnisse

### 1. VIA = Multi-Message Broker (MMB)
- Northbound: I4.0 Interface (OPC UA HTTP API)
- Southbound: Legacy Assets (Multi-Protocol)
- AID/AIMC Submodels für Mapping

### 2. VIA = Microservice Network (gRPC + Protobuf)
- One Microservice per VIA Process
- Code Generation: OpenAPI → Protobuf → C++/Python/Java
- Container Deployment (Docker + Kubernetes)

### 3. VIA = CMFM Domain
- M3/M2/M1 Generality Hierarchy
- VIA Services als CMFs
- Human-Centered Management

### 4. Hybrid Monitoring (SNMP + OPC UA + MQTT)
- SNMP: Lightweight Infrastructure
- OPC UA: Rich Process Data
- MQTT: Cloud Analytics

---

## TODO für Phase 2

### Aktueller Schritt:
1. ✅ PHASE2_MEMORY.md erstellt
2. ⏳ Research_AAS.md in phase2_research verschieben
3. ⏳ Repository-Analyse starten

### Nächste Schritte:
1. open62541 Repository analysieren
2. UA-Nodeset Repository analysieren
3. aas-core-works Repository analysieren
4. OPC UA Research Playbook erstellen
5. AAS Research Playbook finalisieren
6. VIA M3 Mapping dokumentieren

---

## Ordnerstruktur Phase 2

```
playbooks/
├── phase1_research/          ✅ ABGESCHLOSSEN
│   ├── PHASE1_SUMMARY.md
│   └── [alle research docs]
├── phase2_research/          ⏳ IN PROGRESS
│   ├── PHASE2_MEMORY.md      (diese Datei)
│   ├── Research_AAS.md       (zu verschieben)
│   ├── Research_OPC_UA.md    (zu erstellen)
│   ├── Research_open62541.md (zu erstellen)
│   ├── Research_UA_Nodeset.md (zu erstellen)
│   └── VIA_M3_Mapping.md     (zu erstellen)
└── TODO.md                   (aktualisiert)
```

---

## Verfügbare Tokens

**Start Phase 2**: ~73K Tokens
**Geschätzt benötigt**: 150-240K (50-80K pro Repo)
**Status**: Könnte knapp werden, effizient arbeiten!
