# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_links.py — carte des liens & tags du DevBrain v2 + sujets à créer.

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
SCAN = ["Dev", "Wiki"]
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
    return scan_dir == "Dev" or not (V1 & set(fm.keys()))


def main() -> int:
    pages = []
    for d in SCAN:
        base = VAULT / d
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            fm, body = parse(md.read_text(encoding="utf-8"))
            if fm is None or not active(d, fm):
                continue
            pages.append({
                "nom": fm.get("nom") or md.stem, "stem": md.stem,
                "gal": fm.get("galaxie"), "type": fm.get("type"),
                "tags": fm.get("tags") or [], "alias": fm.get("alias") or [],
                "outs": [t.strip().split("/")[-1] for t in LINK.findall(body)],
            })

    byname = {}
    for p in pages:
        byname[p["nom"].lower()] = p
        byname[p["stem"].lower()] = p

    # cibles résolvables : toutes les pages .md + vues .base du vault (hors .git)
    resolvable = set()
    for ext in ("*.md", "*.base"):
        for f in VAULT.rglob(ext):
            if ".git" not in f.parts:
                resolvable.add(f.stem.lower())

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
            elif not key.startswith("rex - "):
                unresolved.append((p["nom"], t))
        p["res"] = sorted(set(res))

    tagpages: dict[str, list[str]] = {}
    for p in pages:
        for tg in p["tags"]:
            tagpages.setdefault(tg, []).append(p["nom"])

    covered = set()
    for p in pages:
        if p["type"] == "concept":
            covered.add(slug(p["nom"]))
            for a in p["alias"]:
                covered.add(slug(a))

    L = ["# Carte des liens — DevBrain v2", "",
         "> Généré par `AI/scripts/build_links.py`. Ne pas éditer à la main.",
         f"> {len(pages)} pages actives.", "", "## Par page", ""]
    for p in sorted(pages, key=lambda e: (e["gal"] or "", e["nom"].lower())):
        L.append(f"### {p['nom']}  ·  {p['gal']}/{p['type']}")
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
          "**Liens non résolus** (cibles inexistantes, hors `REX - *` en attente) :"]
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
