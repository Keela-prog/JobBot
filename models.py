import sqlite3
from contextlib import closing

DB_NAME = "jobbot.db"


def init_db():
    """Erstellt die Datenbank und Tabelle, falls sie noch nicht existiert."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                keyword TEXT,
                description TEXT,
                url TEXT
            )
        """)
        conn.commit()


def insert_jobs(jobs):
    """Fügt eine Liste von Jobs in die Datenbank ein."""
    if not jobs:
        return

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        for job in jobs:
            cur.execute("""
                INSERT INTO jobs (title, company, location, keyword, description, url)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                job.get("title", ""),
                job.get("company", ""),
                job.get("location", ""),
                job.get("keyword", ""),
                job.get("description", ""),
                job.get("url", "")
            ))
        conn.commit()


def fetch_jobs(limit=50):
    """Liest die letzten Jobs aus der DB."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT title, company, location, keyword, description, url
            FROM jobs
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))
        return cur.fetchall()


# Initialisierung beim Import
init_db()
