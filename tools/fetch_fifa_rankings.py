"""
Récupère le classement mondial FIFA depuis Wikipédia et l'enregistre en CSV.

Source : https://en.wikipedia.org/wiki/Module:SportsRankings/data/FIFA_World_Rankings
Ce module Wikipédia est écrit en Lua. Le script télécharge le code brut, en
extrait la table `data.rankings` par expression régulière, et écrit le résultat
dans data/raw/fifa_rankings.csv.

Colonnes du CSV produit : rank, team, rank_change, points

Usage (depuis la racine du projet, venv activé) :
    python tools/fetch_fifa_rankings.py
"""
import csv
import os
import re
import urllib.request

URL = (
    "https://en.wikipedia.org/wiki/"
    "Module:SportsRankings/data/FIFA_World_Rankings?action=raw"
)
OUTPUT = os.path.join(
    os.path.dirname(__file__), "..", "data", "raw", "fifa_rankings.csv"
)


def download_module(url):
    """Télécharge le code Lua brut du module Wikipédia."""
    # Wikipédia refuse les requêtes sans User-Agent identifiable (erreur 403).
    request = urllib.request.Request(
        url, headers={"User-Agent": "AptispaceProjetDataScience/1.0 (educational)"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_rankings(lua_text):
    """Extrait les entrées { "Pays", rang, variation, points } de la table rankings."""
    # On isole d'abord le bloc data.rankings = { ... }, fermé par un } en début de ligne.
    block = re.search(
        r"data\.rankings\s*=\s*\{(.*?)^\}", lua_text, re.DOTALL | re.MULTILINE
    )
    if not block:
        raise ValueError("Table 'data.rankings' introuvable dans le module.")
    # Chaque entrée : { "Nom", rang(entier), variation(entier signé), points(décimal) }
    entry = re.compile(
        r'\{\s*"([^"]+)"\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*([\d.]+)\s*\}'
    )
    rows = []
    for name, rank, change, points in entry.findall(block.group(1)):
        rows.append(
            {
                "rank": int(rank),
                "team": name,
                "rank_change": int(change),
                "points": float(points),
            }
        )
    return rows


def parse_update_date(lua_text):
    """Récupère la date de mise à jour du classement, si présente."""
    match = re.search(
        r"updated\s*=\s*\{[^}]*?day\s*=\s*(\d+)[^}]*?month\s*=\s*'([^']+)'"
        r"[^}]*?year\s*=\s*(\d+)",
        lua_text,
        re.DOTALL,
    )
    if match:
        return f"{match.group(1)} {match.group(2)} {match.group(3)}"
    return "inconnue"


def main():
    print("Téléchargement du module FIFA depuis Wikipédia...")
    lua = download_module(URL)

    rankings = parse_rankings(lua)
    update_date = parse_update_date(lua)

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["rank", "team", "rank_change", "points"]
        )
        writer.writeheader()
        writer.writerows(rankings)

    print(f"OK : {len(rankings)} équipes écrites dans {os.path.normpath(OUTPUT)}")
    print(f"Classement daté du : {update_date}")


if __name__ == "__main__":
    main()
