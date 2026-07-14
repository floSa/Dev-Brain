---
galaxie: wiki
type: concept
nom: Déploiement de modèles
alias: [model deployment, déploiement de modèle, canary, blue-green, shadow deployment, progressive delivery, déploiement progressif, rollout]
categorie: concept/ml
domaines: [mlops]
tags: [deployment-strategy, model-serving, inference]
---

# Déploiement de modèles

## Aperçu

- Mettre une nouvelle version de modèle en production **sans casser le service** : la basculer progressivement et de façon réversible, jamais en *big bang*.
- Le risque est double : un bug logiciel (côté serving) **et** une régression de qualité prédictive (le modèle fonctionne techniquement mais prédit moins bien). Les stratégies de déploiement traitent surtout le second.

## Concepts clés

### Blue-green
- Deux environnements complets : *blue* (actuel) et *green* (nouveau). Bascule de 100 % du trafic d'un coup ; rollback = re-bascule instantanée.
- Simple et réversible, mais coûteux (double infra) et sans validation progressive.

### Canary
- Router une **petite fraction** du trafic (1 %, 5 %, 25 %…) vers la nouvelle version, observer les métriques, puis monter en charge ou rollback.
- Limite le rayon d'impact ; suppose un monitoring fiable et une analyse statistique de la cohorte canary.

### Shadow (mirroring)
- La nouvelle version reçoit une **copie** du trafic réel, mais ses réponses ne sont **pas servies** à l'utilisateur. On compare prédictions et latence à l'ombre du modèle en place.
- Zéro risque utilisateur, idéal pour valider sur du vrai trafic ; ne teste pas la boucle de feedback réelle (les prédictions n'agissent pas).

### A/B test / champion-challenger
- Plusieurs versions servies en parallèle à des cohortes, comparées sur une **métrique métier** (conversion, revenu), pas seulement technique. Le challenger qui gagne devient champion.

### Rollback & feature flags
- Tout déploiement doit être **réversible en un geste**. Un *feature flag* découple le déploiement du code de l'activation du modèle (release ≠ deploy).

## Les maths, simplement

- Décider si une cohorte canary est saine relève d'un test statistique : comparer le taux d'erreur / la métrique métier canary vs baseline, avec un seuil de significativité — cf. [[A-B testing]].
- Garde-fou de rollout : *error budget* — fraction d'erreurs tolérée avant bascule automatique en rollback.

## En pratique

- Promouvoir depuis le [[Model registry & versioning|registre]] la version validée, puis la déployer derrière un serveur d'inférence ([[Dev/Services/BentoML|BentoML]], [[Dev/Services/KServe|KServe]]).
- Brancher le [[Monitoring de modèle en production|monitoring]] **avant** d'ouvrir le trafic : un canary sans métriques observées est un déploiement aveugle.
- Choisir selon le risque : shadow pour valider sans risque, canary pour ouvrir progressivement, blue-green pour une bascule simple et réversible.
- Pièges : labels retardés (la vraie qualité n'est pas mesurable tout de suite → s'appuyer sur des proxies), trafic canary non représentatif, rollback jamais testé.

## Approches voisines & alternatives

- [[Monitoring de modèle en production]] — fournit les signaux qui valident ou invalident un canary / shadow.
- [[Model registry & versioning]] — source des versions promues ; le déploiement consomme ce qui y est validé.
- [[A-B testing]] — cadre statistique de comparaison des cohortes (canary, champion-challenger).
- [[Data drift]] — raison fréquente de redéployer (ré-entraînement déclenché par la dérive).
- [[Dev/Services/MLflow|MLflow]] — format de modèle + déploiement multi-cibles depuis le registre.

## Pour aller plus loin

- Progressive delivery appliquée au serving (Flagger, Argo Rollouts, Seldon).
- Sato, Wider, Windheuser (martinfowler.com) — *Continuous Delivery for Machine Learning (CD4ML)*.
