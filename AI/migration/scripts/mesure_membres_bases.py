# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""mesure_membres_bases.py — le relevé des membres de chaque `.base`, à comparer.

Lot 4. Complément de `mesure_bases_role.py`, qui ne signale qu'un intrus (une page
non-brique absorbée par une vue). Ce script-ci ne juge rien : il **énumère**, pour
chaque comparatif, ses membres actuels, un par ligne, dans un format stable et
diffable.

Motif — remontée 11 de `AI/migration/lot-4-notions.md` : R8b ne se plaint que d'un
comparatif à MOINS de deux membres, donc un comparatif qui gagne des membres devient
plus SILENCIEUX. Symétriquement, un comparatif qui en perd ne dit rien non plus. Le
seul moyen de voir l'un comme l'autre est de relever avant, de relever après, et de
`diff`. Un compteur qui BAISSE est un signal, pas une bonne nouvelle.

Usage : uv run AI/migration/scripts/mesure_membres_bases.py > avant.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import check_brain as cb  # noqa: E402

import yaml  # noqa: E402


def pages() -> list[tuple[str, dict]]:
    out = []
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
        if isinstance(fm, dict) and "role" in fm:
            out.append((cb.rel(md), fm))
    return out


def main() -> int:
    actives = pages()
    for base in sorted(VAULT.rglob("*.base")):
        if cb.hors_vault(base, VAULT):
            continue
        doc = yaml.safe_load(base.read_text(encoding="utf-8")) or {}
        filt = doc.get("filters")
        nom = cb.rel(base)
        if filt is None:
            print(f"{nom} : pas de filtre")
            continue
        membres, indecidable = [], False
        for path, fm in actives:
            r = cb.base_match(filt, path, fm)
            if r is None:
                indecidable = True
                break
            if r:
                membres.append((path, fm.get("role")))
        if indecidable:
            print(f"{nom} : filtre non évaluable hors ligne")
            continue
        print(f"{nom} : {len(membres)} membre(s)")
        for path, role in sorted(membres):
            print(f"    {role:10} {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
