import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SQLViewer(tk.Toplevel):
    def __init__(self, db_file):
        super().__init__()
        self.title("SQL Viewer")
        self.db_file = db_file

        # --- Preset Queries Dropdown ---
        frm_preset = tk.Frame(self)
        frm_preset.pack(fill="x", pady=5)

        tk.Label(frm_preset, text="Schnellabfragen:").pack(side="left", padx=5)

        self.preset_queries = {
            "Top 10 Jobs": "SELECT title, company, location, url FROM jobs LIMIT 10;",
            "Alle Firmen": "SELECT DISTINCT company FROM jobs ORDER BY company;",
            "Jobs pro Ort zählen": "SELECT location, COUNT(*) as Anzahl FROM jobs GROUP BY location ORDER BY Anzahl DESC;",
            "Jobs pro Suchwort zählen": "SELECT keyword, COUNT(*) as Anzahl FROM jobs GROUP BY keyword ORDER BY Anzahl DESC;"
        }

        self.selected_preset = tk.StringVar(value="Top 10 Jobs")
        dropdown = tk.OptionMenu(frm_preset, self.selected_preset, *self.preset_queries.keys(), command=self.use_preset)
        dropdown.pack(side="left", padx=5)

        # --- Eingabe ---
        frm = tk.Frame(self)
        frm.pack(fill="x", pady=5)
        tk.Label(frm, text="SQL Befehl:").pack(side="left")
        self.entry_sql = tk.Entry(frm, width=80)
        self.entry_sql.pack(side="left", padx=5)
        tk.Button(frm, text="Ausführen", command=self.run_sql).pack(side="left")

        # --- Tabelle ---
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill="both", expand=True)

        # --- Diagramm ---
        self.fig, self.canvas = None, None

    def use_preset(self, choice):
        """Preset-Abfrage ins Eingabefeld laden"""
        sql = self.preset_queries.get(choice, "")
        if sql:
            self.entry_sql.delete(0, tk.END)
            self.entry_sql.insert(0, sql)

    def run_sql(self):
        query = self.entry_sql.get()
        if not query.strip():
            return
        try:
            conn = sqlite3.connect(self.db_file)
            df = pd.read_sql_query(query, conn)
            conn.close()
        except Exception as e:
            messagebox.showerror("Fehler", str(e))
            return

        # --- Tabelle anzeigen ---
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # --- Diagramm falls 2 Spalten ---
        if df.shape[1] == 2:
            self.show_plot(df)

    def show_plot(self, df):
        if self.fig:
            plt.close(self.fig)
        self.fig, ax = plt.subplots(figsize=(5, 3))
        df.plot(kind="bar", x=df.columns[0], y=df.columns[1], ax=ax, legend=False)
        ax.set_title(f"{df.columns[1]} pro {df.columns[0]}")
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True, pady=5)
