---
galaxie: dev
type: service
nom: Daytona
alias: [daytona, daytonaio, Daytona Sandboxes]
pitch: "Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; passé closed-source en juin 2026, le dépôt public restant figé à la v0.190.0 et non maintenu."
categorie: compute/sandbox
famille: saas
licence_type: source-available
hosted: managed
maturite: production
langage: "TypeScript, Go"
scaling: serverless
alternatives: ["[[Dev/Services/E2B|E2B]]", "[[Dev/Services/Modal|Modal]]"]
remplace_par: []
status: actif
tags: [agents, llm, container, ai-security]
url_docs: https://www.daytona.io/docs
url_repo: https://github.com/daytonaio/daytona
---

# Daytona

## Pourquoi

Infrastructure d'exécution pour **code généré par IA** : bacs à sable à **kernel dédié** (système de fichiers, pile réseau et noyau propres), démarrage annoncé **sous 90 ms**, et surtout des **snapshots d'état** qui permettent à un agent de retrouver son espace de travail entre deux sessions. S'y ajoutent accès SSH, terminal web et VNC, plus des contrôles d'organisation et des journaux d'audit.

Le produit a pivoté : issu d'un outil d'environnements de développement, il s'est recentré sur les bacs à sable d'agents.

**Point déterminant** : en **juin 2026**, Daytona a basculé son code de production en **closed source**, au motif que l'IA permet de scanner un dépôt ouvert à la recherche de failles plus vite qu'aucune équipe humaine — risque jugé inacceptable pour un produit dont le métier est justement d'isoler du code hostile. Le dépôt public reste en ligne mais **figé à la v0.190.0**, sans correctif ni patch de sécurité. Seuls les SDK et la documentation restent publiés.

## Quand l'utiliser

- Agents **longue durée** qui doivent retrouver leur espace de travail : les snapshots d'état sont le vrai différenciateur.
- Besoin d'accès **interactif** au bac à sable (SSH, terminal web, VNC) pour l'inspection ou le débogage.
- Accepter un fournisseur **entièrement managé et fermé**, avec ce que cela implique de dépendance.

## Quand NE PAS l'utiliser

- Exigence d'**auto-hébergement** ou d'audit du code d'isolation → [[Dev/Services/E2B|E2B]] (Apache-2.0, self-host documenté).
- Besoin de **GPU dans le bac à sable** → [[Dev/Services/Modal|Modal]].
- Volonté de bâtir sur le dépôt public : il n'est **plus maintenu**, s'y appuyer revient à reprendre un fork sans correctifs de sécurité — sur une brique de sécurité.

## Déploiement & coût

- **Managé uniquement** en pratique depuis le passage en closed source ; facturation à la consommation.
- L'ancien dépôt (v0.190.0) reste forkable et auto-hébergeable, mais sans support, correctifs ni patchs — chemin déconseillé sur un composant d'isolation.

## Pièges

- **Le fork open-source est un piège de sécurité** : figé depuis juin 2026, sur un composant dont tout le rôle est de contenir du code hostile.
- **Dépendance forte au fournisseur** : plus aucun moyen d'auditer ou de reprendre l'implémentation du bac à sable.
- Les **snapshots persistent** ce que le bac à sable éphémère effacerait — la surface d'attaque survit d'une session à l'autre. Cf. [[Sandboxing de code généré]].
- Le changement de licence est **récent** : la documentation tierce et les comparatifs antérieurs à mi-2026 le décrivent encore comme open-source.

## Alternatives

- [[Dev/Services/E2B|E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.
- [[Dev/Services/Modal|Modal]] — Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.

## Liens

- Implémente le concept [[Sandboxing de code généré]] — kernel dédié et snapshots d'état.
- Backend d'exécution proposé par [[Dev/Services/Hermes Agent|Hermes Agent]], aux côtés de Docker, SSH, Singularity et Modal.
- Sécurité : [[AI security]], [[Prompt injection]].
- Doc : https://www.daytona.io/docs
