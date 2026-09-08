"""arbo.py — PONT vers `brainkit.valider.chemins`. La dérivation `categorie:` → chemin.

Ce n'est **pas** un script : c'est la bibliothèque que `enrichir-brain` importe
pour savoir où se range une page avant de l'écrire. Son API publique est
inchangée depuis le lot 3 de la migration v3, et elle le reste :

    import sys; sys.path.insert(0, "AI/scripts")
    import arbo
    arbo.domaine("database/vecteur")                      # -> "Bases de données"
    arbo.promotions(["ml/socle", "ml/socle", ...])        # -> {valeur: libellé}
    arbo.dossier_attendu("database/vecteur", promus)      # -> "Bases de données/Vectoriel"

# Ce qui a changé sous la surface, et ce qui n'a pas changé du tout

Les trois tables — `DOM_LABEL` (20 préfixes), `DOM_RATTACHE` (1 rattachement),
`SUB_LABEL` (47 sous-libellés) — et le `SEUIL` ne sont plus écrits ici. Elles
sont dans `brain.yml`, bloc `axes.rangement.prefixes` / `rattachements` /
`seuil_promotion`, **avec le motif de chaque libellé** : « RAG & retrieval »
parce que « RAG » est déjà le nom d'une notion du dossier, « Évaluation de
modèles » parce que « Évaluation » est déjà le hub d'un autre domaine. Un
commentaire de code ne se lit pas depuis un skill ; un `motif:` du manifeste, si.

Conséquence pratique pour qui promeut un sous-domaine : le libellé s'ajoute
désormais dans `brain.yml`, sous le préfixe concerné — **plus dans `SUB_LABEL`**.
La règle n'a pas bougé : une sous-valeur qui franchit le seuil sans libellé
déclaré fait échouer la dérivation plutôt qu'inventer un nom de dossier.

`arbo.LEGACY`, vide depuis la clôture du lot 4, n'est pas reconduit : le kit
n'a pas de notion de dossier hérité, et une valeur morte qu'on transporte finit
par redevenir vraie.

Où vit le kit : `AI/scripts/_pont_kit.py`.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _pont_kit                                            # noqa: E402

_pont_kit.branche()

from brainkit.valider import chemins as _chemins            # noqa: E402
from brainkit.valider import charge as _charge              # noqa: E402

_MO = _charge(_pont_kit.manifeste())

#: Le seuil de promotion, lu dans le manifeste. Était `SEUIL = 5` en dur.
SEUIL: int = _MO.seuil

#: Les rôles rangés par leur rôle, pas par l'axe : ils n'ont pas de `categorie:`.
ROLES_SANS_CATEGORIE: set[str] = {
    r for r in _MO.roles if not _MO.porte_l_axe_de_rangement(r)}

#: Les rôles qui ne pèsent pas sur le seuil — « une vue n'est pas un membre de
#: la vue ». C'est `pese_sur_le_seuil: false` du manifeste.
ROLES_HORS_SEUIL: set[str] = {
    r for r in _MO.roles if not _MO.pese_sur_le_seuil(r)}


def domaine(categorie: str) -> str | None:
    """Le dossier de premier niveau d'une catégorie. `None` si le préfixe est inconnu."""
    return _MO.dossier_de_prefixe.get(str(categorie).split("/")[0])


def dossier_attendu(categorie: str, promus: dict[str, str]) -> str | None:
    """Le dossier d'accueil, relatif à la racine. `None` si indérivable."""
    return _chemins.dossier_attendu(str(categorie), promus, _MO)


@dataclass
class _PageDeSeuil:
    """Le minimum que `chemins.poids_du_seuil` lit d'une page.

    Le kit compte le seuil sur des PAGES, pas sur des chaînes : il doit pouvoir
    écarter un rôle hors seuil et résoudre la valeur dominante d'un axe non
    exclusif. L'API historique d'`arbo`, elle, prend une liste de catégories.
    Ce petit adaptateur tient les deux — et il n'invente rien : chaque catégorie
    devient une page du rôle d'unité, celui qui pèse.
    """

    fm: dict
    role: str
    dossier: str = ""
    illisible: None = None


def promotions(categories: list[str]) -> dict[str, str]:
    """Les sous-domaines promus en dossier, calculés sur la population donnée.

    Lève `KeyError` si une sous-valeur franchit le seuil sans libellé déclaré —
    même contrat qu'avant, et même motif : le libellé se lit, il ne se devine pas.
    """
    unite = _MO.role_de_fonction("unite")
    champ = _MO.champ_rangement
    pages = [_PageDeSeuil(fm={champ: c}, role=unite,
                          dossier=domaine(c) or "") for c in categories]
    promus, sans_libelle = _chemins.promotions(pages, _MO)
    if sans_libelle:
        raise KeyError(
            "; ".join(sans_libelle)
            + " — le libellé s'ajoute dans `brain.yml`, sous "
              "`axes.rangement.prefixes[].sous`, PLUS dans `SUB_LABEL`.")
    return promus
