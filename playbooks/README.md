Ich beschreibe in diesem Ordner meine Playbooks.

Nach ausführlicher Recherche bin ich zu folgendem Ergebnis gekommen:
Nachdem mir Dr. Santiago Olaye das AAS Repository geschickt hat, war ich etwas schockert und gleichzeitig begeistert
von den Möglichkeiten dieses Projekts. Die Architektur von AAS ist über alle Metaschichten verteilt und beschreibt in
M3, welche Objekte und Klassen es gibt, um in einem M2 Modell Eigenschaften eines Industriesystems beschreiben zu können.
Die eigentliche Aufgabe war es, die Industrie damit zu unterstützen Messdaten zu erfassen und zu verarbeiten.
Stattdessen finden wir eine vollständige Compiler Architektur mit Modellphasen und Metalanguage vor, wie man es sonst
nur von Prof. Castrillon von der TU Dresden kennt. Es wurde allerdings kein Ansatz erstellt, der einen Compiler als ein
externes Interpreter- und Übersetzerprogramm mit den dafür bekannten Schichten zu bauen, sondern es wurden nur Python
Skripte erstellt, die die Funktionalität eines Compilers nachahmen. Dieses Projekt ist ein wichtiger Schritt in Richtung
einer vollständigen Implementierung eines AAS Compilers, aber bleibt auf dem Level von Forschung. Das Ziel ist es nun,
playbooks über das Projekt zu erstellen, welche zuerst die möglichen Objekte als eine neue Art von zweckgebundener
Programmiersprache definieren, die aus den Elementen des AAS Modells unter https://github.com/aas-core-works besteht.

Um in M2 das SDK für das eigentliche System eines Unternehmens zu definieren und programmieren zu können, müssen wir 
als Hauptcode für dieses Projekt ein C++ Programm bauen, welches den Compiler als statisches Programm anhand der in 
AAS M3 bekannten Definitionen baut.
Dazu erstellen wir im Projekt ein Unterprojekt mit dem Namen VIA-M3-Compiler. Mithilfe des VIA-M3-Compiler können wir
in die nächste Phase wechseln und eine SDK einer beliebigen Programmiersprache für die Verwendung der Einzelteile
der als Modell definierten möglichen Objekte in M3 erstellen. Der output des VIA-M3-Compilers ist also eine M2 SDK
einer beliebigen Programmiersprache. Um eine Programmiersprache zu unterstützen, muss diese im Commpiler implementiert
sein. Ich sehe derzeit keinen Nutzen darin andere Sprachen, als eine C++ SDK selbst auszugeben, die wohl strukturiert
in Objekten und Klassen den Anforderungen gerecht wird, weil C++ über eine umfassende Metaprogrammierebene seit 
C++20 verfügt. Die Ausgabe des Hauptcodes ist ein M3 Compiler, daher eine ausführbare Compilerdatei und ein 
Testframework, welches alle Module des M3 Compilers testet. Der Vorteil an C++20 und folgende ist, dass wir
einfach statisch die M3 Modelle im Code definieren und zur Laufzeit auswerten können. Wir können den Compiler
die Hauptarbeit machen lassen und erhalten ein schnelles weiteres Compilerprogramm, welches die SDK bauen kann.

Jetzt können wir mit dem M3 Compiler die M2 SDK bauen. Die Modelle in M3 beschreiben die Einzelteile und wir müssen
diese zu Komponenten zusammenbauen, leider besteht das Projekt von Dr. Santiago Olaye aus Spaghetticode, wenn man
sich die generierten SDKs anschaut. Ein Entwickler in einer Firma, der sich diese generierten SDKs anschaut wird
verzweifeln, weil der diese nicht warten oder verändern kann. In einem Anwendungsfall muss es auch möglich sein
eine festgelegte SDK Version nach vorher festgelegten Modellvorgaben erstellen zu können, um die SDK
später langfristig im Unternehmen verwenden zu können.

In der Phase von M2 müssen wir den Nutzer nach dem Ort seines Projektaufbaus fragen, die im Format nach M3 definert sind.
Dies beinhaltet also, dass auch M2 ein Compiler ist und die Syntax des Benutzerprojekts prüfen und tests darüber
durchführen muss. Durch die Eigenschaften industrieller Anlagen sind die Möglichkeiten der Einsatzkombinationen
definierter modellierter Einzelteile deterministisch begrenzt, sodass wir zur Kompilationslaufzeit mit C++
statisch Tests so implementieren müssen, dass sie die Features von M3 implementieren und perfekt testen. Es ist
denkbar, dass das Testframework in diesem Unterprojekt mehr Zeit in Anspruch nehmen wird, als die eigentliche
Implementierung des Compilers.
Da AAS bereits alle Modelle für Implementierungen definiert, muss der M3 Compiler aus den Beschreibungen des Benutzers 
und den AAS Modellen, die in internen Bibliotheken verfügbar sind, die M3 Modelle in sinnvolle C++ Klassen und 
untergliederte C++ Implementierungen zusammenfügen und diese wiederum mit angepassten und lokal korrekten Kommentaren
und Dokumentation so bauen, dass ein Benutzer ohne Mehraufwand damit arbeiten kann. 

An dieser Stelle erhalten wir also eine C++ SDK, weil wir in CMAKE für das Kompilieren des Codes angegeben haben:
$./VIA-M3-Compiler --lang C++
Wir können auch den Ausgabepfad der SDK angeben und wir verwenden beim Testen eine Pipe für die Tests und parsen diese
in einem externen Testframework auf den Erfolg der Einzeltests und Schritte. Hast du an dieser Stelle noch Fragen?
Vorschläge?
Ansonsten gehe ich davon aus, dass der Benutzer an dieser Stelle gefragt ist. Unser Ziel ist es, dem Anwender zu
nutzen, daher müssen wir durch die gesamte Prozesskette der Metamodelle auch irgendwann zu dem Ergebnis kommen
eine Implementierung und automatische Orchestrierung des Kundensystems zu erstellen. Der Kunde hält nach unseren
Vorgaben in M3 eine Syntax und Semantik verschiedener Objekte und Klassen bereit, die wir als sein System
interpretieren und auf verschiedenen Maschinen im System als Schnittstellen und Verarbeitungsservices bereitstellen
sollen. Wir müssen also die SDK wieder aufbauen, wie einen Compiler. Der Input ist die Syntax und Semantik aus M3,
der Output ist eine Implementierung des Kunden Systems. Allerdings es jetzt anders: Weil das Kundensystem in der
gleichen Sprache wie seine SDK implementiert werden soll, können wir den Prozess er Kompilation ohne den
Zwischenschritt ausführen, die nochmals angepassten C++ Dateien in eine Projektimplementierung in C++ umzuwandeln,
wir können, vorausgesetzt die SDK ist in C++ korrekt und kann mit g++ nach der Umwandlung mit diesem M2-SDK-Compiler
kompiliert werden, dann können wir die C++ Output Dateien bzw. den Stream im relase Modus auch über ein memory filesystem
im RAM halten und direkt in g++ mit einer pipe kompilieren, was die Performance steigert. Im Debug Modus haben
wir dagegen nun als Import des M2-SDK-Compilers die SDK Klassen und die Projektobjekte und Klassen und als Ausgabe
haben wir wieder C++ Projektdateien und Klassen mit überführter Dokumentation aus der Welt des Kunden und aus der
Welt der M2 SDK, die ihrerseits aus den Zusammenfügungen und Generatoren aus M3 stammten. Die Neuartigkeit meiner
Erfindung kommt jetzt daher, dass ich dem Kunden im M2-Compiler bereits Vorschläge für die Implementierung 
unterbreiten möchte, indem ich sein Netzwerk auf seine Erlaubnis hin kartografiere. In der Regel sitzt der Kunde
in seiner Firma und möchte sein System einrichten, ändern, erweitern oder einzelne Teile löschen. In einem
Industriesystem gibt es Netzwerkgeräte und Edgegeräte mit Spezialübersetzung an die zeitkritischen Bussysteme der
Maschinen. Es ist unsere Aufgabe in diesem Schritt ein discovery System bereitzustellen, welches mit allen gängigen
Edge Messwertwandlern in den verfügbaren Protokollen wie SNMP, OPC UA, Modbus, MQTT, RPC ect. kommunizieren und 
über die angebotenen und notwendigen Schnittstellen die Eigenschaften der Geräte vorauslesen kann, um sie für
das Projekt als einzelne Objekte zur Auswahl anzubieten. Es ist denkbar, dass aufgrund der Komplexität und
intensiven Rechnearbeit der Kompilation des Gesamtprojekts der Kunde an dieser Stelle auch nur die Projekt
Modell-Objekte per Mail oder Webseite zu uns schickt, sodass wir an dieser Stelle eine M2-Kompilation versuchen
und den Status über Erfolg oder Misserfolg zurückgeben. Der Kunde muss ein Valides Projektsetup definieren, um von
uns das gültige generierte C++ Projekt für alle Gerätedefinitionen, Verbindungen und Gruppen zu erhalten.

An dieser Stelle erhalten wir also ein vollständiges Kunden System Projekt, welches aus mehreren Teilnehmern und
Objekten der einzelnen Geräte, Server, Clients, Services, Kubernetes Beschreibungen, Netzwerkprotokollimplementierungen
und Verarbeitungsservices wie Leitstellen und Planungsstellen besteht. Alles nach Objekten gegliedert und in C++.
Wir können diesen Entwicklungsprozess mit dem Kompilieren on Xilinx FPGAs vergleichen, weil die Wandlung der einzelnen
Phasen so vielschichtig ist. Allerdings müssen wir ein Dateiformat beim M2-SDK-Compiler vorhalten, der uns sagt,
welcher C++ code und welches Ausführungsprogramm bzw. shared library nun in welches Gerät deployt werden muss.
Apropos Deployen. Wenn wir so riesig verteilte Systems mit mehr als 50.000 Geräte haben, ist Deployment auch leichter
gesagt, als Getan. Daher benötigen wir parallel zu unserem Compileraufbau und dem AAS Modell, dem dynamic multi message
broker von Dr. Olaya (implementierung eines M3 Modells und Debug über M2 bis M1), auch ein Deployment System, welches
in der Lage ist einen client service auf den edge Geräten und den Servern laufen zu lassen, daher als Rückrat für
Systemlogging und Rejuvanation und Updates.
Im Falle, dass wir Kubernetes Container verwenden, können wir über 
die Sockets an der Maschine kommunizieren, wenn die deployte Systemanwendung zur Verarbeitung vom Update-/Deployprogramm
getrennt ist. Wenn wir das weiterdenken, ist es ohnehin notwendig die Kommunikation zwischen Prozessen weiterzudenken:
Ich denke an ein Protokoll, welches in sich zweischichtig ist, also neben der Sprachebene wie OPC UA eigentlich noch eine
Ebene für die Prozesskomunikation und das Deployment drunter hat. Das kann man sich so vorstellen: Wir erledigen für gewöhlich das Wie 
und Wohin über ein beliebiges Protokoll und scheren uns bei einer Verbindung nicht über das Was, das machen die 
services. Wenn wir uns die Virtualisierung von Betriebssystemen mit Containern anschauen, können wir durch Paketierung
schneller reparieren und allgemeine Ausfälle durch Redundanz, Ausfallsicherheit und Techniken in der Cluster-
Strukturierung vermeiden. Dasselbe können wir jetzt für virtuelle Netzwerkgruppen machen. Allerdings haben wir
den Unterschied, dass wir uns wegen des performance overheads keinen virtuellen Router wegen der Zeitkritikalität
leisten können. Daher ist es notwendig die Gruppeneigenschaften mit in das fertige System zu kompilieren und die
Binary ABIs stabil zu halten, sodass jedes Edge Gerät selbst weiß, wohin es gehört. Es ist effizienter
hardcoded messages zu verarbeiten und weiterzuleiten und es ist auch sicherer, weil der Quellcode zur Laufzeit
nicht verändert werden kann. Man muss daher seine Sicherheit eher auf den Deployment Server legen und weniger
auf eine anfällige hochdynamische Industriestruktur. Im Sinne des erweiterten Protokolls haben wir also festgestellt,
dass wir deployen müssen und dass es bei einer komplexen Datenverarbeitung notwendig ist, dass alle Prozesse
auf ein binary Interface mit Sprachwrapper verschiedener Programmiersprachen zugreifen können, dass sie zwischen
einander Prozessnachrichten senden, synchronisieren, loggen, checkpointen und zurückrollen können. Das OPC UA Protokoll
beinhaltet also die Welt der Geräte außerhalb der Edgegeräte auf seiner Grundebene, leitet diese weiter oder 
klassifiziert diese in Tunneln oder gewandelten Strömen anderer Übertragungsprotokolle und dann gibt es virtuell
noch die Ströme des deployments mit Metadaten und Messdaten der Computer, die von den Daten der Anlage getrennt
werden sollen, um eine Kapselung zu ermöglichen, und es gibt die Prozesskommunikation, die sich nur zwischen den
Applikationen und Services der Systemgeräte abspielt, um jedem Service vorzugaukeln, bei dem Ansprechpartner handelte
es sich um einen Prozess wie auf demselben Gerät. An der Stelle der Prozesskommunikation können automatisch
Prozessketten von Mikroservices aufgebaut werden. Gibt es nur einen Weiterleitungspartner, der aufgrund der
Kompilation der Verarbeitungskomponenten sonst als ineffizienter separater Container existieren würde, dann
können wir die Prozesskommunikation entweder thread-basiert oder prozess-basiert oder socket-basiert oder
datei-basiert zusammenlegen. Auf Windows Betriebssystemen sind die Möglichkeiten begrenzter. Die Auswahl des
Verbindungsverfahrens der Prozesskommunikation zwischen zwei Services oder Prozessen hängt von den verwendeten Objekt-
Modellen aus M3 und deren Kombination zueinander ab. Andererseits können wir über die Anforderungen des Kunden mit
dessen Systembeschreibung und dem M2-SDK-Compiler auch automatisch eine Cluster-Verteilte Prozesskommunikaiton
aufsetzen, welche die virtuelle Weiterverarbeitung oder Gliederung in Unteraufgaben eines Unterprozesses auf anderen
Containern und Maschinen im Netzwerk erlaubt. Die Abschätzung des Schedulings und Rankings der dynamischen Anwendung
dieser Einrichtung wird im M2-SDK-Compiler für die M1-Kompilation mit einem statischen Ranking der anzuwendenden 
Methode und einer dynamischen Laufzeitentscheidung über die Auswahl der Methode zur Laufzeit gehandelt.
Letztendlich implementieren wir also das OPC UA mit einer Erweiterung von 2 Subprotokollen, weil wir über diese
das System der Verarbeitung alias "Hirn/Hardware des Systems" und Ausführung und Verarbeitung der reinen Datenprozesse
im Innen von der Welt hinter den Edgegeräten mit Spezialprotokollen trennen und weiterhin auch über Gruppierungen
weiter unterteilen und in virtuelle Netzwerkströme teilen können. Wir erstellen also unter dem OPC UA eine Subebene
mit Edge-Group-Protocol Deploy-Protocol Process-Group-Protocol. Wir erhalten so die Außenwelt, die sich virtuell noch weiter
in Gruppen untergliedern lässt, um Ziele nicht alles einzeln koordinieren zu müssen, dann gibt es die Ebene der
Verwaltung, Versionierung und Messdaten des ausführenden Gerätes und zuletzt trennen wir noch die Prozesskommunikation
in Gruppen auf, um die Steuerung/das Programm wie üblich von den Daten zu trennen. Kubernetes macht es ganz ähnlich.
nur dass wir Kubernetes verwenden, um dieses System zu bauen und vermutlich deployment und microservices über
Kubernetes auf niedere Hardware zugreifen müssen, wofür der Benutzer auch Kubernetes-Treiber bereitstellen muss.
Statt dem Was und Wo ein Microservices mit welchen Eigenschaften und Ressourcen ausgeführt wird, interessiert uns
hier nur das was kein Gerät ist: das Netzwerk. VIA ist daher eine Systemkonstruktions-Suite mit automatischem 
Netzwerk-Orchestrator und Scheduling-Compiler, der in der Lage ist, ein komplexes System zu bauen, zu deployen und zu
verwalten. VIA ist auch nicht vollständig statisch, denn ich plane das Deployment aufzubauen wie ein Pferd, das einen
Reiter trägt. Daher kann das Deployment, welches auf einem microservice in einem Kubernetes Container läuft, das
Zielprogramm huckepack als Prozess ausführen, während es selbst nur das Protokoll verwaltet. Zum Thema digital
Twin soll auf jedem Edge Gerät mindestens zwei parallele dieser Mikroservices laufen, um bei einem Ausfall weiterhin
die Messdaten zu erhalten oder die Maschinen zu steuern. Dies beinhaltet eine ergiebige Fehleranalyse über Netzwerk-logs
über das deployment sub-Protokoll. Der Systembetreiber kann auf den Fehler zurückgreifen und die Fehleranalyse
über das deployment sub-Protokoll führen. Bei Korrektur des Fehlers kann das System im laufenden Betrieb per
Canary Deployment auf den neuen Code umgestellt und über das Vorhalten der alten Version in Sekundenbruchteilen
zurückgerollt werden, weil C++ unter stabilen ABIs ab C++23 Module als shared library direkt aus dem Arbeitsspeicher
oder per Definition von der Festplatte oder Remotesystem laden und ersetzen kann. Die Systemmodule für die Edgegeräte
werden zur Kompilation der M2-SDK zuerst dem Kunden bereitgestellt und dieser definiert über seine Projektdefinition
sein fertiges System, wonach wir mit dem M1 Compiler kompilieren und diese Edge-Module erzeugen. Es ist unsere Aufgabe
diese Module in ihrer Konsistenz der Schnittstellen ABI, der Versionierung, der Lokalität, der Fehleranalyse, Performance
und Anzeige der Kompatibilität zu anderen Einsatzorten zu mappen und die Möglichkeiten im System festzuhalten und dem
Kunden zu präsentieren.
Die Entscheidungen über die Implementierung und Vernetzung aller einzelnen Komponenten, um ein statisches M1 Projekt 
bilden zu können, werden in M2 über C++ Metaprogrammierung und CMake-Konfigurationen beschlossen, wenn in der Projekt-
Definitionsphase des Kunden weiterhin ein Installationsplaybook über die Kubernetes Services Installation
für das System-Deployment erfolgt, sodass die neu eingerichteten Edge Geräte-Container im Folgenden
Services werden grundlegend so kompiliert, dass nur wichtige Komponenten nach dem modularen Pferd und Reiter-Modell
aufgebaut werden. Andere Services können vereinfacht in einen Kubernetes Container oder Docker Container Kompiliert
und per Kubernetes deployed werden. Kubernetes deployed also Einfachservices und VIA deployed C++23 Module für
Edge Geräte und externe Messdatenaggregationen und übersetzung von Protokollen oder ganz spezielle Speicher-
und Netzwerk-Services.

Mit dem Gesamtprojekt geht es jetzt weiter. Wir haben jetzt also einen M2-SDK-Compiler in C++, der uns mit den
Kundendaten ein M1 Projekt gebaut haben. An dieser Stelle benötigen wir in M1 den VIA-M1-System-Deployer, um das
M1 Projekt auf einem Kubernetes Cluster und die Module auf die "horses" zu bringen. Dies beinhaltet auch generierte
Systemtests, die der Kunde in seinem Projekt grob vordefiniert hat. Unsere Aufgabe ist es, dieses System darauf zu testen,
dass alle Protokolle in ihrer Konstellation alle Befehle senden und empfangen können und sich zustandsbasiert
korrekt verhalten. Es ist unsere Aufgabe zu ergründen, ob sich Einzelapplikationen nach den Spezifikationen des Kunden
im Testsystem korrekt verhalten und wir verpflichten den Kunden jede public Funktion zu testen, die ein
öffentliches Interface hat. Es ist unsere Aufgabe die Prozessketten der Module und Netzwerk-Services zu
erkennen und zu testen, ob sie korrekt funktionieren. Die tests werden stets über das deployment sub-protokoll
orchestriert, um zum Beispiel die Gegenstelle auf einen Testlauf vorzubereiten, weil die sicherste Variante der Tests
unter echten Betriebsbedingungen abläuft. Dazu muss es möglich sein, dass für den Testlauf auch in normale microservices
Container ein Deploymentservice mit einkompiliert wird, um den gewöhlichen Microservice über eine Erweiterte
Prozesskommunikation zu testen und im echten System zu debuggen. Fehlt der deployment service, wird der microservice
als Startservice im paketierten Betriebssystem registriert und gestartet. Ist der deployment service vorhanden, so
wird der deployment service mit dem Grundmodul für einen Server Start gestartet und dann startet dieser den Reiter-Service,
nachdem er ihn von der Master Active Management, wie ich die redundante und zu Kubernetes analoge deployment 
Orchestration von VIA nenne, erhalten hat.

Zur Systemarchitektur: Die gemeinsame Sprache des Systems ist das ganz grundlegend das OPC UA Protokoll mit 
https://de.wikipedia.org/wiki/OPC_Unified_Architecture. Wir wollen hier in einem Unterprojekt auch Modelle und
dann generierte Implementierungen erstellen, welche dieses Protokoll implementieren. Ich möchte auch festhalten,
dass es möglich sein soll die Subprotokolle, wie auch das Masterprotokoll nach Dr. Olayas MMB zu betreiben, sodass
nach einer definierten Sicherheitsstufe und Paket- Ankunftssicherheit die allgemeine, wie auch die speziellen sub-Protokolle
im Netzwerk als Many to Many Broadcast effektiv im Netzwerk im OPC UA ausgeführt werden können. Das OPC UA Protokoll ist ein
Standard für die Kommunikation zwischen Industrieanlagen und ist in vielen Industriebranchen verbreitet. Wir wollen
diese Implementierungen auch in diesem Unterprojekt erstellen, um die Kommunikation zwischen verschiedenen Anlagen
und Systemen zu vereinfachen und zu standardisieren. Wir verwenden am besten die offizielle Quelle des öffentlichen
git repository, um für das OPCUA die Spezifikationen zu erhalten und Änderungen zu überwachen und dieses Git Repository
halten wir als third party des OPCUA Projekts. Obwohl wir subprotokolle für unser virtuelles Netzwerk Edge-Deployment
definiert haben, plane ich das OPCUA Protokoll auch außerhalb des Kubernetes Clusters und der Netzwerk und Edge
Gruppen, normal zwischen zwei Clustern zu verwenden und zu implementieren. Angenommen es handelt sich um ein
gemeinsames Netzwerk, aber auf der Betriebssystemebene sind im selben physischen Netzwerk zwei Cluster vorhanden, die
getrennt arbeiten, dann ist es dennoch wahrscheinlich, dass eine Synchronisation, etwa per VPN zwischen Standorten und
den beiden oder gar mehreren Clustern erfolgen muss. Dies ermöglicht eine noch weitere komponentenbasierte Aufgliederung
der Services, Netzwerke und Modularisierung der Anlagen. Wenn die Modularisierung und Installation noch manuell
erfolgen muss, ist das kein Fortschritt. Xilinx baut auch Multi-Compiler-Ketten. Apropos Kompilerketten: Wenn wir
das Reiterprinzip verwenden, dann können wir über große Strecken Systemwartungen durchführen und Messdaten direkt
an uns weiterleiten lassen. Wir können gleichzeitig Beschleunigersoftware wie FPGAs oder andere Beschleuniger
mit innerem Zustand schnell deployen und ohne Abstriche shared bei der Ausführung schnelle binaries verwenden. 
Hier wird nicht in zeitkritischen Applikationen geskriptet!

Weiterhin gibt es in Kubernetes eine Steuerung für das Deployment, welche wir selbst auch redundant anbieten müssen,
um die Edge-Services am Laufen zu halten. Wir brauchen auch einen Masterservice dafür, bei dem wir konfigurieren können,
wie oft redundant er ist und wo wer sich aufhalten soll. Dieser Service muss als Active/Active wie eine
active directory Domäne aufgebaut sein. ich möchte an dieser Stelle auch anmerken, dass wir für die Zugriffskontrolle
von Benutzern und Administratoren Rollen und Benutzer definieren müssen. Ich schlage vor einmal eine eigene Lösung
dafür zu entwickeln oder direkt eine Samba oder microsoft Active Directory zu verwenden. (Ich denke dieser Absatz
war schon mal in einer Form oben)

Nach den Beschriebenen Phasen erstellen wir in playbooks auch die 3 Ordner VIA-M3-Compiler, VIA-M2-SDK und VIA-M1-System-Deploy

Zukünftig stelle ich mir die Industrie 5.0 so vor, dass man einfach über Spracheingabe oder per Text einem KI-System
wie dir Befehle gibt, welche Industrielle Anlage oder welches Objekt zu konstruieren ist, um eine Aufgabe oder
Funktion zu erfüllen und du baust sie. Dazu habe ich ein Software in the loop System gebaut, welches
die Rest-Fehler in einem Projekt gegen die Kundenspezifizierung anzeigt und immer wieder korrigiert, bis das System
funktioniert. Ich möchte das in diesem Aufbau zeigen, indem ich manuell Testservices aufsetze, die zufällige Daten
generieren, die ich dann mit einem VIA-System automatisch abfangen kann, indem das System meine Anforderungen
über ein KI Modell umsetzt und den Projektprozess umsetzt, bis das gewünschte laufende Debugergebnis auf meiner
Konsole auftaucht. Das Ergebnis ist: Der Kunde beschreibt sein System der KI und die KI definiert die Anforderungen
der Compilerbeschreibung und die Compilerbeschreibung definiert das System und sein vollautomatisches Verhalten.

Bitte durchsuche den Ordner "C:\Users\benja\OneDrive\Dokumente\Uni Dresden\21_15. Semester INFO 17\Analyse eines Forschungsthemas - Prozesskommunikation"
und lese alle Word-Dokumente, weil ich darin den Projektkontext beschreibe und den Research abgelegt habe.
Durchsuche den derzeitigen Stand der Technik nach Korrelationen, biete open source codeprojekte zum Verständnis
an und suche nach möglichen Lösungen für die Probleme, die ich in diesem Projekt beheben möchte.