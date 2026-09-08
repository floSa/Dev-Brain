# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""sonder_amont.py — PONT vers `brainkit sonder`. La fraîcheur des 337 briques.

    uv run AI/scripts/sonder_amont.py                  # la passe complète
    uv run AI/scripts/sonder_amont.py --limit 60       # une passe bornée
    uv run AI/scripts/sonder_amont.py --recalculer     # AUCUN appel réseau
    uv run AI/scripts/sonder_amont.py --age-max-jours 30

Sonde l'amont de chaque brique — la dernière version publiée, le dernier commit,
l'archivage du dépôt — et range les faits dans `AI/index/fraicheur.json`. Le
bloc `amont:` de `brain.yml` déclare tout : les rôles concernés, le champ qui
porte l'URL, l'hôte et sa sonde, le registre de paquets, les deux seuils, le
chemin du side-car et le nom des deux faits que le bandeau affiche.

# Pourquoi ce pont existe alors que `mesurer` n'en a pas

Parce que celui-ci **entre dans une boucle de travail**. Le bandeau des 337
briques porte une colonne `Fraîcheur` dont la valeur vient du side-car : après
un sondage, `build_bandeau.py` a quelque chose à réécrire, et
`build_bandeau.py --check` sort en 2 tant qu'on ne l'a pas fait. La séquence
est donc : sonder, régénérer, clôturer.

`mesurer` n'a pas de pont parce qu'il ne déclenche rien ; celui-ci si.

# Ce qu'il ne fait pas, et ce n'est pas négociable

- **Aucune écriture dans une page.** Sa seule sortie est le side-car. Un
  désaccord entre l'amont et la fiche se **signale** — c'est la règle
  `amont_concorde` du validateur, en avertissement — il ne se corrige pas.
  `maturite:` reste ce que floSa a écrit.
- **Aucun `--fix`**, et il n'y en aura pas : le seul geste qu'il pourrait
  automatiser est précisément celui qui appartient à l'auteur.
- **Aucun jeton.** Les trois URL sondées sont celles qu'un navigateur charge,
  sans compte et sans quota d'API : `releases.atom`, `commits.atom`, et la page
  du dépôt pour le seul fait qui ne se lit pas ailleurs, l'archivage. L'API REST
  aurait donné tout cela en un appel — et 60 appels par heure sans jeton, soit
  plus de cinq heures pour une passe. Un jeton dans un vault versionné est un
  secret publié.
- **Il sort en 0 même quand il rapporte des amonts morts.** Un dépôt archivé
  n'est pas une faute du vault, et bloquer une clôture dessus rendrait le brain
  otage de l'amont. La règle vient de `verifier_fraicheur.py`, et elle tient.

# Ce qu'il ne remplace pas

`verifier_fraicheur.py`, qui garde ses règles **hors ligne** — URL mortes,
licences divergentes, corps qui décrit un déclin sous une `maturite:` vive,
croisement avec les puces de fin de vie des comparatifs. Il écrit désormais
`AI/index/fraicheur-hors-ligne.json` : deux écrivains sur un même fichier se
seraient effacés l'un l'autre en silence.

Où vit le kit : `AI/scripts/_pont_kit.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402


def main() -> int:
    _pont_kit.sortie_utf8()
    _pont_kit.branche()
    from brainkit.amont.__main__ import main as sonder      # noqa: PLC0415

    sys.argv = ["brainkit sonder", "--vault", str(_pont_kit.VAULT),
                *sys.argv[1:]]
    return sonder()


if __name__ == "__main__":
    raise SystemExit(main())
