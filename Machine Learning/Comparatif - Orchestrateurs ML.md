---
role: comparatif
nom: Comparatif - Orchestrateurs ML
categorie: ml/orchestration
tags: [orchestration, ml-pipeline, reproducibility]
---

# Comparatif - Orchestrateurs ML

> On tranche sur : l'infrastructure qu'on accepte d'opérer — un cluster Kubernetes, un compte AWS, ou aucune des deux.

![[Comparatif - Orchestrateurs ML.base]]

## Ce qui départage

- [[Flyte]] — Kubernetes-natif et backend Go : tâches **fortement typées**, une par pod, avec cache d'exécution et data lineage. C'est le seul qui exige une vraie compétence cluster, et le seul en bascule de SDK (Flyte 2).
- [[Metaflow]] — le flow Python passe du portable au cloud sans changer une ligne, avec versionnage et `resume` intégrés ; l'expérience aboutie est celle d'**AWS**, et il n'a pas d'ordonnanceur temporel à lui.
- [[ZenML]] — n'exécute rien lui-même : il découple le pipeline de l'infra et **orchestre les outils déjà en place** derrière une abstraction unique. Le backend réel reste à opérer, et son serveur de métadonnées est un composant de plus à héberger.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
