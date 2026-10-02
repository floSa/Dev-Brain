---
role: pattern
contexte: Contrôle qualité automatique d'une pièce ou d'une surface en cadence de production, avec un modèle qui n'a appris que le « bon » et tourne sur du matériel d'atelier sans GPU — de la caméra à la décision de rejet, avec un retour pour que le modèle reste juste.
services_cles: [OpenCV, anomalib, patchcore-inspection, Dinomaly, OpenVINO, ONNX Runtime, LiteRT]
projets_appliques: []
tags: [pattern, industrial-inspection, anomaly-detection, computer-vision, edge-inference]
---

# Pattern — Inspection visuelle en ligne de production

## Contexte

Une ligne produit des pièces ; un poste de contrôle les photographie ; une décision (bon, suspect) doit tomber avant que la pièce passe au poste suivant. Les défauts sont rares, variés, et ceux de demain ne sont pas connus d'avance : un classifieur supervisé n'a pas de quoi apprendre ([[Détection d'anomalies visuelle]]).

Le montage tient en cinq étages, de la caméra à la boucle de retour :

```
caméra → prétraitement → modèle d'anomalie (en bord) → décision → retour
```

À appliquer quand la pièce est présentée de façon répétable (cadrage, éclairage), qu'on dispose d'images de bon vérifiées, et que la décision se prend sur place, sans aller-retour vers un serveur central. Quand les défauts sont nombreux, étiquetés et stables, un détecteur supervisé reste le bon outil (cf. [[Détection d'objets]], [[Ultralytics YOLO]]).

## Stack

| Étage | Brique | Rôle |
|---|---|---|
| Prétraitement | [[OpenCV]] | recadrage, redressement, normalisation de l'éclairage, sélection de la zone utile |
| Entraînement et comparaison | [[anomalib]] | essayer plusieurs familles de méthodes sur ses propres images, avec un seul protocole |
| Méthode d'origine | [[patchcore-inspection]], [[Dinomaly]], [[AnomalyCLIP]] | reproduire les chiffres d'un papier, ou prendre une méthode hors de la liste d'anomalib |
| Exécution en bord | [[OpenVINO]] | export depuis anomalib (`ExportType.OPENVINO`, FP16 ou INT8) pour un PC industriel Intel sans GPU |
| Exécution en bord | [[ONNX Runtime]], [[LiteRT]] | autre matériel de l'atelier (ARM, matériel mixte) |
| Décision et retour | un fichier ou une file d'images suspectes, relu par un opérateur | alimenter le jeu de « bon » et celui de réglage du seuil |

Les méthodes se comprennent par famille : [[Anomalie visuelle par banque de mémoire]], [[Anomalie visuelle par reconstruction, distillation et flux]], [[Anomalie visuelle zero-shot et few-shot]]. Le choix du moteur d'exécution est dans [[Comparatif - Runtimes d'inférence CPU et edge]], les quatre bibliothèques de méthodes dans [[Comparatif - Détection d'anomalies visuelles]].

## Décisions clés

### 1. Constituer le bon avant de choisir la méthode

- Le détecteur ne vaut que ce que vaut son « normal » : même éclairage, même cadrage, aucun défaut caché ([[Rule - Entraîner sur du normal vérifié]]).
- Un défaut présent dans la banque ou dans l'entraînement devient du normal : la méthode le reconstruit, l'imite, ou ne l'écarte pas ([[Types d'anomalies et régimes de supervision]], rubrique contamination).
- Un bac, un gabarit ou un détourage évitent de confondre un décalage de pièce avec un défaut.

### 2. Choisir la famille de méthode par la contrainte, pas par le classement public

- Un point de départ raisonnable : banque de mémoire (PatchCore), sans réseau à entraîner, mais avec une mémoire à charger à l'inférence.
- Latence très basse : distillation légère (EfficientAD, dans anomalib). Un modèle pour toutes les références : méthodes multi-classes (UniAD, Dinomaly). Chaque famille a son coût ; la page de méthode le détaille.
- Avant d'avoir des images de bon : zero-shot ou few-shot pour juger si un défaut est visible, jamais pour livrer sans mesure sur les défauts réels de la ligne.
- MVTec AD est saturé : aucun classement sur ce jeu ne prédit le comportement sur une ligne ([[Détection d'anomalies visuelle]]).

### 3. Exporter, quantifier, puis revalider sur la cible

- anomalib exporte vers OpenVINO, ONNX et Torch ; la compression (FP16, INT8) ne vaut que pour OpenVINO.
- Rejouer le même jeu de test avant et après quantification, **sur le matériel de l'atelier** : sur ARM, OpenVINO exécute l'INT8 en simulation flottante, le gain n'y est pas acquis ([[Inférence en bordure - modèles sur du matériel d'atelier]], [[Quantization]]).
- Mesurer la latence sur la résolution réelle des images d'atelier et le matériel visé : les chiffres publiés (GPU, lot de 1) ne se transposent pas.

### 4. La carte pixel sert la décision, pas le seul score

- Le modèle rend un score d'image et une carte d'anomalie. La carte montre l'endroit : c'est elle que l'opérateur regarde pour confirmer ou infirmer un rejet.
- Définir en amont ce qu'est un défaut bloquant (taille minimale, zone critique) : une carte donne une intensité, pas une tolérance.

### 5. Poser le seuil sur du normal vérifié, et le réexaminer

- Le seuil se règle sur des images de bon qui ne servent pas à l'évaluation ([[Score et seuil d'alerte]], [[Évaluer une détection d'anomalies]]). Une image rejetée à tort coûte une inspection ; une image laissée passer coûte plus : c'est un choix de coût.
- Un changement d'éclairage, d'objectif ou de lot de matière décale la distribution des scores : le seuil se réétalonne alors, il ne se corrige pas à la marge ([[Détection hors distribution (OOD)]], [[Data drift]]).

### 6. Fermer la boucle

- Journaliser, pour chaque pièce, l'image, le score et la décision. Sans cela, impossible de réétalonner ni d'auditer un rejet contesté.
- Les pièces suspectes relues par un opérateur deviennent soit des défauts étiquetés (jeu de réglage, plus tard peut-être un détecteur supervisé), soit des images de bon ajoutées au jeu après vérification.
- Superviser le modèle comme un service : une dérive silencieuse ne se voit pas à l'exploitation immédiate ([[Monitoring de modèle en production]]).

## Pièges

- **Valider sur MVTec AD** : un score proche de 100 % ne dit rien de l'éclairage ni de la variabilité d'une ligne.
- **Entraîner un modèle livré sur un jeu public non commercial** : le chargeur de MVTec AD d'anomalib porte la mention CC BY-NC-SA 4.0. Le jeu sert à comparer des méthodes ([[Jeux de données d'anomalies]]).
- **Poids pré-entraînés de licence non lue** : anomalib télécharge des backbones au premier usage, et la fiche note que leur provenance et leur licence n'ont pas été relevées. À lire avant une livraison chez un client.
- **Défauts logiques oubliés** : un objet requis absent ou un agencement invalide n'est pas un défaut d'aspect ; la plupart des méthodes visent l'aspect.
- **Quantifier sans remesurer** : la précision peut se dégrader sur de petits réseaux.
- **Version non épinglée** : anomalib contraint `torch` pour des CVE et exclut deux versions de Lightning ; épingler les versions, y compris côté atelier.
- **Mesurer à l'image** : une carte pixel peut être dominée par les grandes régions ; lire aussi l'AU-PRO ([[Évaluer une détection d'anomalies]]).
- **Télémétrie des outils** : celle d'OpenVINO est activée par défaut pour la conversion et NNCF ; à couper avant un déploiement hors ligne.

## Voir aussi

- [[Détection d'anomalies visuelle]] — le problème, ses entrées et sorties, la saturation de MVTec AD
- [[Vision par ordinateur]] — le domaine, et [[Transfer learning vision]] pour les backbones
- [[Inférence en bordure - modèles sur du matériel d'atelier]] — contraintes de matériel, mise à jour d'un parc, air-gap
- [[Comparatif - Détection d'anomalies visuelles]] — départager anomalib et les dépôts des méthodes
- [[Pattern - Pipeline de maintenance prédictive on-prem]] — la même démarche côté capteurs
- [[Rule - Entraîner sur du normal vérifié]], [[Rule - Évaluer une anomalie par événement, pas par point]]
