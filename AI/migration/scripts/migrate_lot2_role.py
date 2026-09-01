# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""migrate_lot2_role.py — lot 2 de la migration v3 : `role:` remplace `galaxie:`/`type:`.

Spécification : AI/migration/lot-2-role.md (procédure, étapes 1 à 4).

Transformation du SEUL frontmatter des pages de `Dev/` et `Wiki/`. Aucun corps de page
n'est lu ni écrit ; aucun fichier n'est déplacé ni supprimé.

Le frontmatter du vault est plat — vérifié : 646 pages, 0 ligne qui ne soit pas
`clé: valeur`, et `galaxie:` toujours en première clé. La transformation est donc
LIGNE À LIGNE, et non un aller-retour YAML : un `yaml.dump` détruirait les guillemets,
les listes en ligne et l'ordre des champs sur 646 fichiers. Les fins de ligne CRLF
sont conservées telles quelles.

Étape 1 — `role:` prend la place de `galaxie:` (première ligne), `type:` disparaît.
  La correspondance se lit sur `type:` et non sur le dossier : les deux coïncident sur
  645 pages sur 646. La seule divergence est `Wiki/Outils/Obsidian.md` (`type: outil`),
  qui porte un frontmatter de brique (pitch, licence_type, os, alternatives, url_docs) :
  le classer `notion` par son dossier rendrait cinq de ses champs hors gabarit.

Étape 2 — suppression de `galaxie:`, `type:`, `status:`, `remplace_par:`.
  `remplace_par:` : 4 fiches sur 297 ne sont PAS vides (le brief les annonçait toutes
  vides). Leurs 7 cibles sont déjà, toutes, dans `alternatives:` ET nommées dans le
  corps — vérifié avant suppression. Rien n'est perdu.
  `status:` : la valeur est reportée dans `maturite:` là où elle porte un fait que
  `maturite:` ne dit pas déjà — table TRANSPOSE ci-dessous, tenue à la main.

Étape 3 — `hosted:` et `scaling:` deviennent conditionnels à `famille:`.
  Retirés partout où `famille` n'est pas plateforme / saas / application.
  `hosted:` survivant passe en liste : self -> [self], managed -> [managed],
  both -> [self, managed].

Étape 4 — `complements: []` s'ouvre après `alternatives:`, sur les seules pages qui
  portent `alternatives:` (les briques). Symétrique d'`alternatives:`, vide par
  construction : ce lot l'ouvre, il ne le remplit pas.

Usage :
    uv run AI/migration/scripts/migrate_lot2_role.py            # simulation (défaut)
    uv run AI/migration/scripts/migrate_lot2_role.py --apply    # écrit
    uv run AI/migration/scripts/migrate_lot2_role.py --diff Dev/Services/Faker.md
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    sys.exit("PyYAML manquant — lancer via uv.")

VAULT = Path(__file__).resolve().parents[3]
SCAN_DIRS = ["Dev", "Wiki"]

# Étape 1 — correspondance `type:` -> `role:`. Mécanique, aucune valeur inventée.
ROLE = {"service": "brique", "outil": "brique", "concept": "notion",
        "pattern": "pattern", "rule": "rule"}

# Étape 2 — champs supprimés sur toutes les pages.
SUPPRIMES = {"galaxie", "type", "status", "remplace_par"}

# Étape 2 bis — report de `status:` dans `maturite:` avant suppression.
# Une seule fiche : `status: abandonne` sans `maturite:` (le gabarit `outil` ne portait
# pas le champ). Son propre pitch dit « sans commit depuis juillet 2022 » : le fait est
# sourcé par la page, il n'est pas inventé ici.
# Les trois `status: en-eval` sans `maturite:` (Maka, swarm-forge, t3code) ne sont PAS
# transposés : `en-eval` décrit l'état d'évaluation de floSa, pas la maturité du produit.
# Leur donner une maturité serait fabriquer une affirmation sur l'amont. Cas remonté
# dans AI/migration/README.md.
TRANSPOSE = {"Dev/Outils/osint4all.md": ("maturite", "deprecated")}

# Étape 3 — les seules familles pour lesquelles l'hébergement a un sens (spec §5).
FAMILLES_HEBERGEES = {"plateforme", "saas", "application"}
HOSTED_LISTE = {"self": "[self]", "managed": "[managed]", "both": "[self, managed]"}

CLE = re.compile(r"^([A-Za-z_][\w]*):(.*)$")


def decoupe(texte: str) -> tuple[str, list[str], str]:
    """(ouverture, lignes du frontmatter, reste). Les fins de ligne restent dans la ligne."""
    if not texte.startswith("---"):
        raise ValueError("pas de frontmatter")
    i = texte.index("\n") + 1          # après le '---' d'ouverture
    j = texte.index("\n---", i)        # avant le '---' de fermeture
    return texte[:i], texte[i:j].split("\n"), texte[j:]


def transforme(chemin: str, lignes: list[str]) -> tuple[list[str], list[str]]:
    """Réécrit les lignes du frontmatter. Renvoie (nouvelles lignes, actes posés)."""
    eol = "\r" if lignes and lignes[0].endswith("\r") else ""
    fm = yaml.safe_load("\n".join(x.rstrip("\r") for x in lignes)) or {}
    role = ROLE.get(fm.get("type"))
    if role is None:
        raise ValueError(f"{chemin} : type inconnu {fm.get('type')!r}")
    famille = fm.get("famille")
    hebergeable = famille in FAMILLES_HEBERGEES

    out: list[str] = []
    actes: list[str] = []
    for ligne in lignes:
        m = CLE.match(ligne)
        cle = m.group(1) if m else None

        if cle == "galaxie":                       # étape 1 : role prend sa place
            out.append(f"role: {role}{eol}")
            actes.append(f"role: {role}")
            continue
        if cle == "status":                        # étape 2 bis, puis 2
            report = TRANSPOSE.get(chemin)
            if report:
                out.append(f"{report[0]}: {report[1]}{eol}")
                actes.append(f"status reporte dans {report[0]}")
            else:
                actes.append("status supprime")
            continue
        if cle in SUPPRIMES:                       # étape 2
            actes.append(f"{cle} supprime")
            continue
        if cle in ("hosted", "scaling"):           # étape 3
            if not hebergeable:
                actes.append(f"{cle} retire (famille non hebergeable)")
                continue
            if cle == "hosted":
                brut = str(fm.get("hosted") or "").strip()
                if brut in HOSTED_LISTE:
                    out.append(f"hosted: {HOSTED_LISTE[brut]}{eol}")
                    actes.append(f"hosted {brut} en liste")
                    continue
            out.append(ligne)
            continue

        out.append(ligne)
        if cle == "alternatives":                  # étape 4
            out.append(f"complements: []{eol}")
            actes.append("complements ouvert")
    return out, actes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="écrit les fichiers")
    ap.add_argument("--diff", metavar="CHEMIN", help="affiche le avant/après d'une page")
    args = ap.parse_args()

    actes: collections.Counter = collections.Counter()
    touches = 0

    for d in SCAN_DIRS:
        for md in sorted((VAULT / d).rglob("*.md")):
            chemin = md.relative_to(VAULT).as_posix()
            with md.open(encoding="utf-8", newline="") as fh:
                texte = fh.read()
            ouverture, lignes, reste = decoupe(texte)
            neuves, poses = transforme(chemin, lignes)
            if neuves == lignes:
                continue
            touches += 1
            actes.update(poses)
            if args.diff and args.diff.replace("\\", "/") == chemin:
                print(f"--- {chemin} · AVANT\n" + "\n".join(x.rstrip("\r") for x in lignes))
                print(f"--- {chemin} · APRES\n" + "\n".join(x.rstrip("\r") for x in neuves))
            if args.apply:
                with md.open("w", encoding="utf-8", newline="") as fh:
                    fh.write(ouverture + "\n".join(neuves) + reste)

    print(f"{'ECRIT' if args.apply else 'SIMULATION'} — {touches} page(s) touchee(s)")
    for k, v in sorted(actes.items()):
        print(f"  {v:4d}  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
