---
role: notion
nom: Inférence en bordure - modèles sur du matériel d'atelier
alias: ["Inférence en bordure : modèles sur du matériel d'atelier", inférence en bordure, inférence edge, edge inference, edge AI, inférence sur site, IA en bordure]
categorie: ml/serving
domaines: [mlops, infra-ops]
tags: [edge-inference, inference, iiot, model-serving]
---

# Inférence en bordure - modèles sur du matériel d'atelier

## Aperçu

- **Inférer en bordure**, c'est exécuter un modèle déjà entraîné sur la machine ou le PC industriel qui produit la donnée, plutôt que de l'envoyer à un serveur central. L'entraînement reste ailleurs ; seule la prédiction descend dans l'atelier.
- Le sujet n'est pas le modèle mais ce qui l'entoure : un matériel modeste, un réseau qui peut tomber, un **parc** de machines à mettre à jour sans se déplacer, et un réseau d'atelier qu'il faut protéger. Les briques sont dans [[Serving]] ; les stratégies de mise en production générales sont dans [[Déploiement de modèles]], et ce que le modèle prédit dans [[Maintenance prédictive et RUL]].

## Concepts clés

### Pourquoi inférer sur place plutôt qu'au centre
- **Latence et bande passante.** Zhou et al. (2019) relèvent que l'envoi vers le cloud par le réseau étendu peut coûter un délai de transmission et un débit « prohibitifs » ; l'inférence près de la source réduit les deux. Ils notent qu'il n'existe pas de meilleur niveau d'exécution en général : cloud seul, co-inférence entre cloud et bordure, ou sur l'appareil, le choix dépend de l'application, et plus on se rapproche de la source, plus la latence de calcul et l'énergie pèsent.
- **Réseau coupé.** Murshed et al. (2021) comptent la robustesse parmi les bénéfices : un service peut rester disponible pendant une panne de réseau ou une cyberattaque. Zhou et al. ne retiennent pas cet argument dans la version lue de leur article.
- **Données qui ne sortent pas.** Les deux synthèses citent la protection des données personnelles ou de l'exploitation : filtrer ou traiter sur place avant d'envoyer. Pour un industriel, c'est souvent la raison décisive avant toute question de performance.
- **Le coût de la proximité.** Murshed et al. déclarent que les modèles déployés en bordure sont moins précis, que l'entraînement y reste difficile et que les flux non stationnaires sont une question de recherche ouverte. L'inférence sur place est un compromis, pas une amélioration gratuite.

### Les contraintes matérielles
- **Un PC industriel n'a souvent ni GPU ni mémoire abondante.** Le premier critère de choix du runtime est le **processeur** de la cible : [[OpenVINO]] vise le matériel Intel (CPU, GPU intégré, NPU), [[LiteRT]] le CPU x86_64 et ARM64, [[ONNX Runtime]] tous les matériels par ses fournisseurs d'exécution, [[TensorRT]] seulement un GPU NVIDIA. Le tableau est dans [[Comparatif - Runtimes d'inférence CPU et edge]].
- **Une bibliothèque liée à l'application suffit souvent.** Un serveur de modèle (batching dynamique, API réseau) a un sens pour plusieurs clients et un GPU partagé ; sur une machine qui n'a qu'un appelant, le moteur d'exécution seul évite un processus de plus à superviser et à patcher.
- **Les accélérateurs sont un plus, pas un prérequis.** Un NPU ou un GPU intégré demande des pilotes à installer à part et, pour le NPU d'Intel, des formes de tenseurs statiques d'après la documentation d'OpenVINO. Prévoir le repli sur le CPU.
- **Un cas limite documenté** : Mennilli et al. (2025) embarquent un CNN quantifié sur un automate Finder Opta pour estimer une vitesse de rotation à partir d'un signal acoustique ; le modèle tient en 1 029 ko, « juste assez de mémoire » pour le reste du programme. C'est une preuve de concept sur banc d'essai, pas un retour d'atelier.

### Quantification et conversion
- Le principe et les formats sont dans [[Quantization]] ; [[Distillation]] et [[Pruning]] réduisent le modèle autrement. Ce qui est propre à la bordure tient en deux points.
- **La conversion est une étape qui échoue.** Chaque runtime a son format (`.onnx`, IR d'OpenVINO, `.tflite`) et ses opérateurs non couverts, qui retombent sur le CPU ou bloquent la conversion. Le choix du format de départ commande celui du runtime.
- **Revalider la précision sur la cible.** LiteRT écrit que la quantification après entraînement peut dégrader la précision, surtout sur de petits réseaux, et propose l'entraînement conscient de la quantification si la perte est trop forte ; ONNX Runtime écrit qu'elle « n'est pas sans perte ». Rejouer le même jeu de test avant et après, **sur le matériel de l'atelier** : sur ARM, OpenVINO exécute l'INT8 en simulation flottante, le gain attendu n'y est pas acquis.

### Mettre à jour et superviser un parc
- **Deux niveaux à mettre à jour** : le système de la machine (image d'OS, bootloader) et ce qui tourne dessus (conteneurs, modèle). Pour le premier, [[Ansible]] pousse une configuration par SSH sans agent ; pour les images de système avec partitions doubles, RAUC (LGPL-2.1, v1.15.2 du 2026-03-27), SWUpdate (GPL-2.0-only, 2026.05.1 du 2026-06-22) et le client Mender (Apache-2.0, 5.1.1 du 2026-09-28) lisent leurs mises à jour depuis un fichier local ou une clé USB. Mender réserve certaines fonctions à une édition payante ; balena suppose un registre joignable et son option auto-hébergée, openBalena (AGPL-3.0), est en bêta d'après son README : mauvais choix pour un atelier hors ligne.
- **Pour les conteneurs**, [[k3s]] prend en charge l'air-gap (images déposées dans un répertoire local) ; [[Docker Compose]] ou [[Podman]] suffisent sur une machine isolée.
- **Superviser deux choses distinctes.** La santé de la machine (processeur, mémoire, service vivant) se collecte avec [[Telegraf]] et [[Prometheus]] ; la santé du **modèle** relève de [[Monitoring de modèle en production]] et de [[Data drift]]. Sur un parc, la dérive n'est pas la même partout : Zenisek et al. (2019) détectent la dérive de capteurs sur des ventilateurs industriels pour la maintenance prédictive, et Zheng et Paiva (2021) mesurent des pertes de performance sensibles sous dérive de capteurs IoT ; aucune des deux ne traite un parc entier. Paleyes et al. (2022) relient la dérive à la fréquence de remplacement des modèles.

### Bascule et retour arrière
- **Une machine à la fois.** Le partage du trafic en pourcentage ([[Déploiement de modèles]]) n'a pas de sens sur une machine unique : le canary de l'atelier est **une ligne, puis une usine, puis le parc**, avec la mesure du modèle comme critère d'avancement.
- **Le retour arrière du système repose sur le bootloader.** RAUC et SWUpdate l'écrivent explicitement : la mise à jour est écrite sur la copie inactive, le bootloader compte les démarrages ratés et rebascule, et c'est l'application qui doit **confirmer** le bon fonctionnement (`status mark-good` pour RAUC, `ustate` pour SWUpdate). Mender décrit la même étape de confirmation, et ajoute qu'elle exige l'intégration au bootloader.
- **Le retour arrière du modèle est un fichier.** Garder la version précédente à côté de la nouvelle, avec le registre de la version validée ([[Model registry & versioning]]), et basculer en changeant un lien ou une variable plutôt qu'en réinstallant.
- **Kubernetes ne rétrograde pas.** La documentation de k3s indique que le plan de contrôle ne supporte pas le retour à une version antérieure : prévoir une sauvegarde du datastore avant la mise à niveau.

### Sécurité du matériel d'atelier
- **Un PC d'atelier est un point d'entrée dans le réseau industriel.** Les séries IEC 62443 découpent le système en **zones et conduits** et fixent un niveau de sécurité cible par zone (partie 3-2) ; la partie 3-3 liste les exigences du système sur sept exigences fondamentales (identification, contrôle d'usage, intégrité, confidentialité, flux restreint, réponse aux événements, disponibilité), la partie 4-2 celles des composants. Le contenu par niveau est payant : ne pas le recopier de seconde main.
- **NIST SP 800-82 Rév. 3** (2023) décrit une architecture IIoT en trois niveaux (bordure, plateforme, entreprise), demande d'analyser les flux de données qui quittent l'installation et recommande défense en profondeur et segmentation. Il ne traite pas l'inférence de modèles en tant que telle.
- **À en tirer pour un nœud d'inférence** : ne l'exposer qu'à la zone qui en a besoin ; exiger des mises à jour **signées** (RAUC, SWUpdate et Mender vérifient une signature) ; couper la télémétrie des outils quand l'atelier est isolé (celle d'OpenVINO est activée par défaut) ; et suivre la sécurité du réseau d'atelier décrite dans [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]].

## Les maths, simplement

- **Budget de latence.** $t_{total} = t_{capture} + t_{transfert} + t_{calcul} + t_{retour}$. Inférer sur place supprime $t_{transfert}$ et $t_{retour}$ vers le centre et alourdit $t_{calcul}$ ; le gain n'existe que si les deux premiers termes dominaient.
- **Mémoire du modèle.** Le poids d'un modèle vaut environ $N \times b$ octets pour $N$ paramètres stockés sur $b$ octets : 4 pour du flottant 32 bits, 1 pour de l'entier 8 bits. Un million de paramètres passe donc d'environ 4 Mo à 1 Mo, hors activations et hors runtime.

## En pratique

- Partir de la **cible** : processeur, mémoire, système, réseau (permanent, intermittent, absent), avant de choisir un modèle ou un runtime.
- Mesurer sur la machine réelle, avec le modèle réel : aucun benchmark neutre et daté des runtimes sur un même PC industriel n'a été trouvé, et ceux des éditeurs portent sur leur propre matériel.
- Prévoir dès le départ le **retour arrière** et la **confirmation** après mise à jour, avant la première livraison chez un client.
- Séparer la supervision de la machine de celle du modèle, et décider qui reçoit l'alerte quand un modèle dérive sur un site isolé.
- Pièges : un modèle quantifié validé sur un poste de développement x86 puis livré sur ARM ; une dépendance à un service du fabricant (télémétrie, registre) incompatible avec un atelier isolé ; une licence de runtime ou d'outil de conversion non lue avant de livrer le produit à un client.

## Approches voisines & alternatives

- [[Déploiement de modèles]] — les stratégies de bascule (blue-green, canary, shadow) ; la bordure en garde l'idée mais pas la mécanique de partage de trafic.
- [[Maintenance prédictive et RUL]] — le cas d'usage qui descend le plus souvent dans l'atelier.
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — d'où vient la donnée et comment sécuriser le réseau qui la porte ; [[Telegraf]] et [[open62541]] en sont les briques du côté collecte.
- [[Quantization]], [[Distillation]], [[Pruning]] — réduire le modèle avant de le descendre.
- [[Monitoring de modèle en production]], [[Data drift]] — surveiller ce qui a été déployé.
- [[OpenVINO]], [[LiteRT]], [[ONNX Runtime]], [[TensorRT]] — les moteurs d'exécution ; [[Comparatif - Runtimes d'inférence CPU et edge]] les départage.

## Pour aller plus loin

- Zhou, Chen, Li, Zeng, Luo, Zhang, « Edge Intelligence: Paving the Last Mile of Artificial Intelligence With Edge Computing », *Proceedings of the IEEE* 107(8), 2019 — https://arxiv.org/abs/1905.10083 (version 1 du préprint lue, non la version publiée).
- Murshed, Murphy, Hou, Khan, Ananthanarayanan, Hussain, « Machine Learning at the Network Edge: A Survey », *ACM Computing Surveys* 54(8), 2021 — https://arxiv.org/abs/1908.00080 (version 4 lue).
- Paleyes, Urma, Lawrence, « Challenges in Deploying Machine Learning: a Survey of Case Studies », *ACM Computing Surveys*, 2022 — https://arxiv.org/abs/2011.09926.
- Zenisek, Holzinger, Affenzeller, « Machine learning based concept drift detection for predictive maintenance », *Computers & Industrial Engineering* 137, 2019 — https://pure.fh-ooe.at/en/publications/machine-learning-based-concept-drift-detection-for-predictive-mai/ (résumé lu).
- Zheng, Paiva, « Assessing Machine Learning Approaches to Address IoT Sensor Drift », AIoT à KDD 2021 — https://arxiv.org/abs/2109.04356.
- Mennilli, Mazza, Mura, « Integrating Machine Learning for Predictive Maintenance on Resource-Constrained PLCs: A Feasibility Study », *Sensors* 25(2), 2025 — https://doi.org/10.3390/s25020537.
- NIST SP 800-82 Rév. 3, *Guide to Operational Technology (OT) Security*, 2023 — https://csrc.nist.gov/pubs/sp/800/82/r3/final.
- IEC 62443-3-3:2013, 4-2:2019 et 3-2:2020 — pages de l'éditeur https://webstore.iec.ch/en/publication/7033 (3-3), /34421 (4-2) et /30727 (3-2) ; seul un extrait gratuit d'ISA a été lu.
- Documentation de RAUC (https://rauc.readthedocs.io/), de SWUpdate (https://github.com/sbabic/swupdate), de Mender (https://docs.mender.io/) et de k3s en air-gap (https://docs.k3s.io/installation/airgap).
