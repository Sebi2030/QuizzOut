---
title: Design Decisions
nav_order: 3
---

{: .label }
Abinesh Gulasingam
{: .label .label-green }
Sebastian Lukas Nieme

# Design decisions
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Entscheiden für das geeignete Werkzeug für die Datenbank: SQL oder SQLAlchemy ?

{: .label }
Abinesh Gulasingam
{: .label .label-green }
Sebastian Lukas Nieme

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 01-12-2023

### Problem statement

Entscheidung fällen, welches Tool wir für die Datenbank benutzen. Zur Auswahl stehen:

1. SQL
2. SQLALchemy

Mit SQLAlchemy erhalten wir eine ORM-Schicht, die uns eine praktische Oberfläche bietet, um mit Datenbanken zu arbeiten. Sie bietet uns mehr Flexibilität und Abstraktion, was uns bei der Auswahl der Datenbank hilft. Reines SQL gibt uns direkte Kontrolle über unsere Abfragen. Es kann schneller sein und gibt uns ein Gefühl von Kontrolle, erfordert aber auch mehr Arbeit von uns. 

### Decision

Wir haben uns für SQLAlchemy entschieden, weil es uns ermöglicht, unsere Datenbankarbeit auf eine angenehme und intuitive Weise zu erledigen. Die ORM-Schicht vereinfacht unsere Arbeit und gibt uns ein Gefühl von Kontrolle und Vertrautheit. Mit SQLAlchemy können wir unsere Anwendungsentwicklung effizienter gestalten und uns auf das Wesentliche konzentrieren, ohne uns um die Details der Datenbankverwaltung kümmern zu müssen.
### Regarded options

**SQL**

**Pro:**
1. Einfach zu erlernen
2. Ist uns bereits vertraut
3. Einfache Skalierbarkeit

**Contra:**
1. Unflexible Datenstruktur
2. Kompatibilitäsprobleme
3. Schwierigkeiten bei unstruktrukturierten Daten

**SQLAlchemy**

**Pro:**
1. Vereinfacht die Durchführung von Datenbankabfragen durch das SQLAlchemy-Framework
2. Objektrelationale Zuordnung (ORM) erleichtert das Arbeiten mit Datenbanken auf höherer Abstraktionsebene
3. Ermöglicht die Verwendung von Python-Klassen zur Abbildung von Datenbanktabellen, was die Entwicklung erleichtert

**Contra:**
1. ORM kann zu Overhead führen und in bestimmten Szenarien ineffizienter sein als direktes SQL
2. Komplexere Anpassung und Konfiguration im Vergleich zur Verwendung von reinem SQL


## 02: Entscheiden für das geeignete Web-Framework:Jinja oder Django ?

{: .label }
Abinesh Gulasingam
{: .label .label-green }
Sebastian Lukas Nieme

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 01-12-2023

### Problem statement

Entscheidung fällen, welches Web-Framework wir benutzen. Zur Auswahl stehen:

1. Jinja
2. Django

Jinja ist eine flexible und leistungsstarke Template-Engine für Python, die das Rendern dynamischer Inhalte in HTML-Dateien ermöglicht. Im Gegensatz dazu bietet Django eine integrierte Template-Engine mit spezifischen Funktionen für das Django-Framework, wie Template-Tags und -Filter sowie die Vererbung von Templates.
Jinja kann unabhängig von Django in verschiedenen Python-Projekten verwendet werden, während die Django-Template-Engine nahtlos in Django-Projekte integriert ist und eine konsistente Entwicklungspraxis fördert. Jinja ist besonders schnell und effizient in der Verarbeitung von Templates, was es ideal für komplexe Anwendungen macht.

### Decision

Wir haben uns für Jinja entschieden, weil wir von seiner Flexibilität und Leistungsfähigkeit beeindruckt sind. Als Template-Engine für Python ermöglicht es uns, dynamische Inhalte in HTML-Dateien auf eine Weise zu rendern, die einfach und intuitiv ist. Im Vergleich zur integrierten Template-Engine von Django schätzen wir Jinjas einfachere Syntax und höhere Flexibilität, da sie unsere Entwicklungszeit verkürzt und unsere Produktivität steigert.

Ein weiterer Grund, warum wir Jinja bevorzugen, ist seine Unabhängigkeit von Django. Das bedeutet, dass wir Jinja in verschiedenen Python-Projekten verwenden können, ohne an die spezifischen Funktionen oder Konventionen von Django gebunden zu sein. Diese Freiheit gibt uns die Möglichkeit, unsere Templates flexibel anzupassen, um den Anforderungen jedes Projekts gerecht zu werden.

Besonders beeindruckend finden wir Jinjas Geschwindigkeit und Effizienz bei der Verarbeitung von Templates. Diese Eigenschaft macht es ideal für komplexe Anwendungen, in denen eine schnelle Renderleistung erforderlich ist. Insgesamt betrachten wir Jinja als eine großartige Lösung für die Erstellung dynamischer Webseiten, die perfekt zu unserem Entwicklungsstil und unseren Anforderungen passt.




### Regarded options

**Jinja**

**Pro:**
1. Einfache Syntax und höhere Flexibilität im Vergleich zu Django
2. Schnell und effizient in der Verarbeitung von Templates
3. Unterstützt dynamische Inhalte in HTML-Dateien mit Variablen, Bedingungen und Schleifen
4. Ist uns bereits vertraut
**Contra:**
1. Weniger integrierte Funktionen im Vergleich zur Django-Template-Engine
2. Benötigt möglicherweise mehr manuelle Konfiguration und Anpassung

**Django**

**Pro:**
1. Bietet viele vorgefertigte Vorlagen und Bibliotheken für häufige Webentwicklungsanforderungen
2. Unterstützt die Verwendung von ORM für den Datenbankzugriff und erleichtert dadurch die Arbeit mit Datenbanken auf höherer Abstraktionsebene
 

**Contra:**
1. Enge Kopplung von Komponenten kann die Flexibilität in einigen Szenarien einschränken
2. Ist uns nicht vertraut

    
## 03: Welches Datenbanksystem wollen wir nutzen? Erwägung zwischen SQLite und MySQL.

{: .label }
Abinesh Gulasingam
{: .label .label-green }
Sebastian Lukas Nieme


### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 01-12-2023

### Problem statement

Entscheidung fällen, welches Datenbankmanagementsystem am besten für uns geeigent ist. Zur Auswahl stehen:

1. SQLite
2. MySQL

SQLite ist eine leichte, eingebettete Datenbank für lokale Anwendungen, während MySQL eine leistungsstarke Serverdatenbank für größere Projekte ist. SQLite eignet sich gut für kleine Anwendungen ohne Server, während MySQL besser für serverbasierte Anwendungen mit vielen Benutzern und großen Datenmengen geeignet ist. SQLite ist uns bereits bekannt.

### Decision
Datenbanklösung bietet, die perfekt für unser eher kleines Projekt geeignet ist. Da wir hauptsächlich an einem eher kleineren Projekt arbeiten, welches lokal luft und keine umfangreiche Serverinfrastruktur erfordert, ist SQLite die ideale Wahl für uns. Es ermöglicht uns, schnell und effizient Daten zu speichern und abzurufen, ohne die Komplexität einer separaten Serverinstallation. Darüber hinaus bietet SQLite eine gute Leistung und Skalierbarkeit für unser aktuelles Projekt. Insgesamt haben wir festgestellt, dass SQLite eine großartige Lösung ist, die unseren Entwicklungsprozess vereinfacht und unsere Anwendung reibungslos betrieben werden kann.
### Regarded options

**SQLite**

**Pro:**
1. Unflexible Datenstruktur
2. Kompatibilitäsprobleme
3. SQLite ist plattformübergreifend und läuft auf verschiedenen Betriebssystemen, einschließlich Windows, macOS und Linux.


**Contra:**
1.Da SQLite eine eingebettete Datenbank ist, bietet sie keine nativen Netzwerkfunktionen und erfordert zusätzlichen Aufwand, um den Zugriff über das Netzwerk zu ermöglichen.
2. Die Leistung nimmt mit zunehmender Größe der Datenbank ab

  **MySQL**

**Pro:**
1. MySQL läuft auf verschiedenen Betriebssystemen, darunter Windows, macOS, Linux und verschiedene Unix-Varianten, was die Portabilität von Anwendungen erleichtert.
2. Hohe Leistung

**Contra:**
1. Benötigt viel Speicherplatz
2. Müsste neu erlernt werden







---
