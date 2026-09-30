---
role: notion
nom: Annotation de données
alias: [annotation, data labeling, étiquetage de données, labellisation, labeling, annotation d'images, annotation de texte]
categorie: ml/annotation
domaines: [data-sci, ml-eng]
tags: [annotation, human-in-the-loop, supervised, self-hosted]
---

# Annotation de données

## Aperçu

- Produire à la main, ou corriger à la main, les **étiquettes** d'un jeu de données : la classe d'une image, les boîtes d'une scène, les entités d'un texte, les intervalles d'un signal. Sans elles, un apprentissage supervisé n'a ni cible ni jeu de mesure.
- Une étiquette est une **décision humaine consignée**, pas une vérité : sa qualité se mesure par la cohérence entre annotateurs et par les erreurs qui survivent, et elle coûte du temps de personnes avant de coûter du calcul.
- Sur site, chez un industriel ou pour une ESN, la contrainte dominante est que **les données ne sortent pas** : l'outil s'héberge chez le client, les annotateurs sont des salariés ou des experts métier, et ni le crowdsourcing public ni un SaaS ne sont disponibles.

## Concepts clés

### Types de tâches

- **Classification** d'un objet entier, à une ou plusieurs étiquettes : image, document, segment audio.
- **Détection** : une boîte englobante par instance. **Segmentation** : un polygone ou un masque par pixel, sémantique (une classe par pixel) ou par instance. **Points clés et squelettes** pour la pose, **pistes** pour suivre un objet d'une image de vidéo à l'autre.
- **Texte** : reconnaissance d'entités par spans (schémas IOB ou BILOU, cf. [[NER et étiquetage de séquence]]), relations entre entités, classification de documents.
- **Audio et séries** : transcription, intervalles étiquetés sur un signal ou sur une série temporelle.
- Deux outils du brain se partagent le terrain : [[CVAT]] pour la vision — images, vidéo, nuages de points 3D, avec suivi et squelettes —, [[Label Studio]] pour tout le reste, texte, audio et séries compris, et aussi pour les images.

### Guide d'annotation

- Le **guide** est le texte qui tranche les cas limites : ce qui compte comme une instance, où s'arrête une boîte, quoi faire d'un objet coupé par le cadre. Il s'écrit sur un lot pilote annoté par plusieurs personnes, puis se corrige là où elles divergent.
- Il se **versionne avec les étiquettes** : un jeu sans la version du guide qui l'a produit ne se compare pas à un autre, cf. [[Versionnage de données]].
- Un guide plus long ne supprime pas le désaccord. C'est l'un des « sept mythes de l'annotation » que dressent Aroyo et Welty (2015) : croire que des consignes détaillées font converger les annotateurs, et croire qu'une seule vérité existe.

### Accord inter-annotateurs

- Le taux brut d'accord $p_o$ flatte : sur une classe rare, deux annotateurs qui répondent au hasard s'accordent beaucoup. Le **kappa de Cohen** (1960) corrige du hasard, pour deux juges et des catégories nominales :

  $$\kappa = \frac{p_o - p_e}{1 - p_e}$$

  où $p_e$ est l'accord attendu par hasard d'après la fréquence de chaque classe chez chaque juge. Cohen l'illustre par deux psychiatres qui classent au hasard 10 % de cas positifs : ils s'accordent à 82 % par pur hasard, et $\kappa$ vaut alors 0.
- Pour plus de deux annotateurs, des valeurs manquantes ou des échelles d'intervalle, on emploie l'**alpha de Krippendorff**. La synthèse de référence est Artstein et Poesio (2008) : les coefficients pondérés de type alpha conviennent à beaucoup de tâches d'annotation, mais leur valeur est plus difficile à interpréter.
- **Les seuils ne sont pas objectifs.** Artstein et Poesio notent que les échelles d'interprétation viennent de la médecine ou de choix d'usage ; si un seuil est nécessaire, 0,8 est selon eux une bonne valeur, mais ils doutent qu'un seuil unique convienne à tous les usages.
- **Le désaccord porte de l'information.** Plank (2022) défend que la variation humaine d'étiquetage est souvent traitée à tort comme du bruit, alors qu'elle peut venir d'un vrai désaccord ou de plusieurs réponses plausibles, et qu'elle touche les données, la modélisation et l'évaluation ; Aroyo et Welty (2015) en font le principe du « crowd truth ». Conserver les étiquettes non agrégées est donc un choix de méthode, pas seulement de stockage.

### Pré-annotation par un modèle

- Un modèle propose une étiquette, l'annotateur la corrige. Le gain de temps est réel : dans le « data engine » de Segment Anything (Kirillov et al., 2023), la phase assistée fait passer l'annotation d'un masque de 34 à 14 secondes, avant que le modèle prenne la main sur une partie du corpus ; sur du texte, Fort et Sagot (2010) mesurent, pour dix phrases, un passage de 7,5 à 2,5 minutes chez un annotateur et de 11,5 à 2,5 minutes chez l'autre avec une bonne pré-annotation.
- **Le risque est l'ancrage.** Dans l'étude de Fort et Sagot, l'annotateur le plus précis se dégrade avec une mauvaise pré-annotation (98,1 % à 95,8 %) tandis que le moins précis progresse : l'effet dépend de la personne, et les auteurs le relient à une attention réduite. Schroeder, Roy et Kabbara (2025), avec 410 annotateurs sur des tâches subjectives, observent que les suggestions d'un LLM n'accélèrent pas le travail mais augmentent la confiance, que les annotateurs les adoptent, et que le consensus à cinq sur cinq passe de 8 % à 38 % quand les étiquettes sont pré-remplies.
- **Conséquence pour la mesure** : le F1 de GPT-4 évalué sur ces étiquettes assistées passe de 0,47 à 0,79 dans la même étude — un modèle noté sur des étiquettes qu'il a lui-même suggérées paraît meilleur qu'il ne l'est. Il faut donc garder un **sous-échantillon annoté sans suggestion**, pour mesurer et pour évaluer, et relever le taux d'acceptation des propositions.
- Outils : le SDK de backends ML de [[Label Studio]] (exemples officiels pour [[Ultralytics YOLO]], [[segment-anything]], [[spaCy]] et [[GLiNER]]) et les fonctions serverless de [[CVAT]] (SAM, YOLOv7, [[Detectron2]]). **SetFit n'est pas fourni en exemple** par l'un ni par l'autre.

### Active learning

- Plutôt que d'étiqueter au hasard, l'algorithme choisit les exemples dont il tirera le plus : Settles (2009) le définit comme la possibilité d'atteindre une meilleure précision avec moins d'étiquettes en interrogeant un oracle, par exemple un annotateur. Les stratégies les plus courantes sont l'échantillonnage par incertitude — étiquette la moins sûre, marge, entropie —, puis le vote d'un comité de modèles ; Ren et al. (2021) classent celles du deep learning.
- **Dans les outils** : [[Label Studio]] réserve la boucle automatique à Enterprise, la Community se contente de trier les tâches à la main et de relire des prédictions ; la documentation de [[CVAT]] lue ici ne décrit pas de boucle.
- **Le piège** : un jeu construit par échantillonnage d'incertitude n'est pas représentatif de la population, il ne sert donc pas à évaluer le modèle.

### Contrôle qualité

- **Double annotation d'un sous-échantillon** et calcul de l'accord, **revue** d'un échantillon par un relecteur, puis ce qu'on appelle un jeu « or » : des éléments annotés à l'avance par un expert, glissés dans le flux pour repérer un annotateur qui dérive. Dans les deux outils, la revue assignée et le contrôle qualité automatique sont des fonctions payantes ; en édition libre, l'accord se calcule sur l'export.
- **Détecter les étiquettes erronées après coup** : le *confident learning* de Northcutt, Jiang et Chuang (2021) estime la loi jointe entre étiquettes bruitées et vraies et désigne les exemples suspects, outil cleanlab à l'appui. Le même groupe trouve au moins 3,3 % d'erreurs en moyenne dans dix jeux de test très utilisés (2021), ce qui renverse parfois le classement des modèles.

### Coût

- Le poste dominant est le temps humain, et il dépend de la forme : une boîte coûte peu, un masque précis beaucoup plus, une vidéo suivie image par image encore davantage ; la pré-annotation déplace ce coût sans le supprimer.
- Snow et al. (2008) montrent, sur cinq tâches de langue, que des étiquettes non expertes agrégées atteignent l'accord d'un expert — environ quatre par item pour l'affect — pour une fraction du prix. **Cela ne se transpose pas sur site** : le crowdsourcing public suppose de sortir les données, et les tâches industrielles demandent un œil expert.

### Données sensibles et annotation sur site

- Un outil **auto-hébergé** garde les données chez le client : Label Studio en Community (Apache-2.0, SQLite ou PostgreSQL) et CVAT en Community (MIT, `docker compose`), sans dépendance à un service extérieur pour l'application.
- **Les comptes et les rôles sont la limite.** Les rôles, le SSO et les journaux d'audit sont payants dans les deux outils ; en libre, les comptes sont locaux. CVAT documente SSO par Keycloak, en Enterprise seulement ; aucune page officielle lue ne décrit Keycloak ou Authentik pour Label Studio.
- Les **modèles de pré-annotation** doivent tourner sur place aussi : les exemples des deux outils s'exécutent en local (CPU ou GPU), mais leur licence est propre à chaque modèle.

## En pratique

- Commencer par un **lot pilote** annoté par au moins deux personnes, calculer l'accord par classe, corriger le guide là où il est faible, puis lancer le lot complet.
- Choisir l'outil par le type de donnée : images et vidéo à forme précise → [[CVAT]] ; texte, audio, séries ou un mélange → [[Label Studio]].
- Garder **un sous-échantillon sans pré-annotation** et le jeu d'évaluation hors de toute suggestion de modèle.
- Conserver les étiquettes **non agrégées**, le guide et sa version, l'identifiant de l'annotateur ; versionner l'ensemble ([[Versionnage de données]]).
- Relire les erreurs résiduelles avec un détecteur d'étiquettes suspectes avant d'entraîner, surtout sur le jeu de test.
- **Pièges** : mesurer l'accord brut au lieu d'un coefficient corrigé du hasard ; évaluer un modèle sur des étiquettes qu'il a pré-remplies ; confondre accord élevé et exactitude (deux annotateurs peuvent partager le même biais) ; construire le jeu de test par active learning.

## Approches voisines & alternatives

- [[Label Studio]] — plateforme multimodale, gabarit XML, backends ML ; rôles, SSO et active learning automatique réservés aux éditions payantes.
- [[CVAT]] — la vision en profondeur : suivi, squelettes, 3D, 27 formats ; SSO et contrôle qualité automatique en Enterprise.
- **Pas de fiche, cités pour situer le terrain** (relevé le 2026-09-30) :
  - **Doccano** — texte seulement, MIT, version 1.8.5 du 2026-01-11, environ 10 800 étoiles : activité faible mais pas éteinte.
  - **Argilla** — Apache-2.0, environ 5 100 étoiles, dernière version 2.8.0 de mars 2025 ; son README annonce que les auteurs d'origine sont passés à d'autres projets, que le code est stable et qu'aucune fonction nouvelle n'est prévue, seulement des correctifs : maintenance minimale, écarté.
  - **Prodigy** — outil d'Explosion, **commercial**, licence par poste, sans dépôt public : hors du critère open source, cité surtout pour le texte.
  - **Labelme** — application de bureau pour images, **GPL-3.0**, environ 16 200 étoiles, version 7.7.0 du 2026-09-18 : léger pour un poste isolé, sans serveur ni rôles.
- **Pourquoi aucun comparatif** : les deux briques retenues ne couvrent pas les mêmes données — le recouvrement (images, vidéo) est borné — et la comparaison tient dans leurs fiches et ici.
- [[Augmentation d'images]] — multiplier les exemples étiquetés sans annoter davantage.
- [[Validation croisée]] et [[Data leakage]] — ce qu'une annotation mal séparée fausse dans la mesure.

## Pour aller plus loin

- Cohen, J. (1960), *A Coefficient of Agreement for Nominal Scales*, Educational and Psychological Measurement 20(1) — https://doi.org/10.1177/001316446002000104
- Artstein, R. et Poesio, M. (2008), *Inter-Coder Agreement for Computational Linguistics*, Computational Linguistics 34(4) — https://aclanthology.org/J08-4004/
- Aroyo, L. et Welty, C. (2015), *Truth Is a Lie: Crowd Truth and the Seven Myths of Human Annotation*, AI Magazine 36(1) — https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2564
- Plank, B. (2022), *The "Problem" of Human Label Variation*, EMNLP 2022 — https://aclanthology.org/2022.emnlp-main.731/
- Fort, K. et Sagot, B. (2010), *Influence of Pre-annotation on POS-tagged Corpus Development*, Linguistic Annotation Workshop IV — https://aclanthology.org/W10-1807/
- Kirillov, A. et al. (2023), *Segment Anything* — https://arxiv.org/abs/2304.02643
- Schroeder, H., Roy, A. et Kabbara, J. (2025), *Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks*, Findings of ACL 2025 — https://aclanthology.org/2025.findings-acl.1323/
- Settles, B. (2009), *Active Learning Literature Survey*, rapport technique 1648, Université du Wisconsin-Madison — https://burrsettles.com/pub/settles.activelearning.pdf
- Ren, P. et al., *A Survey of Deep Active Learning*, ACM Computing Surveys 54(9), 2022 (arXiv 2009.00236, 2020-2021) — https://arxiv.org/abs/2009.00236
- Northcutt, C., Jiang, L. et Chuang, I. (2021), *Confident Learning: Estimating Uncertainty in Dataset Labels*, JAIR 70 — https://arxiv.org/abs/1911.00068
- Northcutt, C., Athalye, A. et Mueller, J. (2021), *Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks*, NeurIPS 2021, Datasets and Benchmarks — https://arxiv.org/abs/2103.14749
- Snow, R. et al. (2008), *Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks*, EMNLP 2008 — https://aclanthology.org/D08-1027/
- Gu, Y. et al. (2025), *Large Language Models Are Effective Human Annotation Assistants, But Not Good Independent Annotators*, arXiv 2503.06778 (prépublication ; venue non vérifiée) — https://arxiv.org/abs/2503.06778 ; sur le seul volet « l'IA comme assistante » : les experts reprennent les arguments extraits par l'IA 60 % du temps, pour 25 % de temps d'extraction en moins.
- Le sujet voisin de l'**active learning** n'a pas de page propre dans le brain : à créer si le besoin revient.
