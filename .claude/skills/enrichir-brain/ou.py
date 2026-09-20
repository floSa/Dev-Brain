# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""ou.py — où se range une catégorie ? La dérivation officielle, sur la population réelle.

    uv run .claude/skills/enrichir-brain/ou.py "<categorie>" [--role brique|notion|...]
    D=$(uv run .claude/skills/enrichir-brain/ou.py "<categorie>")   # stdout = le dossier, seul

Applique les MÊMES règles que `check_arbo.py` — la dérivation du kit, jamais une copie :
  - la population est lue dans les FICHIERS du vault, pas dans l'index (qui n'est régénéré
    qu'à la clôture : une page écrite plus tôt dans la même session lui est invisible) ;
  - les rôles qui pèsent sur le seuil de promotion sont ceux que `brain.yml` déclare
    (`pese_sur_le_seuil`, `range_par`, `porte_categorie`) — brique ET notion, pas comparatif,
    hub, pattern ni rule. Aucune liste de rôles n'est écrite ici ;
  - la page à insérer COMPTE : la 5e page d'un sous-domaine crée son dossier, et la
    dérivation doit le voir avant l'écriture. Son rôle compte aussi (`--role`, défaut :
    le rôle d'unité) : un comparatif inséré ne fait franchir aucun seuil.

Sortie : le dossier d'accueil sur stdout, seul ; le diagnostic sur stderr.
Codes de retour :
    0  dérivation sûre
    2  préfixe inconnu — catégorie à arbitrer, pas de dossier (stdout vide)
    3  préfixe connu, valeur NON déclarée dans `brain.yml` — le dossier affiché est
       hypothétique : `check_brain` refuserait la valeur en dur (R14)
    4  le seuil est franchi sans `libelle:` déclaré — la dérivation refuse d'inventer un nom
    5  incohérence avec le kit : ce script et `check_arbo` ne calculent plus la même chose
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "AI" / "scripts"))
import _pont_kit                                                # noqa: E402

_pont_kit.sortie_utf8()
sys.stdout.reconfigure(newline="\n")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import arbo                                                     # noqa: E402
from brainkit.valider import chemins, vault                     # noqa: E402


def dire(msg: str = "") -> None:
    print(msg, file=sys.stderr)


def main() -> int:
    mo = _pont_kit.modele()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("categorie")
    ap.add_argument("--role", default=mo.role_de_fonction("unite"),
                    help="rôle de la page à insérer (défaut : le rôle d'unité)")
    a = ap.parse_args()
    cat, role = a.categorie, a.role

    if role not in mo.roles:
        dire(f"rôle inconnu `{role}` — rôles du manifeste : {', '.join(sorted(mo.roles))}")
        return 2
    dom = arbo.domaine(cat)
    if dom is None:
        dire(f"préfixe `{cat.split('/')[0]}` inconnu : ce n'est pas un domaine du manifeste. "
             "Catégorie à arbitrer avec floSa (procédure « nouvelle valeur de catégorie »), "
             "pas à contourner.")
        return 2

    pages = [p for p in vault.lire_vault(_pont_kit.VAULT, mo.non_pages)
             if p.illisible is None]

    def pese(r: str | None) -> bool:
        return bool(r in mo.roles and mo.porte_l_axe_de_rangement(r)
                    and mo.pese_sur_le_seuil(r))

    champ = mo.champ_rangement
    cats = [str(p.fm[champ]) for p in pages if pese(p.role) and p.fm.get(champ)]

    try:
        avant = arbo.promotions(cats)
    except KeyError as e:
        dire(f"l'état ACTUEL du vault viole déjà la dérivation : {e.args[0]}")
        return 4
    # Garde-fou : ce script doit rendre exactement le verdict de check_arbo.
    attendu, _ = chemins.promotions(pages, mo)
    if avant != attendu:
        dire("INCOHÉRENT avec le kit : arbo.promotions() et chemins.promotions() divergent "
             f"({sorted(set(avant) ^ set(attendu))}). Ne pas se fier à ce script, "
             "le signaler à floSa.")
        return 5

    compte = pese(role)
    apres_cats = cats + [cat] if compte else cats
    try:
        apres = arbo.promotions(apres_cats)
    except KeyError as e:
        dire(f"L'insertion fait franchir le seuil ({mo.seuil}) : {e.args[0]}")
        dire("→ ouvrir le libellé dans brain.yml (procédure « nouvelle valeur de catégorie »), "
             "avec l'accord de floSa.")
        return 4

    dossier = arbo.dossier_attendu(cat, apres)
    n_avant, n_apres = cats.count(cat), apres_cats.count(cat)
    total = sum(1 for c in apres_cats if arbo.domaine(c) == dom)
    declaree = cat in mo.valeurs_rangement
    stems = {p.chemin.rsplit("/", 1)[-1][:-3].lower() for p in pages}

    dire(f"valeur          : {cat}  (déclarée dans brain.yml : {'oui' if declaree else 'NON'})")
    if compte:
        motif_role = "pèse sur le seuil"
    elif not mo.porte_l_axe_de_rangement(role):
        motif_role = "ne porte pas de catégorie : rangé par son rôle, rien à dériver ni à compter"
    else:
        motif_role = "ne pèse PAS sur le seuil : rien n'est ajouté au compte"
    dire(f"rôle inséré     : {role}  ({motif_role})")
    dire(f"pages pesantes  : {n_avant} avant, {n_apres} après — seuil {mo.seuil}"
         f"{', plafond actif' if mo.plafond else ''} ; domaine « {dom} » : {total} page(s) pesante(s)")

    if "/" not in cat:
        issue = f"valeur de tête : se range au niveau du domaine, « {dom} »"
    elif cat in avant:
        issue = f"DÉJÀ PROMUE → « {dossier} »"
        if not (_pont_kit.VAULT / dossier).is_dir():
            issue += " — mais ce dossier n'existe pas : l'état actuel viole check_arbo"
    elif cat in apres:
        issue = (f"FRANCHIT LE SEUIL → crée le dossier « {dossier} » : ce n'est plus une "
                 "insertion, c'est une réorganisation (git mv, hub, à signaler à floSa AVANT)")
    elif n_apres >= mo.seuil and mo.plafond and n_apres == total:
        issue = ("seuil atteint MAIS plafond : toutes les pages pesantes du domaine portent cette "
                 "valeur, un dossier fils redoublerait le parent → reste au niveau du domaine")
    else:
        issue = f"sous le seuil ({n_apres} < {mo.seuil}) → reste au niveau du domaine"
    dire(f"issue           : {issue}")

    # Effets de bord : d'autres valeurs du domaine peuvent basculer (levée du plafond).
    for v, lib in sorted(apres.items()):
        if v not in avant and v != cat:
            dire(f"effet de bord   : `{v}` bascule aussi en dossier « {lib} » "
                 "(le plafond du domaine est levé par cette insertion)")
    # Un dossier promu porte un hub à son nom : son nom de fichier doit être unique.
    for v, lib in sorted(apres.items()):
        if v not in avant and lib.lower() in stems:
            dire(f"COLLISION       : un fichier `{lib}.md` existe déjà — le hub du dossier "
                 "promu ne peut pas porter ce nom (liens nus). Libellé à revoir dans brain.yml.")

    print(dossier)
    if not declaree:
        dire("valeur NON déclarée : `axes.rangement.prefixes[].sous` de brain.yml est la source "
             "machine des valeurs légales. Dossier ci-dessus HYPOTHÉTIQUE — procédure "
             "« nouvelle valeur de catégorie », avec l'accord de floSa.")
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
