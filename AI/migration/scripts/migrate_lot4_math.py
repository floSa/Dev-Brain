# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_math.py — descend les 26 notions `concept/math` dans l'arbre.

Lot 4, domaine « Mathématiques ». Deux gestes par page, et rien d'autre :
réécrire la ligne `categorie:` du frontmatter, puis `git mv` vers le dossier
que `AI/scripts/arbo.py` dérive de cette catégorie. Le CORPS des notions n'est
pas touché — le lot range, il n'édite pas.

La table ci-dessous n'est PAS une projection de `concept/math` sur `math/*` : elle
est le relevé du **corps du hub** `Mathématiques/Mathématiques.md`, écrit au lot 3,
dont les quatre puces « Algèbre linéaire / Optimisation / Théorie de l'information /
Théorie de l'apprentissage » citent les 26 notions nommément, une seule fois chacune.
C'est l'étape 0 de la procédure du lot (remontée 1 du pilote stats) : le corps du hub
range mieux que les tags, parce qu'il est écrit par quelqu'un qui connaissait le
domaine. Un seul écart tag / hub, assumé et documenté dans les Remontées :
`Optimal transport` porte le tag `optimization` et va en `math/information`.

Usage : uv run AI/migration/scripts/migrate_lot4_math.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

# nom de fichier (sans .md) -> categorie cible
CIBLES = {
    # --- math/algebre-lineaire : les objets et leurs propriétés, pas les méthodes
    #     qui s'en servent. Puce « Algèbre linéaire » du hub, 6 pages.
    "Vector norms": "math/algebre-lineaire",
    "Matrix products": "math/algebre-lineaire",
    "Matrix decompositions": "math/algebre-lineaire",
    "SVD": "math/algebre-lineaire",
    "Eigendecomposition": "math/algebre-lineaire",
    "Projections": "math/algebre-lineaire",

    # --- math/optimisation : minimiser une fonction — le mécanisme, ses garanties,
    #     et la branche discrète. Puce « Optimisation » du hub, 8 pages + PuLP.
    "Gradient descent": "math/optimisation",
    "Convexity": "math/optimisation",
    "Loss landscape and saddle points": "math/optimisation",
    "Newton & quasi-Newton": "math/optimisation",
    "Learning rate schedules": "math/optimisation",
    "Optimisation sous contrainte": "math/optimisation",
    "Optimisation combinatoire": "math/optimisation",
    "Programmation linéaire en nombres entiers (MIP)": "math/optimisation",

    # --- math/information : mesurer l'incertitude et l'écart entre deux lois.
    #     Puce « Théorie de l'information » du hub, 7 pages.
    "Shannon entropy": "math/information",
    "Cross-entropy": "math/information",
    "KL divergence": "math/information",
    "Jensen-Shannon divergence": "math/information",
    "Mutual information": "math/information",
    "Optimal transport": "math/information",
    "Wasserstein distance": "math/information",

    # --- math/theorie-apprentissage : pourquoi la généralisation est possible.
    #     Puce « Théorie de l'apprentissage » du hub, 5 pages — et ce sont les
    #     5 SEULES pages du vault taguées `learning-theory`, donc le « exactement 5 »
    #     est un fait mesuré, pas un arbitrage qui viserait le seuil (remontée 4).
    "PAC learning": "math/theorie-apprentissage",
    "VC dimension": "math/theorie-apprentissage",
    "Rademacher complexity": "math/theorie-apprentissage",
    "Generalization bounds": "math/theorie-apprentissage",
    "No Free Lunch theorem": "math/theorie-apprentissage",
}


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

    # L'arbre d'arrivée se calcule sur la population FINALE du domaine : les briques
    # déjà en place plus les notions qui descendent. Le seuil ne se devine pas page
    # par page, il se compte sur l'ensemble.
    cats = list(CIBLES.values())
    for md in (VAULT / arbo.DOM_LABEL["math"]).rglob("*.md"):
        for ligne in md.read_text(encoding="utf-8").split("\n")[:40]:
            if ligne.startswith("categorie:"):
                cats.append(ligne.split(":", 1)[1].strip())
    promus = arbo.promotions(cats)
    print(f"sous-domaines promus : {promus}")

    print()
    print("-- les notions qui descendent --")
    for nom, cible in sorted(CIBLES.items()):
        src = SOURCE / f"{nom}.md"
        dest_dir = VAULT / arbo.dossier_attendu(cible, promus)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:46} {cible:26} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # Seconde passe — les BRIQUES déjà en place, que la promotion déplace.
    print()
    print("-- les briques que la promotion deplace --")
    bouges = 0
    dom = VAULT / arbo.DOM_LABEL["math"]
    for md in sorted(dom.rglob("*.md")):
        fm = md.read_text(encoding="utf-8").splitlines()[:40]
        if any(l.strip() == "role: hub" for l in fm):
            continue
        cat = next((l.split(":", 1)[1].strip() for l in fm
                    if l.startswith("categorie:")), "")
        attendu = VAULT / arbo.dossier_attendu(cat, promus)
        if md.parent == attendu:
            continue
        bouges += 1
        print(f"  {md.stem:46} {cat:26} -> "
              f"{(attendu / md.name).relative_to(VAULT).as_posix()}")
        if dry:
            continue
        attendu.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                        str((attendu / md.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)

    # Troisième passe — les vues `.base` dont le filtre est une catégorie EXACTE
    # désormais promue. Un comparatif vit dans le dossier de ses membres (convention
    # CLAUDE.md) ; « Comparatif - Solveurs d'optimisation » filtre
    # `categorie == "math/optimisation"` et n'a donc de membres que dans le dossier
    # promu. Celui de « Statistiques & inférence » filtre le préfixe `stats/` entier
    # et enjambe les quatre sous-dossiers : il est resté au niveau du domaine, et
    # c'est cohérent — la règle porte sur les membres, pas sur le nom du fichier.
    print()
    print("-- les comparatifs que la promotion deplace --")
    deplaces_base = 0
    for base in sorted(dom.rglob("*.base")):
        txt = base.read_text(encoding="utf-8")
        cible = next((c for c in promus if 'categorie == "' + c + '"' in txt), None)
        if cible is None:
            continue
        attendu = VAULT / arbo.dossier_attendu(cible, promus)
        if base.parent == attendu:
            continue
        deplaces_base += 1
        print(f"  {base.stem:46} {cible:26} -> "
              f"{(attendu / base.name).relative_to(VAULT).as_posix()}")
        if dry:
            continue
        subprocess.run(["git", "mv", str(base.relative_to(VAULT)),
                        str((attendu / base.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)

    verbe = "a deplacer" if dry else "deplace(e)(s)"
    print()
    print(f"{len(CIBLES)} notion(s), {bouges} brique(s) et {deplaces_base} "
          f"comparatif(s) {verbe}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
