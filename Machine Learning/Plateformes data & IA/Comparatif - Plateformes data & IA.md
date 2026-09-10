---
role: comparatif
nom: Comparatif - Plateformes data & IA
categorie: ml/plateforme
tags: [ml-platform, data-governance, automl, low-code]
---

# Comparatif - Plateformes data & IA

> On tranche sur : **où tournent les données**, et **ce qu'on réécrit le jour où l'on part**.
> Dans cet ordre, et pas dans l'autre. La contrainte d'hébergement élimine avant qu'on ait
> parlé de fonctionnalités — trois de ces huit s'installent sur des serveurs qu'on possède,
> les cinq autres exigent un compte chez un fournisseur. Le coût de sortie, lui, ne se voit
> qu'au dixième projet : il se lit dans le format de stockage, dans la portabilité de la
> logique métier, et dans le catalogue de droits qu'il faudra rebâtir ailleurs.

![[Comparatif - Plateformes data & IA.base]]

## Ce qui départage

- [[Dataiku]] — la seule à s'installer **en entier** sur des serveurs du client tout en servant les deux publics sur les mêmes objets : recette visuelle et notebook Python sur le même graphe. Ce qu'elle enferme est la recette visuelle, qui ne se rejoue nulle part ailleurs ; elle se facture par utilisateur, donc le coût suit la taille de l'équipe et non l'usage.
- [[DataRobot]] — même liberté d'hébergement, par Helm sur un Kubernetes du client, mais un périmètre **plus étroit et plus automatisé** : elle produit et classe des modèles, elle ne prépare pas les données de bout en bout. Ce qu'elle coûte n'est pas un format propriétaire mais la compréhension : l'automatisation cache ce qui a été appris.
- [[Alteryx]] — l'extrémité **sans code** du spectre, et le seul dont la conception est liée à un poste Windows. Il rend des analystes métier autonomes et s'arrête avant la modélisation industrialisée. Le prix de sortie est le plus élevé du lot en proportion : un flux visuel ne s'exporte pas, il se réécrit.
- [[Databricks]] — la plus technique, et **sans aucun déploiement sur site** : elle tourne dans le compte cloud du client, ce qui n'est pas de l'auto-hébergement. Elle est la moins enfermante des cinq managées sur le stockage — format de table ouvert, moteur Spark connu — et la plus exigeante en compétences comme en pilotage du coût de calcul.
- [[Snowflake]] — le concurrent frontal du précédent, avec le point de départ inverse : l'entrepôt SQL, où l'IA vient à la donnée. Exploitation nulle, mais l'enfermement est le plus profond du lot quand on écrit du Cortex en SQL ou des procédures Snowpark, qui ne s'exécutent qu'ici. Aucune installation sur site n'existe ni n'est annoncée.
- [[Microsoft Azure Machine Learning]] — **le seul des trois clouds à faire tourner entraînement et inférence sur le matériel du client**, par une extension Azure Arc posée sur un Kubernetes déjà en place. Le plan de contrôle reste chez Microsoft et une connexion sortante est nécessaire : c'est un compromis, pas une souveraineté. C'est aussi le plus déclaratif des trois, pilotable en YAML versionné.
- [[AWS SageMaker]] — la surface la plus large et la plus morcelée, réunie depuis 2025 sous une console commune avec les services data d'AWS. Sa descente sur site passe par des **baies AWS louées** et exploitées par AWS dans la salle machine : les données restent, le contrat et l'exploitation partent.
- [[Google Cloud Vertex AI]] — l'accès direct aux modèles Gemini sous contrat d'entreprise est son argument propre. Sur site, il ne descend qu'**une partie** — un jeu restreint d'API pré-entraînées sur une appliance air-gapped. Point de vigilance qui n'est pas technique : le produit est en cours de rebaptême en Gemini Enterprise Agent Platform, et sa documentation bouge.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Plateforme data & IA — concept]] — les quatre étages, et le test de sortie en quatre questions.
- [[Comparatif - Orchestrateurs ML]] — l'autre branche du choix : assembler un pipeline au lieu d'acheter une suite.
