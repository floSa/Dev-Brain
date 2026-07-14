---
galaxie: meta
nom: brain-v2
type: design-doc
created: 2026-06-03
modified: 2026-06-03
status: en-discussion
tags: [meta, design, v2]
---

# DevBrain v2 — Spec de reconstruction

> Document de conception vivant. On co-écrit ici la cible **avant** tout code.
> Quand la spec est validée, on reconstruit le vault et on remigre le contenu v1.
> Statut actuel : **en discussion** — sections marquées 🟡 = à trancher.

---

## 1. Objectif & principe directeur

Reconstruire le DevBrain proprement, en récupérant le contenu v1 comme matière première.

**Principe organisateur : on range par NATURE du contenu.**

| Galaxie | Contenu | Optimisé pour | Forme |
|---------|---------|---------------|-------|
| **DEV** | tout ce qui est **technique** : briques à déployer (services, frameworks, libs, BDD) **et** outils techniques que l'on utilise (clients GUI, CLI, utilitaires) | retrouver vite la bonne techno | frontmatter dense + corps court et prévisible |
| **WIKI** | les **notions** à comprendre (concepts) + skills/extensions de pratique perso (Claude Code, Obsidian) | se rafraîchir la mémoire, comprendre | hiérarchie vulgarisée, parties + bullets |

Règle simple : **est-ce technique ? → Dev. Est-ce une notion / un skill perso ? → Wiki.** Un client SQL (DBeaver), un CLI (uv) ou un framework sont techniques → `Dev/`, jamais `Wiki/`. La proximité thématique (DBeaver près des bases) est assurée par le **graphe** (liens + MOC), pas par le dossier.

Conséquence : un même sujet peut exister des deux côtés (concept Wiki + service Dev) et **se lier**. Pas de doublon, deux usages.

**Principe de conception : on conçoit à l'envers, depuis les usages.** Une brique ou un champ qui ne sert à aucun des deux workflows cibles (§2) ne mérite pas d'exister.

---

## 2. Les deux workflows cibles (= critères d'acceptation)

### W1 — Enrichir le brain depuis une conversation (skill `enrichir-brain`)

Deux modes :
- **Ciblé** : « ajoute Weaviate » / « ajoute le sujet bases vectorielles ».
- **Balayage** : « mets à jour DevBrain » en fin de conversation → repère tout ce qui mérite une page.

Exigence forte : **faire les choses bien, sans rien oublier**. Créer la page demandée *et* les pages connexes manquantes (Weaviate → concept « bases vectorielles » s'il manque), poser les bons tags, créer les liens, mettre à jour bidirectionnellement les pages existantes (alternatives qui se citent mutuellement).

### W2 — Planifier un projet depuis le brain (skill `planifier-projet`)

En début de projet : « je veux une appli copie de tel jeu » / « propose-moi un plan ».
Le skill interroge surtout DEV (+ quelques Concepts Wiki) et **propose un plan en posant des questions à choix**, chaque candidat affiché avec son pitch d'une ligne. floSa tranche vite. Le plan devient le cahier des charges qui **contraint l'IA de dev** ensuite.

---

## 3. Arborescence cible

```
DevBrain/
├── Dev/                  ← galaxie DEV (tout le technique)
│   ├── Services/             briques à déployer (frameworks, BDD, libs…)
│   ├── Outils/               outils techniques que l'on utilise (clients GUI, CLI, utilitaires)
│   ├── Patterns/             architectures réutilisables + comparatifs .base
│   ├── Rules/                règles transverses (Global, Types, Documentation)
│   └── REX/                  retours d'expérience / bugs (1 fichier par service)
├── Wiki/                 ← galaxie WIKI (notions + skills perso)
│   ├── Concepts/             notions, techniques (cheat-sheet/cours)
│   ├── Workflows/            procédures pas-à-pas
│   ├── Outils/               skills / extensions de pratique perso (Claude Code, Obsidian, MCP)
│   └── Roadmaps/             cartes de compétences
├── Skills/               ← skills exécutables (sortis de AI/skills)
├── Templates/            ← gabarits de pages
├── Documentation/        ← colonne vertébrale (gouvernance + appuis) — cf. §6
│   ├── general/              guide réutilisable par quiconque (template)
│   └── perso/                vision, conventions, config machine de floSa
└── AI/                   ← espace agent (sessions, décisions, scripts, index généré)
    ├── scripts/              utilitaires Python (uv)
    ├── index/                index généré (lu/écrit par les skills)
    ├── sessions/  decisions/  design/
```

Changements vs v1 : `Bugs/` → `Dev/REX/` ; `Documentation/` apparaît et se scinde general/perso ; scripts passent en Python.

---

## 4. Galaxies (champ `galaxie:`)

| Valeur | Dossiers | Mode d'écriture |
|--------|----------|-----------------|
| `dev` | `Dev/` | mode build |
| `wiki` | `Wiki/` | mode wiki |
| `skills` | `Skills/` | build/wiki |
| `meta` | docs racine + `Documentation/` + `AI/` | tout mode |

Sert au code couleur (graphe Obsidian) et aux requêtes Bases.

---

## 5. Gabarits de pages

### Convention de ton (toutes les pages)

**Ton impersonnel.** Ni « tu » ni « vous ». Phrases courtes, segmentées. Hiérarchie claire (parties + bullets) pour se repérer d'un coup d'œil.

### 5.1 Page DEV — Service (pour l'IA : dense, filtrable)

Frontmatter élagué aux seuls champs qui servent à **planifier** :

```yaml
galaxie: dev
type: service
nom: Weaviate
alias: []
pitch: "Base vectorielle orientée production, hybride dense+keyword, self-host ou managé."  # ← une ligne, réutilisée partout
categorie: database/vector
licence_type: open-source        # sert à "commercialisable ?"
hosted: both                     # self | managed | both — sert à "déployable ?"
maturite: production             # production | beta | experimental | deprecated
langage: Go
scaling: distributed             # single-node | distributed | serverless-ok
alternatives: ["[[Qdrant]]", "[[Milvus]]", "[[pgvector]]"]
remplace_par: []
status: actif                    # actif | en-eval | abandonne
tags: [vector-db, rag]           # pioche dans Documentation/general/tags
url_docs:
url_repo:
```

> **Champs morts supprimés** : `score` et `mes_projets` (jamais remplis à la main → ils mentent). « Projets où X est utilisé » se **déduit** des liens entrants depuis `Projects/`.

Corps :
```markdown
## Pourquoi          (2-3 lignes : ce qu'il fait, sa différence)
## Quand l'utiliser  (bullets)
## Quand NE PAS      (bullets + liens [[alternatives]])
## Déploiement & coût (self-host vs managé, prix, scaling)
## Pièges            (court → détail dans [[REX - Weaviate]])
## Alternatives
- [[Qdrant]] — base vectorielle Rust, ultra-rapide, simple à self-host
- [[pgvector]] — extension Postgres, idéale si du Postgres est déjà en place
- [[Milvus]] — distribué costaud, pour gros volumes
## Liens
```

**Mécanique du pitch (anti-duplication)** : chaque outil porte SON pitch (frontmatter `pitch:`), écrit une seule fois. La ligne d'info affichée dans la section *Alternatives* d'une autre page, et dans les propositions du skill `planifier-projet`, est **réinjectée** depuis le pitch de la page cible. Une donnée, trois usages. Le skill `enrichir-brain` synchronise.

### 5.2 Page WIKI — Concept (pour l'humain : technique + vulgarisé)

Frontmatter :
```yaml
galaxie: wiki
type: concept
nom: Bases de données vectorielles
alias: [vector db, vector store]
categorie: concept/data
domaines: [data-eng, ai-eng]
tags: [vector-db, rag]
# pas de lecture_min (inutile)
```

Corps — **hiérarchie parties/bullets, technique vulgarisé, ton impersonnel** (la longueur n'est pas un impératif) :
```markdown
## Aperçu
- définition en 1-2 bullets
- à quoi ça sert

## Concepts clés
### <notion 1>
- bullet court
- bullet court
### <notion 2>
- ...

## Les maths, simplement
- formule (LaTeX) + ce qu'elle veut dire en une phrase
- notations explicitées

## En pratique
- quand l'utiliser / comment / pièges (bullets)

## Approches voisines & alternatives
- [[concepts liés]]

## Pour aller plus loin
- refs, papiers, [[pages Wiki connexes]]
```

Les notions trop grosses → leur propre page Wiki, liée depuis « Concepts clés » / « Approches voisines ».

### 5.3 Autres gabarits (à reprendre de v1, quasi inchangés)

- **Pattern** (`Dev/Patterns/`) : Contexte → Décisions clés → Stack récap → Pièges → Voir aussi.
- **Rule** (`Dev/Rules/`) : Principe → MUST / SHOULD / NICE → Exemples → Exceptions.
- **REX** (`Dev/REX/`) : entrées datées `## YYYY-MM-DD — <symptôme>`, plus récent en haut.
- **Workflow** (`Wiki/Workflows/`) : étapes numérotées.
- **Outil** (`Wiki/Outils/`) : catalogue d'outils de travail (skills, CLI, MCP).

---

## 6. Gouvernance : le dossier `Documentation/`

Appui partagé entre l'humain et les skills. Les skills le **lisent** pour rester cohérents et le **mettent à jour**.

### `Documentation/general/` (réutilisable par quiconque — partie "template")
- `tags` — **vocabulaire de tags contrôlé**. Un skill pioche ici ou propose un ajout (interdit d'inventer).
- `taxonomie` — catégories autorisées (ex-CLAUDE-build).
- `themes` — grandes thématiques (DS / DE / MLOps / ML eng / AI eng) et MOC associés.
- `questions-projet` — checklist du skill planificateur (§8).
- guide « qu'est-ce que ce second brain, comment le refaire pour ton domaine avec l'IA ».

### `Documentation/perso/` (vision/usage de floSa)
- conventions perso, stacks par défaut, archétypes de projet (§8).
- `machines` — config par machine (GPU/CPU, chemins, Windows/WSL, pro/perso).

### `AI/index/` (généré, jamais édité à la main)
- index agrégé : pour chaque page → pitch, tags, alternatives, catégorie, galaxie.
- C'est le **« document qui récapitule les liens »** : le skill `enrichir-brain` le lit **avant** de créer (références réelles, rien d'oublié) et le **régénère après**. Le skill `planifier-projet` le **requête** pour filtrer les candidats sans lire 160 fichiers.
- **Format tranché** : deux artefacts distincts.
  - `AI/index/brain-index.json` — catalogue machine régénéré par script Python à chaque modif. Lu/écrit par les **skills**. L'humain n'y touche jamais.
  - **Vues `.base`** dans le vault — pour la navigation humaine dans Obsidian (filtrage visuel). Lisent le frontmatter en live, pas besoin de l'index.

---

## 7. Skills (protocoles)

### 7.1 `enrichir-brain` (capture)

Mode ciblé — protocole :
1. Lire `AI/index/` (état courant) + `Documentation/general/tags` + `taxonomie`.
2. Vérifier si la page existe (alias inclus).
3. Identifier les **pages connexes** nécessaires (concept parent, comparatif, alternatives citées).
4. Créer/mettre à jour chaque page manquante via le sous-skill adéquat (`add-service`, `add-concept`…).
5. Poser les tags depuis le vocabulaire contrôlé.
6. Câbler les wikilinks (réutilise le moteur de découverte de liens).
7. **Synchroniser bidirectionnellement** les alternatives (si A→B, alors B→A) et les pitches.
8. Régénérer `AI/index/`.

Mode balayage — protocole séquentiel :
1. Analyser la conversation → liste de pages candidates.
2. Écrire la file dans `AI/backlog.md` (fichier de travail temporaire de l'agent).
3. **Drainer la file une page à la fois**, chacune via le protocole ciblé. Repassable, rien d'oublié.

### 7.2 `planifier-projet` (kickoff)

1. Lire la description du projet.
2. Identifier l'**archétype** (§8) → ne poser que les questions pertinentes (`Documentation/general/questions-projet`).
3. Pour chaque brique nécessaire : requêter `AI/index/`, proposer 2-3 **candidats** (nom + pitch d'une ligne), laisser trancher.
4. Produire un **plan/cahier des charges** sourcé (liens vers Services/Patterns/Rules) qui contraindra l'IA de dev.

---

## 8. Archétypes de projet & questions (profil floSa)

### Archétypes (pilotent le branchement des questions)
1. Analyse / exploration de données (notebook, stats, viz, rapport).
2. App data/ML interactive (Streamlit : annotation, dashboard temps réel).
3. ML/IA algorithmique (jeux MCTS/CFR, détection image, reco).
4. Pipeline data / ingestion (ELT, robustesse, ops).
5. RAG / app LLM (retrieval, LLM, knowledge graph, éval).
6. Tuto / apprentissage (repro, pas de prod).
7. Réplique ludique (perso).

### Axe transverse critique : **on-premise**
Profil pro : data scientist / data analyst / AI eng / MLOps, spécialité **on-prem** (industriels, ESN). Le skill demande tôt : cloud autorisé ou **on-prem strict / air-gapped** ? GPU ou CPU only ? données qui sortent du réseau client ?

### Checklist `questions-projet`
- **Cadrage** : archétype ? perso / pro-client ? jetable, outil durable, ou livrable ?
- **Exécution** : tourne où (notebook local, Streamlit local, service on-prem, conteneur client) ? on-prem strict / air-gapped ? GPU/CPU ? one-shot ou continu ?
- **Données** : source & volumétrie ? type (tabulaire/texte/image/audio/série temporelle) ? persistance ? confidentielles / RGPD / réseau client ?
- **IA/LLM** : besoin LLM ? local (petit modèle, sans GPU) vs API (interdit si air-gapped) ? entraînement ou inférence seule ?
- **Légal** : livré/commercialisé ? licences compatibles (éviter copyleft si fermé) ?
- **Qualité** : jetable (notebook propre) vs packagé (uv + tests + CI) ? repris par client/équipe ? repro exigée (seed, env figé) ?

---

## 9. Décisions structurelles

### 9.1 Portabilité (Windows ↔ WSL, pro ↔ perso, fixe ↔ portable)
- Contenu : déjà couvert par Git.
- **Scripts utilitaires réécrits en Python (lancés via uv)** → cross-OS. Plus de PowerShell.
- Aucun chemin absolu dans scripts/config (relatif au vault).
- Config par machine dans `Documentation/perso/machines`.

### 9.2 Partageable / template
- Séparer **moteur générique** (`Documentation/general/`, Templates, Skills, scripts) du **contenu perso**.
- Cible : cloner le repo → lire le guide général → skill « bootstrap » → l'IA régénère un brain vide structuré pour un autre domaine.
- **Conçu maintenant, implémenté en dernier** (sinon le scope explose).

### 9.3 Navigation
- Graphe : dépend de la densité de liens → garantie par `enrichir-brain`.
- Arborescence + **MOC** (pages-index par thème) dans `Documentation/`.

---

## 10. Plan de récupération du contenu v1

À détailler une fois la spec validée. Principe : remigrer Services/Concepts existants en remplissant les nouveaux champs (`pitch`, `scaling`), en élaguant les champs morts, et en passant chaque page au crible du nouveau gabarit. Probablement semi-automatisé par un script + le skill `enrichir-brain`.

---

## 11. Décisions tranchées (clôture du 2026-06-03)
- ✅ Format de l'index : `AI/index/brain-index.json` (skills) + vues `.base` (navigation humaine).
- ✅ `score` : abandonné totalement (pas de remplacement).
- ✅ Noms de skills `enrichir-brain` / `planifier-projet` validés ; on récupère les skills v1 utiles.
- ✅ File d'attente du mode balayage : `AI/backlog.md`.

La spec est complète. Reste à valider l'ensemble, puis lancer la reconstruction (§10).
