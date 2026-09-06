# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""lot6_fermer_complements.py — refermer les moitiés de couple `complements:`.

Le protocole parallèle du lot 6 demandait à une conversation qui voit un
appariement vers une fiche HORS de son périmètre de poser sa moitié et
d'inscrire l'autre dans ses remontées. Douze moitiés sont restées ouvertes,
plus un couple dont AUCUN lot n'était propriétaire (txtai / sentence-transformers,
remontée 2 du lot 2). Ce script ferme les treize, dans les deux sens.

Deux gestes par fermeture :

1. la cible gagne l'entrée dans son `complements:` de frontmatter ;
2. elle gagne la puce correspondante sous `### Compléments`, avec le **pitch
   courant** de la source réinjecté (règle 6) et le motif de l'appariement.

Quand la source figure déjà en `## Voir aussi`, la puce est **déplacée**, pas
dupliquée — précédent posé par le lot 2 sur `pgAdmin` et `MySQL Workbench`.

Idempotent.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[3]

# cible -> [(source, motif de l'appariement)]
FERMETURES = {
    "MLflow": [("Evidently", "le versant dérive et qualité des données, en aval du run suivi")],
    "LangChain": [("LangChain SQL agent", "son module text-to-SQL : SQLDatabaseToolkit et l'agent qui l'exploite")],
    "MongoDB Compass": [("MongoDB", "le moteur exploré — le client n'a pas d'objet sans lui")],
    "Redis Insight": [("Redis", "le moteur exploré — le client n'a pas d'objet sans lui")],
    "FastAPI": [("SQLModel", "la couche de persistance typée du même auteur, modèles partagés entre table et schéma d'API")],
    "Pydantic": [("SQLModel", "la variante ORM bâtie sur ce socle : un modèle sert de schéma et de table")],
    "Postgres": [
        ("TimescaleDB", "l'extension qui ajoute les hypertables et les agrégats continus, sans changer de moteur"),
        ("psycopg2", "le driver DB-API historique, sous la plupart des accès Python à cette base"),
    ],
    "Polars": [("connectorx", "le moteur derrière `read_database(engine=\"connectorx\")`")],
    "DuckDB": [("jupysql", "le compagnon notebook : du SQL analytique local en magic cell")],
    "Dash": [("plotly", "le moteur de rendu des graphes, du même éditeur")],
    "Dask": [("xarray", "les tableaux étiquetés qui dépassent la RAM en `chunks=`, la voie documentée du passage à l'échelle")],
    "txtai": [("sentence-transformers", "le socle d'embeddings sous-jacent")],
    "sentence-transformers": [("txtai", "l'index et les workflows qui se montent au-dessus des embeddings produits")],
}


def index() -> dict[str, Path]:
    out = {}
    for p in VAULT.rglob("*.md"):
        s = str(p.relative_to(VAULT)).replace("\\", "/")
        if s.startswith(("AI/", "Templates/", "Documentation/", ".claude/")):
            continue
        out.setdefault(p.stem, p)
    return out


def pitch(p: Path) -> str:
    fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
    return (fm.get("pitch") or "").strip()


def main() -> int:
    idx = index()
    poses = deplaces = 0
    for cible, sources in FERMETURES.items():
        p = idx[cible]
        txt = p.read_text(encoding="utf-8")

        # 1. frontmatter
        m = re.search(r"^complements: (.*)$", txt, re.M)
        if not m:
            raise SystemExit(f"{cible} : pas de champ complements:")
        actuels = [x for x in re.findall(r"\[\[([^\]|]+)", m.group(1))]
        neufs = [s for s, _ in sources if s not in actuels]
        if neufs:
            liste = actuels + neufs
            txt = txt[:m.start()] + "complements: [" + ", ".join(
                f'"[[{x}]]"' for x in liste) + "]" + txt[m.end():]

        # 2. puces
        for source, motif in sources:
            puce = f"- [[{source}]] — {pitch(idx[source])} — {motif}"
            if f"[[{source}]]" in (re.search(
                    r"\n### Compléments\n(.*?)(?=\n#{2,3} |\Z)", txt, re.S) or
                    type("", (), {"group": lambda *_: ""})()).group(1):
                continue
            # la source figure-t-elle déjà en « Voir aussi » ? alors on déplace.
            va = re.search(r"\n## Voir aussi\n(.*?)(?=\n## |\Z)", txt, re.S)
            if va:
                lignes = va.group(1).split("\n")
                restant = [l for l in lignes
                           if not (l.startswith("- ") and f"[[{source}]]" in l)]
                if len(restant) != len(lignes):
                    txt = txt[:va.start(1)] + "\n".join(restant) + txt[va.end(1):]
                    deplaces += 1
            # insertion sous ### Compléments, créée au besoin
            mc = re.search(r"\n### Compléments\n(.*?)(?=\n#{2,3} |\Z)", txt, re.S)
            if mc:
                bloc = mc.group(1).rstrip("\n")
                txt = txt[:mc.start(1)] + bloc + "\n" + puce + "\n\n" + txt[mc.end(1):]
            else:
                ma = re.search(r"\n### Alternatives\n(.*?)(?=\n#{2,3} |\Z)", txt, re.S)
                if not ma:
                    raise SystemExit(f"{cible} : ni ### Compléments ni ### Alternatives")
                bloc = ma.group(1).rstrip("\n")
                txt = (txt[:ma.start(1)] + bloc + "\n\n### Compléments\n\n"
                       + puce + "\n\n" + txt[ma.end(1):])
            poses += 1
        p.write_text(txt, encoding="utf-8")
    print(f"{poses} puce(s) de complément posée(s), dont {deplaces} déplacée(s) "
          f"depuis « Voir aussi ».")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
