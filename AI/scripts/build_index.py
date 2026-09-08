# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_index.py — PONT vers `brainkit generer --quoi index`. Le catalogue machine et le document humain.

    uv run AI/scripts/build_index.py            # écrit dans le vault
    uv run AI/scripts/build_index.py --check    # n'écrit rien, sort en 2 s'il reste un écart

Produit `AI/index/brain-index.json` (lu par les skills et par `query_index.py`)
et `AI/index/brain-index.md` (lu par floSa). Les deux sortent du même jeu
d'entrées, dans le même ordre : tri stable, aucun horodatage — sans quoi deux
régénérations d'un vault inchangé ne produiraient pas le même octet.

`generated_by` du catalogue vaut `AI/scripts/build_index.py`, et c'est exact :
la signature nomme le fichier qu'on lance, pas le paquet qui fait le travail.
Elle est déclarée dans `brain.yml`, bloc `genere.index.signature`.

# Ce que le lot 9 a changé dans l'artefact, et c'est tout

La clé `scanned` ne publie plus que les dossiers qui **portent au moins une
page**. Avant, elle publiait tout dossier de premier niveau hors `non_pages`,
suivi par git ou non : le catalogue committé annonçait
`obsidian_outer_backup_20260907`, une sauvegarde locale qui n'existe plus, et
`.githooks`, qui ne porte aucune page. Un artefact versionné cessait donc d'être
reproductible — deux machines, deux catalogues. Deux lignes de moins, aucune
page touchée.

# Le moteur de zone AUTO, et ce qui n'a pas changé

Le kit reprend le contrat mot pour mot : balises dédiées, remplacement en bloc,
préservation de ce qui est écrit à la main autour, **idempotence** — zéro octet
écrit si rien ne change — et `--check` qui sort en 2. Le lot 4 de BrainKit l'a
prouvé sur ce vault même : 413 artefacts sur 414 régénérés identiques à l'octet,
le 414e étant la clé `scanned` du catalogue, corrigée par le lot 9.

Où vit le kit : `AI/scripts/_pont_kit.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402

QUOI = "index"


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
