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
alternatives: ["[[E2B]]", "[[Daytona]]"]
complements: []
tags: [agents, gpu, llm, container]
url_docs: https://modal.com/docs
url_repo: 
---

# Modal

<!-- AUTO:BANDEAU:START -->
> Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de calcul **serverless orientée Python** : une fonction décorée devient une
unité déployable, sans Dockerfile ni configuration d'infrastructure. Le positionnement
d'origine est le GPU à la demande pour l'IA — inférence, entraînement, traitement par lots
— avec scale-to-zero et facturation à la seconde. Les **Sandboxes** en sont la déclinaison
pour les agents : des conteneurs isolés par **gVisor**, un kernel en espace utilisateur qui
intercepte les syscalls, créés à l'exécution pour faire tourner du code non fiable. Leur
particularité face aux bacs à sable concurrents est l'accès au **GPU à l'intérieur du bac à
sable**. Aucun self-host : ni version auto-hébergeable, ni dépôt public du cœur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exécuter du code d'agent qui a besoin d'un **GPU dans le bac à sable** lui-même | **Dépendance au fournisseur** : décorateurs, images et volumes Modal ne se portent pas ailleurs sans réécriture |
| Vouloir une seule plateforme pour le calcul GPU **et** l'isolation d'agent, plutôt que deux fournisseurs | Le serverless coûte cher à l'échelle : au-delà d'un certain taux d'occupation, une capacité réservée revient moins cher — surveiller le point de bascule |
| Charges intermittentes : scale-to-zero et facturation à la seconde évitent de payer de l'inactif | gVisor n'est pas une microVM : pour du code franchement hostile en multi-tenant, mesurer si le niveau d'isolation suffit |
| | Timeout par défaut court (5 minutes) sur les Sandboxes : à relever explicitement pour les tâches d'agent longues |
| | Exigence de self-host ou de souveraineté sur l'infrastructure → [[E2B]], auto-hébergeable |
| | Besoin de l'isolation la plus stricte, à kernel dédié → [[E2B]] et sa microVM Firecracker |

## Mise en œuvre

- Installation — `uv add modal`, puis authentification auprès du service
- Point d'entrée — décorateurs Python sur des fonctions ; Sandboxes créées à l'exécution pour le code non fiable
- Prérequis — un compte Modal ; **aucun self-host**, ni dépôt public du cœur
- Exécution — managé, serverless ; GPU du T4 au B200, démarrage à froid annoncé sous la seconde
- Coût — **propriétaire**, facturé à la seconde sur CPU, mémoire et GPU consommés ; scale-to-zero entre deux exécutions

## Écosystème

### Alternatives

- [[E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.
- [[Daytona]] — Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; **passé closed-source en juin 2026**, le dépôt public restant figé à la v0.190.0 et non maintenu.

## Ressources

- Documentation — https://modal.com/docs

## Voir aussi

- [[Sandboxing de code généré]] — la notion qu'il implémente, ici par gVisor
- [[Calcul distribué]] — le hub du domaine
- [[Hermes Agent]] — le propose comme backend d'exécution, aux côtés de Docker, SSH, Singularity et Daytona
- [[Ray]] — voisin sur l'axe calcul, mais approche opposée : cluster open-source à opérer plutôt que managé et serverless
