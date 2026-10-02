# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_carte.py — PONT vers `brainkit generer --quoi carte`. La carte de lecture.

    uv run AI/scripts/build_carte.py            # écrit dans le vault
    uv run AI/scripts/build_carte.py --check    # n'écrit rien, sort en 2 s'il reste un écart

Produit deux choses, sous `AI/index/` :

  - `carte.md` (L0) — moins de 100 lignes : chaque dossier, ses sous-dossiers
    promus, le nombre de pages par rôle, et le lien vers son fichier L1 ;
  - `carte/<Dossier>.md` (L1) — toutes les pages du dossier, tous rôles réunis,
    chacune avec son chemin et UNE ligne de description. Un dossier qui dépasse
    8 000 jetons est coupé par sous-dossier : « Machine Learning - 1 sur 3 ».

C'est le moyen de « prendre la vue d'ensemble » d'un domaine sans lire l'index
entier (~40 000 jetons, et sans description des notions) ni les hubs un à un.

# La description d'une ligne est extraite, jamais écrite

`brain.yml` (`genere.carte.descriptions`) dit où la lire, par rôle : le pitch
d'une brique, la première puce d'« Aperçu » pour une notion, la ligne « On
tranche sur » d'un comparatif, « Contexte » d'un pattern, « Principe » d'une
règle. Rien n'est stocké dans les pages.

Un fichier L1 sans source (dossier supprimé) est rapporté en écart et jamais
supprimé par le générateur : `--check` reste rouge jusqu'à un `git rm`.

Où vit le kit : `AI/scripts/_pont_kit.py`. Ce vault est figé : le générateur
`carte.py` est dans `AI/scripts/brainkit/`, reporté à la main (cf. `FIGE.md`).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402

QUOI = "carte"


def main() -> int:
    _pont_kit.sortie_utf8()
    _pont_kit.branche()
    from brainkit.generer.__main__ import main as generer   # noqa: PLC0415

    reste = [a for a in sys.argv[1:] if a != "--check"]
    mode = ["--check"] if "--check" in sys.argv[1:] else ["--ecrire"]
    sys.argv = ["brainkit generer", "--vault", str(_pont_kit.VAULT),
                "--quoi", QUOI, *mode, *reste]
    return generer()


if __name__ == "__main__":
    raise SystemExit(main())
