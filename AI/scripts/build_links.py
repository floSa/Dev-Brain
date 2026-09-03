# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_links.py — carte des liens & tags du DevBrain + sujets à créer.

Génère AI/index/liens.md (humain, régénéré à chaque build) :
  - Par page : tags · liens sortants · liens entrants (backlinks)
  - Tag → pages
  - À créer : liens non résolus + tags sans page concept dédiée

Usage : uv run AI/scripts/build_links.py
Cross-OS, chemins relatifs, sortie déterministe.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/build_links.py")

VAULT = Path(__file__).resolve().parents[2]
# Périmètre de balayage. Avant le lot 3, deux dossiers fixes : `Dev` et `Wiki`.
# Depuis, les pages descendent dans un arbre de DOMAINES à la racine (« Bases de
# données/ », « Machine Learning/ »…), et `Dev/`+`Wiki/` ne portent plus que les
# domaines pas encore migrés. On énumère donc par la NÉGATIVE : tout dossier de la
# racine qui n'est pas de l'outillage est un dossier de pages. Aucune table de
# domaines à tenir à jour, et le jour où `Dev/` et `Wiki/` disparaissent, rien à
# changer ici. Cf. AI/design/brain-v3.md §4 et §11.
NON_PAGES = {".git", ".claude", ".obsidian", "AI", "Documentation", "Templates",
             "Projects", "docs", "MOC"}


def scan_dirs() -> list[str]:
    """Dossiers de premier niveau qui portent des pages, triés."""
    return sorted(d.name for d in VAULT.iterdir()
                  if d.is_dir() and d.name not in NON_PAGES)
OUT = VAULT / "AI" / "index" / "liens.md"
V1 = {"created", "modified", "maturite", "lecture_min", "auteurs_cles",
      "sous_categories", "score", "mes_projets", "clients_officiels",
      "plateforme", "remplace", "url_officiel", "licence"}
LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def parse(t: str):
    if not t.startswith("---"):
        return None, t
    p = t.split("---", 2)
    if len(p) < 3:
        return None, t
    try:
        fm = yaml.safe_load(p[1])
    except yaml.YAMLError:
        return None, p[2]
    return (fm if isinstance(fm, dict) else None), p[2]


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return s.lower().strip().replace(" ", "-").replace("_", "-")


def active(scan_dir: str, fm: dict) -> bool:
    return scan_dir != "Wiki" or not (V1 & set(fm.keys()))


def hors_vault(p, racine) -> bool:
    """Le chemin est-il hors du perimetre logique du vault ?

    Les worktrees git vivent sous `.claude/worktrees/` et sont des copies completes :
    les balayer double tout. Le test porte sur le chemin RELATIF a la racine — un
    vault qui vit lui-meme sous `.claude/` (cas d'un worktree) reste entierement
    valide, seul son propre `.claude/` interne est ecarte.
    """
    try:
        parts = p.relative_to(racine).parts
    except ValueError:
        return True
    return bool(parts) and parts[0] in {".git", ".claude"}


def main() -> int:
    pages = []
    for d in scan_dirs():
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm, body = parse(md.read_text(encoding="utf-8"))
            if fm is None or not active(d, fm):
                continue
            pages.append({
                "nom": fm.get("nom") or md.stem, "stem": md.stem,
                "role": fm.get("role"),
                "tags": fm.get("tags") or [], "alias": fm.get("alias") or [],
                "outs": [t.strip().split("/")[-1] for t in LINK.findall(body)],
            })

    byname = {}
    for p in pages:
        byname[p["nom"].lower()] = p
        byname[p["stem"].lower()] = p

    # cibles résolvables : toutes les pages .md + vues .base du vault (hors .git)
    # Deux clés par fichier, comme `check_brain.resolvable_names` : le stem pour la
    # convention nue, le nom complet pour l'embed d'une vue `.base` par une page de
    # comparatif (lot 5). Sans la seconde, ces liens comptaient comme NON RÉSOLUS,
    # et la clôture exige 0.
    resolvable = set()
    for ext in ("*.md", "*.base"):
        for f in VAULT.rglob(ext):
            if not hors_vault(f, VAULT):
                resolvable.add(f.stem.lower())
                resolvable.add(f.name.lower())

    backlinks = {p["nom"]: set() for p in pages}
    unresolved = []
    for p in pages:
        res = []
        for t in p["outs"]:
            key = t.lower()
            if key in byname:
                nm = byname[key]["nom"]
                res.append(nm)
                backlinks[nm].add(p["nom"])
            elif key in resolvable:
                res.append(t)  # cible valide non-page (ex. une vue .base)
            else:
                unresolved.append((p["nom"], t))
        p["res"] = sorted(set(res))

    tagpages: dict[str, list[str]] = {}
    for p in pages:
        for tg in p["tags"]:
            tagpages.setdefault(tg, []).append(p["nom"])

    covered = set()
    for p in pages:
        if p["role"] == "notion":
            covered.add(slug(p["nom"]))
            for a in p["alias"]:
                covered.add(slug(a))

    L = ["# Carte des liens — DevBrain", "",
         "> Généré par `AI/scripts/build_links.py`. Ne pas éditer à la main.",
         f"> {len(pages)} pages actives.", "", "## Par page", ""]
    for p in sorted(pages, key=lambda e: (e["role"] or "", e["nom"].lower())):
        L.append(f"### {p['nom']}  ·  {p['role']}")
        L.append(f"- tags : {', '.join('`' + t + '`' for t in p['tags']) or '—'}")
        L.append(f"- liens sortants : {', '.join('[[' + x + ']]' for x in p['res']) or '—'}")
        bl = sorted(backlinks[p["nom"]])
        L.append(f"- liens entrants : {', '.join('[[' + x + ']]' for x in bl) or '—'}")
        L.append("")

    L += ["## Tags → pages", ""]
    for tg in sorted(tagpages):
        flag = "" if slug(tg) in covered else "  — pas de page concept dédiée"
        L.append(f"- `{tg}` : {', '.join(sorted(set(tagpages[tg])))}{flag}")

    L += ["", "## À créer (gaps)", "",
          "**Liens non résolus** (cibles inexistantes) :"]
    L += [f"- depuis [[{a}]] → `{b}`" for a, b in sorted(set(unresolved))] or ["- aucun"]
    L += ["", "**Tags sans page concept dédiée** (sujets candidats à créer) :"]
    missing = sorted(t for t in tagpages if slug(t) not in covered)
    L += [f"- `{t}` (porté par : {', '.join(sorted(set(tagpages[t])))})" for t in missing] or ["- aucun"]

    OUT.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"Carte écrite : {OUT.relative_to(VAULT).as_posix()} — {len(pages)} pages, "
          f"{len(unresolved)} lien(s) non résolu(s), {len(missing)} tag(s) sans page concept")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
