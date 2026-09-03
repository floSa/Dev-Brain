# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_data.py — descend 8 des 13 notions `concept/data` dans l'arbre.

Lot 4, domaine « Data & pipelines ». Deux gestes par page : réécrire la ligne
`categorie:` du frontmatter, puis `git mv` vers le dossier que `AI/scripts/arbo.py`
dérive de cette catégorie. Le CORPS des notions n'est pas touché.

**Huit sur treize, et c'est voulu.** `v3-arborescence.md` note dès le lot 3 que
« aucune [des 13] n'est propre à ce domaine ». Cinq appellent un sous-domaine hors
du périmètre de cette conversation ; la consigne de floSa est de ne PAS les déplacer
et de les remonter. Elles sont listées dans RESTENT ci-dessous, avec l'effet de seuil
mesuré pour chacune — mesure faite AVANT de décider, comme l'exige la remontée 3.

Usage : uv run AI/migration/scripts/migrate_lot4_data.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

# nom de fichier (sans .md) -> categorie cible
CIBLES = {
    # --- data/scraping : le hub du sous-dossier porte déjà les 10 briques du sujet.
    "Web scraping": "data/scraping",

    # --- data/format : le rangement physique sur disque. La page décrit partitions,
    #     bucketing et taille de fichiers sur stockage objet ; ses voisins de dossier
    #     sont Parquet, Avro et Apache Iceberg. Le corps du hub de domaine la cite
    #     dans sa puce « format sur disque ».
    "Partitionnement & layout de données": "data/format",

    # --- data/ingestion : rapatrier depuis une source. Arbitrage sourcé sur la page
    #     elle-même, qui écrit « Debezium, Fivetran / Airbyte — candidats
    #     `data/ingestion` » : la page dit où vit son outillage (remontée 2).
    "Change Data Capture (CDC)": "data/ingestion",

    # --- data/streaming : traiter au fil de l'eau. Le corps du hub de domaine :
    #     « Traiter au fil de l'eau plutôt que par lots -> Flink, et Stream processing
    #     pour la théorie. »
    "Stream processing": "data/streaming",

    # --- data/fiabilite : VALEUR NOUVELLE. Ce qu'un pipeline doit garantir, quel que
    #     soit l'outil qui l'exécute. Le corps du hub les tient déjà ensemble :
    #     « Un pipeline se juge sur sa rejouabilité avant sa vitesse. »
    "ELT vs ETL & idempotence": "data/fiabilite",
    "Architecture médaillon": "data/fiabilite",
    "Contrats de données & qualité": "data/fiabilite",
    "Versionnage de données": "data/fiabilite",
}

# Les cinq qui NE bougent pas — consigne 3 de floSa : une notion qui appelle un
# sous-domaine hors des quatre domaines de cette conversation se remonte, elle ne se
# déplace pas. L'effet de seuil est mesuré pour chacune, et il est nul : aucune ne
# forcerait de restructuration. La décision reste à floSa.
RESTENT = {
    "ORM": ("database/orm", "3 -> 4 pages, sous le seuil, pas de dossier"),
    "Migrations de schéma": ("database/migration", "3 -> 4 pages, sous le seuil"),
    "Bases de données vectorielles": ("database/vecteur", "12 -> 13, « Vectoriel/ » existe"),
    "Index ANN — internes": ("database/vecteur", "-> 14, « Vectoriel/ » existe"),
    "Notebooks-as-code": ("devtools/notebook", "5 -> 6, « Notebooks/ » existe"),
}


def recategoriser(path: Path, cible: str) -> None:
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def main() -> int:
    dry = "--dry-run" in sys.argv
    manquants = [n for n in list(CIBLES) + list(RESTENT)
                 if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")

    cats = list(CIBLES.values())
    for md in (VAULT / arbo.DOM_LABEL["data"]).rglob("*.md"):
        for ligne in md.read_text(encoding="utf-8").split("\n")[:40]:
            if ligne.startswith("categorie:"):
                cats.append(ligne.split(":", 1)[1].strip())
    promus = arbo.promotions(cats)
    print(f"sous-domaines promus : {sorted(promus)}")

    print()
    print("-- les notions qui descendent --")
    for nom, cible in sorted(CIBLES.items()):
        src = SOURCE / f"{nom}.md"
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:38} {cible:20} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    print()
    print("-- les notions REMONTEES, qui ne bougent pas (consigne 3) --")
    for nom, (cible, effet) in sorted(RESTENT.items()):
        print(f"  {nom:38} appellerait {cible:22} {effet}")

    print()
    print("-- les briques que la promotion deplace --")
    bouges = 0
    dom = VAULT / arbo.DOM_LABEL["data"]
    for md in sorted(dom.rglob("*.md")):
        fm = md.read_text(encoding="utf-8").splitlines()[:40]
        if any(l.strip() == "role: hub" for l in fm):
            continue
        cat = next((l.split(":", 1)[1].strip() for l in fm
                    if l.startswith("categorie:")), "")
        attendu = VAULT / arbo.dossier_attendu(cat, promus)
        if md.parent == attendu:
            continue
        bouges += 1
        print(f"  {md.stem:38} {cat:20} -> "
              f"{(attendu / md.name).relative_to(VAULT).as_posix()}")
        if dry:
            continue
        attendu.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                        str((attendu / md.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)

    verbe = "a deplacer" if dry else "deplacee(s)"
    print()
    print(f"{len(CIBLES)} notion(s) et {bouges} brique(s) {verbe} ; "
          f"{len(RESTENT)} remontee(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
