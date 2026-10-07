---
role: brique
nom: MADR - le modèle de fiche
alias: [adr/madr, Markdown Architectural Decision Records, Markdown ADR]
pitch: "Modèle de fiche en Markdown (MIT ou CC0-1.0, quatre variantes) pour consigner une décision d'architecture : contexte, options envisagées, décision et conséquences, un fichier par décision dans `docs/decisions` — mais c'est un gabarit à copier, sans outil de génération, ni de contrôle, ni d'index."
categorie: devtools/projet
famille: specification
domaines: [ai-eng]
licence_type: open-source
maturite: production
alternatives: []
complements: []
tags: [adr, documentation, project-management]
url_docs: https://adr.github.io/madr/
url_repo: https://github.com/adr/madr
---

# MADR - le modèle de fiche

<!-- AUTO:BANDEAU:START -->
> Modèle de fiche en Markdown (MIT ou CC0-1.0, quatre variantes) pour consigner une décision d'architecture : contexte, options envisagées, décision et conséquences, un fichier par décision dans `docs/decisions` — mais c'est un gabarit à copier, sans outil de génération, ni de contrôle, ni d'index.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification | open-source | rien à exécuter | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Format, pas logiciel.** MADR (*Markdown Architectural Decision Records*) est un **modèle de fiche** pour tenir le journal des décisions d'un projet, un fichier Markdown par décision. Le dépôt livre quatre gabarits : `adr-template.md` (toutes les sections, avec explications), `adr-template-minimal.md` (seulement les sections obligatoires, expliquées), `adr-template-bare.md` (toutes les sections, vides) et `adr-template-bare-minimal.md`. On copie le gabarit dans `docs/decisions`, puis une fois par décision sous le nom `nnnn-titre.md`, et on l'adapte.

Le gabarit complet s'ouvre sur un titre court, puis les sections **Context and Problem Statement** (le problème, de préférence en une question), **Considered Options** (la liste des options), **Decision Outcome** (« option choisie : … parce que… »), et, en option, **Consequences** (le bon et le mauvais). C'est la liste des options écartées qui évite de rediscuter dix fois le même choix : la notion [[ADR et design docs]] détaille les variantes d'ADR et les compare au gabarit de Nygard. MADR suit SemVer, publie un CHANGELOG et vient d'une communauté de recherche en génie logiciel (article de Kopp, Armbruster et Zimmermann, ZEUS 2018). Dernière release 4.0.0 du 2024-09-17, dépôt poussé le 2026-08-28.

**Licence.** L'API GitHub ne détecte pas de licence unique : le fichier `LICENSE` du dépôt dit « MIT OR CC0-1.0 », et les fichiers `LICENSE.MIT` et `LICENSE.CC0-1.0` sont présents. Copier le gabarit dans un projet ne pose pas de question.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Garder la raison des choix techniques dans le dépôt, relisible en pull request avec le code | Une décision à discuter en amont avant de choisir : un document de conception ou une RFC, cf. [[ADR et design docs]] |
| Un gabarit qui force à lister les options écartées | Un outil qui numérote, indexe ou valide les fichiers : MADR n'en fournit pas |
| Donner à un agent de code la raison d'un choix avant qu'il ne le remette en cause (cf. [[Fichiers de contexte pour agents]]) | Une description du comportement d'un changement à venir : [[OpenSpec]] ou [[Développement piloté par la spécification]] |
| Projet solo comme projet d'équipe : quatre variantes, de la plus courte à la plus complète | Un modèle plus détaillé que la variante complète : le gabarit ne couvre pas l'architecture en vues, cf. [[Modèle C4]] |

## Mise en œuvre

- Installation — aucune : copier `template/adr-template.md` (ou la variante minimale) dans `docs/decisions`
- Point d'entrée — une première fiche `0000-use-markdown-architectural-decision-records.md`, fournie par le dépôt, qui consigne le choix du format lui-même
- Prérequis — aucun
- Exécution — rien à exécuter ; le dépôt de MADR utilise markdownlint pour ses propres fichiers
- Coût — gratuit, MIT ou CC0-1.0 au choix

## Écosystème

### Alternatives

- Aucune alternative déclarée : le gabarit de Nygard et les RFC sont décrits dans la notion [[ADR et design docs]], sans fiche d'outil.
- voisin : [[OpenSpec]] — décrit le comportement visé d'un changement, là où MADR garde la raison d'un choix.

## Ressources

- Documentation — https://adr.github.io/madr/
- Dépôt — https://github.com/adr/madr

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[ADR et design docs]] — la notion : les ADR, leurs variantes et les design docs
- [[Fichiers de contexte pour agents]] — ce qu'un agent ne peut pas deviner et qu'on lui écrit une fois
- [[Outils de développement]] — le hub du domaine
