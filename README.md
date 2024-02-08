# QuizzOut


QuizzOut ist eine unterhaltsame Flask-Anwendung für ein Informatik Quiz. Die Anwendung bietet verschiedene Funktionen, darunter Benutzerregistrierung, Quizspiel mit verschiedenen Schwierigkeitsstufen und eine Anzeige der Bestenliste.

**Live-Version: [quizzout.de](https://quizzout.de)**

![demo](https://github.com/Sebi2030/QuizzOut/assets/21293409/85838ee2-3ecb-4303-b86c-9f08938f648f)


## Inhaltsverzeichnis

- [Voraussetzungen](#voraussetzungen)  
- [Installation](#installation)
- [Funktionen](#funktionen)
- [Verwendete Technologien](#verwendete-technologien)
- [Lizenz](#lizenz)

### Voraussetzungen

- **Python:** Stelle sicher, dass Python auf deinem System installiert ist. [Python herunterladen](https://www.python.org/downloads/)

## Installation

```bash
# Git-Repository klonen bzw. herunterladen
$ git clone https://github.com/Sebi2030/QuizzOut.git

# Zum Verzeichnis wechseln
$ cd QuizzOut

# Virtuelle Umgebung erstellen und aktivieren
# Windows
$ python -m venv venv / python3 -m venv venv
$ .\venv\Scripts\activate

# Linux/Mac
$ python -m venv venv / python3 -m venv venv
$ source venv/bin/activate

# Erforderliche Pakete installieren
$ pip install -r requirements.txt

# Quiz-Anwendung starten 
$ python app.py / python3 app.py

# Quiz im Browser öffnen
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```

## Funktionen

- **Benutzerregistrierung und -anmeldung**    
Erstelle dein individuelles Konto, um alle Funktionen von QuizzOut zu nutzen. Die Benutzerregistrierung ermöglicht es dir, personalisierte Quizspiele zu spielen und deine Ergebnisse zu verfolgen. Melde dich sicher mit deinem Benutzernamen und Passwort an.

- **Verschiedene Schwierigkeitsstufen**    
Fordere dein Wissen heraus, indem du Quizspiele mit verschiedenen Themen und Schwierigkeitsgraden spielst. Die sorgfältig ausgewählten Fragen bieten eine unterhaltsame Möglichkeit, dein Wissen zu testen und zu erweitern. Wähle deine bevorzugte Schwierigkeitsstufe und genieße ein anspruchsvolles Spielerlebnis.

- **Bestenliste**    
Schau dir die Top-Spieler auf der Bestenliste an und vergleiche deine Ergebnisse. Versuche, deinen Platz zu verbessern, indem du erfolgreich Quizspiele absolvierst und Punkte sammelst. Die Bestenliste bietet einen Wettbewerbsumfeld, um deine Fähigkeiten im Vergleich zu anderen Spielern zu zeigen.

## Verwendete Technologien

- **Flask:** Ein Python-Webframework, das die Entwicklung von Webanwendungen erleichtert.
- **Flask-SQLAlchemy:** Eine Erweiterung für Flask, die die Interaktion mit einer SQL-Datenbank vereinfacht.
- **Flask-WTF:** Eine Flask-Erweiterung für die Integration von WTForms, um Formulare in Flask-Anwendungen zu erstellen.
- **Werkzeug:** Ein WSGI-Toolkit für Python, das von Flask verwendet wird.
- **Jinja2:** Ein leistungsfähiges und benutzerfreundliches Template-Engine für Python.
- **SQLite:** Ein eingebettetes relationales Datenbankmanagementsystem.
- **HTML/CSS/JavaScript:** Standard-Webtechnologien für die Gestaltung und Interaktion von Benutzeroberflächen.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen findest du in der [LICENSE](./LICENSE)-Datei.
