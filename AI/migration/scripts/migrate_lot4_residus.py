# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_residus.py — descend les 5 notions `concept/data` remontées.

Lot 4, résidus de la conversation « Data & pipelines » du 2026-09-05. Ces cinq
notions étaient **évidentes mais intraitables dans leur lot** (remontée 15) : leur
domaine d'accueil — « Bases de données », « Outils de développement » — était hors
du périmètre du lot qui rangeait `concept/data`. Consigne de floSa : une notion qui
appelle un sous-domaine hors périmètre se **remonte**, elle ne se déplace pas.

Le périmètre est maintenant celui du domaine d'accueil, et la remontée 15 le disait :
« envisager un dernier passage PAR DOMAINE D'ACCUEIL plutôt que par famille
d'origine, pour les résidus ». C'est ce passage-là.

La cible est dite par les pages elles-mêmes, pas dérivée d'un tag :

  - `ORM` ouvre sur « faire correspondre des tables relationnelles à des objets » et
    pointe vers [[Prisma]] et [[SQLAlchemy]] — `database/orm` ;
  - `Migrations de schéma` décrit le DDL versionné et pointe vers [[Flyway]] et
    [[Liquibase]] — `database/migration` ;
  - `Bases de données vectorielles` est la notion chapeau des moteurs de
    `Bases de données/Vectoriel/`, et le hub de domaine la désigne déjà comme
    « sous-famille spécialisée détaillée » — `database/vecteur` ;
  - `Index ANN — internes` décrit ce qui tourne SOUS ces moteurs (HNSW, IVF, PQ) et
    cite [[Faiss]], [[hnswlib]], [[ScaNN]] — `database/vecteur` ;
  - `Notebooks-as-code` décrit le pairing [[jupytext]] et le passage notebook →
    module, exactement la population de `Outils de développement/Notebooks/` —
    `devtools/notebook`.

**Effet de seuil revérifié avant d'exécuter** (remontée 3), sur la population réelle
des deux domaines, et non sur la mémoire du lot précédent :

  Bases de données         orm 3->4, migration 3->4 (sous le seuil, pas de dossier)
                           vecteur 11->13 (« Vectoriel/ » existe déjà)
  Outils de développement  notebook 5->6 (« Notebooks/ » existe déjà)

Les deux ensembles de sous-domaines promus sont IDENTIQUES avant et après — le
script le vérifie lui-même et s'arrête si ce n'est pas le cas.

Usage : uv run AI/migration/scripts/migrate_lot4_residus.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

CIBLES = {
    "ORM": "database/orm",
    "Migrations de schéma": "database/migration",
    "Bases de données vectorielles": "database/vecteur",
    "Index ANN — internes": "database/vecteur",
    "Notebooks-as-code": "devtools/notebook",
}

DOMAINES = ["Bases de données", "Outils de développement"]


def categorie(md: Path) -> str:
    for ligne in md.read_text(encoding="utf-8").split("\n")[:40]:
        if ligne.startswith("categorie:"):
            return ligne.split(":", 1)[1].strip()
    return ""


def est_hub(md: Path) -> bool:
    return any(l.strip() == "role: hub"
               for l in md.read_text(encoding="utf-8").split("\n")[:40])


def population(dom: str) -> list[str]:
    return [categorie(md) for md in (VAULT / dom).rglob("*.md")
            if not est_hub(md)]


def recategoriser(path: Path, cible: str) -> None:
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def main() -> int:
    dry = "--dry-run" in sys.argv
    manquants = [n for n in CIBLES if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")

    # --- l'effet de seuil, mesuré AVANT de décider (remontée 3) ---
    promus_avant, promus_apres = {}, {}
    for dom in DOMAINES:
        avant = population(dom)
        apres = avant + [c for n, c in CIBLES.items()
                         if arbo.domaine(c) == dom]
        pa, pb = arbo.promotions(avant), arbo.promotions(apres)
        promus_avant.update(pa)
        promus_apres.update(pb)
        print(f"{dom} : {len(avant)} -> {len(apres)} pages")
        print(f"    promus avant : {sorted(pa)}")
        print(f"    promus apres : {sorted(pb)}")
        if sorted(pa) != sorted(pb):
            raise SystemExit(
                f"ARRET — « {dom} » : le deplacement PROMEUT un sous-domaine "
                f"({sorted(set(pb) - set(pa))}). Ce n'est pas ce qui a ete annonce "
                f"aux remontees 15 et 19 ; le seuil ne se negocie pas, l'arbitrage "
                f"se rouvre.")

    print()
    print("-- les 5 notions remontees descendent --")
    for nom, cible in sorted(CIBLES.items()):
        src = SOURCE / f"{nom}.md"
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus_apres)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:32} {cible:20} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # --- les briques qu'une promotion deplacerait : aucune attendue ---
    print()
    print("-- les briques que la promotion deplace --")
    bouges = 0
    for dom in DOMAINES:
        for md in sorted((VAULT / dom).rglob("*.md")):
            if est_hub(md):
                continue
            attendu = VAULT / arbo.dossier_attendu(categorie(md), promus_apres)
            if md.parent == attendu:
                continue
            bouges += 1
            print(f"  {md.stem:32} -> "
                  f"{(attendu / md.name).relative_to(VAULT).as_posix()}")
            if dry:
                continue
            attendu.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                            str((attendu / md.name).relative_to(VAULT))],
                           cwd=VAULT, check=True)
    if bouges == 0:
        print("  aucune — les deux ensembles de promus sont identiques.")

    restants = [md.stem for md in SOURCE.glob("*.md")
                if categorie(md) == "concept/data"]
    print()
    verbe = "a deplacer" if dry else "deplacee(s)"
    print(f"{len(CIBLES)} notion(s) {verbe} ; "
          f"{len(restants)} page(s) portent encore `concept/data` : {restants}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
