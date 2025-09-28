REM ==============================
REM JobBot Starter für Python 3.13
REM ==============================

REM echo off = Verhindert die Anzeige der Befehle im Konsolenfenster
REM echo = steuert, ob Befehle im Konsolenfenster angezeigt werden oder nicht
REM REM = Remark, für Kommentar, wird nicht ausgeführt
REM cd = change directory, wechselt das Verzeichnis auf dem aktuellen Laufwerk
REM cd /d = change directory and drive, wechselt gleichzeitig das Laufwerk und das Verzeichnis
REM start = startet ein Programm oder öffnet ein Dokument in einem neuen Fenster
REM exit = schließt das aktuelle Konsolenfenster

@echo off
REM 🔹 In Projektordner wechseln
cd /d "C:\Users\Admin\Desktop\Jobbot_AA_2"

REM 🔹 Dashboard starten mit Python 3.13
REM "C:\Users\Admin\AppData\Local\Programs\Python\Python313\python.exe" main.py

REM 🔹 Falls du kein Konsolenfenster willst:
start "" "C:\Users\Admin\AppData\Local\Programs\Python\Python313\pythonw.exe" main.py
exit
