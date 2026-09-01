---
galaxie: dev
type: service
nom: E2B
alias: [e2b, e2b-dev, E2B Sandbox, Code Interpreter SDK]
pitch: "Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform."
categorie: compute/a-la-demande
famille: plateforme
licence_type: open-source
hosted: both
maturite: production
langage: "TypeScript, Python, Go"
scaling: serverless
alternatives: ["[[Dev/Services/Modal|Modal]]", "[[Dev/Services/Daytona|Daytona]]"]
remplace_par: []
status: actif
tags: [agents, llm, container, ai-security]
url_docs: https://e2b.dev/docs
url_repo: https://github.com/e2b-dev/E2B
---

# E2B

## Pourquoi

Infrastructure spécialisée dans une seule chose : **exécuter du code généré par un LLM sans exposer l'hôte**. Chaque bac à sable est une **microVM Firecracker** — kernel dédié, isolation matérielle — créée à la demande et détruite après usage. Le démarrage annoncé est inférieur à **200 ms**, et descend à ~80 ms lorsque le client est dans la même région.

L'usage passe par un SDK (Python, TypeScript) qui pilote le cycle de vie : créer, exécuter, lire le système de fichiers, récupérer les sorties. Licence **Apache-2.0**, avec un chemin d'**auto-hébergement documenté** (Terraform sur AWS, GCP, Azure ou machines Linux) — ce qui distingue E2B de la plupart de ses concurrents managés.

## Quand l'utiliser

- Faire tourner du code écrit par un agent, un *code interpreter* ou un utilisateur, avec une **isolation forte** et non un simple conteneur.
- Vouloir garder l'option du **self-host** ou du BYOC (déploiement dans son propre compte cloud) pour des raisons de conformité ou de souveraineté.
- Cycles **courts et nombreux** : le coût de démarrage d'une microVM est ici assez bas pour être payé à chaque appel.

## Quand NE PAS l'utiliser

- Besoin de **GPU dans le bac à sable** (exécution de modèles, entraînement) → [[Dev/Services/Modal|Modal]].
- Le besoin réel est de **packager et déployer une application de confiance**, pas d'isoler du code hostile → conteneur classique, [[Dev/Services/Docker|Docker]].
- Charge de calcul **distribuée** sur un cluster plutôt que multitude de petites exécutions isolées → [[Dev/Services/Ray|Ray]].

## Déploiement & coût

- **Cloud managé** (démarrage gratuit) ou **auto-hébergé** via Terraform — l'infrastructure complète est open-source.
- Facturation à la consommation du bac à sable (durée × ressources) côté managé ; en self-host, coût de l'infrastructure sous-jacente.
- Scaling **serverless** : les bacs à sable naissent et meurent à la demande, pas de capacité à provisionner.

## Pièges

- L'isolation du calcul **ne filtre pas le réseau sortant** : sans liste blanche, le code isolé exfiltre quand même. Cf. [[Sandboxing de code généré]].
- **Ne jamais monter de secret de production** dans un bac à sable qui exécute du code non relu.
- Poser un **délai maximum** et des plafonds mémoire : une boucle infinie coûte cher avant d'être remarquée.
- Le self-host est réel mais **non trivial** (Terraform, réseau, images) — ne pas l'annoncer comme un `docker compose up`.

## Alternatives

- [[Dev/Services/Modal|Modal]] — Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.
- [[Dev/Services/Daytona|Daytona]] — Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; **passé closed-source en juin 2026**, le dépôt public restant figé à la v0.190.0 et non maintenu.

## Liens

- Implémente le concept [[Sandboxing de code généré]] — isolation par microVM Firecracker.
- Backend d'exécution possible pour les agents auto-hébergés ([[Dev/Services/Hermes Agent|Hermes Agent]], [[Dev/Services/OpenHands|OpenHands]]).
- Sécurité : [[Prompt injection]], [[AI security]].
- Doc : https://e2b.dev/docs
