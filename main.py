import os
from models import init_db
from dashboard import JobDashboard


def ensure_db():
    """Stellt sicher, dass jobbot.db existiert und initialisiert ist."""
    if not os.path.exists("jobbot.db"):
        print("⚙️ jobbot.db fehlt – wird erstellt...")
        init_db()
        print("✅ jobbot.db wurde erstellt.")


if __name__ == "__main__":
    ensure_db()
    app = JobDashboard()
    app.mainloop()
