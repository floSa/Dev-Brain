---
role: notion
nom: Plateforme data & IA — concept
alias: [plateforme ML, plateforme data science, build vs buy, enfermement fournisseur, vendor lock-in]
categorie: ml/plateforme
domaines: [data-sci, data-eng, mlops, ml-eng]
tags: [ml-platform, data-governance, automl, low-code, ml-pipeline]
---

# Plateforme data & IA — concept

## Aperçu

- Une plateforme data et IA vend l'**intégration**, pas une fonction : elle réunit sous une console et un modèle de droits uniques ce qu'on assemblerait autrement à partir de cinq ou six briques indépendantes.
- Ce qu'on achète en réalité n'est pas du calcul — il se loue partout — mais la **cohérence** : un catalogue commun, un lignage continu de la source au modèle servi, et une seule liste de qui a le droit de quoi.
- Le choix se ramène donc à un arbitrage classique : **assembler ou acheter**. Assembler garde la maîtrise et coûte une équipe plateforme ; acheter supprime cette équipe et transfère le pouvoir de négociation au fournisseur.

## Concepts clés

### Les quatre étages, et pourquoi ils font un tout

- **Préparation** — connecter les sources, nettoyer, joindre, produire des tables exploitables. C'est l'étage le plus consommateur de temps, et celui qui décide de la qualité de tout le reste.
- **Entraînement** — cadrer, entraîner, comparer, choisir. Cf. [[Validation croisée]] et [[Data leakage]] : une plateforme accélère les essais, elle ne protège pas d'un protocole faux.
- **Déploiement** — exposer le modèle, gérer les versions et les bascules. Cf. [[Déploiement de modèles]] et [[Model registry & versioning]].
- **Gouvernance** — catalogue, lignage, droits par rôle, journal d'audit. C'est l'étage qu'on sous-estime en phase d'évaluation et qui décide de l'achat en phase finale, parce que c'est le seul qu'une équipe ne rebâtit pas en quelques semaines.

Une brique qui ne couvre qu'un étage n'est pas une plateforme : c'est un outil. La frontière est écrite dans la taxonomie sous la règle D-R9.

### Le socle de calcul : apporté, ou emprunté

- Certaines plateformes **apportent** leur moteur — c'est le cas d'un lakehouse bâti sur [[Spark]], ou d'un entrepôt à entrepôts virtuels.
- D'autres **empruntent** celui qui est déjà là : un Kubernetes, une base SQL, un cluster existant. Elles pèsent alors moins lourd à l'installation, mais elles supposent que quelqu'un opère ce socle.
- Conséquence pratique : la question « combien coûte la plateforme » n'a pas de sens seule. Il faut lui ajouter le coût du socle, et pour une plateforme empruntée, le coût de l'équipe qui le tient.

### Sans code, avec code, ou les deux

- La couche visuelle achète l'**autonomie de gens qui n'écriront jamais de Python**. C'est un gain réel et souvent le motif d'achat.
- Elle coûte ce qu'un flux visuel coûte toujours : il se relit mal, se teste mal, se compare mal d'une version à l'autre, et ne sort pas de l'outil qui l'a produit.
- Les plateformes qui servent les deux publics sur les **mêmes objets** — un notebook au milieu d'un flux visuel, sur le même graphe de dépendances — évitent la fracture entre deux équipes qui ne partagent plus rien.

### L'enfermement se mesure à la sortie

Le bon test n'est pas « qu'est-ce que j'y gagne » mais **« qu'est-ce que je réécris si je pars »** :

- Le **format de stockage** est-il ouvert et lisible par un autre moteur, ou propriétaire ? Cf. [[Apache Iceberg]] et les formats de table.
- La **logique métier** est-elle du code standard qu'on peut exécuter ailleurs, ou des recettes visuelles et des fonctions SQL maison ?
- Le **catalogue de droits** est-il exportable, ou faudra-t-il le reconstruire à la main chez le suivant ?
- L'**orchestration** est-elle décrite dans un format portable, ou dans l'ordonnanceur de la plateforme ?

Une plateforme qui répond « ouvert » aux quatre se quitte. Une qui répond « maison » aux quatre ne se quitte pas : le devis de sortie dépasse celui de l'entrée.

### Sur site : trois sens différents d'un même mot

C'est la distinction qui décide des projets industriels, et elle est plus fine que « cloud ou pas » :

- **Le logiciel s'installe sur des serveurs qu'on possède** — plan de contrôle compris. C'est le seul cas où le fournisseur n'a aucun accès.
- **Le fournisseur pose son matériel dans la salle machine.** Les données restent physiquement là, mais l'exploitation et le contrat restent chez lui.
- **Le calcul descend, le pilotage reste en ligne.** Une extension déployée sur un cluster existant exécute les traitements sur le matériel du client ; la console, elle, est chez le fournisseur, et une connexion sortante est nécessaire.

Les trois s'annoncent « on-premise » en avant-vente. Il faut demander lequel des trois, par écrit.

## En pratique

- **Établir la liste courte par la contrainte d'hébergement d'abord**, jamais par les fonctionnalités : c'est la seule contrainte qui ne se contourne pas en cours de projet.
- **Faire évaluer la gouvernance par ceux qui l'exploiteront**, pas par les data scientists : c'est l'étage qui décide en fin d'évaluation et celui que les essais techniques ignorent.
- **Exiger un chemin de sortie écrit** — export des données dans un format ouvert, export des définitions de modèles, export des droits — avant de signer, pas après.
- **Se méfier du démonstrateur** : toutes ces suites démontrent bien. Ce qui les sépare apparaît au dixième projet, quand la gouvernance et le coût de calcul deviennent le sujet.
- **Comparer avec l'option « assembler »**, ne serait-ce que pour chiffrer ce qu'on achète : [[ZenML]], [[Metaflow]] ou [[Flyte]] côté pipeline, [[MLflow]] côté suivi, [[KServe]] ou [[BentoML]] côté service. Le total est rarement moins cher en licences, souvent moins cher en liberté.

## Approches voisines & alternatives

- [[Dataiku]] — la suite installable sur site qui sert les deux publics, visuel et code, sur les mêmes objets.
- [[Databricks]] — l'approche lakehouse : un seul jeu de fichiers pour le SQL, les pipelines et le ML, en code et sans installation sur site.
- [[DataRobot]] — la plateforme dont le cœur est l'automatisation de la modélisation, installable sur Kubernetes.
- [[Alteryx]] — l'extrémité sans code du spectre, centrée sur la préparation par des analystes métier.
- [[Snowflake]] — l'entrepôt SQL devenu plateforme, où l'IA vient à la donnée plutôt que l'inverse.
- [[AWS SageMaker]] · [[Google Cloud Vertex AI]] · [[Microsoft Azure Machine Learning]] — les écosystèmes natifs des trois clouds, qui ne se comparent qu'à profondeur d'engagement égale chez leur fournisseur.
- [[ZenML]] · [[Metaflow]] · [[Flyte]] — l'alternative « assembler » : un pipeline portable, sans le catalogue ni les droits.
- [[Feature store — concept]] — un étage qu'une plateforme intègre et qu'on outille autrement quand on assemble.
- [[Monitoring de modèle en production]] — ce que la moitié MLOps de ces suites automatise.

## Pour aller plus loin

- [[Comparatif - Plateformes data & IA]] — les huit suites du dossier, et le critère qui les départage vraiment.
- [[Plateformes data & IA]] — le hub du dossier.
- [[Architecture médaillon]] — le découpage en couches que ces plateformes présupposent souvent.
