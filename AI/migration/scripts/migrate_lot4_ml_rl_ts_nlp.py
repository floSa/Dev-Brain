# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_ml_rl_ts_nlp.py — descend les 37 notions `rl`, `ts` et `nlp`.

Lot 4, les trois plus petites familles restantes, toutes du domaine « Machine
Learning ». Deux gestes par page : réécrire la ligne `categorie:` du frontmatter,
puis `git mv` vers le dossier dérivé par `AI/scripts/arbo.py`. Le CORPS des notions
n'est pas touché.

**Le lot le plus mécanique de la migration, et c'est mesuré.** Les trois
sous-dossiers d'accueil existent depuis le lot 3, les trois valeurs (`ml/rl`,
`ml/series-temporelles`, `ml/nlp`) sont dans le vocabulaire depuis la v2, et les
trois libellés sont dans `arbo.SUB_LABEL`. **Zéro valeur ouverte, zéro sous-dossier
créé, zéro libellé à trancher** — le premier lot de notions dans ce cas.

L'étape 0 a rangé **37 notions sur 37** : les trois sous-hubs les citent toutes
nommément, et le croisement des 37 noms contre les corps des 53 hubs du vault ne
montre AUCUNE contention — chaque notion est revendiquée par un seul hub, le sien
(`Reinforcement learning` l'est aussi par le hub de domaine, son parent, ce qui ne
la dispute pas). C'est une partition plus nette que celle de « Mathématiques »
(remontée 12), et la lecture des 37 pages n'en a contredit aucune (remontée 2).

**Effet de seuil : nul**, mesuré sur la population réelle du domaine (remontées 3 et
20). Les trois sous-domaines sont déjà des dossiers ; ils passent de 6 à 23, de 7 à
20 et de 6 à 13 pages sans que l'ensemble des promotions du vault bouge — 42 avant,
42 après. Le plafond n'est pas approché : « Machine Learning » garde 19 pages à son
niveau. Le script recalcule les deux ensembles et **s'arrête** s'ils diffèrent.

Les `concept/dl` (52) et `concept/ml` (67) ne sont PAS touchés : ils sont réservés à
deux conversations dédiées, et la remontée 20 du lot 3 signale que la moitié des `dl`
relèvent de `ml/vision` — un arbitrage qui a besoin de voir les 52 d'un coup.

Usage : uv run AI/migration/scripts/migrate_lot4_ml_rl_ts_nlp.py <rl|ts|nlp> [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"
DOMAINE = arbo.DOM_LABEL["ml"]

# Une famille `concept/*` -> la valeur `ml/*` qui la remplace. Le rangement par
# défaut est le sous-domaine homonyme, et rien ne s'en écarte : les 37 pages le
# confirment une par une. Deux ont été relues deux fois plutôt qu'une, et les deux
# restent (cf. les remontées du lot) — `Fuzzy matching & similarité de chaînes`,
# seule des 37 dont `domaines:` porte `data-eng`, et `Théorie des jeux`, seule dont
# le sujet soit une branche des mathématiques.
FAMILLES = {
    "rl": ("ml/rl", [
        "Actor-Critic methods",
        "AlphaZero and self-play",
        "Bellman equations",
        "Counterfactual Regret Minimization",
        "Exploration vs exploitation",
        "Imitation learning",
        "Markov Decision Process",
        "Model-based RL",
        "Monte Carlo Tree Search",
        "Offline RL",
        "PPO",
        "Policy gradient",
        "Q-learning and DQN",
        "Reinforcement learning",
        "Reward shaping and hacking",
        "Théorie des jeux",
        "Value functions",
    ]),
    "ts": ("ml/series-temporelles", [
        "ARIMA SARIMA",
        "Autocorrelation",
        "Exponential smoothing",
        "Forecasting framing",
        "Forecasting metrics",
        "Foundation models pour séries temporelles",
        "Hierarchical forecasting",
        "Intermittent demand",
        "Maintenance prédictive et RUL",
        "Stationarity",
        "Time series anomaly detection",
        "Time series feature engineering",
        "Walk-forward CV",
    ]),
    "nlp": ("ml/nlp", [
        "BM25",
        "Classification de texte",
        "Fuzzy matching & similarité de chaînes",
        "NER et étiquetage de séquence",
        "Recherche d'information",
        "TF-IDF",
        "Traitement du langage naturel",
    ]),
}


def lignes_fm(md: Path) -> list[str]:
    return md.read_text(encoding="utf-8").split("\n")[:40]


def categorie(md: Path) -> str:
    for ligne in lignes_fm(md):
        if ligne.startswith("categorie:"):
            return ligne.split(":", 1)[1].strip()
    return ""


def est_hub(md: Path) -> bool:
    return any(l.strip() == "role: hub" for l in lignes_fm(md))


def population() -> list[str]:
    return [categorie(md) for md in (VAULT / DOMAINE).rglob("*.md")
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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if len(args) != 1 or args[0] not in FAMILLES:
        raise SystemExit(f"usage : ... <{'|'.join(FAMILLES)}> [--dry-run]")
    famille = args[0]
    cible, noms = FAMILLES[famille]

    manquants = [n for n in noms if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")
    mauvaises = [n for n in noms
                 if categorie(SOURCE / f"{n}.md") != f"concept/{famille}"]
    if mauvaises:
        raise SystemExit(f"n'est/ne sont pas `concept/{famille}` : {mauvaises}")

    # --- l'effet de seuil, mesuré AVANT de décider (remontées 3 et 20) ---
    avant = population()
    apres = avant + [cible] * len(noms)
    pa, pb = arbo.promotions(avant), arbo.promotions(apres)
    print(f"{DOMAINE} : {len(avant)} -> {len(apres)} pages")
    print(f"  {cible} : {avant.count(cible)} -> {apres.count(cible)}")
    if pa != pb:
        raise SystemExit(
            "STOP — l'ensemble des sous-domaines promus change :\n"
            f"  avant : {sorted(pa)}\n  apres : {sorted(pb)}\n"
            "Le seuil ne se negocie pas page par page (remontees 4 et 25) : "
            "rouvrir l'arbitrage plutot qu'encaisser la promotion.")
    print(f"  promotions identiques avant/apres ({len(pa)} sous-dossiers)")

    print()
    print("-- les notions qui descendent --")
    dest_dir = VAULT / arbo.dossier_attendu(cible, pb)
    for nom in noms:
        src = SOURCE / f"{nom}.md"
        dest = dest_dir / f"{nom}.md"
        print(f"  {nom:44} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # Aucune brique ne bouge : les trois sous-dossiers existent depuis le lot 3,
    # donc leurs briques y sont deja. Le script le verifie plutot que de l'affirmer.
    print()
    print("-- les briques que la promotion deplacerait --")
    bouges = 0
    for md in sorted((VAULT / DOMAINE).rglob("*.md")):
        if est_hub(md):
            continue
        attendu = VAULT / arbo.dossier_attendu(categorie(md), pb)
        if md.parent != attendu:
            bouges += 1
            print(f"  {md.stem} -> {attendu.relative_to(VAULT).as_posix()}")
    print(f"  {bouges} — attendu : 0")

    # Les comparatifs ne bougent pas non plus, et c'est la regle de la remontee 16 :
    # un comparatif vit dans le dossier de ses MEMBRES. Les trois `.base` concernes
    # sont deja dans le sous-dossier de leurs membres depuis le lot 3, et leurs
    # filtres portent `role == "brique"` depuis le correctif de la remontee 11 —
    # donc aucune des 37 notions ne peut y entrer.
    print()
    print("-- comparatifs : aucun a deplacer (deja dans le dossier de leurs membres)")

    verbe = "a deplacer" if dry else "deplacee(s)"
    print()
    print(f"{len(noms)} notion(s) {verbe} vers {cible}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
