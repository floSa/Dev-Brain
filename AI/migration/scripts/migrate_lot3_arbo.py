# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""migrate_lot3_arbo.py — lot 3 : déplace un domaine vers l'arbre v3, par `git mv`.

Spécification : AI/migration/lot-3-arborescence.md · arbre : AI/design/v3-arborescence.md

Le chemin d'une page se DÉRIVE de sa `categorie:` — personne ne choisit un dossier
(brain-v3 §4, règle 4). Ce script est cette dérivation, rendue exécutable :

    categorie: database/vecteur   ->  Bases de données/Vectoriel/Qdrant.md
    categorie: database/orm       ->  Bases de données/SQLAlchemy.md

La dérivation elle-même (tables DOM_LABEL / SUB_LABEL, seuil de promotion) vit dans
AI/scripts/arbo.py, partagée avec AI/scripts/check_arbo.py — celui qui déplace et
celui qui vérifie doivent appliquer exactement la même règle.

Le seuil de promotion est de 5 pages (brain-v3 §4, règle 2) : au-dessous, les pages
du sous-domaine restent au niveau du domaine. Il se compte sur les PAGES (`.md`) ;
les vues `.base` suivent leur catégorie sans peser sur le seuil — un comparatif
n'est pas un membre du comparatif.

Idempotent : il ne lit que `Dev/` et `Wiki/`. Relancé sur un domaine déjà migré, il
ne trouve plus rien et s'arrête.

Aucun `rm`, aucune écriture dans les fichiers : uniquement `git mv`.

Usage :
    uv run AI/migration/scripts/migrate_lot3_arbo.py database --dry-run
    uv run AI/migration/scripts/migrate_lot3_arbo.py database
"""

from __future__ import annotations

import argparse
import collections
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv.")

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCES = list(arbo.LEGACY)  # d'où partent les pages non encore migrées

# Les deux tables et le seuil vivent dans AI/scripts/arbo.py : la dérivation
# `categorie:` -> chemin doit être IDENTIQUE ici (qui déplace) et dans
# AI/scripts/check_arbo.py (qui vérifie). Deux copies dériveraient.


def parse_fm(p: Path) -> dict | None:
    txt = p.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def pages_du_domaine(prefixe: str) -> list[tuple[Path, str]]:
    """(chemin, categorie) des pages `.md` dont la `categorie:` est sous `prefixe/`."""
    out = []
    for d in SOURCES:
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm = parse_fm(md)
            if not fm:
                continue
            cat = str(fm.get("categorie") or "")
            if cat == prefixe or cat.startswith(prefixe + "/"):
                out.append((md, cat))
    return out


def bases_du_domaine(prefixe: str) -> list[tuple[Path, list[str]]]:
    """(chemin, catégories filtrées) des vues `.base` qui ne filtrent que ce domaine.

    Un `.base` dont le filtre nomme des catégories d'un SEUL domaine appartient à ce
    domaine. Les 9 comparatifs qui ne filtrent sur aucune `categorie:` (listés en
    « Hors arbre » de v3-arborescence.md) ne sont jamais captés ici : leur dossier
    se pose à la main.
    """
    out = []
    for base in sorted((VAULT / "Dev").rglob("*.base")):
        cats = re.findall(r'categorie\s*==\s*"([^"]+)"', base.read_text(encoding="utf-8"))
        cats += re.findall(r'categorie\.startsWith\("([^"]+)"\)',
                           base.read_text(encoding="utf-8"))
        if cats and all(c == prefixe or c.startswith(prefixe + "/") for c in cats):
            out.append((base, sorted(set(cats))))
    return out


def sous_domaines_promus(pages: list[tuple[Path, str]]) -> dict[str, str]:
    """{categorie complète: libellé du dossier} pour les sous-domaines au-dessus du seuil."""
    try:
        return arbo.promotions([cat for _, cat in pages])
    except KeyError as e:
        sys.exit(f"ARRÊT — {e}. Ne pas inventer un nom de dossier.")


def cible(src: Path, cat: str, domaine: str, promus: dict[str, str]) -> Path:
    dossier = VAULT / domaine
    if cat in promus:
        dossier = dossier / promus[cat]
    return dossier / src.name


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", str(src.relative_to(VAULT)), str(dst.relative_to(VAULT))],
                   cwd=VAULT, check=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefixe", help="préfixe de `categorie:` du domaine, ex. `database`")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.prefixe not in arbo.DOM_LABEL:
        sys.exit(f"Préfixe inconnu `{args.prefixe}` — connus : {sorted(arbo.DOM_LABEL)}")
    domaine = arbo.DOM_LABEL[args.prefixe]

    pages = pages_du_domaine(args.prefixe)
    if not pages:
        sys.exit(f"Aucune page de catégorie `{args.prefixe}/*`.")
    promus = sous_domaines_promus(pages)

    plan: list[tuple[Path, Path]] = [(src, cible(src, cat, domaine, promus))
                                     for src, cat in pages]
    for base, cats in bases_du_domaine(args.prefixe):
        cat = cats[0] if len(cats) == 1 else ""
        plan.append((base, cible(base, cat, domaine, promus)))

    par_dossier: dict[str, list[str]] = collections.defaultdict(list)
    for src, dst in plan:
        par_dossier[dst.parent.relative_to(VAULT).as_posix()].append(dst.name)
    for dossier in sorted(par_dossier):
        noms = sorted(par_dossier[dossier])
        print(f"\n{dossier}/  — {len(noms)} fichier(s)")
        for n in noms:
            print(f"    {n}")

    print(f"\n{len(plan)} fichier(s) — {len(par_dossier)} dossier(s) — "
          f"sous-domaines promus : {sorted(promus.values()) or 'aucun'}")
    if args.dry_run:
        print("SIMULATION — rien n'a bougé.")
        return 0
    for src, dst in plan:
        git_mv(src, dst)
    print("git mv effectués.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
