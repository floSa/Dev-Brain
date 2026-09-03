---
galaxie: meta
nom: Home
type: meta-doc
tags: [meta]
---

# DevBrain — Accueil

## Domaines migrés en v3

Un dossier par domaine, à la racine ; sa page `role: hub` porte son nom.

- [[Machine Learning]] — 85 briques, 9 sous-domaines : [[Apprentissage profond]], [[Apprentissage par renforcement]], [[Séries temporelles]], [[NLP]], [[Serving]], [[Vision]], [[Suivi d'expériences]], [[Interprétabilité]], [[Tabulaire]]
- [[LLM & IA générative]] — 74 briques, 6 sous-domaines : [[Agents de code]], [[Runtimes]], [[Agents]], [[Fine-tuning]], [[Text-to-SQL]], [[Assistants]]
- [[Bases de données]] — 47 briques, 4 sous-domaines
- [[Statistiques & inférence]] — 10 briques
- [[Data & pipelines]] — 46 briques, 5 sous-domaines
- [[Mathématiques]] — 1 brique
- [[Outils de développement]] — 20 briques, 1 sous-domaine
- [[Signal & audio]] — 3 briques
- [[Design & diagrammes]] — 7 briques, 1 sous-domaine
- [[Calcul distribué]] — 7 briques
- [[Web & API]] — 6 briques
- [[Stockage]] — 6 briques
- [[Automatisation no-code]] — 5 briques
- [[Médias]] — 4 briques
- [[Interfaces & apps data]] — 4 briques
- [[Sécurité]] — 3 briques
- [[Observabilité]] — 3 briques
- [[Réseau]] — 2 briques
- [[Documents]] — 2 briques
- [[DevOps]] — 2 briques

## Métiers — les 6 axes transverses

Le seul axe qui traverse l'arbre technique : il se lit dans le champ `domaines:`.

- [[Data Science]] · [[Data Engineering]] · [[MLOps]] · [[ML Engineering]] · [[AI Engineering]] · [[Infrastructure & Ops]]

> `Infrastructure & Ops` est apparu au lot 4, le 2026-09-05, sans qu'on le décide : `themes.md`
> le déclare depuis le 2026-09-02, mais `build_mocs.py` ne comptait que les pages `Wiki/`, où
> aucune notion ne le portait. Le lot a étendu ce périmètre à l'arbre, et les 3 briques qui le
> portent — [[Sniffnet]], [[croc]], [[osint4all]] — ont matérialisé la page.

## Rangés par `role:` — aucune `categorie:` ne les range

- [[Patterns]] — 5 architectures type, chacune enjambant plusieurs domaines
- [[Rules]] — 5 règles transverses, applicables quelle que soit la stack

## Pilotage

- [[brain-index|Index lisible]] — toutes les pages par domaine et par `role:`
- [[liens|Carte des liens]] — tags & liens par page, + sujets à créer
- Gouvernance : `Documentation/general/` (tags, taxonomie, themes)
- Réservoir v1 : [[reservoir-v1|Inventaire v1]] (+ `Archive-v1.zip`)

## Ce qui n'est pas encore dans l'arbre

La v3 remplace les deux galaxies par un arbre de domaines : la nature d'une page
est portée par `role:`, son domaine par son dossier (cf. `AI/design/brain-v3.md`).
`Dev/` n'existe plus. Il reste **`Wiki/Concepts/`** — **119** notions `concept/*` que
le lot 4 descendra dans l'arbre, et **2** `MOC/Concepts/` avec elles : ces pages sont
aujourd'hui leur seule porte d'entrée, et chacune meurt le jour où il est **mesuré** que
plus aucune notion ne dépend d'elle seule. Familles déjà rangées au 2026-09-05 :
statistiques, mathématiques, data, signal, sécurité IA, LLM, le renforcement, les séries
temporelles et le NLP. Restent le machine learning (67) et le deep learning (52).

## Skills

- `enrichir-brain` — ajouter / compléter un sujet (propose un plan, puis construit)
- `planifier-projet` — cadrer un projet depuis le brain
