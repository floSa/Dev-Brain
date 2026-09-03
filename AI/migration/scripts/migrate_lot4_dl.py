# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""migrate_lot4_dl.py — descend les 52 notions `concept/dl`.

Lot 4, l'avant-dernière famille. Deux gestes par page : réécrire la ligne
`categorie:` du frontmatter, puis `git mv` vers le dossier dérivé par
`AI/scripts/arbo.py`. Le CORPS des notions n'est pas touché.

**La famille se répartit sur QUATRE valeurs, et c'est tout l'objet du lot.** La
remontée 20 du lot 3 l'annonçait : la projection `concept/dl` -> `ml/apprentissage-
profond` du tableau de `v3-arborescence.md` est fausse pour une bonne moitié des
pages, qui décrivent des **tâches de vision** et non des socles d'entraînement.
Mesuré ici, avant tout `git mv`, par le croisement de la remontée 30 — les 52 noms
contre les corps des 71 hubs du vault, zone `<!-- AUTO -->` exclue :

  - **0 notion muette** : les 52 sont revendiquées par au moins un hub ;
  - **42 sur 52** le sont par un seul, et c'est à chaque fois le hub de leur cible ;
  - **10 en contention**, toutes tranchées par la lecture de la page.

**Contre la prédiction de la remontée 29, cette famille ne paie AUCUNE promotion.**
Ses trois dossiers d'accueil existent depuis le lot 3 : le seuil n'est franchi nulle
part, aucun libellé n'est à trancher, aucun sous-hub n'est à écrire. La remontée 29
prévoyait l'inverse parce qu'elle comptait `ml/apprentissage-profond` seul (8 briques
pour 52 candidates) ; c'est la répartition sur trois dossiers qui annule le coût, pas
la taille du dossier d'accueil.

Les dix contentions, et ce qui les a tranchées :

  - `Attribution par gradient`, `Interprétabilité mécaniste`, `Probing`,
    `Sparse autoencoders`, `Superposition` — le hub « Apprentissage profond » les cite
    pour **déléguer** (« l'interprétabilité de ces réseaux est un domaine à part
    entière, outillé dans [[Interprétabilité]] »), le hub « Interprétabilité » les
    revendique dans ses puces de fond. Ce n'est pas une dispute, c'est un renvoi.
  - `Quantization`, `Pruning`, `Distillation` — le hub « Serving » les cite comme un
    levier **amont** (« la latence se gagne surtout avant le serveur »), le hub
    « Apprentissage profond » leur consacre une puce entière (« compresser après
    l'entraînement est un sujet distinct », trois familles). Elles restent en `dl`.
  - `OCR` — le hub « Parsing » la cite comme la technique dont son outillage a besoin,
    le hub « Vision » lui consacre une puce (« l'OCR est un pipeline, pas un modèle »)
    et renvoie explicitement l'**outillage** vers Documents et Parsing. La notion va en
    vision, l'outillage reste où il est.
  - `Architectures CNN` — cf. l'arbitrage nº 4 de floSa ci-dessous.

Quatre arbitrages de floSa, posés en une fois avant tout déplacement :

  1. **Pas de valeur `ml/generatif`.** Elle n'aurait que 4 membres solides (`Diffusion
     models`, `GANs`, `Image generation`, `Video generation`), donc sous le seuil : les
     quatre iraient à plat au niveau du domaine, hors du dossier dont le hub les
     revendique nommément. Le 5e candidat, `Autoencodeurs`, écrit lui-même qu'« un
     autoencodeur ordinaire n'est PAS génératif » — l'y verser pour atteindre 5 serait
     exactement la remontée 4. Les quatre restent en `ml/apprentissage-profond`.
  2. **`Vision Language Models` -> `llm/modele`**, seule des 52 à changer de domaine.
     La page décrit « brancher un encodeur visuel sur un LLM » ; le hub « Vision » la
     dit lui-même « à cheval, son outillage est du côté LLM », et son critère d'entrée
     (« produit une structure : classe, boîte, masque ») exclut un modèle qui produit
     du texte. Le hub « Modèles de langage » dit « ici on décrit l'objet ». Effet de
     seuil mesuré de l'autre côté de la frontière (remontée 3) : `llm/modele` 6 -> 7,
     dossier déjà promu, arbre du domaine LLM inchangé (12 sous-dossiers avant comme
     après). C'est le cas de la remontée 25 : la frontière ne bloque pas quand ce
     qu'on trouve de l'autre côté est arbitré depuis la veille.
  3. **`Graph Neural Networks` -> `ml/apprentissage-profond`** et non `ml/graphe`.
     La page est écrite comme une architecture (« là où CNN et Transformers supposent
     une grille ») et ses voisines sont `CNN`, `Self-attention`, `Transformer
     architectures`. `ml/graphe` reste la catégorie de la brique `PyTorch Geometric`.
     Aucun effet de seuil dans un sens comme dans l'autre.
  4. **`CNN` et `Architectures CNN` se séparent.** `CNN` est le mécanisme — voisine de
     `Perceptron et MLP`, et l'ossature que `Classification audio par spectrogramme`
     réutilise hors de la vision — donc `ml/apprentissage-profond`. `Architectures CNN`
     est le catalogue de backbones vision (ResNet, MobileNet, ConvNeXt), que le hub
     « Vision » nomme avec `Vision Transformers (ViT)` comme « les deux familles de
     backbones » : les séparer de ViT aurait été le vrai contresens.

Deux pages ont été relues deux fois plutôt qu'une, et les deux restent en
`ml/apprentissage-profond` : `Classification audio par spectrogramme` et
`Speech models`, dont les voisines pointent vers « Signal & audio ». L'arbre de
décision de `taxonomie.md` met **D2** (« entraîne-t-il un modèle d'apprentissage ? »)
avant **D5** (« calcule-t-il du signal ? ») ; les deux pages décrivent une recette
d'apprentissage, pas un traitement de signal — le pré-traitement qu'elles consomment
(`STFT et spectrogramme`) vit bien, lui, dans « Signal & audio/Traitement/ ».

**Effet de seuil : nul**, mesuré sur la population réelle des deux domaines touchés
(remontées 3 et 20). « Machine Learning » passe de 122 à 173 pages, `ml/vision` de 9
à 26, `ml/interpretabilite` de 7 à 12, `ml/apprentissage-profond` de 8 à 37 — et
l'ensemble des promotions du domaine ne bouge pas, 9 avant, 9 après. Le plafond n'est
pas approché : le domaine garde 20 pages à son niveau. Le script recalcule les deux
ensembles pour chaque cible et **s'arrête** s'ils diffèrent.

Les 67 `concept/ml` ne sont PAS touchées : conversation dédiée.

Usage : uv run AI/migration/scripts/migrate_lot4_dl.py <cible> [--dry-run]
        cibles : interpretabilite | vision | modele | apprentissage-profond
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(VAULT / "AI" / "scripts"))
import arbo  # noqa: E402

SOURCE = VAULT / "Wiki" / "Concepts"

# Un lot de commit -> (categorie cible, notions). L'ordre des lots compte : le dernier
# vide `concept/dl`, et c'est LUI qui remplit la seconde moitié de la condition de mort
# de `MOC/Concepts/Deep learning` (build_mocs.py cesse de la régénérer). La première
# moitié — la mesure R7 — est acquise depuis le lot 3 (remontée 33), et se refait au
# moment du commit : la remontée 20 interdit de faire confiance à une mesure d'hier.
LOTS = {
    "interpretabilite": ("ml/interpretabilite", [
        "Attribution par gradient",
        "Interprétabilité mécaniste",
        "Probing",
        "Sparse autoencoders",
        "Superposition",
    ]),
    "vision": ("ml/vision", [
        "Apprentissage auto-supervisé en vision",
        "Architectures CNN",
        "Augmentation d'images",
        "Classification d'images",
        "Détection d'objets",
        "Estimation de pose",
        "Metric learning & ré-identification",
        "Modèles de fondation vision",
        "Métriques vision",
        "OCR",
        "Rendu neuronal 3D & estimation de profondeur",
        "Segment Anything (SAM)",
        "Segmentation",
        "Suivi d'objets",
        "Transfer learning vision",
        "Vision Transformers (ViT)",
        "Vision par ordinateur",
    ]),
    "modele": ("llm/modele", [
        "Vision Language Models",
    ]),
    "apprentissage-profond": ("ml/apprentissage-profond", [
        "Adam optimizer",
        "Architectures hybrides LLM",
        "Attention Residuals",
        "Attention linéaire",
        "Autoencodeurs",
        "CNN",
        "Calculs adaptatifs",
        "Classification audio par spectrogramme",
        "Diffusion models",
        "Distillation",
        "Entraînement distribué",
        "Flash Attention and efficient attention",
        "GANs",
        "Gradient checkpointing",
        "Graph Neural Networks",
        "Image generation",
        "Kolmogorov-Arnold Networks",
        "Maximal Update Parametrization",
        "Mixed precision",
        "Mixture of Experts",
        "Multi-head Latent Attention",
        "Positional encoding",
        "Pruning",
        "Quantization",
        "Self-attention",
        "Speech models",
        "State Space Models",
        "Transformer architectures",
        "Video generation",
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


def population(dom: str) -> list[str]:
    return [categorie(md) for md in (VAULT / dom).rglob("*.md") if not est_hub(md)]


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
    cible, noms = LOTS[args[0]]
    dom = arbo.DOM_LABEL[cible.split("/")[0]]

    manquants = [n for n in noms if not (SOURCE / f"{n}.md").exists()]
    if manquants:
        raise SystemExit(f"introuvable(s) sous {SOURCE} : {manquants}")
    mauvaises = [n for n in noms if categorie(SOURCE / f"{n}.md") != "concept/dl"]
    if mauvaises:
        raise SystemExit(f"n'est/ne sont pas `concept/dl` : {mauvaises}")

    # --- l'effet de seuil, mesuré AVANT de décider (remontées 3 et 20) ---
    avant = population(dom)
    apres = avant + [cible] * len(noms)
    pa, pb = arbo.promotions(avant), arbo.promotions(apres)
    print(f"{dom} : {len(avant)} -> {len(apres)} pages")
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
        print(f"  {nom:46} -> {dest.relative_to(VAULT).as_posix()}")
        if dry:
            continue
        recategoriser(src, cible)
        dest_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src.relative_to(VAULT)),
                        str(dest.relative_to(VAULT))], cwd=VAULT, check=True)

    # Aucune brique ne bouge : les dossiers d'accueil existent depuis le lot 3, donc
    # leurs briques y sont deja. Le script le verifie plutot que de l'affirmer.
    print()
    print("-- les briques que la promotion deplacerait --")
    bouges = 0
    for md in sorted((VAULT / dom).rglob("*.md")):
        if est_hub(md):
            continue
        attendu = VAULT / arbo.dossier_attendu(categorie(md), pb)
        if md.parent != attendu:
            bouges += 1
            print(f"  {md.stem} -> {attendu.relative_to(VAULT).as_posix()}")
    print(f"  {bouges} — attendu : 0")

    # Les comparatifs ne bougent pas : regle de la remontee 16, un comparatif vit dans
    # le dossier de ses MEMBRES. Les `.base` concernes y sont depuis le lot 3, et leurs
    # filtres portent `role == "brique"` depuis le correctif de la remontee 11 — donc
    # aucune des 52 notions ne peut y entrer.
    print()
    print("-- comparatifs : aucun a deplacer (deja dans le dossier de leurs membres)")

    verbe = "a deplacer" if dry else "deplacee(s)"
    print()
    print(f"{len(noms)} notion(s) {verbe} vers {cible}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
