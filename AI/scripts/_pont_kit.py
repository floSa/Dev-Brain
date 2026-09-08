"""_pont_kit.py — COMMENT CE VAULT ATTEINT BRAINKIT. Écrit une fois, lu par six ponts.

Depuis le lot 9, le DevBrain est une **instance** de BrainKit : il ne porte plus
son outillage, il le lit. Les deux validateurs et les quatre générateurs de
`AI/scripts/` sont devenus des **ponts** de vingt lignes — ils résolvent la
racine du kit, chargent `brain.yml`, et appellent le kit. Aucune ligne du kit
n'est copiée ici : une copie forkerait le jour où elle est faite, et c'est
exactement le défaut que `brain.yml` existe pour supprimer (cf. `design/00-cadrage.md`
§5.1 et §5.10 du dépôt BrainKit).

# Pourquoi un pont, et pas la commande du kit directement

`cloturer-brain`, `enrichir-brain`, `.claude/settings.json` et le hook Stop
nomment tous `AI/scripts/<script>.py`. Ces quatre fichiers sont les contrats de
travail du vault, et ils sont lus à chaque session. Un lot qui remplace
l'outillage sans les toucher est un lot qui n'a rien cassé : c'est le critère
d'acceptation du lot 9, « aucun contenu de page modifié », étendu à ce qui pilote
l'écriture. Le pont est ce qui rend les deux vrais en même temps.

Deuxième raison, mesurable celle-là : `genere.index.signature` du manifeste vaut
`AI/scripts/build_index.py`, et cette chaîne est **dans l'artefact versionné**
(`generated_by` du catalogue, en-tête du document humain). Tant que le fichier
lancé porte ce nom, la signature reste exacte et l'artefact ne bouge pas d'un
octet. Une bascule vers `brainkit generer` aurait réécrit 2 fichiers pour rien.

# La résolution — remontée 5 du lot 7, « une instance ne sait pas où vit le kit »

`kit.mode: branche` dit que le code vit ailleurs, sans dire **où**. Le lot 7
proposait un champ `kit.racine:` au manifeste ou une étape d'installation qui
mette le kit sur le PATH. Ni l'un ni l'autre n'est pris ici, et le motif compte :

  - un `kit.racine:` serait un **chemin absolu de poste** dans un fichier
    versionné et partagé entre trois machines (cf. `Documentation/perso/machines.md`) ;
  - mettre `brainkit` sur le PATH est une étape d'installation, donc du lot 10,
    et une étape d'installation qu'on oublie est un outillage qui ne tourne plus.

Le pont cherche donc, dans cet ordre, et **s'arrête au premier qui répond** :

  1. `$BRAINKIT_RACINE` — l'échappatoire explicite, pour un kit rangé ailleurs ;
  2. `AI/scripts/brainkit/` — une instance FIGÉE (`kit.mode: fige`), où
     `brainkit freeze` a copié le kit dans le vault. Ce cas passe AVANT la
     recherche par voisinage : une instance figée est une instance qui ne doit
     plus jamais lire un kit du dehors, c'est toute sa raison d'être ;
  3. le **voisinage**, en remontant depuis la racine du vault : `<parent>/BrainKit`
     à chaque niveau. Le cas nominal — les deux dépôts côte à côte sous
     `Projets/` — répond au premier parent ; un worktree, qui vit trois niveaux
     plus bas sous `.claude/worktrees/`, répond au quatrième. C'est la remontée
     qui rend le pont utilisable depuis un worktree sans rien configurer.

Si aucun ne répond, le pont **s'arrête et dit les trois pistes**. Il ne devine
pas : un kit deviné est un verdict rendu par un code qu'on n'a pas choisi.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# La racine du vault : ce fichier vit dans `<vault>/AI/scripts/`.
VAULT = Path(__file__).resolve().parents[2]
MANIFESTE = VAULT / "brain.yml"

_MARQUEUR = Path("brainkit") / "__init__.py"


def _porte_le_kit(racine: Path) -> bool:
    return (racine / _MARQUEUR).is_file()


def racine_du_kit() -> Path:
    """Où vit BrainKit. S'arrête si personne ne répond — jamais de devinette."""
    pistes: list[str] = []

    env = os.environ.get("BRAINKIT_RACINE")
    if env:
        p = Path(env).expanduser()
        if _porte_le_kit(p):
            return p.resolve()
        pistes.append(f"$BRAINKIT_RACINE = `{env}` — ne porte pas `brainkit/__init__.py`")

    fige = VAULT / "AI" / "scripts" / "brainkit"
    if (fige / "__init__.py").is_file():
        return (VAULT / "AI" / "scripts").resolve()

    for parent in [VAULT, *VAULT.parents]:
        candidat = parent / "BrainKit"
        if _porte_le_kit(candidat):
            return candidat.resolve()
    pistes.append(f"aucun `BrainKit/` en remontant depuis `{VAULT}`")

    print("BrainKit introuvable — ce vault est une instance `kit.mode: branche`, "
          "donc son outillage vit dans le kit.", file=sys.stderr)
    for p in pistes:
        print(f"  - {p}", file=sys.stderr)
    print("\n  Trois façons de le dire, de la plus locale à la plus durable :\n"
          "    1. poser le dépôt BrainKit à côté du vault (`.../Projets/BrainKit`) ;\n"
          "    2. exporter BRAINKIT_RACINE=<racine du dépôt BrainKit> ;\n"
          "    3. `uv run brainkit freeze` depuis le kit, qui le copie DANS le "
          "vault et coupe la dépendance (livraison on-prem).", file=sys.stderr)
    raise SystemExit(2)


def branche() -> Path:
    """Met le kit sur `sys.path` et rend sa racine. Idempotent."""
    racine = racine_du_kit()
    if str(racine) not in sys.path:
        sys.path.insert(0, str(racine))
    return racine


def manifeste() -> Path:
    if not MANIFESTE.is_file():
        print(f"manifeste introuvable : {MANIFESTE}\n"
              "  Un manifeste ne se devine pas : c'est ce contre quoi le verdict "
              "est rendu.", file=sys.stderr)
        raise SystemExit(2)
    return MANIFESTE


def modele():
    """Le manifeste du vault, chargé par le kit."""
    branche()
    from brainkit.valider import charge          # noqa: PLC0415 — après `branche()`
    return charge(manifeste())


def sortie_utf8() -> None:
    """La console Windows est en cp1252 ; le vault, lui, est accentué partout."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):        # pragma: no cover
        pass
