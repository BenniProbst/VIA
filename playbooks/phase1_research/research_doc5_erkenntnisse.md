# Erkenntnisse: CMFM Generality and Workflow (Santiago Olaya 2022)

## Quelle
Santiago Soler Perez Olaya, Martin Wollschlaeger
TU Dresden, Chair of Industrial Communications
IEEE 2022 INDIN Conference

## Kernkonzept: Comprehensive Management Function Model (CMFM)

### 1. Manager-Centric Paradigm
**Problem**: System-centric Management spiegelt die Komplexität des Systems
**Lösung**: Manager-centric Paradigm fokussiert auf Ziele statt auf System-Details

### 2. CMF Komponenten
**Mandatory**:
- **Goal**: Was soll erreicht werden
- **Output**: Was wird zurückgegeben

**Optional**:
- Input: Parameter für die CMF
- Constraints: Bedingungen/Einschränkungen
- Representations: Implementierungen für verschiedene Management-Systeme (Facade-Pattern)

### 3. Generality-Konzept (NEU!)
**Drei Ebenen**:
1. **Implementation**: Spezifisch für eine Implementierung
2. **User**: Für einen Benutzer über mehrere Implementierungen
3. **Domain**: Für eine ganze Wissensdomäne (z.B. HetIndNet, Autonomous Driving, Private 5G)

**Hierarchie**: Implementation → User → Domain → Parent Domain

### 4. Workflow für CMF-Erstellung

#### Stakeholder:
1. **Users**: Erstellen CMFs aus Scratch oder basierend auf existierenden
2. **Standardization Bodies**: Promotion von Vocabulary und CMF zu Core
3. **Standardization Bodies**: Konfliktlösung, Äquivalenzen, False Friends
4. **Users**: Nutzen nur existierende CMFs

#### Catalog vs Core:
- **Catalog**: Liste aller CMFs
- **Core**: Allgemein anwendbare CMFs nach Promotion
- **Promotion**: Von User-Generality → Domain-Generality durch Standardisierung

#### Vocabulary Management:
- Öffentlich zugängliches Repository (wie GitHub für Code)
- Verknüpfung mit e-Class, CDD, I4.0 SemanticID
- Tacit Promotion: Automatisch durch häufige Nutzung gleicher Terme
- Explicit Promotion: Durch Standardization Bodies

### 5. CMF-Interrelations
**Equivalence**: Gleiche Goal, gleichwertiger Input/Output → Merge
**Composition**:
- Upwards: Mehrere CMFs bilden zusammen höhere CMF
- Downwards: Große CMF kann in kleinere aufgeteilt werden

### 6. Beispiel-CMFs
- `live-list`: Liste lebender Nodes mit Network Addresses
- `topology`: Verfügbare Verbindungen im Netzwerk
- `post-fw-update`: Node nach Firmware-Update konfigurieren

### 7. Implementation in Industry 4.0
**Asset Administration Shell (AAS)**:
- CMFs als **Operations** im AAS Meta-Model
- Input/Output als Attributes
- Goal & Constraints als Expressions (Submodels)
- References zwischen CMFs für Taxonomie

### 8. Evaluation: CMFM vs Open Source vs Standardization

| Criteria | CMFM | Open Source | Standardization |
|----------|------|-------------|-----------------|
| Use readiness | ++ | +++ | + |
| Flexibility | +++ | ++ | + |
| Reliability | ++ | + | +++ |
| Coverage | +++ | + | +++ |
| Time to use | ++ | +++ | + |

**CMFM = Compromise**: Kombiniert Vorteile von Open Source (Flexibilität, schnell) und Standardization (Reliability, Coverage)

## Relevanz für VIA

### Direkter Bezug zu VIA-Projekt:
1. **M3 Metamodell** → CMFM Generality-Konzept übernehmen
2. **Service Registry/Orchestrierung** → CMF für Service Management
3. **Vocabulary Management** → Semantic Repository für VIA
4. **Multi-Layer (M3/M2/M1)** → Generality Hierarchy analog

### VIA-spezifische CMFs:
- `process-register`: Prozess im VIA Registry registrieren
- `process-discover`: Verfügbare Prozesse finden
- `route-message`: Message zum richtigen Prozess routen
- `schedule-task`: Task im VIA Scheduler einplanen

### Workflow für VIA:
1. **User-Level**: Developer erstellt CMFs für ihre Services
2. **VIA-Core**: Promotion häufig genutzter CMFs zu VIA-Core
3. **Domain-Level**: VIA als Domain für Prozesskommunikation

### AAS Integration:
- VIA Prozesse als AAS Assets
- VIA CMFs als AAS Operations
- VIA Semantic Model als AAS Submodel

## Offene Fragen für VIA
1. Wie mapping zwischen CMFM Generality und VIA M3/M2/M1?
2. GraphQL API für VIA CMF Repository?
3. AI-basierte CMF Discovery aus existierenden Scripts?
4. Integration mit OPC UA CMFs?
