import requests


def search(what, where, limit=20):
    """
    Jobsuche über die öffentliche Arbeitsagentur-API.
    Gibt ein JSON zurück, das 'stellenangebote' enthält.
    """
    params = {
        "angebotsart": "1",
        "page": "1",
        "pav": "false",
        "size": str(limit),
        "umkreis": "25",
        "was": what,
        "wo": where,
    }
    headers = {
        "User-Agent": "Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4",
        "Host": "rest.arbeitsagentur.de",
        "X-API-Key": "jobboerse-jobsuche",
        "Connection": "keep-alive",
    }
    url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs"

    response = requests.get(url, headers=headers, params=params, timeout=15)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Mini-Test in der Konsole, Bei Bedarf kannst du api.py auch alleine ausführen (kleiner Konsolentest)
    what = input("🔎 Wonach suchst du? (z. B. 'Python Entwickler'): ") or "Python Entwickler"
    where = input("📍 Wo soll gesucht werden? (z. B. 'Berlin'): ") or "Berlin"

    result = search(what, where, limit=5)

    if "stellenangebote" in result:
        jobs = result["stellenangebote"]
        print(f"✅ Gefundene Jobs: {len(jobs)}")
        for j in jobs[:3]:
            print(f"- {j.get('titel')}, {j.get('arbeitgeber')}, {j.get('arbeitsort', {}).get('ort', '')}")
    else:
        print("⚠️ Keine Stellenangebote gefunden.")
