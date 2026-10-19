---
role: brique
nom: Qwen-Image
alias: [Qwen Image, Qwen/Qwen-Image, Qwen-Image 20B]
pitch: "Modèle de génération et d'édition d'images d'Alibaba (Apache-2.0, 20 B) — texte vers image avec un rendu de texte soigné, anglais et chinois, 1328 × 1328 en carré ; la base livrable de la lignée Qwen-Image, avant la 2.1 sous licence de recherche."
categorie: ml/apprentissage-profond
famille: modele
licence_type: open-source
maturite: production
alternatives: ["[[Qwen-Image-2.1]]"]
complements: ["[[Qwen-Image-Layered]]"]
tags: [generative-model, image-generation, diffusion, multimodal]
url_docs: https://huggingface.co/Qwen/Qwen-Image
url_repo: https://github.com/QwenLM/Qwen-Image
---

# Qwen-Image

<!-- AUTO:BANDEAU:START -->
> Modèle de génération et d'édition d'images d'Alibaba (Apache-2.0, 20 B) — texte vers image avec un rendu de texte soigné, anglais et chinois, 1328 × 1328 en carré ; la base livrable de la lignée Qwen-Image, avant la 2.1 sous licence de recherche.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Modèle de fondation de génération d'images de l'équipe Qwen d'Alibaba, dépôt Hugging Face `Qwen/Qwen-Image` créé le 2025-08-02, dernière modification le 2025-08-18 (lecture du 2026-10-20). La carte le présente comme un modèle qui progresse surtout sur le **rendu de texte complexe** dans l'image, en anglais et en chinois, et sur l'édition précise. 20 Md de paramètres d'après la table de lignée d'un document de veille du 2026-09-22 ; chargement par `DiffusionPipeline` de la bibliothèque `diffusers`. Résolutions recommandées par la carte : 1328 × 1328 (carré), 1664 × 928 (16:9), 928 × 1664 (9:16), 1472 × 1140 (4:3), 1584 × 1056 (3:2) et leurs inverses. C'est la **dernière base de la lignée entièrement livrable** : la version 2.1 a quitté Apache-2.0 pour une licence de recherche.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des images **livrées à un client** : Apache-2.0, fichier `LICENSE` dans le dépôt GitHub, champ `license: apache-2.0` sur la carte | Un **canal alpha natif** dans le même modèle → [[Qwen-Image-2.1]] (licence de recherche, non livrable) ou [[Qwen-Image-Layered]] (couches RGBA, Apache-2.0) |
| Du **texte lisible dans l'image** (affiches, interfaces), en anglais ou en chinois | Un **classement indépendant** : Artificial Analysis Image Arena le place 100e à 886 Elo le 2026-09-22, derrière Z-Image Turbo (942, poids ouverts) |
| Un socle commun avec [[Qwen-Image-Layered]], pour décomposer ensuite l'image en couches | Une **VRAM annoncée** : aucune chiffrée dans ce qui a été relu ; 20 Md en bfloat16 pèsent déjà 40 Go (calcul, hors encodeur de texte) |

## Mise en œuvre

- Installation — `uv add diffusers transformers` ; `DiffusionPipeline.from_pretrained("Qwen/Qwen-Image", torch_dtype=...)`, d'après la carte
- Point d'entrée — pipeline `diffusers`, résolutions recommandées ci-dessus
- Prérequis — un GPU ; 20 Md × 2 octets = 40 Go en bfloat16, donc quantification ou délestage sur une carte grand public (calcul, non mesuré ici)
- Exécution — local ou auto-hébergé ; aucun fournisseur d'inférence géré n'a été vérifié
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Licence** : Apache-2.0, vérifiée le 2026-10-20 dans le fichier `LICENSE` du dépôt `QwenLM/Qwen-Image` (non archivé, dernier push le 2026-02-10) et sur la carte. La licence de la version suivante, 2.1, est différente : lire celle du dépôt visé.
- **Rang indépendant modeste** : 100e sur plus de 155 modèles dans l'arène d'Artificial Analysis le 2026-09-22 (886 Elo). Un autre modèle d'Alibaba à poids ouverts, Z-Image Turbo, le devance (942). Pour une option livrable, la base de Qwen n'est pas le meilleur choix par défaut.
- **Aucun score repris** : les classements d'éditeur de la lignée portent sur un banc interne sans version ni barres d'erreur.
- **Fraîcheur** : poids inchangés depuis août 2025.

## Écosystème

### Alternatives

- [[Qwen-Image-2.1]] — Modèle d'image d'Alibaba sous licence de recherche non commerciale (qwen-research) — texte vers image, édition jusqu'à 10 références et canal alpha natif en un seul checkpoint de 7 B (16,6 B pour la chaîne complète) ; recherche et évaluation seulement, jamais de livraison à un client. — un canal alpha natif et dix références dans 7 Md, mais non livrable : Qwen-Image reste la base Apache-2.0.

### Compléments

- [[Qwen-Image-Layered]] — Modèle d'Alibaba qui décompose une image en couches RGBA éditables (Apache-2.0, 20 B) — chaque couche se redimensionne, se déplace ou se recolore sans toucher aux autres ; la voie livrable vers la transparence. — décompose en couches l'image que Qwen-Image génère.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/Qwen/Qwen-Image
- Dépôt — https://github.com/QwenLM/Qwen-Image

## Voir aussi

- [[Image generation]] — la notion : générer une image depuis un texte
- [[Diffusion models]] — le moteur des générateurs d'images actuels
- [[Licences de modèles open weights]] — Apache-2.0 contre licence de recherche dans une même lignée
- [[Lire un score publié]] — un classement d'éditeur contre un classement indépendant
- [[Quantization]] — ce qui permet de charger un tel modèle sur une carte grand public
