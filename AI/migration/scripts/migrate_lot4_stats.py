# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_stats.py — descend les 37 notions `concept/stats` dans l'arbre.

Lot 4, domaine pilote « Statistiques & inférence ». Deux gestes par page, et
rien d'autre : réécrire la ligne `categorie:` du frontmatter, puis `git mv` vers
le dossier que `AI/scripts/arbo.py` dérive de cette catégorie. Le CORPS des
notions n'est pas touché — le lot range, il n'édite pas.

La table ci-dessous est le relevé d'arbitrage, fait page par page (titre,
`## Aperçu`, liens sortants), et NON une projection de `concept/<sub>` sur
`stats/<sub>` : la remontée 20 du lot 3 a montré que cette projection est fausse
dès que le découpage Dev est plus fin que le découpage wiki.

Usage : uv run AI/migration/scripts/migrate_lot4_stats.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

# nom de fichier (sans .md) -> categorie cible
CIBLES = {
    # --- stats/inference : tester une hypothèse sur un échantillon déjà collecté
    "Tests d'hypothèse": "stats/inference",
    "Test t et ANOVA": "stats/inference",
    "Test du khi-deux": "stats/inference",
    "Tests non paramétriques": "stats/inference",
    "MANOVA et tests multivariés": "stats/inference",
    "Correction des tests multiples": "stats/inference",
    "Intervalles de confiance": "stats/inference",
    "Bootstrap": "stats/inference",
    "Maximum de vraisemblance": "stats/inference",
    "Analyse de puissance": "stats/inference",
    "Analyse de survie": "stats/inference",
    # --- stats/exploratoire : analyse factorielle, l'interprétation des axes
    "PCA": "stats/exploratoire",
    "CA": "stats/exploratoire",
    "MCA": "stats/exploratoire",
    "FAMD": "stats/exploratoire",
    "MFA": "stats/exploratoire",
    "GPA": "stats/exploratoire",
    "PGA": "stats/exploratoire",
    "HCPC": "stats/exploratoire",
    "Réduction de dimension": "stats/exploratoire",
    "Manifold learning": "stats/exploratoire",
    # --- stats/bayesien : l'a priori, l'a posteriori et leur échantillonnage
    "Inférence bayésienne": "stats/bayesien",
    "A priori conjugués": "stats/bayesien",
    "Estimation MAP": "stats/bayesien",
    "MCMC": "stats/bayesien",
    # --- stats/probabilite : théorèmes de convergence et processus aléatoires
    "Loi des grands nombres": "stats/probabilite",
    "Théorème central limite": "stats/probabilite",
    "Inégalités de concentration": "stats/probabilite",
    "Chaînes de Markov": "stats/probabilite",
    "Mouvement brownien": "stats/probabilite",
    "Processus de Poisson": "stats/probabilite",
    # --- stats/experimentation : concevoir l'expérience, décider quand l'arrêter
    "A-B testing": "stats/experimentation",
    "CUPED": "stats/experimentation",
    "Sequential testing": "stats/experimentation",
    "Multi-armed bandits": "stats/experimentation",
    # --- stats/causal : l'effet d'une cause, sans randomisation
    "Inférence causale": "stats/causal",
    "Diff-in-Diff": "stats/causal",
}

SOURCE = VAULT / "Wiki" / "Concepts"


def recategoriser(path: Path, cible: str) -> bool:
    """Réécrit la SEULE ligne `categorie:` du frontmatter. Rien d'autre."""
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            if ligne.strip() == f"categorie: {cible}":
                return False
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return True
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def main() -> int:
    dry = "--dry-run" in sys.argv
    manquants = [n for n in CIBLES if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")

    # L'arbre d'arrivée se calcule sur la population FINALE du domaine : les
    # briques déjà en place plus les notions qui descendent. Le seuil ne se
    # devine pas page par page, il se compte sur l'ensemble.
    cats = list(CIBLES.values())
    for md in (VAULT / arbo.DOM_LABEL["stats"]).rglob("*.md"):
        txt = md.read_text(encoding="utf-8")
        for ligne in txt.split("\n")[:40]:
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
        print(f"  {nom:32} {cible:22} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # Seconde passe — les BRIQUES déjà en place. Elles ne changent pas de
    # catégorie, mais quatre sous-domaines viennent de franchir le seuil : leur
    # dossier d'accueil n'est plus le même. Ne rien faire ici laisserait
    # `scipy.stats` au niveau du domaine à côté d'un dossier « Tests &
    # estimation » qui porte les notions du même sujet — et check_arbo le
    # signalerait, puisqu'il dérive le chemin sur la population réelle.
    print()
    print("-- les briques que la promotion déplace --")
    bouges = 0
    dom = VAULT / arbo.DOM_LABEL["stats"]
    for md in sorted(dom.rglob("*.md")):
        txt = md.read_text(encoding="utf-8")
        fm = txt.splitlines()[:40]
        if any(l.strip() == "role: hub" for l in fm):
            continue
        cat = next((l.split(":", 1)[1].strip() for l in fm
                    if l.startswith("categorie:")), "")
        attendu = VAULT / arbo.dossier_attendu(cat, promus)
        if md.parent == attendu:
            continue
        bouges += 1
        print(f"  {md.stem:32} {cat:22} -> "
              f"{(attendu / md.name).relative_to(VAULT).as_posix()}")
        if dry:
            continue
        attendu.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                        str((attendu / md.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)

    verbe = "à déplacer" if dry else "déplacée(s)"
    print()
    print(f"{len(CIBLES)} notion(s) et {bouges} brique(s) {verbe}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
