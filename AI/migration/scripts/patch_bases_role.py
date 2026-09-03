# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""patch_bases_role.py — ajoute `role == "brique"` au filtre des comparatifs.

Lot 4. Un comparatif compare des BRIQUES. Jusqu'au lot 3 la clause était inutile :
les notions portaient `concept/*`, un vocabulaire disjoint de celui des briques,
donc `categorie == "<dom>/<sub>"` ne pouvait sélectionner qu'une brique. Le lot 4
supprime cette disjonction — une notion se range sur la même `categorie:` que les
briques de son dossier — et chaque vue absorbe alors les notions de son sous-domaine.

R8b ne peut pas le voir : elle ne se plaint que d'un comparatif à MOINS de deux
membres. Ajouter des membres rend le validateur plus silencieux, jamais plus bruyant
— c'est exactement le profil de défaut de la remontée 5 du pilote stats.

La substitution est celle que le lot 3 a déjà appliquée à 9 comparatifs dont le
filtre croisait un chemin `Dev/Services/` (remontées 7, 14 et 16) : `role` dit ce
que le chemin ou la disjonction des vocabulaires disait, et ne bouge plus avec l'arbre.

Fidélité vérifiable avant / après par `mesure_bases_role.py` : la clause ne retire
que des pages `role: notion`, et ne touche aucune brique.

Usage : uv run AI/migration/scripts/patch_bases_role.py [--dry-run]
"""

from __future__ import annotations

import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
CLAUSE = '    - role == "brique"'
NOTE = ("    # Un comparatif compare des briques. Clause ajoutée au lot 4 : depuis que\n"
        "    # les notions se rangent sur la même `categorie:` que les briques, un filtre\n"
        "    # de catégorie seul absorbe les notions du sous-domaine.\n")


def main() -> int:
    dry = "--dry-run" in sys.argv
    touches = 0
    for base in sorted(VAULT.rglob("*.base")):
        if ".git" in base.parts:
            continue
        txt = base.read_text(encoding="utf-8")
        if 'role == "brique"' in txt:
            continue
        nl = "\r\n" if "\r\n" in txt else "\n"
        lignes = txt.split(nl)
        try:
            i = next(k for k, l in enumerate(lignes) if l.rstrip() == "  and:")
        except StopIteration:
            print(f"  [SKIP] {base.relative_to(VAULT).as_posix()} : pas de bloc `and:` "
                  "au premier niveau — à traiter à la main")
            continue
        touches += 1
        print(f"  {base.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        lignes[i + 1:i + 1] = NOTE.rstrip("\n").split("\n") + [CLAUSE]
        base.write_text(nl.join(lignes), encoding="utf-8")

    verbe = "à patcher" if dry else "patché(s)"
    print(f"\n{touches} comparatif(s) {verbe}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
