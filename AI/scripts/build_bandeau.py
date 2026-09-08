# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""build_bandeau.py — PONT vers `brainkit generer --quoi bandeau`. Les bandeaux des 337 briques.

    uv run AI/scripts/build_bandeau.py            # écrit dans le vault
    uv run AI/scripts/build_bandeau.py --check    # n'écrit rien, sort en 2 s'il reste un écart

Compose la zone `<!-- AUTO:BANDEAU -->` des pages `role: brique` depuis leur
frontmatter : Nature, Licence, Exécution, Maturité. Les quatre colonnes, leurs
tables de libellés et le caractère affiché quand la source manque sont déclarés
dans `brain.yml`, bloc `bandeau:`.

La règle dure du lot 6 est portée par le kit sans une retouche : **une cellule
sans source dans le frontmatter affiche un tiret cadratin, jamais une valeur
plausible.** 39 bandeaux du vault ont aujourd'hui au moins une cellule vide, et
le rapport les nomme — une fiche vide honnêtement vaut mieux qu'une fiche
remplie au jugé.

`--check` est la forme vérifiable de la règle 9 du brain (« bandeau à jour »),
que `brain.yml` déclare **déléguée** à cette commande : le validateur ne la joue
pas, il dit qui la porte.

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

QUOI = "bandeau"


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
