---
role: brique
nom: Daytona
alias: [daytona, daytonaio, Daytona Sandboxes]
pitch: "Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; passé closed-source en juin 2026, le dépôt public restant figé à la v0.190.0 et non maintenu."
categorie: compute/a-la-demande
famille: saas
licence_type: source-available
hosted: [managed]
maturite: production
langage: "TypeScript, Go"
scaling: serverless
alternatives: ["[[E2B]]", "[[Modal]]"]
complements: []
tags: [agents, llm, container, ai-security]
url_docs: https://www.daytona.io/docs
url_repo: https://github.com/daytonaio/daytona
---

# Daytona

<!-- AUTO:BANDEAU:START -->
> Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; passé closed-source en juin 2026, le dépôt public restant figé à la v0.190.0 et non maintenu.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | source-available | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Infrastructure d'exécution pour **code généré par IA** : bacs à sable à **kernel dédié** —
système de fichiers, pile réseau et noyau propres —, démarrage annoncé sous 90 ms, et
surtout des **snapshots d'état** qui permettent à un agent de retrouver son espace de
travail d'une session à l'autre. S'y ajoutent accès SSH, terminal web et VNC, plus des
contrôles d'organisation et des journaux d'audit. Le produit a pivoté depuis un outil
d'environnements de développement. Le fait déterminant est ailleurs : en **juin 2026**,
Daytona a basculé le code de son produit en **closed source**, au motif que l'IA permet de
scanner un dépôt ouvert à la recherche de failles plus vite qu'aucune équipe humaine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Agents longue durée qui doivent retrouver leur espace de travail : les snapshots d'état sont le vrai différenciateur | Le fork open-source est un **piège de sécurité** : dépôt figé à la v0.190.0 depuis juin 2026, sans correctif, sur un composant dont tout le rôle est de contenir du code hostile |
| Besoin d'accès interactif au bac à sable — SSH, terminal web, VNC — pour inspecter ou déboguer | **Dépendance forte au fournisseur** : plus aucun moyen d'auditer ni de reprendre l'implémentation du bac à sable |
| Accepter un fournisseur entièrement managé et fermé, avec ce que cela implique | Les snapshots **persistent** ce que le bac à sable éphémère effacerait : la surface d'attaque survit d'une session à l'autre |
| | Changement de licence récent : la documentation tierce et les comparatifs antérieurs à mi-2026 le décrivent encore comme open-source |
| | Exigence d'auto-hébergement ou d'audit du code d'isolation → [[E2B]], Apache-2.0 et self-host documenté |
| | Besoin de GPU dans le bac à sable → [[Modal]] |

## Mise en œuvre

- Installation — SDK Python ou TypeScript ; les SDK et la documentation restent publiés, le cœur non
- Point d'entrée — SDK qui pilote le bac à sable, plus SSH, terminal web et VNC pour l'accès interactif
- Prérequis — un compte Daytona ; **managé uniquement** en pratique depuis le passage en closed source
- Exécution — managé, serverless, kernel dédié ; l'ancien dépôt v0.190.0 reste forkable et auto-hébergeable, mais sans support ni patchs — chemin déconseillé sur un composant d'isolation
- Coût — **source-available** et facturé à la consommation

## Écosystème

### Alternatives

- [[E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.
- [[Modal]] — Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.

## Ressources

- Documentation — https://www.daytona.io/docs
- Dépôt — https://github.com/daytonaio/daytona (figé à la v0.190.0, non maintenu)

## Voir aussi

- [[Sandboxing de code généré]] — la notion qu'il implémente, ici par kernel dédié et snapshots d'état
- [[Calcul distribué]] — le hub du domaine
- [[Hermes Agent]] — le propose comme backend d'exécution, aux côtés de Docker, SSH, Singularity et Modal
- [[AI security]] · [[Prompt injection]] — le contexte de sécurité
