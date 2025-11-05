# 🧑‍💻 JobBot Dashboard

Ein Desktop-Tool zur **Jobsuche über die Arbeitsagentur-API**.
Mit **Tkinter GUI**, **SQLite-Datenbank**, CSV-Export und eigenem **Desktop-Icon**.

---

## 🚀 Features
- 🔍 **Jobsuche** über die offizielle [BA Jobsuche API](https://jobsuche.api.bund.dev/)
- 📊 **Dashboard** mit Tkinter (Suchfeld, Ergebnistabelle, Links)
- 💾 Speicherung der Ergebnisse in **SQLite** (`jobbot.db`)
- 📂 **Export** nach CSV
- 🗄️ Integrierter **SQL Viewer**
- 🖼️ Eigene **Icons** (JobBot, Lupe)

---
### JobBot/
#### api.py - Anbindung an die Arbeitsagentur
#### dashboard.py - eine kleine Benutzeroberfläche, Tkinter GUI
#### models.py - gefundene Jobs im SQLite Format
#### sql_viewer.py - einfacher SQL Viewer, Schnellabfragen
#### main.py - Startpunkt der App
#### icons.py - icons selbst erstellen
#### jobbot.db - Datenbank wird automatisch erstellt
#### JobBot_Start.bat - JobBot vom Desktop starten
---
## 📦 Installation

### Voraussetzungen
- **Python 3.13** oder neuer
- Bibliotheken/bash:
  requests,
  pandas,
  pillow, ...

## Projektstruktur

### JobBot/
#### │── api.py
#### │── dashboard.py
#### │── models.py
#### │── sql_viewer.py
#### │── main.py
#### │── icons.py
#### │── jobbot.db
#### │── JobBot_Start.bat
#### │── README.md

---
📝 Lizenz

Dieses Projekt ist zu Lernzwecken gedacht.
Keine Garantie für Vollständigkeit oder Funktionalität.

---

Viel Freude!

Keela-prog

