---
role: brique
nom: E2B
alias: [e2b, e2b-dev, E2B Sandbox, Code Interpreter SDK]
pitch: "Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform."
categorie: compute/a-la-demande
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: "TypeScript, Python, Go"
scaling: serverless
alternatives: ["[[Modal]]", "[[Daytona]]"]
complements: []
tags: [agents, llm, container, ai-security]
url_docs: https://e2b.dev/docs
url_repo: https://github.com/e2b-dev/E2B
---

# E2B

<!-- AUTO:BANDEAU:START -->
> Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript, Python, Go | open-source | self-hébergé ou managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Infrastructure spécialisée dans une seule chose : **exécuter du code généré par un LLM sans
exposer l'hôte**. Chaque bac à sable est une **microVM Firecracker** — kernel dédié,
isolation matérielle — créée à la demande et détruite après usage, avec un démarrage annoncé
sous 200 ms, et jusqu'à ~80 ms quand le client est dans la même région. L'usage passe par un
SDK Python ou TypeScript qui pilote le cycle de vie : créer, exécuter, lire le système de
fichiers, récupérer les sorties. Ce qui le distingue de la plupart de ses concurrents
managés est la licence **Apache-2.0** et un chemin d'auto-hébergement documenté.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire tourner du code d'agent, de *code interpreter* ou d'utilisateur avec une isolation forte, pas un simple conteneur | L'isolation du calcul **ne filtre pas le réseau sortant** : sans liste blanche, le code isolé exfiltre quand même |
| Garder l'option du self-host ou du BYOC pour des raisons de conformité ou de souveraineté | Ne jamais monter de **secret de production** dans un bac à sable qui exécute du code non relu |
| Cycles courts et nombreux : le coût de démarrage d'une microVM est assez bas pour être payé à chaque appel | Poser un délai maximum et des plafonds mémoire : une boucle infinie coûte cher avant d'être remarquée |
| | Le self-host est réel mais **non trivial** — Terraform, réseau, images : ce n'est pas un `docker compose up` |
| | Besoin de GPU **dans** le bac à sable, pour exécuter ou entraîner un modèle → [[Modal]] |
| | Le besoin réel est de packager et déployer une application de confiance, pas d'isoler du code hostile → [[Docker]] |
| | Charge de calcul distribuée sur un cluster, plutôt qu'une multitude de petites exécutions isolées → [[Ray]] |

## Mise en œuvre

- Installation — `uv add e2b-code-interpreter` côté Python, ou le SDK TypeScript ; en self-host, déploiement Terraform
- Point d'entrée — SDK qui pilote le cycle de vie du bac à sable : création, exécution, système de fichiers, sorties
- Prérequis — un compte pour le cloud managé ; pour le self-host, AWS, GCP, Azure ou des machines Linux, plus Terraform
- Exécution — self-hébergé ou managé, serverless : les bacs à sable naissent et meurent à la demande, sans capacité à provisionner
- Coût — gratuit, Apache-2.0 ; managé facturé à la consommation (durée × ressources), self-host au coût de l'infrastructure

## Écosystème

### Alternatives

- [[Modal]] — Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.
- [[Daytona]] — Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; **passé closed-source en juin 2026**, le dépôt public restant figé à la v0.190.0 et non maintenu.

## Ressources

- Documentation — https://e2b.dev/docs
- Dépôt — https://github.com/e2b-dev/E2B

## Voir aussi

- [[Sandboxing de code généré]] — la notion qu'il implémente, ici par microVM Firecracker
- [[Calcul distribué]] — le hub du domaine
- [[Hermes Agent]] · [[OpenHands]] — backend d'exécution possible pour ces agents auto-hébergés
- [[Prompt injection]] · [[AI security]] — le contexte de sécurité
