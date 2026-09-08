# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_links.py — PONT vers `brainkit generer --quoi liens`. La carte des liens.

    uv run AI/scripts/build_links.py            # écrit dans le vault
    uv run AI/scripts/build_links.py --check    # n'écrit rien, sort en 2 s'il reste un écart

Produit `AI/index/liens.md` : mots-clés → pages, liens sortants, backlinks, et
la section « à créer » — les liens **non résolus**, qui sont le mécanisme de
backlog du vault. `cloturer-brain` lit cette dernière : un lien non résolu à
l'étape de clôture est un lien à créer ou à retirer, pas une ligne de rapport.

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

QUOI = "liens"


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
