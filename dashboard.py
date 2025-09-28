import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser, csv
from api import search
from models import insert_jobs, fetch_jobs
from sql_viewer import SQLViewer


class JobDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JobBot Dashboard")
        self.geometry("1000x600")
        self.current_jobs = []

        # 🔎 Suchfelder
        frm_search = tk.Frame(self)
        frm_search.pack(fill="x", pady=5)

        tk.Label(frm_search, text="Suchwort:").pack(side="left")
        self.entry_kw = tk.Entry(frm_search, width=25)
        self.entry_kw.pack(side="left", padx=5)

        tk.Label(frm_search, text="Ort:").pack(side="left")
        self.entry_loc = tk.Entry(frm_search, width=25)
        self.entry_loc.pack(side="left", padx=5)

        tk.Button(frm_search, text="🔍 Suche", command=self.search).pack(side="left", padx=5)
        tk.Button(frm_search, text="💾 Export CSV", command=self.export_csv).pack(side="left", padx=5)
        tk.Button(frm_search, text="📊 SQL Viewer", command=self.open_sql).pack(side="left", padx=5)

        # 📋 Ergebnistabelle
        self.tree = ttk.Treeview(
            self,
            columns=("title", "company", "location", "keyword", "url"),
            show="headings"
        )
        for col in ("title", "company", "location", "keyword", "url"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180 if col != "url" else 250)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.open_link)

        # Startdatenbank laden
        self.load_from_db()

    def search(self):
        """Suche über API starten"""
        kw = self.entry_kw.get().strip() or "Python"
        loc = self.entry_loc.get().strip() or "Berlin"

        try:
            result = search(kw, loc, limit=20)

            if "stellenangebote" in result:
                jobs = []
                for j in result["stellenangebote"]:
                    jobs.append({
                        "title": j.get("titel"),
                        "company": j.get("arbeitgeber"),
                        "location": j.get("arbeitsort", {}).get("ort", ""),
                        "keyword": kw,
                        "description": j.get("stellenbeschreibung", ""),
                        "url": j.get("linkEmpfehlung", "")
                    })

                self.current_jobs = jobs
                insert_jobs(jobs)
                self.show_jobs(jobs)
            else:
                messagebox.showinfo("Info", "Keine Stellenangebote gefunden.")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def show_jobs(self, jobs):
        """Tabellenanzeige aktualisieren"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for job in jobs:
            self.tree.insert(
                "", "end",
                values=(job["title"], job["company"], job["location"], job["keyword"], job["url"])
            )

    def load_from_db(self):
        """Letzte Jobs aus DB laden"""
        rows = fetch_jobs(50)
        jobs = []
        for r in rows:
            jobs.append({
                "title": r[0],
                "company": r[1],
                "location": r[2],
                "keyword": r[3],
                "description": r[4],
                "url": r[5]
            })
        self.current_jobs = jobs
        self.show_jobs(jobs)

    def export_csv(self):
        """Jobs als CSV exportieren"""
        if not self.current_jobs:
            messagebox.showinfo("Info", "Keine Jobs zum Exportieren vorhanden.")
            return
        filepath = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["Titel", "Firma", "Ort", "Suchwort", "Beschreibung", "URL"])
                for job in self.current_jobs:
                    writer.writerow([
                        job["title"], job["company"], job["location"],
                        job["keyword"], job["description"], job["url"]
                    ])
            messagebox.showinfo("Export", f"Gespeichert nach {filepath}")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def open_link(self, event):
        """Job-URL im Browser öffnen"""
        item = self.tree.focus()
        if not item:
            return
        values = self.tree.item(item, "values")
        if values and values[4]:
            webbrowser.open(values[4])

    def open_sql(self):
        """SQL Viewer öffnen"""
        SQLViewer("jobbot.db")
