# Memory Reconstruction - Benjamins Anfragen aus TODO.md

## Ursprüngliche Anfrage (Me):
"Bitte bearbeite die riesen Aufgabe in den Playbooks im README."

## Benjamins Antworten auf meine 6 Fragen:

### Zu 1. Forschungsdokumente:
✅ **BESTÄTIGT**: "Alle Dokumente sind entscheidend"
✅ **WICHTIG**: "im Unterordner ChatGPT findest du noch allgemeine Forschung"
✅ **OPTIONAL**: "5G Artikel vielleicht nicht ganz so wichtig"
✅ **KEINE EINSCHRÄNKUNGEN**: "Ich gebe dir KEINE Einschränkungen dazu"
✅ **ZUSATZ-AUFGABE**: "Bitte aktualisiere '20251015 Antrag_Aufgabenstellung_AnalyseForschungsthema_Probst.docx'"
✅ **ZUSATZ-AUFGABE**: "erstelle separat ein Expose zum Thema"

### Zu 2. AAS Repository:
✅ **BESTÄTIGT**: "Ja das sollst du bitte ALLES tun, alle 3 Punkte"
- Metamodell-Definitionen (M3) analysieren
- Python SDK Implementierungen reviewen
- Spezifikationen für C++ Compiler extrahieren
✅ **ZUSATZ**: "Sammle die Modelle und Objekte und lege auch dafür ein Playbook an"

### Zu 3. OPC UA Integration:
✅ **BESTÄTIGT**: "Du musst tatsächlich die beiden, die du genannt hast vollständig analysieren"
- https://github.com/OPCFoundation/UA-Nodeset
- https://github.com/open62541/open62541
✅ **GRUND**: "weil diese das OPC UA Protokoll schon implementieren"
✅ **ZIEL**: "wir benötigen einige Playbooks über deren Struktur und genaue Funktionalität"

### Zu 4. Projektstruktur:
✅ **KLARGESTELLT**: Korrigierte Struktur:
```
VIA/
├── playbooks/
│   ├── README.md (existiert)
│   ├── Main_System_playbook_DAYXX.md (erste Ebene)
│   ├── VIA-M3-Compiler/
│   │   ├── implementation/
│   │   │   └── M3_implementation_playbook_DAYXX.md
│   │   └── tests/
│   │       └── M3_tests_playbook_DAYXX.md
│   ├── VIA-M2-SDK/
│   │   ├── implementation/
│   │   └── tests/
│   └── VIA-M1-System-Deploy/
│       ├── implementation/
│       └── tests/
├── VIA-M3-Compiler/ (später generiert, .gitignore)
├── VIA-M2-SDK-C++/ (später generiert, .gitignore)
├── VIA-M1-System-Deploy-C++/ (später generiert, .gitignore)
├── tests/
└── docs/
```

### Zu 5. Research-Priorität:
✅ **WAHL A**: "Zuerst Uni-Dokumente lesen + Web-Research + Strukturierung → dann Playbooks erstellen"
✅ **ZUSATZ**: "strukturierst du gesammelte Informationen und arbeitest research playbooks aus"
✅ **WORKFLOW**: "research playbooks → dann in output_playbooks_DAYXX einfließen"
✅ **PARALLEL**: "In die output playbooks arbeitest du parallel research ein"

### Zu 6. Exposé-Erstellung:
✅ **VORLAGE**: "C:\Users\benja\OneDrive\Dokumente\Firmensachen\BEP Venture UG\Projekte\CELM\docs\*rev11e.docx"
✅ **TIMING**: "Den Research musst du dafür gemacht haben, um das zu bearbeiten"
✅ **ABLAGE**: "als separates Dokument unter docs/"
✅ **ZUSATZ**: "Stichpunkte auf eine Seite für Projektanmeldung"
✅ **WORKFLOW**: "Das Expose kann erst aus den Playbooks entstehen"

## Benjamins Kritik nach erstem Versuch:
❌ "du hast Dinge getan, wie Head 8000 verwendet und auch nicht wirklich ALLE Dokumente gelesen"
✅ "Bitte hole das kleinschrittig nach"

## Benjamins Bestätigung:
✅ "Der Rest stimmt perfekt, ich bestätige den Antrag an dich"
✅ "Bitte arbeite ohne Einschränkungen automatisch weiter"

## Was ich bisher WIRKLICH gemacht habe:
✅ 4 Dokumente vollständig gelesen (keine head-Limits):
   - 20251015 Antrag
   - d1-02 (SOA Communication)
   - CMFM Generality (Santiago 2022)
   - CMFM HetIndNets (Santiago 2019)
✅ Erkenntnisse dokumentiert in 4 Markdown-Dateien
✅ Fortschritt in TODO.md dokumentiert

## Was noch FEHLT (gemäß Benjamins Anfragen):

### 1. ChatGPT Unterordner NICHT gelesen:
❌ Funktionsweise von OPC UA
❌ SCADA-, MES- und OPC UA-Server
❌ SNMP in der Industrie 4.0
❌ Typische SNMP-MIB-Objekte

### 2. Weitere Santiago Papers NICHT gelesen:
❌ Dynamic Multi-Message Broker for Industry 4.0 Digital Twins
❌ Service-Oriented Architecture for I4.0 Digital Twins
❌ The role of comprehensive function models (frühere Version)

### 3. Exposé NICHT gelesen:
❌ 20251014 Expose Analyse eines Forschungsthemas - Prozesskommunikation Probst.docx

### 4. AAS Repository NICHT analysiert:
❌ aas-core-works Metamodell M3
❌ Python SDK Implementation
❌ C++ Compiler Specs
❌ Playbook für AAS Modelle/Objekte

### 5. OPC UA Repositories NICHT analysiert:
❌ UA-Nodeset Strukturdefinitionen
❌ open62541 C99 Implementation
❌ Playbooks über Struktur und Funktionalität

### 6. Research Playbooks NICHT erstellt:
❌ OPC UA Research Playbook (open62541 + NodeSets + M3 Mapping)
❌ CMFM Research Playbook (alle Santiago Papers)
❌ Prozesskommunikation Playbook (Forschungsantrag)
❌ AAS Research Playbook

### 7. Output Playbooks NICHT erstellt:
❌ Main_System_playbook_DAY01.md
❌ M3/M2/M1 implementation playbooks
❌ M3/M2/M1 tests playbooks

### 8. Exposé NICHT erstellt:
❌ Nach CELM-Vorlage
❌ Unter docs/

### 9. Antrag NICHT aktualisiert:
❌ Auf 1 Seite Stichpunkte für Projektanmeldung

## Meine nächsten Schritte (korrekte Reihenfolge):

### PHASE 1: Dokumente vervollständigen
1. ✅ ChatGPT Unterordner lesen (OPC UA + SNMP) - **HÖCHSTE PRIORITÄT für OPC UA Playbook**
2. ✅ Weitere Santiago Papers lesen
3. ✅ Exposé lesen (als Referenz)

### PHASE 2: Repository-Analyse
4. ✅ AAS Repository vollständig analysieren
5. ✅ OPC UA Repositories vollständig analysieren

### PHASE 3: Research Playbooks erstellen
6. ✅ OPC UA Research Playbook
7. ✅ AAS Research Playbook
8. ✅ CMFM Research Playbook (alle Santiago Papers)
9. ✅ Prozesskommunikation Research Playbook

### PHASE 4: Output Playbooks erstellen
10. ✅ Main_System_playbook_DAY01.md
11. ✅ M3/M2/M1 implementation/tests playbooks

### PHASE 5: Dokumentation
12. ✅ Exposé nach CELM-Vorlage erstellen
13. ✅ Antrag auf 1 Seite aktualisieren

## Was für "OPC UA Research Playbook" noch fehlt:
1. ❌ ChatGPT OPC UA Dokumente (Funktionsweise, SCADA/MES/OPC UA-Server)
2. ❌ UA-Nodeset Repository Analyse
3. ❌ open62541 Repository Analyse
4. ❌ M3 Mapping zwischen OPC UA und VIA
