---
role: hub
nom: MLOps
pitch: Mettre un modèle en production et savoir, ensuite, s'il marche encore.
---

# MLOps

> Mettre un modèle en production et savoir, ensuite, s'il marche encore.

## Ce qu'il faut comprendre

- Un modèle en production est un **service qui se périme**. Cet axe traite de ce que l'entraînement ne traite pas : versionner, servir, mesurer la dérive, revenir en arrière.
- Il n'a pas de branche à lui dans l'arbre, et c'est normal — il se lit dans [[Serving]] et [[Suivi d'expériences]] côté [[Machine Learning]], dans [[Observabilité]] pour ce qu'on regarde ensuite, dans [[DevOps]] et [[Web & API]] pour ce qui l'emballe et l'expose.
- La frontière avec [[Data Engineering]] est le contenu du flux ; celle avec [[ML Engineering]] est le moment. Un incident MLOps se manifeste presque toujours en amont, dans l'un des deux.

## Choisir

- Exposer un modèle derrière une API → [[Serving]], puis [[Web & API]].
- Retrouver quel modèle a produit quel résultat → [[Suivi d'expériences]].
- Surveiller ce qui tourne, mesurer une dérive → [[Observabilité]].
- Emballer et déployer → [[DevOps]].

<!-- AUTO:START -->
Axe métier **MLOps** (`mlops`) — explorer par sous-domaine, puis descendre via le graphe local.

- [[Machine learning (notions)]] — 5 notion(s)
- [[Données (notions)]] — 2 notion(s)
- [[Deep learning]] — 2 notion(s)
- [[LLM (notions)]] — 2 notion(s)
- [[Séries temporelles]] — 2 notion(s)
<!-- AUTO:END -->
