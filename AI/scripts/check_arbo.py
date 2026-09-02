# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_arbo.py — le chemin d'une page concorde-t-il avec sa `categorie:` ?

Spec : AI/design/brain-v3.md §10 règle 2 et §11 · lot : AI/migration/lot-3-arborescence.md

Contrôle trois choses, et rien d'autre :

  1. **Concordance chemin / catégorie** — une page migrée vit dans le dossier que sa
     `categorie:` désigne (dérivation de AI/scripts/arbo.py). Le cas contraire est
     signalé avec le déplacement à faire.
  2. **Seuil de promotion** — un sous-domaine à 5 pages ou plus a son dossier ; un
     sous-domaine en dessous n'en a pas. Le seuil décide, pas l'humeur.
  3. **Hub par dossier** — tout dossier de l'arbre porte une page `role: hub` à son nom.

Sort en code 1 si un écart est trouvé. Les pages encore sous `Dev/` et `Wiki/` sont
comptées à part : elles n'ont pas de chemin à respecter tant que leur domaine n'est
pas passé au lot 3.

Usage : uv run AI/scripts/check_arbo.py
"""

from __future__ import annotations

import collections
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arbo  # noqa: E402

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv : uv run AI/scripts/check_arbo.py")

VAULT = Path(__file__).resolve().parents[2]


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


def dossiers_de_pages() -> list[Path]:
    return sorted(d for d in VAULT.iterdir()
                  if d.is_dir() and d.name not in arbo.NON_PAGES)


def main() -> int:
    migrees: list[tuple[Path, str]] = []   # pages descendues dans l'arbre
    legacy = 0                             # pages encore sous Dev/ ou Wiki/
    hubs: set[str] = set()

    for racine in dossiers_de_pages():
        for md in sorted(racine.rglob("*.md")):
            fm = parse_fm(md)
            if not fm:
                continue
            rel = md.relative_to(VAULT)
            if fm.get("role") == "hub":
                hubs.add(rel.parent.as_posix())
                continue
            if racine.name in arbo.LEGACY:
                legacy += 1
                continue
            migrees.append((rel, str(fm.get("categorie") or "")))

    ecarts: list[str] = []

    # (2) seuil de promotion — calculé sur la population réelle des pages migrées
    try:
        promus = arbo.promotions([cat for _, cat in migrees])
    except KeyError as e:
        print(f"[FAIL] {e}")
        return 1

    # (1) concordance chemin / catégorie
    for rel, cat in migrees:
        attendu = arbo.dossier_attendu(cat, promus)
        if attendu is None:
            ecarts.append(f"{rel.as_posix()} : `categorie: {cat or '(vide)'}` hors "
                          f"des 20 préfixes de DOM_LABEL — domaine indérivable")
            continue
        if rel.parent.as_posix() != attendu:
            ecarts.append(f"{rel.as_posix()} : `categorie: {cat}` attend "
                          f"`{attendu}/` — git mv à faire")

    # (3) un hub par dossier de l'arbre
    dossiers = {rel.parent.as_posix() for rel, _ in migrees}
    for d in sorted(dossiers):
        # tout niveau du chemin doit porter son hub, pas seulement la feuille
        parts = d.split("/")
        for i in range(1, len(parts) + 1):
            niveau = "/".join(parts[:i])
            if niveau not in hubs:
                ecarts.append(f"{niveau}/ : aucune page `role: hub` à son nom")

    par_dom: dict[str, int] = collections.Counter(
        rel.parts[0] for rel, _ in migrees)
    print(f"check_arbo : {len(migrees)} page(s) migrée(s) dans "
          f"{len(par_dom)} domaine(s) — {legacy} page(s) encore sous "
          f"{sorted(arbo.LEGACY)}")
    for dom, n in sorted(par_dom.items()):
        print(f"  {dom}/ — {n} page(s)")
    if ecarts:
        print(f"\n{len(ecarts)} écart(s) :")
        for e in sorted(set(ecarts)):
            print(f"  [FAIL] {e}")
        return 1
    print("OK — chemin et catégorie concordent partout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
