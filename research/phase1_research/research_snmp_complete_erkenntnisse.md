# Erkenntnisse: SNMP in Industrie 4.0 (Vollständig)

## Quellen
- doc_chatgpt_3.txt (10 Seiten) - SNMP in Industrie 4.0 Überwachung
- doc_chatgpt_4.txt (7 Seiten) - Typische SNMP-MIB-Objekte

---

## SNMP Architektur (Manager-Agent-Model)

### Polling (Pull)
- **Manager**: Sendet GET-Anfragen (UDP Port 161)
- **Agent**: Antwortet mit GET-RESPONSE
- **Zyklisch**: Regelmäßige Abfragen (z.B. alle 60s)

### Traps (Push)
- **Agent**: Sendet unaufgefordert bei Ereignissen (UDP Port 162)
- **Fire-and-Forget**: Unbestätigt (außer Inform in SNMPv2)
- **Proaktiv**: Kritische Zustände sofort melden

### MIB (Management Information Base)
- **Hierarchische OID-Struktur**: z.B. .1.3.6.1.2.1.2.2.1.8
- **Standard-MIBs**: MIB-II, IF-MIB, HOST-RESOURCES-MIB, ENTITY-SENSOR-MIB
- **Private/Enterprise-MIBs**: Vendor-spezifisch (z.B. Cisco, Hirschmann, WAGO)

---

## Industrie 4.0 Einsatzszenarien

### 1. IIoT-Gateways Überwachung
**Beispiel**: 100+ Schweißroboter-Gateways (Automobilfertigung)
- Temperatur, Spannungswerte, Modbus-TCP Fehlerrate
- ML-Modell → Predictive Maintenance
- **Ergebnis**: 60% weniger ungeplante Stillstände

### 2. Industrielle Netzwerkkomponenten
**TSN-Switches, Profinet-Switches**:
- IF-MIB: Portzustände, Bandbreite, Fehlerraten
- gPTP-Status (Synchronisation)
- QoS-Pufferzustände
- Automatische Topologie-Erkennung (LLDP via MIB)

### 3. Server Überwachung
**SCADA, MES, OPC UA Server**:
- CPU, RAM, Netzwerk-Interface, Temperatur
- **Parallel**: OPC UA für Prozessdaten, SNMP für Hardware-Status
- **Trend**: Neue Geräte (Beckhoff, Bosch Rexroth) setzen auf OPC UA statt SNMP

### 4. Umgebungs- und Energie-Monitoring
**Smart Meter, USV, Klimakontroller**:
- Leistungsaufnahme, Batteriespannung, Temperatur/Feuchtigkeit
- **Beispiel**: 15% Energieeinsparung durch dynamische Laststeuerung

---

## Wichtige MIB-Module

### ENTITY-SENSOR-MIB (RFC 3433)
- **OID**: .1.3.6.1.2.1.99
- **Sensoren**: Temperatur, Spannung, Strom, Lüfterdrehzahl
- **Datentyp**: Integer mit Einheitentyp (celsius(8)) + Skalierung
- **Beispiel**: 0–100°C mit 0,1° Auflösung → Wert 0–1000

### HOST-RESOURCES-MIB (RFC 2790)
- **CPU**: hrProcessorLoad (.1.3.6.1.2.1.25.3.3.1.2) in %
- **RAM**: hrMemorySize, hrMemoryUsed
- **Datentyp**: Integer32, Gauge32

### IF-MIB (RFC 2863)
- **OID**: .1.3.6.1.2.1.2
- **Netzwerk-Interfaces**: Speed, Status, Bytes (ifInOctets/ifOutOctets)
- **Errors**: ifInErrors, ifOutErrors
- **Datentyp**: Counter32/64, Gauge32
- **Steuerbar**: ifAdminStatus (Port up/down setzen)

### ALARM-MIB (RFC 3877)
- **alarmActiveTable**: Aktive Alarme mit Schweregrad
- **Severity**: minor=10, major=20, critical=30
- **Historie**: alarmHistoryTable

### DISMAN-EVENT-MIB
- **OID**: .1.3.6.1.2.1.88
- **Framework**: mteTrigger für Schwellwerte (z.B. Temperatur > 70°C)
- **Aktion**: Trap senden ODER OID setzen

---

## Vendor-spezifische MIBs

### Hirschmann (Industrial Ethernet Switches)
- **Enterprise-ID**: 248
- **Temperatur**: hmTemperature (Integer32 in °C)
- **Schwellwerte**: hmTempUprLimit, hmTempLwrLimit
- **Trap**: hmTemperatureTrap bei Überschreitung
- **Flow Control**: hmIfaceFlowControl (aktivieren/deaktivieren per Port)

### Cisco (CISCO-ENVMON-MIB)
- **Temperatur**: ciscoEnvMonTemperatureStatusTable
- **Traps**: ciscoEnvMonTemperatureNotification bei Übertemperatur
- **Lüfter**: ciscoEnvMonFanNotification bei Ausfall

### WAGO (Ethernet-Koppler)
- **Analoge Eingänge**: Gauge32 oder skalierter Integer
- **Digitale Eingänge**: INTEGER (0/1) oder Bitfeld (16-Bit für 16 Kanäle)
- **Private MIB**: Prozessdaten direkt per SNMP

### Moxa ioLogik (Remote I/O)
- **I/O-MIB**: Jede Klemme als OID
- **Analog**: Integer, Digital: 0/1
- **Steuerbar**: Digitalausgänge per SNMP-Set

### Siemens (PROFIBUS, SCALANCE)
- **RUN/STOP-Status**: SIMATIC-CPU als Enum
- **PROFINET-Alarm**: SNMP-Trap bei Nachbar-Ausfall

---

## SNMP-Versionen und Sicherheit

### SNMPv1 (1988) & SNMPv2c (1993)
**Community-String** (Klartext):
- Standard: "public" (read), "private" (write)
- **Unsicher**: Unverschlüsselt übertragen
- **Risiko**: Abhören, unberechtigter Zugriff
- **Nur für**: Isolierte Intranets, niemals öffentlich

### SNMPv3 (2002)
**User-Based Security Model (USM)**:
- **Authentication**: HMAC-SHA oder HMAC-MD5
- **Privacy**: AES oder DES Verschlüsselung
- **Security Levels**:
  - noAuthNoPriv (keine Auth, keine Verschlüsselung)
  - authNoPriv (mit Auth, ohne Verschlüsselung)
  - **authPriv** (mit Auth + Verschlüsselung) → **EMPFOHLEN**
- **View-Based Access Control**: Feingranulare OID-Zugriffssteuerung

### Best Practices
- **Default-Communities deaktivieren** ("public" ändern/abschalten)
- **SNMPv3 authPriv** in Produktion
- **Netzwerksegmentierung**: SNMP nur über Management-VLAN/VPN
- **Access Lists**: Nur legitime Manager-IPs erlauben
- **IPsec/SSH-Tunnel**: Zusätzliche Transport-Sicherung
- **Auditing**: SNMP-Zugriffslogs überwachen

---

## SNMP Datentypen und Empfehlungen

### Gauge32/Integer32 → Kontinuierliche Werte
- **Use-Case**: Temperatur, Druck, Füllstand, CPU-Last (0–100%)
- **Nicht-monoton**: Werte gehen auf und ab
- **Beispiel**: entPhySensorValue (Temperatur)

### Counter32/64 → Summierende Größen
- **Use-Case**: Netzwerkbytes, gefertigte Teile, Laufzeitzähler
- **Monoton**: Läuft hoch bis Overflow
- **Manager berechnet**: Differenz über Zeit → Durchsatz
- **Beispiel**: ifInOctets (empfangene Bytes)

### BITS/Bitfeld → Multiple Status
- **Use-Case**: Viele binäre Zustände gleichzeitig (32 Fehler in 32-Bit)
- **Effizient**: Statt 32 OIDs → 1 OID
- **Beispiel**: SPS-Statuswort (Bit0=Not-Halt, Bit1=Überlast, Bit2=Comm-Fehler)

### Enum-INTEGER → Modi/Zustände
- **Use-Case**: Betriebsarten (1=Auto, 2=Hand, 3=Service)
- **Lesbarkeit**: MIB dokumentiert Werte
- **Steuerbar**: Nur bei sicherem Fernzugriff
- **Beispiel**: ifAdminStatus (1=up, 2=down)

### OCTET STRING → Texte/Bitfelder
- **Use-Case**: sysName (Gerätename), sysLocation, hrPrinterDetectedErrorState (Bitmaske)

---

## SNMP Grenzen in Industrie 4.0

### 1. Polling-Paradigma (Pull-only)
- **Problem**: Zyklisches Polling → Netzlast, verzögerte Erkennung
- **Traps**: Nur für Alarme, Fire-and-Forget (UDP)
- **Kein Pub/Sub**: Wie MQTT/OPC UA Event Notifications
- **Skalierung**: Bei 100en Geräten mit 1000en OIDs limitiert

### 2. Keine strukturierte Datenmodellierung
- **Flache OID-Liste**: Keine Objekthierarchien wie OPC UA
- **Keine Semantik**: Unterschiedliche Hersteller → unterschiedliche OIDs für gleiche Konzepte
- **Keine Units/Typen**: Nur Rohwerte, Bedeutung aus MIB-Dokumentation

### 3. Begrenzte Interaktion
- **Primär Monitoring**: Nicht für Steuerung konzipiert
- **SNMP Set**: Selten verwendet (Sicherheitsbedenken)
- **Keine Transaktionen**: Keine komplexen Kommandos
- **Fehlermeldungen**: Nur einfache Error-Status per PDU

### 4. Skalierbarkeit und Performance
- **Große Installationen**: 1000e Geräte, 100.000e OIDs → Grenzen
- **Serielles Polling**: Manager-Stationen abarbeiten sequentiell
- **UDP-Basis**: Paketverluste unbemerkt
- **Zentralisiert**: Kein verteiltes Konzept (vs. Pub/Sub)

---

## SNMP vs. Moderne Alternativen

### Wann SNMP sinnvoll bleibt:
✅ **Herstellerübergreifende Grundüberwachung**: Diverse Altgeräte, Switches, Sensorboxen
✅ **Infrastruktur-Monitoring**: Netzwerkdiagnose, Basis-Health-Checks
✅ **Ressourcenbeschränkte Geräte**: Geringer Overhead
✅ **Schnelle Integration**: Out-of-the-box Support in NMS (Zabbix, PRTG)
✅ **Brownfield**: Legacy-Systeme ohne OPC UA

### Wann OPC UA geeigneter:
✅ **Tiefere Integration**: MES/ERP Verknüpfung
✅ **Semantisch reich**: Typ, Einheit, Kontext, Historie
✅ **Steuerkommandos**: Methodenaufrufe, transaktional
✅ **Security**: Eingebaut (Verschlüsselung, Authentifizierung)
✅ **Subscription**: Echtzeit-Updates
✅ **Neue Geräte**: Beckhoff, Bosch Rexroth setzen voll auf OPC UA

### Wann MQTT geeigneter:
✅ **IoT-Sensorik**: Viele verteilte Sensoren
✅ **Cloud-Anbindung**: Effiziente Weiterleitung an Cloud
✅ **Pub/Sub**: Skalierbar (Millionen Nachrichten)
✅ **Lose Kopplung**: Über Broker
✅ **Bandbreite-kritisch**: Extrem schlank
✅ **Mobile Assets**: Zustandsmonitoring via Mobilfunk

### Hybrid-Ansatz (Empfohlen):
- **SNMP**: Lokales Frühwarnsystem (Infrastruktur)
- **OPC UA**: Detaillierte Prozessdaten (SCADA/MES)
- **MQTT**: Cloud-Weitermeldung, Big Data Analysen

**Beispiel IIoT-Gateway**: Spricht alle 3 Protokolle gleichzeitig
- SNMP → klassisches NMS (OT-Abteilung)
- OPC UA → SCADA/MES
- MQTT → Cloud Analytics

---

## Relevanz für VIA

### 1. VIA Telemetrie via SNMP
**VIA Processes als SNMP Agents**:
- **Standard-MIBs**: CPU, RAM (HOST-RESOURCES-MIB)
- **VIA-spezifische MIB**: Task Queue Length, Message Rates, IPC Latencies
- **Traps**: Process-Crash, Scheduler-Overload, Router-Congestion

### 2. VIA Registry als SNMP Manager
- **Zentral**: Sammelt Zustandsdaten aller VIA Processes
- **Polling**: Regelmäßig Health-Checks
- **Trap-Receiver**: Empfängt kritische Alarme

### 3. VIA Custom MIB Objekte
**Private Enterprise-ID für VIA**:
- `viaProcessStatus` (Enum: Running, Stopped, Error)
- `viaTaskQueueLength` (Gauge32)
- `viaMessageRate` (Counter64)
- `viaIPCLatency` (Gauge32 in µs)
- `viaSchedulerLoad` (Gauge32 in %)
- `viaRouterHops` (Counter32)

### 4. Hybrid Monitoring
**Kombination**:
- **SNMP**: Lightweight Health-Checks (CPU, RAM, Basic Counters)
- **OPC UA**: Rich Process Data (Address Space mit VIA Services)
- **MQTT**: Aggregierte Telemetrie an Cloud

### 5. VIA Traps
**viaProcessCrashTrap**: Bei Process-Absturz
**viaSchedulerOverloadTrap**: Wenn Queue > Threshold
**viaRouterCongestionTrap**: Wenn Routing-Latenz > Threshold
**viaIPCErrorTrap**: Wenn IPC Mechanism failed

### 6. Security
**SNMPv3 authPriv** für VIA:
- **Authentication**: SHA-256
- **Privacy**: AES-128
- **User**: "via-monitor" mit starkem Passwort
- **View-Based Access**: Nur benötigte VIA-OIDs

### 7. Integration mit Kubernetes
**VIA Monitoring in K8s**:
- SNMP Exporter (Prometheus) → sammelt VIA SNMP Metriken
- Grafana Dashboard → visualisiert VIA Process Health
- Alertmanager → sendet Alerts bei VIA Traps

---

## Offene Fragen für VIA

1. **VIA Enterprise-ID**: Eigene OID-Nummer beantragen?
2. **MIB-Definition**: VIA-MIB formal spezifizieren?
3. **Granularität**: Welche VIA-Metriken via SNMP, welche via OPC UA?
4. **Trap-Strategie**: Welche Ereignisse als Trap, welche nur Poll?
5. **SNMPv3 Deployment**: Key Management für viele VIA Processes?
6. **SNMP vs Native VIA API**: SNMP nur als Zusatz oder Hauptinterface?
