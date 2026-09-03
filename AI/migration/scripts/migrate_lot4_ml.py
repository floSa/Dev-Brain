# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_ml.py — descend les 67 notions `concept/ml`, la DERNIÈRE famille.

Lot 4, dernière conversation. Deux gestes par page : réécrire la ligne `categorie:`
du frontmatter, puis `git mv` vers le dossier dérivé par `AI/scripts/arbo.py`. Le
CORPS des notions n'est pas touché.

**Ce lot paie des promotions, contrairement aux cinq précédents.** La remontée 35 le
pronostiquait, et sa règle corrigée — « chacune des cibles réelles est-elle déjà un
dossier ? » — répond non trois fois : `ml/socle` (2 briques), `ml/eval` (2) et
`ml/non-supervise` (4) sont sous le seuil aujourd'hui et le franchissent en recevant
leurs notions. Trois sous-dossiers naissent, trois libellés sont arbitrés, trois
sous-hubs sont écrits à la main.

Mais la nº 35 se trompait aussi, en sens inverse : elle listait **six** candidats.
Mesuré ici, trois d'entre eux ne franchissent rien — `ml/hyperopt` finit à 4,
`ml/monitoring` à 3, `ml/feature-store` et `ml/embeddings` à 2. Ces cinq notions-là
restent au niveau du domaine, et c'est ce que le hub annonce depuis le lot 3.

**Zéro valeur de catégorie ouverte** : les 67 tombent toutes dans le vocabulaire
existant. Trois valeurs sont en revanche ÉLARGIES, parce qu'elles avaient été écrites
pour des briques du temps où les notions portaient `concept/*` — cf. `taxonomie.md`.

Croisement de la remontée 30, fait AVANT tout `git mv` : les 67 noms contre les corps
des 71 hubs, zone `<!-- AUTO -->` exclue.

  - **0 notion muette** ;
  - **les 67 sont revendiquées par le hub de DOMAINE**, dont les dix puces les
    partitionnent exactement — c'est le cas « Mathématiques » de la remontée 12 ;
  - **28 en contention** avec un sous-hub, toutes tranchées par la phrase et non par
    la page. La plupart sont des renvois : « Serving » et « Suivi d'expériences »
    délèguent le monitoring, la dérive, le feature store et l'hyperopt « au niveau du
    domaine » ; « Optimisation » renvoie `Optimisation d'hyperparamètres` « au domaine
    Machine Learning » ; « Analyse factorielle » nomme `t-SNE and UMAP`, `ICA` et
    `NMF` comme le côté ML de sa frontière.

> Une nuance qui affaiblit ce croisement ICI et qu'il faut écrire : `v3-arborescence.md`
> notait au lot précédent que « les hubs les citent toutes en clair en attendant ». La
> revendication par le hub de domaine ne prouve donc pas une destination — elle était
> voulue. C'est la revendication par un SOUS-hub qui informe, et l'absence de
> revendication qui dit « niveau du domaine ».

Quatre arbitrages de floSa, posés en une fois avant tout déplacement :

  1. **Libellés des trois dossiers : « Socle », « Évaluation de modèles », « Non
     supervisé »**, vérifiés contre les quatre ensembles de la remontée 26.
     « Évaluation » est INTERDIT : c'est le nom de fichier du hub
     `LLM & IA générative/Évaluation/Évaluation.md` (ensemble nº 3), et un lien nu ne
     résoudrait plus. « Apprentissage non supervisé » est interdit aussi : c'est une
     page QUI VIVRA DANS LE DOSSIER (ensemble nº 4).
  2. **`Manifold learning` part de `stats/exploratoire` vers `ml/non-supervise`** —
     l'arbitrage reporté deux fois, cf. remontée 3. Ses trois sœurs (`t-SNE and UMAP`,
     `ICA`, `NMF`) partent ensemble ; ses tags sont identiques à ceux de `t-SNE and
     UMAP` ; sa page écrit « coordonnées exploitables en aval (features, pipeline) »,
     qui est mot pour mot le critère ML de la frontière `stats/exploratoire`, et ne
     parle jamais d'interpréter des axes ; son outillage est `sklearn.manifold`, pas
     Prince. Effet de seuil mesuré dans LES DEUX SENS : au départ
     `stats/exploratoire` passe de 12 à 11 et reste promu ; à l'arrivée
     `ml/non-supervise` promeut de toute façon (21 sans elle, 22 avec). Les 45
     promotions du vault sont identiques dans les deux cas. C'est le cas de la
     remontée 25 : ce qui bloquait n'était pas la frontière mais l'incertitude sur ce
     qu'on trouve de l'autre côté, et cette conversation la lève.
  3. **Les 8 pages arbres/ensembles et les 7 de préparation de variables vont en
     `ml/tabulaire`.** Le sous-hub les revendique nommément dans deux puces dédiées, et
     leurs briques y sont déjà (XGBoost, LightGBM, CatBoost, Featuretools,
     category_encoders, imbalanced-learn). Sa première puce — « ce dossier ne contient
     que ce qui va plus loin que Scikit-Learn » — est un critère écrit pour des
     BRIQUES et ne se transpose pas à un concept ; le hub est réécrit en conséquence
     (remontée 39).
  4. **`ml/eval` est élargi** plutôt que doublé d'une valeur neuve. `taxonomie.md` le
     définissait comme « bibliothèques de métriques », « distinct du concept transverse
     porté par le tag `model-evaluation` » — une phrase d'exclusion qui datait
     exactement de la disjonction brique/notion que le lot 4 supprime. Précédent :
     `math/optimisation`, élargi au même lot.

**Effet de seuil : trois promotions, mesurées et ATTENDUES.** Le script ne se contente
pas d'exiger l'égalité des ensembles comme celui de `dl` : chaque lot déclare la
promotion qu'il ouvre, et le script s'arrête si l'ensemble bouge autrement. Une
promotion non déclarée est un arbitrage à rouvrir, pas un résultat à encaisser
(remontées 4 et 25). Le domaine passe de 173 à 240 pages, garde 17 pages à son niveau,
et le plafond n'est jamais approché.

Usage : uv run AI/migration/scripts/migrate_lot4_ml.py <cible> [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

# Un lot de commit -> (categorie cible, promotions ouvertes, notions).
# `promotions ouvertes` : les catégories qui deviennent un dossier DANS CE LOT. Vide
# quand le dossier existe déjà ou quand la cible reste sous le seuil.
LOTS = {
    "socle": ("ml/socle", {"ml/socle"}, [
        "Analyse discriminante",
        "Apprentissage supervisé",
        "Classification",
        "GAM",
        "GLM",
        "Gaussian Process",
        "Naive Bayes",
        "Perceptron et MLP",
        "Régression",
        "Régression et classification multi-sorties",
        "Régression linéaire",
        "Régression logistique",
        "Régression quantile",
        "Régularisation",
        "SVM",
        "Systèmes de recommandation",
        "Types de données et choix de modèle",
        "k-NN",
    ]),
    "tabulaire": ("ml/tabulaire", set(), [
        "AdaBoost",
        "Arbres de décision",
        "Bagging",
        "Boosting",
        "Encodage des variables catégorielles",
        "Ensembling",
        "Extra Trees",
        "Gradient Boosting (GBDT)",
        "Imbalanced classification",
        "Imputation des valeurs manquantes",
        "Ingénierie des caractéristiques",
        "Mise à l'échelle",
        "Mécanismes de données manquantes",
        "Random Forest",
        "Sélection de variables",
    ]),
    "eval": ("ml/eval", {"ml/eval"}, [
        "Calibration",
        "Classification metrics",
        "Compromis biais-variance",
        "Data leakage",
        "ROC-AUC & courbe PR",
        "Ranking metrics",
        "Regression metrics",
        "Validation croisée",
    ]),
    "non-supervise": ("ml/non-supervise", {"ml/non-supervise"}, [
        "Apprentissage non supervisé",
        "Classification hiérarchique (CAH)",
        "Clustering",
        "Clustering evaluation",
        "Clustering hiérarchique par densité",
        "DBSCAN",
        "Détection d'outliers multivariée",
        "Détection d'outliers univariée",
        "Gaussian Mixture Models (GMM)",
        "ICA",
        "Isolation Forest",
        "K-Means",
        "Local Outlier Factor",
        "Manifold learning",
        "NMF",
        "One-Class SVM",
        "k-médoïds (PAM)",
        "t-SNE and UMAP",
    ]),
    # Les trois dossiers déjà promus qui reçoivent une notion chacun. Le hub de chacun
    # la citait déjà : `Explicabilité des modèles` est « le cadre général » de
    # l'interprétabilité, `Déploiement de modèles` « pose le cadre » du serving,
    # `Model registry & versioning` est « la moitié qui sert au-delà de l'équipe » du
    # suivi d'expériences — trois revendications positives, aucune contention réelle.
    "interpretabilite": ("ml/interpretabilite", set(), [
        "Explicabilité des modèles",
    ]),
    "serving": ("ml/serving", set(), [
        "Déploiement de modèles",
    ]),
    "tracking": ("ml/tracking", set(), [
        "Model registry & versioning",
    ]),
    # Les cinq qui restent au NIVEAU DU DOMAINE, parce que leur sous-domaine ne
    # franchit pas le seuil : `ml/monitoring` finit à 3, `ml/feature-store` et
    # `ml/embeddings` à 2, `ml/hyperopt` à 4. C'est le démenti chiffré de la
    # remontée 35, qui les comptait parmi les six promotions à payer. Le seuil ne se
    # négocie pas pour les atteindre (remontée 4).
    "monitoring": ("ml/monitoring", set(), [
        "Data drift",
        "Monitoring de modèle en production",
    ]),
    "feature-store": ("ml/feature-store", set(), [
        "Feature store — concept",
    ]),
    "embeddings": ("ml/embeddings", set(), [
        "embeddings",
    ]),
    "hyperopt": ("ml/hyperopt", set(), [
        "Optimisation d'hyperparamètres",
    ]),
    # La seule des 67 qui change de DOMAINE. `data/eda` est défini dans `taxonomie.md`
    # comme le « profiling automatique d'un jeu de données », et le hub « Data &
    # pipelines » la revendique en nommant ses trois briques de profilage. Effet de
    # seuil de l'autre côté de la frontière (remontée 3) : `data/eda` passe de 3 à 4,
    # reste sous le seuil, et l'arbre du domaine ne bouge pas.
    "eda": ("data/eda", set(), [
        "EDA automatisée & profiling",
    ]),
}

# La page qui ne vient pas de `Wiki/Concepts/` : arbitrage nº 2 ci-dessus.
HORS_WIKI = {
    "Manifold learning": VAULT / "Statistiques & inférence" / "Analyse factorielle",
}


def lignes_fm(md: Path) -> list[str]:
    return md.read_text(encoding="utf-8").split("\n")[:40]


def categorie(md: Path) -> str:
    for ligne in lignes_fm(md):
        if ligne.startswith("categorie:"):
            return ligne.split(":", 1)[1].strip()
    return ""


def est_hub(md: Path) -> bool:
    return any(ligne.strip() == "role: hub" for ligne in lignes_fm(md))


def population(dom: str) -> list[str]:
    return [categorie(md) for md in (VAULT / dom).rglob("*.md") if not est_hub(md)]


def source(nom: str) -> Path:
    return HORS_WIKI.get(nom, SOURCE) / f"{nom}.md"


def recategoriser(path: Path, cible: str) -> None:
    lignes = path.read_text(encoding="utf-8").split("\n")
    for i, ligne in enumerate(lignes[:40]):
        if ligne.startswith("categorie:"):
            lignes[i] = f"categorie: {cible}"
            path.write_text("\n".join(lignes), encoding="utf-8")
            return
    raise SystemExit(f"{path} : aucune ligne `categorie:` dans le frontmatter")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if len(args) != 1 or args[0] not in LOTS:
        raise SystemExit(f"usage : ... <{'|'.join(LOTS)}> [--dry-run]")
    cible, ouvre, noms = LOTS[args[0]]
    dom = arbo.DOM_LABEL[cible.split("/")[0]]

    manquants = [n for n in noms if not source(n).exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) : {manquants}")
    attendue = {"concept/ml", "stats/exploratoire"}
    mauvaises = [n for n in noms if categorie(source(n)) not in attendue]
    if mauvaises:
        raise SystemExit(f"categorie de depart inattendue : {mauvaises}")

    # --- l'effet de seuil, mesuré AVANT de déplacer (remontées 3, 20 et 25) ---
    # Les pages qui partent d'un AUTRE domaine y sont retirées avant d'être ajoutées
    # ici, sinon l'effet de seuil du domaine d'origine passe inaperçu.
    origines: dict[str, list[str]] = {}
    for n in noms:
        src = source(n)
        if src.parent != SOURCE:
            d = src.relative_to(VAULT).parts[0]
            origines.setdefault(d, []).append(categorie(src))

    avant = population(dom)
    apres = avant + [cible] * len(noms)
    pa, pb = arbo.promotions(avant), arbo.promotions(apres)
    print(f"{dom} : {len(avant)} -> {len(apres)} pages")
    print(f"  {cible} : {avant.count(cible)} -> {apres.count(cible)}")
    nouvelles = set(pb) - set(pa)
    perdues = set(pa) - set(pb)
    if nouvelles != ouvre or perdues:
        raise SystemExit(
            "STOP — l'ensemble des sous-domaines promus ne bouge pas comme declare :\n"
            f"  promotions ouvertes attendues : {sorted(ouvre)}\n"
            f"  promotions ouvertes mesurees  : {sorted(nouvelles)}\n"
            f"  promotions PERDUES            : {sorted(perdues)}\n"
            "Le seuil ne se negocie pas page par page (remontees 4 et 25).")
    print(f"  promotions : {len(pa)} -> {len(pb)}"
          + (f", ouvre {sorted(nouvelles)}" if nouvelles else ", inchangees"))

    for d, cats in sorted(origines.items()):
        pop = population(d)
        reste = list(pop)
        for c in cats:
            reste.remove(c)
        qa, qb = arbo.promotions(pop), arbo.promotions(reste)
        print(f"  [origine] {d} : {len(pop)} -> {len(reste)} pages, "
              f"promotions {len(qa)} -> {len(qb)}")
        if qa != qb:
            raise SystemExit(
                f"STOP — le depart de {cats} defait un dossier dans {d} :\n"
                f"  avant : {sorted(qa)}\n  apres : {sorted(qb)}")

    print()
    print("-- les notions qui descendent --")
    dest_dir = VAULT / arbo.dossier_attendu(cible, pb)
    for nom in noms:
        src = source(nom)
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:46} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # Les briques et notions que la PROMOTION deplace par ricochet : elles etaient au
    # niveau du domaine, elles descendent dans le dossier qui vient de naitre.
    print()
    print("-- les pages que la promotion deplace par ricochet --")
    bouges = 0
    for md in sorted((VAULT / dom).rglob("*.md")):
        if est_hub(md):
            continue
        attendu = VAULT / arbo.dossier_attendu(categorie(md), pb)
        if md.parent == attendu:
            continue
        bouges += 1
        print(f"  {md.stem:46} -> {attendu.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        attendu.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(md.relative_to(VAULT)),
                        str((attendu / md.name).relative_to(VAULT))],
                       cwd=VAULT, check=True)
    print(f"  {bouges} page(s)")

    # Les comparatifs suivent leurs MEMBRES (remontee 16). Un `.base` dont la categorie
    # filtree vient d'etre promue doit descendre avec elle.
    print()
    print("-- les comparatifs a deplacer --")
    n_base = 0
    for b in sorted((VAULT / dom).rglob("*.base")):
        txt = b.read_text(encoding="utf-8")
        for cat in sorted(pb, key=len, reverse=True):
            if f'"{cat}"' in txt or f"'{cat}'" in txt:
                attendu = VAULT / arbo.dossier_attendu(cat, pb)
                if b.parent != attendu:
                    n_base += 1
                    print(f"  {b.stem} -> {attendu.relative_to(VAULT).as_posix()}")
                    if not dry:
                        attendu.mkdir(parents=True, exist_ok=True)
                        subprocess.run(
                            ["git", "mv", str(b.relative_to(VAULT)),
                             str((attendu / b.name).relative_to(VAULT))],
                            cwd=VAULT, check=True)
                break
    print(f"  {n_base} comparatif(s)")

    verbe = "a deplacer" if dry else "deplacee(s)"
    print()
    print(f"{len(noms)} notion(s) {verbe} vers {cible}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
