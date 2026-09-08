# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_arbo.py — PONT vers `brainkit valider`. La STRUCTURE, et elle seule.

    uv run AI/scripts/check_arbo.py

Sort en 1 si une règle de structure est violée en DUR, en 0 sinon. Trois règles
du kit, qui sont exactement les quatre contrôles de l'ancien script :

    chemin_categorie      concordance chemin ↔ `categorie:`, seuil de promotion
                          et son plafond compris — la dérivation est UNE, et
                          c'est elle qui décide du dossier attendu ;
    hub_par_niveau        tout niveau du chemin porte son hub, pas seulement la
                          feuille ;
    frontmatter_lisible   un frontmatter illisible est une ERREUR, jamais une
                          absence — la leçon R17, née d'une page sautée en
                          silence pour un `pitch:` non quoté contenant « : ».

# Pourquoi cette entrée survit alors que le kit n'a qu'UN validateur

BrainKit a fusionné `check_brain.py` et `check_arbo.py` en un seul moteur. Les
deux entrées restent, et ce n'est pas de la nostalgie : `cloturer-brain` les
lance toutes les deux, et sa mise en garde — « ne lancer que `check_brain` et
croire le vault validé » — reste vraie. Un verdict de 111 avertissements où l'on
cherche à l'œil les trois lignes de structure n'est pas le même outil qu'un
verdict de structure.

Ce que ce pont ne fait plus, et qu'il faut savoir : il ne propose plus le
`git mv` en toutes lettres. Le kit dit le dossier attendu, ce qui est la même
information ; la phrase, elle, n'a pas survécu à la réécriture.

Où vit le kit : `AI/scripts/_pont_kit.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402

# Les règles du kit qui portent la structure. Fermée volontairement : une règle
# de CONTENU qui entrerait ici rendrait les deux entrées redondantes, et la mise
# en garde de `cloturer-brain` fausse.
STRUCTURE = ("chemin_categorie", "hub_par_niveau", "frontmatter_lisible")


def main() -> int:
    _pont_kit.sortie_utf8()
    _pont_kit.branche()
    from brainkit.valider import charge, valide              # noqa: PLC0415
    from brainkit.valider import constat                     # noqa: PLC0415

    mo = charge(_pont_kit.manifeste())
    v = valide(mo, _pont_kit.VAULT)

    tenus = [c for c in v.rapport.constats if c.regle in STRUCTURE]
    dures = [c for c in tenus if c.severite == constat.DURE]
    autres = [c for c in tenus if c.severite != constat.DURE]

    par_dom: dict[str, int] = {}
    for p in v.contexte.pages:
        if "/" in p.chemin:
            tete = p.chemin.split("/", 1)[0]
            par_dom[tete] = par_dom.get(tete, 0) + 1

    print(f"check_arbo : {len(v.contexte.pages)} page(s) dans "
          f"{len(par_dom)} dossier(s) de premier niveau — règles de structure : "
          f"{', '.join(STRUCTURE)}")
    for dom, n in sorted(par_dom.items()):
        print(f"  {dom}/ — {n} page(s)")

    for c in sorted(autres, key=lambda c: (c.regle, c.page)):
        print(f"  [WARN] {c.regle} — {c.rendu()}")
    if dures:
        print(f"\n{len(dures)} écart(s) :")
        for c in sorted(dures, key=lambda c: (c.regle, c.page)):
            print(f"  [FAIL] {c.regle} — {c.rendu()}")
        return 1
    print("\nOK — chemin et catégorie concordent partout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
