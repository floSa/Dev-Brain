# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""check_brain.py — PONT vers `brainkit valider`. Le contenu des pages.

    uv run AI/scripts/check_brain.py
    uv run AI/scripts/check_brain.py --regle voisinage_declare
    uv run AI/scripts/check_brain.py --tout

Sort en 1 si une règle DURE est violée, en 0 sinon. Contrat de sortie inchangé
depuis le lot 8 : une ligne `[FAIL]` par violation dure, `[WARN]` par
avertissement, et une dernière ligne `OK — aucune violation dure. (N
avertissement(s))` que `cloturer-brain` lit avec `tail -1` et que le hook Stop
`stop_check_brain.py` filtre sur `[FAIL]`.

# Ce que ce fichier n'est plus

Les 1 500 lignes de règles du DevBrain, écrites entre le lot 2 et le lot 8, ont
été **réécrites dans BrainKit et branchées sur `brain.yml`** — pas copiées. Le
lot 3 de BrainKit l'a prouvé par le verdict et non par la ressemblance du code :
même verdict règle par règle, même compte de violations, 0 dure et 111
avertissements. Ce qui a disparu au passage est la dette v1 (`V1_MARKERS`,
`is_active_v2()`), que le kit n'avait aucune raison d'hériter.

Les deux validateurs du vault sont devenus **un seul** moteur. Les deux entrées
survivent parce que `cloturer-brain` les nomme et parce qu'elles ne contrôlent
toujours pas la même chose : celle-ci rend le verdict entier, `check_arbo.py`
rend les seules règles de STRUCTURE. Aucune ne remplace l'autre — cf. la mise en
garde de `cloturer-brain`.

Où vit le kit, et pourquoi ce pont existe : `AI/scripts/_pont_kit.py`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402


def main() -> int:
    _pont_kit.sortie_utf8()
    _pont_kit.branche()
    from brainkit.valider import charge, imprime, valide     # noqa: PLC0415

    ap = argparse.ArgumentParser(
        description="Valide le contenu des pages du vault contre `brain.yml`.")
    ap.add_argument("--regle", default=None,
                    help="n'imprimer que les constats d'une règle")
    ap.add_argument("--tout", action="store_true",
                    help="imprimer aussi les notes")
    ns = ap.parse_args()

    mo = charge(_pont_kit.manifeste())
    v = valide(mo, _pont_kit.VAULT)
    return imprime(v, mo, _pont_kit.VAULT, regle=ns.regle, tout=ns.tout)


if __name__ == "__main__":
    raise SystemExit(main())
