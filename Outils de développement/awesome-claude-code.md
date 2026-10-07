---
role: brique
nom: awesome-claude-code
alias: [hesreallyhim/awesome-claude-code, awesome claude code]
pitch: "Annuaire GitHub d'environ deux cents ressources pour Claude Code, rangées par thème — skills, agents, serveurs, lignes d'état, suivi de coûts, orchestration, configuration — avec un compteur de projets en vogue, publié sous licence CC BY-NC-ND 4.0 : usage non commercial, sans modification — une liste à lire, pas un outil, et chaque ressource garde sa propre licence."
categorie: devtools/annuaire-standard
famille: annuaire
domaines: [ai-eng]
licence_type: source-available
maturite: production
alternatives: []
complements: []
tags: [agent-skill, skills, agents]
url_docs: https://github.com/hesreallyhim/awesome-claude-code
url_repo: https://github.com/hesreallyhim/awesome-claude-code
---

# awesome-claude-code

<!-- AUTO:BANDEAU:START -->
> Annuaire GitHub d'environ deux cents ressources pour Claude Code, rangées par thème — skills, agents, serveurs, lignes d'état, suivi de coûts, orchestration, configuration — avec un compteur de projets en vogue, publié sous licence CC BY-NC-ND 4.0 : usage non commercial, sans modification — une liste à lire, pas un outil, et chaque ressource garde sa propre licence.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Annuaire | source-available | rien à exécuter | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Un annuaire, pas un outil.** `awesome-claude-code` est une liste GitHub, tenue à la main par `hesreallyhim`, de ressources pour l'agent de code Claude Code : documentation et apprentissage, skills, agents, serveurs et plugins, lignes d'état, clients alternatifs, orchestration d'agents, mémoire et persistance du contexte, observabilité (moniteurs de session, usage et coût), configuration, tests, analyse statique et autres. Le README s'ouvre par un « ticker » des projets Claude Code en vogue sur GitHub, une rubrique « Recently Added » et une table des matières ; compté le 2026-10-07, il porte 212 entrées en puces. Le dépôt, créé le 2025-04-19, n'est pas archivé et a été poussé le 2026-10-07. Les données vivent dans un fichier CSV (`THE_RESOURCES_TABLE_NEW.csv`) d'où un script (`generate_readme.py`) produit le README.

**Licence, à lire en premier.** Le fichier `LICENSE` du dépôt dit : CC BY-NC-ND 4.0 (attribution, **pas d'usage commercial, pas de modification**). L'API GitHub ne la détecte pas comme licence standard. Le mainteneur écrit que ce choix vise à empêcher que son travail et celui des auteurs listés soient repris de manière nuisible, et qu'on peut le contacter pour une version modifiée. Pour un usage non commercial, la licence n'interdit pas de **lire** la liste ; elle interdit de la reprendre modifiée. Aucune entrée n'est recopiée ici, et **la licence de chaque ressource listée est celle de son propre dépôt** : l'annuaire n'en dit rien.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Chercher quels skills, serveurs et lignes d'état existent pour Claude Code, par thème | Un skill précis pour une étape du cycle de projet, avec sa licence relevée : [[Quel skill pour quelle étape]] |
| Repérer un outil à verser au brain : la section « Usage & Cost » liste les suiveurs de consommation, dont [[Claude-Code-Usage-Monitor]] | Une source de skills sous licence connue : le dépôt officiel, cf. [[Skills d'Anthropic]] |
| Voir comment les gens organisent leurs fichiers de contexte et leurs commandes | Une description fiable de ce que fait un outil listé : la ligne de l'annuaire est celle de son auteur ; lire le dépôt |
| Suivre l'actualité de l'écosystème par la rubrique « Recently Added » | Reprendre le texte de la liste dans un document modifié : la licence l'interdit |

## Mise en œuvre

- Installation — aucune ; une page GitHub à lire
- Point d'entrée — le `README.md` ; le CSV des ressources est dans le dépôt
- Prérequis — aucun
- Exécution — rien à exécuter
- Coût — gratuit à lire ; usage non commercial, sans modification (CC BY-NC-ND 4.0)

## Écosystème

### Alternatives

- voisin : [[Skills d'Anthropic]] — le dépôt officiel de skills d'Anthropic, lui aussi rangé comme annuaire ; il porte des skills, la liste ici renvoie vers des ressources externes.
- voisin : [[Agent Skills - la spécification]] — le format que suivent les skills listés.
- voisin : awesome-claude-skills (`ComposioHQ`) — une autre liste, sans fichier de licence détecté ; pas de page dans le brain (règle de licence).

## Ressources

- Documentation — https://github.com/hesreallyhim/awesome-claude-code
- Dépôt — https://github.com/hesreallyhim/awesome-claude-code

## Voir aussi

- [[Outils de développement]] — le hub du domaine ; les annuaires et standards de l'écosystème des agents sont rangés à part des outils (règle D-R14)
- [[Agent skills]] — la notion : ce qu'est un skill et comment il se charge
- [[Fichiers de contexte pour agents]] — le contexte permanent d'un dépôt, à côté des skills
