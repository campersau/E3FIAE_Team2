# Chatbot-Projekt – E3FIAE_Team2
## Projektstruktur
```plaintext
project_chatbot/
├─ scripts/
│  └─ main.py           
├─ venv/                
├─ requirements.txt     # Projekt-Abhängigkeiten
├─ .gitignore           # Ignorierte Dateien
└─ readme.md            # Dokumentation
```

## Anleitung zur Nutzung

### 1 Virtuelle Umgebung anlegen und aktivieren

#### Virtuelle Umgebung anlegen
```bash
cd project_chatbot
python -m venv venv
```
#### Virtuelle Umgebung aktivieren
Windows
```bash
venv\Scripts\activate
````
Linux/macOS
```bash
source venv/bin/activate
```
### 2 Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```
oder 
```bash
pip install flask
```
## 3. Projekt starten
```bash
cd project_chatbot
source venv/bin/activate
python scripts/main.py   # Startet Flask auf http://localhost:5050
```
### projektstruktur

```project_chatbot/
├─ app/                         # Haupt-Anwendung
│  ├─ __init__.py              # Flask-App wird hier erstellt
│  ├─ routes.py                # Flask-Routen (Home, Login, Chat)
│  ├─ static/                  # CSS, JS, Bilder
│  │  ├─ css/
│  │  │  └─ style.css          # Design der Webseite
│  │  ├─ js/
│  │  │  └─ script.js          # Optional: Chatfunktionen
│  │  └─ images/               # Logos & Hintergründe
│  │     ├─ logo.png
│  │     └─ bg.png
│  └─ templates/
│     ├─ base.html             # Grundlayout (Header/Navbar)
│     ├─ index.html            # Chat-Seite
│     └─ login.html            # Login-Seite
│
├─ venv/                       # Virtuelle Umgebung (nicht in GitHub hochladen!)
├─ main.py                     # Startpunkt der App → `python main.py`
├─ requirements.txt            # Notwendige Python-Bibliotheken (Flask usw.)
└─ README.md                   # Dokumentation
```
### webseite öffnen
Browser öffnen → http://localhost:5050