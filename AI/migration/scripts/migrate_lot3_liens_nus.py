# /// script
# requires-python = ">=3.10"
# ///
"""migrate_lot3_liens_nus.py — lot 3, passe préalable : tout wikilink devient nu.

Spécification : AI/migration/lot-3-arborescence.md, section « Les wikilinks ».
Arbitrage rendu par floSa le 2026-09-04 : option « tout passer en nu », étendue au
vault entier en une passe, AVANT le moindre `git mv`.

Pourquoi maintenant. Un lien qualifié porte l'ancien chemin ; il casse au déplacement.
Le lot 3 déplace 682 fichiers en 20 conversations, et les lots 4, 5 et 6 en déplaceront
encore. Ne réparer que les liens qui cassent à chaque domaine rouvrirait le chantier
vingt fois. Obsidian résout un lien nu par nom de fichier : une fois le vault dénudé,
un déplacement ne touche plus aucun lien.

Transformation, sur le CORPS et le FRONTMATTER (les deux portent des wikilinks —
`alternatives:` en porte 796 à lui seul) :

    [[Dev/Services/Postgres|Postgres]]   ->  [[Postgres]]        (alias = nom de fichier)
    [[Dev/Services/Postgres|la base]]    ->  [[Postgres|la base]] (alias conservé)
    [[Dev/Services/Postgres]]            ->  [[Postgres]]        (36 cas, sans alias)
    [[Wiki/Concepts/PCA#Les maths|PCA]]  ->  [[PCA#Les maths|PCA]] (ancre conservée)

Un lien déjà nu n'est pas touché. Une ancre `#` ou `#^` est reportée telle quelle.
Les fins de ligne sont conservées (lecture/écriture en `newline=""`, Python 3.10+).

EXCEPTIONS — les collisions de basename
---------------------------------------
Dénuder un lien dont le nom de fichier n'est pas unique le rend ambigu : Obsidian
résout par nom, sans tenir compte de la casse. Le script calcule les collisions sur
le vault réel et REFUSE de dénuder ces cibles-là ; elles restent qualifiées et sont
listées en fin de rapport.

`MOC/` est exclu du calcul des collisions : la v3 le supprime, et sa page
`MOC/Categories/Bases de données.md` fusionne avec la notion homonyme à l'étape 4 du
lot 3. La collision qu'elles forment aujourd'hui n'existera plus.

Usage :
    uv run AI/migration/scripts/migrate_lot3_liens_nus.py --dry-run   # rapport seul
    uv run AI/migration/scripts/migrate_lot3_liens_nus.py             # écrit
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]

# Périmètre d'écriture : les 646 pages du brain, plus les quelques pages de service
# qui portent des liens qualifiés à la main. `MOC/` en est absent — il est REGÉNÉRÉ
# par build_mocs.py, réécrire ses fichiers ici serait écraser du généré.
SCAN_DIRS = ["Dev", "Wiki", "Templates", "Documentation"]
SCAN_ROOT_FILES = ["Home.md"]

# Dossiers ignorés pour le calcul des noms résolvables (copies complètes du vault).
HORS_VAULT = {".git", ".claude"}
# Ignoré pour le calcul des collisions : supprimé par la v3 (cf. docstring).
COLLISION_IGNORE = {"MOC"}

LINK = re.compile(r"(!?)\[\[([^\[\]|]+?)(?:\|([^\[\]]*))?\]\]")


def basenames() -> dict[str, list[str]]:
    """Nom de fichier (minuscule) -> chemins qui le portent, hors `MOC/`."""
    idx: dict[str, list[str]] = collections.defaultdict(list)
    for ext in ("*.md", "*.base"):
        for p in VAULT.rglob(ext):
            parts = p.relative_to(VAULT).parts
            if not parts or parts[0] in HORS_VAULT or parts[0] in COLLISION_IGNORE:
                continue
            idx[p.stem.lower()].append(p.relative_to(VAULT).as_posix())
    return idx


def cibles_ambigues(idx: dict[str, list[str]]) -> set[str]:
    return {k for k, v in idx.items() if len(v) > 1}


def fichiers() -> list[Path]:
    out: list[Path] = []
    for d in SCAN_DIRS:
        base = VAULT / d
        if base.exists():
            out += sorted(base.rglob("*.md"))
    for f in SCAN_ROOT_FILES:
        if (VAULT / f).exists():
            out.append(VAULT / f)
    return out


def denuder(texte: str, ambigus: set[str], garde: collections.Counter) -> tuple[str, int]:
    """Réécrit les wikilinks qualifiés du texte. Renvoie (texte, nombre de réécritures)."""
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        embed, cible, alias = m.group(1), m.group(2), m.group(3)
        tete, sep, ancre = cible.partition("#")
        tete = tete.strip()
        if "/" not in tete:
            return m.group(0)  # déjà nu
        nom = tete.split("/")[-1]
        if nom.lower() in ambigus:
            garde[nom] += 1
            return m.group(0)  # collision : on garde le chemin, seule désambiguïsation
        n += 1
        nouvelle = nom + sep + ancre
        if alias is not None and alias.strip() != nom:
            return f"{embed}[[{nouvelle}|{alias}]]"
        return f"{embed}[[{nouvelle}]]"

    return LINK.sub(sub, texte), n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="n'écrit rien, imprime le rapport")
    args = ap.parse_args()

    idx = basenames()
    ambigus = cibles_ambigues(idx)
    garde: collections.Counter = collections.Counter()

    total = 0
    touches = 0
    for p in fichiers():
        with p.open("r", encoding="utf-8", newline="") as fh:
            avant = fh.read()
        apres, n = denuder(avant, ambigus, garde)
        if n:
            total += n
            touches += 1
            if not args.dry_run:
                with p.open("w", encoding="utf-8", newline="") as fh:
                    fh.write(apres)

    mode = "SIMULATION" if args.dry_run else "ÉCRIT"
    print(f"{mode} — {total} lien(s) dénudé(s) dans {touches} fichier(s)")
    if ambigus:
        print(f"\n{len(ambigus)} nom(s) de fichier en collision — jamais dénudés :")
        for nom in sorted(ambigus):
            print(f"  {nom} -> {idx[nom]}")
    if garde:
        print(f"\nLiens laissés qualifiés faute d'un nom unique : {sum(garde.values())}")
        for nom, n in sorted(garde.items()):
            print(f"  [[.../{nom}]] — {n} occurrence(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
