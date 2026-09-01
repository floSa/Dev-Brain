---
role: brique
nom: Modal
alias: [modal, modal.com, Modal Labs, Modal Sandboxes]
pitch: "Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur."
categorie: compute/a-la-demande
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: "Python, JavaScript, Go"
scaling: serverless
alternatives: ["[[Dev/Services/E2B|E2B]]", "[[Dev/Services/Daytona|Daytona]]"]
complements: []
tags: [agents, gpu, llm, container]
url_docs: https://modal.com/docs
url_repo: 
---

# Modal

## Pourquoi

Plateforme de calcul **serverless orientée Python** : une fonction décorée devient une unité déployable, sans Dockerfile ni configuration d'infrastructure. Le positionnement d'origine est le calcul **GPU à la demande** pour l'IA — inférence, entraînement, traitement par lots — avec scale-to-zero et facturation **à la seconde**.

Les **Sandboxes** en sont la déclinaison pour les agents : des conteneurs isolés par **gVisor** (kernel en espace utilisateur interceptant les syscalls), créés à l'exécution pour faire tourner du code non fiable. Leur particularité par rapport aux bacs à sable concurrents est l'accès au **GPU à l'intérieur du bac à sable**. Le SDK Agents d'OpenAI l'a retenu comme bac à sable officiel.

Produit **propriétaire**, sans self-host.

## Quand l'utiliser

- Exécuter du code d'agent qui a besoin d'un **GPU** dans le bac à sable lui-même.
- Vouloir une seule plateforme pour le calcul GPU **et** l'isolation d'agent, plutôt que deux fournisseurs.
- Charges **intermittentes** : le scale-to-zero et la facturation à la seconde évitent de payer de l'inactif.

## Quand NE PAS l'utiliser

- Exigence de **self-host** ou de souveraineté sur l'infrastructure → [[Dev/Services/E2B|E2B]], auto-hébergeable.
- Besoin de l'isolation la plus stricte : gVisor réduit la surface mais reste en deçà d'une **microVM à kernel dédié** → [[Dev/Services/E2B|E2B]] (Firecracker).
- Charge **soutenue et prévisible** : le serverless facturé à la seconde devient plus cher qu'une capacité réservée.

## Déploiement & coût

- **Managé uniquement**, pas de version auto-hébergeable ni de dépôt public du cœur.
- Facturation **à la seconde** sur CPU, mémoire et GPU consommés ; scale-to-zero entre deux exécutions.
- GPU disponibles du T4 au B200 ; démarrage à froid annoncé sous la seconde.

## Pièges

- **Dépendance au fournisseur** : le modèle de programmation (décorateurs, images, volumes Modal) n'est pas portable ailleurs sans réécriture.
- Le serverless **coûte cher à l'échelle** : au-delà d'un certain taux d'occupation, une capacité réservée revient moins cher — surveiller le point de bascule.
- gVisor n'est pas une microVM : pour du code franchement hostile en multi-tenant, mesurer si le niveau d'isolation suffit. Cf. [[Sandboxing de code généré]].
- Timeout par défaut court (5 minutes) sur les Sandboxes — à relever explicitement pour les tâches d'agent longues.

## Alternatives

- [[Dev/Services/E2B|E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.
- [[Dev/Services/Daytona|Daytona]] — Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; **passé closed-source en juin 2026**, le dépôt public restant figé à la v0.190.0 et non maintenu.

## Liens

- Implémente le concept [[Sandboxing de code généré]] — isolation par gVisor.
- Backend d'exécution proposé par [[Dev/Services/Hermes Agent|Hermes Agent]], aux côtés de Docker, SSH, Singularity et Daytona.
- Sur l'axe calcul, voisin de [[Dev/Services/Ray|Ray]] (distribué, open-source, self-host) — approche opposée : managé et serverless plutôt que cluster à opérer.
- Doc : https://modal.com/docs
