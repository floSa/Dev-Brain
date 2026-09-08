# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_mocs.py — PONT vers `brainkit generer --quoi hubs`. Les zones AUTO des hubs.

    uv run AI/scripts/build_mocs.py            # écrit dans le vault
    uv run AI/scripts/build_mocs.py --check    # n'écrit rien, sort en 2 s'il reste un écart

Remplit les zones `<!-- AUTO -->` des 74 hubs : les 67 hubs de l'arbre depuis
`ls` de leur dossier, les 6 hubs de `Métiers/` depuis le champ `domaines:`, et
`Comparatifs/Comparatifs.md` depuis le rôle. Le **corps** d'un hub, hors zone
AUTO, s'écrit à la main et n'est jamais touché.

Le kit boucle sur `axes.transverses` au lieu de coder un seul axe : le DevBrain
n'en déclare qu'un (`domaines:` → `Métiers/`), et la forme d'avant était juste
*parce qu'il n'en a qu'un*. Ce qui a été jeté au passage : `MOC_CONCEPT`,
`WIKI_LABEL` et `wiki_group()`, branches mortes pour des dossiers supprimés à la
clôture du lot 4 de la migration v3.

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

QUOI = "hubs"


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
