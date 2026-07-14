---
galaxie: dev
type: outil
nom: Bruno
alias: [bruno, usebruno]
pitch: "Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud."
categorie: tooling/api
domaines: [data-eng, ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: JavaScript (Electron)
status: actif
alternatives: ["[[Dev/Outils/Postman|Postman]]"]
tags: [api-client, version-control]
url_docs: https://docs.usebruno.com/
url_repo: https://github.com/usebruno/bruno
---

# Bruno

## Pourquoi

Client d'API léger et open-source (MIT), pensé git-native : les collections sont stockées en clair sur le système de fichiers dans un langage de balisage texte, **Bru** (fichiers `.bru`). Conçu comme alternative sobre à Postman/Insomnia, sans compte ni synchronisation cloud — tout reste local et se versionne avec git comme n'importe quel code.

## Quand l'utiliser

- Versionner les collections d'API dans le dépôt git du projet (diffs lisibles, revue de code, branches).
- Travailler 100 % hors-ligne, sans compte ni envoi de données vers un cloud tiers.
- Client de requêtes simple et rapide : scripting JavaScript, assertions style Chai, import npm dans une collection.

## Quand NE PAS l'utiliser

- Besoin de l'écosystème complet (mocks, monitoring, doc publiée, catalogue, collaboration cloud clés en main) → [[Dev/Outils/Postman|Postman]].
- Équipe déjà investie dans les espaces de travail partagés Postman → [[Dev/Outils/Postman|Postman]].

## Bases & plateformes

- Open-source, licence MIT. Cœur gratuit ; offre commerciale (support / fonctions entreprise) en option, sans rendre l'outil propriétaire.
- Application desktop Windows, macOS, Linux. Installation par binaire ou gestionnaires de paquets (Homebrew, Chocolatey, Scoop, Snap, Flatpak, Apt). CLI disponible pour l'exécution en CI.

## Pièges

- Format `.bru` propre à Bruno : pas un standard interopérable (import/export Postman/OpenAPI disponible mais imparfait).
- Moins de fonctions « plateforme » que Postman (pas de monitoring/mocks cloud intégrés) — c'est le compromis assumé.

## Alternatives

- [[Dev/Outils/Postman|Postman]] — Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.

## Liens

- [[Comparatif - Clients d'API]] — comparatif des clients d'API
- Doc : https://docs.usebruno.com/
