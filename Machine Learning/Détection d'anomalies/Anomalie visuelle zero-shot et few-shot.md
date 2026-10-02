---
role: notion
nom: Anomalie visuelle zero-shot et few-shot
alias: [WinCLIP, AnomalyCLIP, AnomalyDINO, AdaCLIP, Détection d'anomalies zero-shot, Few-shot anomaly detection, Anomalie visuelle avec modèle vision-langage]
categorie: ml/anomalie
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, computer-vision, industrial-inspection, zero-shot, vision-language, foundation-model]
---

# Anomalie visuelle zero-shot et few-shot

## Aperçu

- Détecter des défauts sur une pièce **sans image de bon** (zero-shot) ou avec **une poignée** (few-shot), en réutilisant un modèle de fondation entraîné ailleurs : CLIP pour le langage et l'image, DINOv2 pour les features visuelles.
- Cas d'usage : démarrage d'une ligne, changement de référence, pièces produites en petite série, où réunir des dizaines d'images de bon vérifiées est déjà un coût.
- Les résultats sont bons pour la catégorie, mais **plus bas que les méthodes entraînées sur le bon** quand celles-ci ont leurs images. Cadre dans [[Détection d'anomalies visuelle]].

## Concepts clés

### Ce que « zero-shot » veut dire ici

- **Pas d'image de la pièce cible**, mais pas « sans aucune donnée » : AnomalyCLIP et AdaCLIP entraînent des prompts sur un **jeu auxiliaire** annoté puis testent sur d'autres jeux. WinCLIP en zero-shot s'en tient à des prompts composés à la main, sans prompt appris.
- Le résultat annoncé dépend donc du couple jeu auxiliaire / jeu de test, et d'un protocole qui n'est pas celui d'une ligne d'atelier. Voir [[Modèles de fondation vision]] pour les modèles réutilisés.

### WinCLIP

Jeong et al. (CVPR 2023). CLIP reçoit un ensemble **compositionnel** de prompts — des mots d'état (« flawless », « damaged ») croisés avec des modèles de phrase — et des **fenêtres glissantes** multi-échelles : les features de chaque fenêtre, alignées avec le texte, donnent une carte d'anomalie. WinCLIP+ ajoute des images normales de référence.

| Régime (MVTec AD, valeurs du papier) | Classification (AUROC) | Segmentation (AUROC) |
|---|---|---|
| Zero-shot | 91,8 | 85,1 |
| 1 image (WinCLIP+) | 93,1 | 95,2 |
| 4 images | 95,2 | 96,2 |
| PatchCore, jeu complet (référence du papier) | 99,6 | 98,2 |

Le papier note qu'une **définition précise de l'anomalie** est nécessaire pour de bons résultats : la qualité du prompt compte.

### AnomalyCLIP

Zhou et al. (ICLR 2024). Au lieu de prompts écrits à la main, **deux prompts apprenables** — un normal, un anormal — indépendants de l'objet (le nom de la classe est remplacé par « object »). CLIP ViT-L/14@336px reste gelé ; l'optimisation est « glocale » (globale et locale) et l'attention est remplacée par une attention diagonale-saillante pour mieux localiser. Entraînement sur un jeu auxiliaire (le test de VisA pour évaluer MVTec AD, le test de MVTec AD pour les autres jeux), 17 jeux industriels et médicaux évalués. MVTec AD : 91,5 % d'AUROC image, 91,1 % pixel. Brique : [[AnomalyCLIP]].

### AnomalyDINO

Damm et al. (WACV 2025, oral). **Vision seule, sans entraînement** : un plus proche voisin au niveau du patch avec DINOv2, le même schéma que [[Anomalie visuelle par banque de mémoire|la banque de mémoire]] mais avec une banque faite de quelques images, plus un masquage de l'objet et une augmentation par rotation facultatifs.

| Nombre d'images de bon (MVTec AD, ViT-S, résolution 672) | AUROC image |
|---|---|
| 1 | 96,6 |
| 4 | 97,7 |
| 16 | 98,4 |

À une image, le papier donne 93,1 % pour WinCLIP+ et 83,4 % pour PatchCore. Le modèle par défaut (ViT-S, 21 M de paramètres) tourne en environ 60 ms par image à la résolution 448 sur un GPU A40.

### D'autres travaux, un par une

- **AdaCLIP** (Cao et al., ECCV 2024) : prompts appris statiques et dynamiques (par image) sur des données auxiliaires ; 89,2 % d'AUROC image sur MVTec AD en zero-shot, contre 91,8 % rapporté pour WinCLIP dans son propre tableau.
- **AA-CLIP** (Ma et al., CVPR 2025) : constate que CLIP est « *anomaly-unaware* », construit d'abord un espace texte normal/anormal puis aligne les patchs par des adaptateurs résiduels. Chiffres non repris ici, faute de lecture sûre.
- Côté médical, MVFA (Huang et al., CVPR 2024) : hors périmètre de cette page.

### Limites

- **Un écart avec les méthodes entraînées sur le bon.** WinCLIP zero-shot est à 91,8 % contre 99,6 % pour PatchCore sur jeu complet (papier WinCLIP) ; AnomalyDINO à 16 images atteint 98,4 %. Les protocoles diffèrent : à lire comme un ordre de grandeur, pas comme un classement.
- **Défauts logiques non détectés.** L'annexe d'AnomalyDINO le dit : les anomalies sémantiques ou logiques ne sont pas détectées, l'exemple étant l'échange de deux câbles sur MVTec AD. Voir la distinction sensoriel / logique dans [[Anomalie visuelle par reconstruction, distillation et flux]].
- **Dépendance au prompt** pour WinCLIP ; aucune source lue ne la chiffre pour AnomalyCLIP ou AdaCLIP.
- **Coût d'un grand ViT** : AnomalyCLIP s'appuie sur un ViT-L/14 à 336 px, et aucun papier lu n'en chiffre la latence. À titre de repère, Dinomaly mesure un ViT-L à 24,2 images par seconde contre 58,1 pour un ViT-B (RTX 3090, lot de 16) : un autre modèle, mais le même ordre de coût.
- **Statut des poids** : les poids CLIP d'OpenAI ne portent pas de licence explicite ; la fiche de modèle écrit que tout usage déployé, commercial ou non, est « hors périmètre ». À trancher avant une livraison (voir [[AnomalyCLIP]]).
- **Le terrain d'essai est le même que pour les autres méthodes** : MVTec AD est saturé ; ni WinCLIP, ni AnomalyCLIP, ni AnomalyDINO ne sont évalués dans le papier MVTec AD 2.

## Les maths, simplement

- Zero-shot par CLIP : le score d'une fenêtre est la probabilité de la classe « anormal » parmi deux prompts, $s=\dfrac{e^{\langle f,t_a\rangle/\tau}}{e^{\langle f,t_n\rangle/\tau}+e^{\langle f,t_a\rangle/\tau}}$, où $f$ est la feature de la fenêtre, $t_n$ et $t_a$ les features de texte « normal » et « anormal », $\tau$ une température. Forme générique du principe, pas la formule exacte d'un des papiers.
- Few-shot par patchs : $s(p)=\min_{m\in\mathcal{M}}\lVert\phi_p-m\rVert$ avec $\mathcal{M}$ les patchs de quelques images de bon — la formule de la banque de mémoire, sur un $\mathcal{M}$ minuscule.

## En pratique

- **Prototyper avant de collecter** : tester si un défaut est visible par un modèle vision-langage avant d'investir dans un jeu d'images de bon.
- **Passer au few-shot dès qu'il existe quelques images de bon vérifiées** : sur MVTec AD, AnomalyDINO à une image (96,6 %) dépasse déjà WinCLIP+ (93,1 %) dans le papier ; un seul jeu, donc à confirmer sur la ligne.
- **Ne jamais livrer un score zero-shot sans le mesurer sur des défauts réels de la ligne** ; le chiffre d'un jeu public ne dit rien de l'éclairage ou du cadrage de l'atelier.
- Les méthodes zero-shot et few-shot existent dans [[anomalib]] (WinCLIP, AnomalyDINO, entre autres modèles listés) ; AnomalyCLIP s'utilise via son propre dépôt.

## Approches voisines & alternatives

- [[Anomalie visuelle par banque de mémoire]] — la même logique de plus proche voisin, avec la banque complète.
- [[Anomalie visuelle par reconstruction, distillation et flux]] — entraîner sur le bon quand il est disponible.
- [[Modèles de fondation vision]] — CLIP, DINOv2 et les autres modèles réutilisés tels quels.
- [[Transfer learning vision]] — le cadre d'ensemble de la réutilisation de features.
- [[Apprentissage auto-supervisé en vision]] — d'où viennent les features de DINOv2.
- [[Détection hors distribution (OOD)]] — le cas où on juge une entrée d'un classifieur existant.

## Pour aller plus loin

- Jeong et al. (2023), *WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation*, CVPR. arXiv : https://arxiv.org/abs/2303.14814
- Zhou et al. (2024), *AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection*, ICLR. arXiv : https://arxiv.org/abs/2310.18961
- Damm et al. (2025), *AnomalyDINO: Boosting Patch-based Few-shot Anomaly Detection with DINOv2*, WACV. arXiv : https://arxiv.org/abs/2405.14529
- Cao et al. (2024), *AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection*, ECCV. arXiv : https://arxiv.org/abs/2407.15795
- Ma et al. (2025), *AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP*, CVPR. arXiv : https://arxiv.org/abs/2503.06661
