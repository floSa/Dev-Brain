---
role: brique
nom: Qwen-Image-Layered
alias: [Qwen Image Layered, Qwen/Qwen-Image-Layered, QwenImageLayeredPipeline]
pitch: "Modèle d'Alibaba qui décompose une image en couches RGBA éditables (Apache-2.0, 20 B) — chaque couche se redimensionne, se déplace ou se recolore sans toucher aux autres ; la voie livrable vers la transparence."
categorie: ml/apprentissage-profond
famille: modele
licence_type: open-source
maturite: production
alternatives: ["[[Qwen-Image-2.1]]"]
complements: ["[[Qwen-Image]]"]
tags: [generative-model, image-generation, diffusion, multimodal]
url_docs: https://huggingface.co/Qwen/Qwen-Image-Layered
url_repo: https://github.com/QwenLM/Qwen-Image-Layered
---

# Qwen-Image-Layered

<!-- AUTO:BANDEAU:START -->
> Modèle d'Alibaba qui décompose une image en couches RGBA éditables (Apache-2.0, 20 B) — chaque couche se redimensionne, se déplace ou se recolore sans toucher aux autres ; la voie livrable vers la transparence.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Modèle de l'équipe Qwen d'Alibaba qui prend une image et la **décompose en plusieurs couches RGBA**. Chaque couche s'édite sans toucher aux autres (redimensionner, déplacer, recolorer) ; le nombre de couches varie et une couche peut être décomposée à son tour. Dépôt Hugging Face `Qwen/Qwen-Image-Layered` créé le 2025-12-17, modifié le 2025-12-19 (lecture du 2026-10-20), 20 Md de paramètres en bfloat16, chargé par `QwenImageLayeredPipeline` de `diffusers` (version de développement). C'est le modèle de transparence dédié que Qwen-Image-2.1 dit avoir replié dans un checkpoint unifié : sa fonction reste disponible sous une licence qui se livre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| De la **transparence livrable** à un client : Apache-2.0, fichier `LICENSE` dans le dépôt GitHub | Générer l'image **et** son canal alpha en une passe → [[Qwen-Image-2.1]] (licence de recherche, non livrable) |
| **Séparer** les éléments d'une image existante pour les éditer un à un | Une **génération** de texte vers image sans image d'entrée → [[Qwen-Image]] |
| Les cas où un détourage classique échoue (cheveux, fumée, verre) à tester sur ses propres images | Un **matte de studio garanti** : aucune évaluation publiée de la qualité des bords |
| Un socle Apache-2.0 sur lequel bâtir une chaîne de retouche | Peu de mémoire : 20 Md en bfloat16 pèsent 40 Go (calcul), trois fois le module de génération de la 2.1 |

## Mise en œuvre

- Installation — `uv add transformers` et la version de développement de `diffusers` (`pip install git+https://github.com/huggingface/diffusers` dans la carte)
- Point d'entrée — `QwenImageLayeredPipeline.from_pretrained("Qwen/Qwen-Image-Layered")`, d'après la carte
- Prérequis — un GPU ; la carte ne chiffre pas la VRAM
- Exécution — local ; la carte renvoie aussi vers ModelScope et un Space de démonstration
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Licence** : Apache-2.0, vérifiée le 2026-10-20 dans le fichier `LICENSE` du dépôt `QwenLM/Qwen-Image-Layered` (non archivé, dernier push le 2025-12-31) et sur la carte. Les dépôts Hugging Face n'ont pas de fichier `LICENSE` à la racine.
- **Dépendance à du code non figé** : la classe `QwenImageLayeredPipeline` s'installe depuis la branche de développement de `diffusers`.
- **Aucune évaluation publiée** de la qualité du canal alpha contre la 2.1 : le billet de la 2.1 ne la compare pas à ce modèle.
- **Taille** : trois fois le module de génération de la 2.1, sans l'unification génération et édition.

## Écosystème

### Alternatives

- [[Qwen-Image-2.1]] — Modèle d'image d'Alibaba sous licence de recherche non commerciale (qwen-research) — texte vers image, édition jusqu'à 10 références et canal alpha natif en un seul checkpoint de 7 B (16,6 B pour la chaîne complète) ; recherche et évaluation seulement, jamais de livraison à un client. — le même savoir-faire de transparence, unifié avec la génération, mais non livrable ; Layered reste sous Apache-2.0.

### Compléments

- [[Qwen-Image]] — Modèle de génération et d'édition d'images d'Alibaba (Apache-2.0, 20 B) — texte vers image avec un rendu de texte soigné, anglais et chinois, 1328 × 1328 en carré ; la base livrable de la lignée Qwen-Image, avant la 2.1 sous licence de recherche. — génère l'image que Layered décompose ensuite en couches.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/Qwen/Qwen-Image-Layered
- Dépôt — https://github.com/QwenLM/Qwen-Image-Layered

## Voir aussi

- [[Image generation]] — la notion : générer une image depuis un texte
- [[Diffusion models]] — le moteur de ce type de modèle
- [[Licences de modèles open weights]] — pourquoi la fonction phare d'une 2.1 reste livrable dans une version antérieure
- [[Vision par ordinateur]] — le détourage et la segmentation, versant analyse
