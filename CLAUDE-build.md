---
galaxie: meta
nom: CLAUDE-build
type: meta-doc
created: 2026-05-19
modified: 2026-07-07
tags: [meta, build-mode]
---

# CLAUDE-build.md — Mode construction du DevBrain

Tu es en mode **BUILD** : on enrichit le brain. Toute modification est lecture/écriture légitime sur `Dev/` (Services, Outils, Patterns, Rules, REX), `Templates/`, `Documentation/`, `AI/`. Suis ces conventions strictement. Spec de référence : `AI/design/brain-v2.md`.

> ⚠️ **Wiki/ est hors-périmètre du mode build**, sauf pour `Wiki/Concepts/` que le skill `enrichir-brain` alimente en même temps que `Dev/` (il ne fait pas de bascule de mode). Ne touche pas à `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` en mode build — ils appartiennent au mode wiki (cf. CLAUDE.md, section *Mode wiki*), et sont vides tant que le contenu v1 n'a pas été remigré.

## Modèle de galaxies (champ frontmatter `galaxie:`)

Toute fiche du brain a un champ `galaxie:` dans son frontmatter (sauf les `SKILL.md`, qui suivent le frontmatter Anthropic strict — pas de champ `galaxie:`) :

| Galaxie | Dossiers | Mode d'écriture |
|---|---|---|
| **`dev`** | `Dev/Services/`, `Dev/Outils/`, `Dev/Patterns/`, `Dev/Rules/`, `Dev/REX/` | mode build |
| **`wiki`** | `Wiki/Concepts/`, `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` | mode wiki (+ `Concepts/` via `enrichir-brain`) |
| **`meta`** | docs racine (README, CHANGELOG, INSTALL, CLAUDE*, CONTRIBUTING, Home, Inbox) + `Documentation/`, `AI/design/`, `AI/scripts/` | tout mode |

Le champ permet requêtes `.base` croisées et code couleur du graphe (cf. `Documentation/perso/obsidian-graph.md`).

## Workflow général

L'utilisateur va te demander :

1. **D'ajouter une fiche Service, Outil ou Concept** ("ajoute le service X", "documente Y") → invoque le skill `enrichir-brain` (mode ciblé, cf. `.claude/skills/enrichir-brain/SKILL.md`).
2. **De faire un balayage en fin de conversation** ("mets à jour DevBrain") → `enrichir-brain` en mode balayage : repère tout ce qui mérite une page, draine la file dans `AI/backlog.md`.
3. **De créer un Pattern ou Comparatif** ("compare X et Y", "fais une base pour…") → `enrichir-brain` crée/met à jour `Dev/Patterns/Comparatif - <thème>.base` ou `Pattern - <nom>.md`.
4. **De traiter l'Inbox** ("traite mon inbox") → il n'existe pas encore de skill dédié à `Inbox.md` en v2 (le `process-inbox` v1 n'a pas été porté). Traite manuellement : lis `Inbox.md`, propose une destination par item, demande confirmation, crée la fiche via `enrichir-brain`.
5. **D'enrichir une fiche existante** depuis un article web ou une expérience → patch la fiche concernée.
6. **De refactorer une partie du brain** ("réorganise X", "audite Y") → opération en lot ; les scripts `AI/scripts/check_brain.py` et `audit-vault.ps1` peuvent aider.

## Conventions de fiches Services (strictes)

Toute nouvelle fiche Service va dans `Dev/Services/<Nom>.md` avec le frontmatter complet.

### Champs du frontmatter (Dev/Services/)

```yaml
---
galaxie: dev
type: service
nom: <Name>
alias: []
pitch: "<une ligne, réutilisée dans les Alternatives des autres pages et par planifier-projet>"
categorie: <domaine>/<sous-domaine>   # cf. Documentation/general/taxonomie.md
licence_type: open-source | source-available | proprietary | open-core
hosted: self | managed | both
maturite: production | beta | experimental | deprecated
langage: <langage d'implémentation>
scaling: single-node | distributed | serverless-ok
alternatives: ["[[Dev/Services/X|X]]", ...]
remplace_par: []
status: actif | en-eval | abandonne
tags: [...]                            # pioche dans Documentation/general/tags.md, jamais inventé
url_docs:
url_repo:
---
```

> **Champs volontairement absents** (v1 → v2) : `score`, `mes_projets`, `sous_categories`, `licence` (SPDX), `clients_officiels`, `plateforme`, `remplace`, `url_officiel`, `created`/`modified`. Décision actée dans `AI/design/brain-v2.md` §5.1/§11 : ces champs n'étaient jamais fiables (jamais remplis, ou mentaient). Ne les recrée pas sur une nouvelle fiche.

### Frontmatter Outil (`Dev/Outils/`)

Outils techniques **utilisés** (clients GUI, CLI, utilitaires) — par opposition aux Services **déployés**. Même galaxie `dev`.

```yaml
---
galaxie: dev
type: outil
nom: <Name>
alias: []
pitch: "<une ligne>"
categorie: tooling/<famille>          # ex: tooling/db-admin, tooling/api, tooling/code-assistant
domaines: [<data-eng, ai-eng, ...>]
licence_type: open-source | open-core | proprietary
os: "Windows, macOS, Linux"
langage: <langage>
status: actif | en-eval | abandonne
alternatives: ["[[Dev/Outils/X|X]]", ...]
tags: [...]
url_docs:
url_repo:
---
```

### Taxonomie autorisée pour `categorie`

Voir **`Documentation/general/taxonomie.md`** — c'est la source de vérité, ne la duplique pas ici de mémoire. Résumé des familles :

- `Dev/Services/` → `<domaine>/<sous-domaine>` (`database/*`, `framework/*`, `ui/*`, `language/*`, `devops/*`, `llm/*`, `ml/*`, `data/*`, `automation/*`, `compute/distributed`, `auth`, `storage`, `observability/*`, `tooling/*`)
- `Dev/Outils/` → `tooling/<famille>` (`db-admin`, `api`, `code-assistant`, …)
- `Wiki/Concepts/` → `concept/<sous-domaine>` (`data`, `ai`, `ml`, `dl`, `rl`, `ts`, `nlp`, `signal`, `stats`, `math`, `devops`, `llm`)
- `Wiki/Outils/` → `skill/<famille>` (`documents`, `dev-flow`, `code-quality`, `knowledge`, `data`, `meta`) — section vide en v2 tant qu'aucun skill perso n'est documenté

Catégorie qui ne correspond à rien de listé → **demander avant d'inventer**.

### Valeurs autorisées pour `status`

| Périmètre | Valeurs |
|---|---|
| Services / Outils Dev | `actif`, `en-eval`, `abandonne` |
| REX (`Dev/REX/`) | n/a (frontmatter REX dédié) |

### Corps de la fiche Service/Outil

Sections types (cf. `AI/design/brain-v2.md` §5.1, `Templates/Service-Dev.md`) :

```markdown
# <Nom>

## Pourquoi          (2-3 lignes : ce qu'il fait, sa différence)
## Quand l'utiliser  (bullets)
## Quand NE PAS      (bullets + wikilinks vers alternatives)
## Déploiement & coût (self-host vs managé, prix, scaling — pour les Services)
## Pièges            (court → détail dans [[Dev/REX/REX - <Nom>|REX - <Nom>]] si ça existe)
## Alternatives
- [[Dev/Services/X|X]] — reprend le pitch de X
## Liens
```

**Mécanique du pitch (anti-duplication)** : chaque page porte SON `pitch:` dans le frontmatter, écrit une seule fois. La ligne affichée dans la section *Alternatives* d'une autre page, et dans les propositions de `planifier-projet`, est **réinjectée** depuis ce pitch — jamais retapée à la main. `enrichir-brain` synchronise.

**Important** : les **REX / bugs** ne vont PAS dans `Dev/Services/` ou `Dev/Outils/` — ils ont leur propre dossier `Dev/REX/REX - <Nom>.md` (cf. section suivante).

## Conventions REX (dossier `Dev/REX/`)

Les retours d'expérience (bugs rencontrés, pièges, leçons) sont **séparés** des fiches Service/Outil. Ils vivent dans `Dev/REX/REX - <Nom>.md` — un fichier par service.

### Pourquoi séparer

- Les fiches Service/Outil restent **factuelles et durables** (lisibles et partageables).
- Les REX sont **personnels et évoluent** (une entrée par session quand un bug arrive).
- Wikilinks clairs : `[[Dev/Services/Postgres|Postgres]]` = fiche Service, `[[Dev/REX/REX - Postgres|REX - Postgres]]` = retours d'expérience.

### Frontmatter REX

```yaml
---
galaxie: dev
service: "<Nom>"
type: rex
created: <YYYY-MM-DD>
modified: <YYYY-MM-DD>
tags: [rex, bugs, <nom>]
---
```

### Format d'une entrée REX

```markdown
## YYYY-MM-DD — <Symptôme court>

**Symptôme** : <ce qu'on a vu, logs, erreurs, comportement>

**Cause racine** : <ce qui le causait réellement>

**Fix** :
1. ...
2. ...

**Référence** : [[Projects/<projet>/Bugs#YYYY-MM-DD]]

**Leçon** : <synthèse réutilisable, ce qu'on aurait dû savoir avant>
```

Tri : **plus récent en haut**.

### Création initiale d'un fichier REX

1. Créer `Dev/REX/REX - <Nom>.md` avec le frontmatter ci-dessus
2. Titre H1 : `# REX — <Nom>`
3. Phrase de présentation : `> Retours d'expérience et bugs rencontrés avec [[Dev/Services/<Nom>|<Nom>]].`
4. Première entrée datée

### Mise à jour des liens dans la fiche Service

Quand on crée un fichier REX pour un service, ajouter dans la section "Liens" de la fiche Service :

```markdown
- [[Dev/REX/REX - <Nom>|REX - <Nom>]] — REX accumulés
```

## Conventions Patterns (`Dev/Patterns/`)

### `.base` pour comparatifs dynamiques

```yaml
filters:
  and:
    - file.path.startsWith("Dev/Services/")
    - categorie == "<categorie>"
views:
  - type: table
    name: "<titre>"
    order: [file.name, hosted, licence_type, maturite, alternatives]
```

Path : `Dev/Patterns/Comparatif - <thème>.base`.

### `.md` pour patterns architecturaux opinionnés

```yaml
---
galaxie: dev
type: pattern
contexte: <quand l'appliquer>
services_cles: ["[[Dev/Services/A|A]]", "[[Dev/Services/B|B]]"]
tags: [pattern, ...]
---
```

Corps : Contexte → Décisions clés → Stack récap → Pièges → Voir aussi.

## Conventions Rules (`Dev/Rules/`)

Une règle = un fichier `Dev/Rules/Rule - <nom>.md`.

```yaml
---
galaxie: dev
type: rule
domaine: <git | docs | tests | code-style | security | logging | dependencies | ...>
applicable: global | type-cli | type-web | stack-python-fastapi
strictness: must | should | nice-to-have
created: <YYYY-MM-DD>
modified: <YYYY-MM-DD>
tags: [rule, ...]
---
```

Corps : Principe (1 phrase) → MUST → SHOULD → NICE-TO-HAVE → Exemples (bon/mauvais) → Exceptions → Voir aussi.

## Conventions Concept Wiki (`Wiki/Concepts/`)

```yaml
---
galaxie: wiki
type: concept
nom: <Nom>
alias: []
categorie: concept/<sous-domaine>
domaines: [<data-sci, data-eng, mlops, ml-eng, ai-eng>]
tags: [...]
---
```

Corps (ton impersonnel, technique vulgarisé — cf. `AI/design/brain-v2.md` §5.2, `Templates/Concept-Wiki.md`) : Aperçu → Concepts clés → Les maths, simplement (si pertinent) → En pratique → Approches voisines & alternatives → Pour aller plus loin.

## Workflow d'ajout depuis l'Inbox

`Inbox.md` à la racine, format checkboxes `- [ ]` avec hints de type (`service`, `concept`, `pattern`...). Aucun skill v2 ne l'automatise encore (cf. Workflow général, point 4) — traiter manuellement en attendant.

## Workflow d'ajout depuis URL

Si l'utilisateur fournit une URL : utilise le skill `defuddle` (kepano) pour extraire le contenu propre, puis lance `enrichir-brain` sur le contenu extrait.

## Mémoire de session

À la fin de chaque session de build, écris dans `AI/sessions/YYYY-MM-DD-HHmm-build.md` :
- Fiches ajoutées/modifiées (chemin)
- Décisions de catégorisation
- À reprendre

(Idéalement automatisé par hook Stop — voir `AI/scripts/session_to_devbrain.py`.)

## Git

**Ne commit et ne push jamais automatiquement.** Propose le commit une fois une fiche/un lot vérifié, mais attends la validation explicite de l'utilisateur avant `git commit`/`git push` — cohérent avec la règle globale de CLAUDE.md (aucune action destructrice ou visible sans confirmation).

Exemple de proposition :
```
À commit :
- Dev/Services/Postgres.md (modifié — section Liens)
- Dev/REX/REX - Postgres.md (nouveau)

Message suggéré :
docs(postgres): add REX file with connection pool incident
```

## Anti-patterns à éviter

- Inventer un score ou une note si l'utilisateur n'a pas testé (le champ `score` n'existe plus — ne pas le réintroduire).
- Mettre `production` si la doc dit "beta".
- Créer la fiche dans une catégorie improvisée — toujours vérifier `Documentation/general/taxonomie.md`, demander sinon.
- Inventer un tag hors `Documentation/general/tags.md` sans le proposer d'abord.
- Modifier une fiche `status: abandonne` sans demander.
- Réécrire une fiche entière au lieu de patcher la section concernée.
