---
role: brique
nom: Qwen-Image-2.1
alias: [Qwen Image 2.1, Qwen/Qwen-Image-2.1, QwenImage21Pipeline, qwen-research]
pitch: "Modèle d'image d'Alibaba sous licence de recherche non commerciale (qwen-research) — texte vers image, édition jusqu'à 10 références et canal alpha natif en un seul checkpoint de 7 B (16,6 B pour la chaîne complète) ; recherche et évaluation seulement, jamais de livraison à un client."
categorie: ml/apprentissage-profond
famille: modele
licence_type: source-available
maturite: beta
alternatives: ["[[Qwen-Image]]", "[[Qwen-Image-Layered]]"]
tags: [generative-model, image-generation, diffusion, multimodal]
url_docs: https://huggingface.co/Qwen/Qwen-Image-2.1
url_repo: 
---

# Qwen-Image-2.1

<!-- AUTO:BANDEAU:START -->
> Modèle d'image d'Alibaba sous licence de recherche non commerciale (qwen-research) — texte vers image, édition jusqu'à 10 références et canal alpha natif en un seul checkpoint de 7 B (16,6 B pour la chaîne complète) ; recherche et évaluation seulement, jamais de livraison à un client.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | source-available | à charger dans un runtime | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Modèle d'image d'Alibaba à poids téléchargeables sous licence de recherche non commerciale : gratuit en local pour un usage non commercial, mais à ne jamais utiliser pour produire des images livrées à un client.** Dépôt Hugging Face `Qwen/Qwen-Image-2.1`, créé le 2026-09-14, modifié le 2026-09-30 (lecture du 2026-10-20) ; sortie annoncée le 2026-09-20. Un checkpoint, trois fonctions : texte vers image, édition (jusqu'à 10 images de référence) et image RGBA à **canal alpha natif**, choisie par une phrase du prompt. Le module de génération est un **DiT** de 32 couches « single-stream » à **7,1 Md** de paramètres ; la chaîne complète (encodeur de texte Qwen3-VL de 8,8 Md, VAE de 0,7 Md) pèse **16,6 Md, soit 33,1 Go en bfloat16**. Le VAE déclare 4 canaux : la transparence est vraisemblablement portée par lui (déduction d'après les `config.json`, non documentée).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| **Évaluer** le canal alpha natif, l'édition à dix références ou les trois modes de masquage, à titre personnel ou en recherche | **Toute livraison à un client**, même d'une image : le fait de faire tourner le modèle à des fins commerciales est hors de la concession → [[Qwen-Image]] ou [[Qwen-Image-Layered]], sous Apache-2.0 |
| Un masque **séparé** de l'image source, seul mode des trois qui s'industrialise (les cercles et l'annotation peinte écrivent dans les pixels) | Une chaîne montée sur `diffusers` **publié** : `QwenImage21Pipeline` n'est que dans la branche de développement |
| Une carte de 24 ou 32 Go **avec une quantification** communautaire (INT8 : 16,1 Gio pour la chaîne complète) | Un modèle sans quantification : 33,1 Go en bf16, hors de portée d'une RTX 3090 ou 5090 |

## Mise en œuvre

- Installation — `pip install git+https://github.com/huggingface/diffusers` (la carte demande la branche principale) ; `QwenImage21Pipeline.from_pretrained(...)` en bfloat16, puis `pipe.enable_model_cpu_offload()` pour réduire la VRAM
- Point d'entrée — le prompt doit être explicite pour la transparence : décrire le sujet, puis « The image has alpha channel and the background is transparent. » (une phrase, pas un drapeau d'API)
- Prérequis — un GPU et une quantification : 33,1 Go de poids en bfloat16 (calcul sur les tailles de fichiers : 14,2 Go le DiT, 17,5 Go l'encodeur, 1,35 Go le VAE) ; aucune VRAM ni latence publiées par l'éditeur
- Exécution — local seulement : aucun fournisseur d'inférence géré au 2026-09-22 ; essais de tiers sur une RTX 3090 en INT8 (82 à 96 s par image de 2048 × 1152, 50 pas) et sur une RTX 5090 (19 à 20 s à 1024², mesures non reproduites)
- Coût — gratuit en local, non commercial ; toute licence commerciale se demande à l'éditeur, sans tarif publié

## Limites à connaître

- **Licence `qwen-research`, lue le 2026-10-20** (champ `license_name` de la carte, fichier `LICENSE` daté du 2026-09-20) : « Non-Commercial » = recherche ou évaluation seulement (§1.i), concession limitée aux fins non commerciales (§2.a), licence commerciale distincte exigée (§2.b). Aucun seuil de revenu ni d'utilisateurs. Droit chinois, tribunaux de Hangzhou. Si on entraîne un modèle distribué avec ses sorties : mention « Built with Qwen » (§4.b). **Ne pas livrer** d'image produite par ce modèle à un client.
- **La bannière dit « open weights »** et le billet « open-source » ; le champ de licence est passé d'Apache-2.0 (toute la lignée précédente) à `qwen-research`. Open weights et open source sont deux choses : voir [[Licences de modèles open weights]].
- **« 7 B » est le seul module de génération**, 43 % du modèle réel.
- **Dix références et carte grand public ne tiennent pas ensemble** : un cache KV de 512 Kio par token (calcul sur la configuration publiée, attention pleine) fait 5 Gio pour dix images de 512², 20 Gio à 1024², 80 Gio à 2048² ; aucun essai de tiers n'utilise plus d'une référence.
- **Le canal alpha brut n'est pas un matte de studio** : sur l'image d'exemple de l'éditeur, 23,4 % des pixels sont partiellement transparents, dont 6,5 % de l'image à plus de 6 pixels de tout bord (mesure d'une seule image, par la source de veille).
- **Aucun score indépendant** : le 60,28 est celui de Qwen-Image-Bench, banc interne sans version ni barres d'erreur ; le modèle est absent des classements d'Artificial Analysis au 2026-09-22.

## Écosystème

### Alternatives

- [[Qwen-Image]] — Modèle de génération et d'édition d'images d'Alibaba (Apache-2.0, 20 B) — texte vers image avec un rendu de texte soigné, anglais et chinois, 1328 × 1328 en carré ; la base livrable de la lignée Qwen-Image, avant la 2.1 sous licence de recherche. — la base livrable : Apache-2.0, trois fois le module de génération de la 2.1, sans alpha natif.
- [[Qwen-Image-Layered]] — Modèle d'Alibaba qui décompose une image en couches RGBA éditables (Apache-2.0, 20 B) — chaque couche se redimensionne, se déplace ou se recolore sans toucher aux autres ; la voie livrable vers la transparence. — la même fonction de transparence que la 2.1 absorbe, livrable sous Apache-2.0.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/Qwen/Qwen-Image-2.1
- Texte de la licence : https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE

## Voir aussi

- [[Licences de modèles open weights]] — la notion : le cas `qwen-research`, ni seuil ni exception commerciale
- [[Image generation]] — la notion : générer une image depuis un texte
- [[Diffusion models]] — le moteur : un DiT qui débruite
- [[Lire un score publié]] — un 60,28 de banc d'éditeur, sans version ni barres d'erreur
- [[Quantization]] — ce qui permet de charger les 33,1 Go sur une carte de 24 Go
