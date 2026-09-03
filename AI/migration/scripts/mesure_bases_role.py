# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""mesure_bases_role.py — les membres d'un `.base` avec et sans clause de rôle.

Lot 4. Jusqu'au lot 3, un `.base` qui filtrait `categorie == "<dom>/<sub>"` ne
pouvait sélectionner que des BRIQUES : les notions portaient `concept/*`, un
vocabulaire disjoint. Le lot 4 supprime cette disjonction — une notion se range
désormais sur la même `categorie:` que les briques de son dossier — et chacune de
ces vues absorbe donc, en silence, les notions de son sous-domaine.

Le validateur ne peut pas le voir : R8b ne se plaint que d'un comparatif à MOINS de
deux membres. Ajouter des membres le rend plus silencieux, jamais plus bruyant.

Ce script énumère, pour chaque `.base`, les membres actuels et ceux qu'il aurait
avec `role == "brique"` ajouté à son filtre. La différence est exactement ce que la
vue a absorbé sans qu'on le demande.

Usage : uv run AI/migration/scripts/mesure_bases_role.py
"""

from __future__ import annotations

import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import check_brain as cb  # noqa: E402

import yaml  # noqa: E402


def main() -> int:
    actives = cb.pages_actives() if hasattr(cb, "pages_actives") else None
    if actives is None:
        # check_brain assemble sa liste dans main() ; on la refait ici, mêmes règles.
        actives = []
        for md in sorted(VAULT.rglob("*.md")):
            if cb.hors_vault(md, VAULT):
                continue
            txt = md.read_text(encoding="utf-8")
            if not txt.startswith("---"):
                continue
            parts = txt.split("---", 2)
            if len(parts) < 3:
                continue
            try:
                fm = yaml.safe_load(parts[1])
            except yaml.YAMLError:
                continue
            if not isinstance(fm, dict) or "role" not in fm:
                continue
            actives.append((cb.rel(md), fm, parts[2]))

    total_absorbe = 0
    for base in sorted(VAULT.rglob("*.base")):
        if cb.hors_vault(base, VAULT):
            continue
        doc = yaml.safe_load(base.read_text(encoding="utf-8")) or {}
        filt = doc.get("filters")
        if filt is None:
            continue
        avec, sans = [], []
        indecidable = False
        for path, fm, _ in actives:
            r = cb.base_match(filt, path, fm)
            if r is None:
                indecidable = True
                break
            if r:
                sans.append((path, fm.get("role")))
                if fm.get("role") == "brique":
                    avec.append(path)
        nom = cb.rel(base)
        if indecidable:
            print(f"  [?] {nom} : filtre non évaluable hors ligne")
            continue
        intrus = [p for p, role in sans if role != "brique"]
        if intrus:
            total_absorbe += len(intrus)
            print(f"  [!] {nom} : {len(sans)} membre(s) dont {len(intrus)} NON-brique "
                  f"-> {len(avec)} avec `role == \"brique\"`")
            for p in intrus:
                print(f"         absorbé : {p}")
    print()
    print(f"{total_absorbe} page(s) absorbée(s) par un comparatif qui ne devrait pas "
          f"les contenir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
