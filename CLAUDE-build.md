---
galaxie: meta
nom: CLAUDE-build
type: meta-doc
created: 2026-05-19
modified: 2026-07-07
tags: [meta, build-mode]
---

# CLAUDE-build.md — Mode construction du DevBrain

Tu es en mode **BUILD** : on enrichit le brain. Toute modification est lecture/écriture légitime sur `Dev/` (quatre piliers : Services, Outils, Patterns, Rules), `Templates/`, `Documentation/`, `AI/`. Suis ces conventions strictement. Spec de référence : `AI/design/brain-v2.md`.

> ⚠️ **Wiki/ est hors-périmètre du mode build**, sauf pour `Wiki/Concepts/` que le skill `enrichir-brain` alimente en même temps que `Dev/` (il ne fait pas de bascule de mode). Ne touche pas à `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` en mode build — ils appartiennent au mode wiki (cf. CLAUDE.md, section *Mode wiki*), et sont vides tant que le contenu v1 n'a pas été remigré.

## Modèle de galaxies (champ frontmatter `galaxie:`)

Toute fiche du brain a un champ `galaxie:` dans son frontmatter (sauf les `SKILL.md`, qui suivent le frontmatter Anthropic strict — pas de champ `galaxie:`) :

| Galaxie | Dossiers | Mode d'écriture |
|---|---|---|
| **`dev`** | `Dev/Services/`, `Dev/Outils/`, `Dev/Patterns/`, `Dev/Rules/` | mode build |
| **`wiki`** | `Wiki/Concepts/`, `Wiki/Outils/`, `Wiki/Workflows/`, `Wiki/Roadmaps/` | mode wiki (+ `Concepts/` via `enrichir-brain`) |
| **`meta`** | docs racine (README, CHANGELOG, INSTALL, CLAUDE*, CONTRIBUTING, Home, Inbox) + `Documentation/`, `AI/design/`, `AI/scripts/` | tout mode |

Le champ permet requêtes `.base` croisées et code couleur du graphe (cf. `Documentation/perso/obsidian-graph.md`).

## Workflow général

L'utilisateur va te demander :

1. **D'ajouter une fiche Service, Outil ou Concept** ("ajoute le service X", "documente Y") → invoque le skill `enrichir-brain` (mode ciblé, cf. `.claude/skills/enrichir-brain/SKILL.md`).
2. **De faire un balayage en fin de conversation** ("mets à jour DevBrain") → `enrichir-brain` en mode balayage : repère tout ce qui mérite une page, draine la file dans `AI/backlog.md`.
3. **De créer un Pattern ou Comparatif** ("compare X et Y", "fais une base pour…") → `enrichir-brain` crée/met à jour `Dev/Patterns/Comparatif - <thème>.base` ou `Pattern - <nom>.md`.
4. **De traiter l'Inbox** ("traite mon inbox") → il n'existe pas encore de skill dédié à `Inbox.md` en v2 (le `process-inbox` v1 n'a pas été porté). Traite manuellement : lis `Inbox.md`, propose une destination par item, demande confirmation, crée la fiche via `enrichir-brain`.
5. **D'enrichir une fiche existante** depuis un article web ou une expérience → **jamais un patch improvisé** : suivre la *Procédure — mode mise à jour* de `.claude/skills/enrichir-brain/SKILL.md`. Une page qui existe a des **consommateurs** (lignes `## Alternatives` des citeurs, comparatifs `.base`, hubs MOC, index) ; la procédure fournit, pour chaque champ modifié, la liste des consommateurs à repropager et la commande qui le vérifie. Modifier un champ sans dérouler cette table est l'origine mesurée des pitchs périmés du vault (constat C1 de `AI/audit/rapports/axe-2-integrite.md`).
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
scaling: single-node | distributed | serverless
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
categorie: <domaine>/<sous-domaine>   # ex: database/admin, devtools/client-api, llm/agent-de-code
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

- `Dev/Services/` **et** `Dev/Outils/` → `<domaine>/<sous-domaine>`, **même vocabulaire de 94 valeurs** : 20 préfixes de tête (`ml`, `llm`, `database`, `data`, `devtools`, `stats`, `compute`, `design`, `storage`, `web`, `automation`, `media`, `ui`, `observability`, `security`, `signal`, `network`, `devops`, `docs`, `math`). Il n'y a **plus** de préfixe `tooling/` : un outil prend le domaine de son **sujet** (DBeaver → `database/admin`, uv → `devtools/paquet`, Aider → `llm/agent-de-code`). Le dossier d'accueil ne détermine pas la catégorie.
- Le domaine se **dérive** de l'arbre D1→D14 de `taxonomie.md`, il ne se choisit pas.
- `Wiki/Concepts/` → `concept/<sous-domaine>` (`data`, `ai`, `ml`, `dl`, `rl`, `ts`, `nlp`, `signal`, `stats`, `math`, `devops`, `llm`)
- `Wiki/Outils/` → `skill/<famille>` (`documents`, `dev-flow`, `code-quality`, `knowledge`, `data`, `meta`) — section vide en v2 tant qu'aucun skill perso n'est documenté

Catégorie qui ne correspond à rien de listé → **demander avant d'inventer**.

### Valeurs autorisées pour `status`

| Périmètre | Valeurs |
|---|---|
| Services / Outils Dev | `actif`, `en-eval`, `abandonne` |

### Corps de la fiche Service/Outil

Sections types (cf. `AI/design/brain-v2.md` §5.1, `Templates/Service-Dev.md`) :

```markdown
# <Nom>

## Pourquoi          (2-3 lignes : ce qu'il fait, sa différence)
## Quand l'utiliser  (bullets)
## Quand NE PAS      (bullets + wikilinks vers alternatives)
## Déploiement & coût (self-host vs managé, prix, scaling — pour les Services)
## Pièges            (pièges connus et retours d'expérience de la brique)
## Alternatives
- [[Dev/Services/X|X]] — reprend le pitch de X
## Liens
```

**Mécanique du pitch (anti-duplication)** : chaque page porte SON `pitch:` dans le frontmatter, écrit une seule fois. La ligne affichée dans la section *Alternatives* d'une autre page, et dans les propositions de `planifier-projet`, est **réinjectée** depuis ce pitch — jamais retapée à la main. `enrichir-brain` synchronise.

**Convention unique de réinjection** (une seule, arbitrée le 2026-09-02 — cf. `AI/design/brain-v2.md` §5.1) :

| Cas | Règle | Exemple |
|---|---|---|
| Cible listée en frontmatter `alternatives:` | la ligne **commence par** le `pitch:` courant de la cible (normalisation : `**` retirés, espaces réduits, casse ignorée) ; **suffixe libre autorisé après** | `- [[Dev/Services/Qdrant\|Qdrant]] — <pitch de Qdrant> — plus simple à self-host ici.` |
| Cible **absente** du frontmatter `alternatives:` | mention de voisinage : ligne libre, **préfixée de `voisin :`** | `- [[Dev/Services/SDV\|SDV]] — voisin : autre nature, synthèse par modèles appris.` |
| Prose comparative à la place du pitch | **interdit** : soit la prose devient le suffixe du cas 1, soit la cible sort de `alternatives:` et passe au cas 2 | — |

**Important** : les **retours d'expérience et bugs rencontrés** vont dans la section `## Pièges` de la fiche Service/Outil concernée. Il n'y a pas de dossier séparé.

| Convention | Format / règle |
|---|---|
| **Entrée d'expérience datée** (`## Pièges`) | `- YYYY-MM-DD — <symptôme> : <correctif>.` — la date distingue le vécu du piège documenté ; sans date, c'est un piège générique |
| **Imputation d'un incident inter-briques** | il s'inscrit **sous la brique qui a porté le correctif**, une seule fois, les autres briques nommées **en clair** dans la ligne. La fiche de l'autre brique **ne le mentionne pas** — une entrée dupliquée devient une seconde chose à synchroniser ; le nom en clair suffit à la retrouver par `grep` |

Exemple d'entrée inter-briques, dans `Dev/Services/Docker.md` (le correctif a porté sur la configuration Docker, WSL2 et le runtime GPU sont nommés) :

```markdown
- 2026-09-02 — GPU invisible du conteneur sous WSL2 (nvidia-container-toolkit) : déclarer
  le runtime NVIDIA côté Docker Desktop, WSL2 ne le propage pas seul.
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

**La politique git n'est pas écrite ici.** Elle vit dans un seul fichier, `.claude/skills/cloturer-brain/SKILL.md`, section *Politique git du vault*. Trois formulations divergentes coexistaient auparavant dans ce document, dans `CLAUDE.md` et dans `enrichir-brain`, dont deux se contredisaient frontalement sur le commit automatique (constat C3 de `AI/audit/rapports/axe-3-skills.md`). Toute écriture dans `Dev/` ou `Wiki/` se clôt en invoquant `cloturer-brain`, y compris une modification faite à la main dans Obsidian.

Exemple de proposition :
```
À commit :
- Dev/Services/Postgres.md (modifié — section Pièges)

Message suggéré :
docs(postgres): ajoute le piege de saturation du pool de connexions
```

## Anti-patterns à éviter

- Inventer un score ou une note si l'utilisateur n'a pas testé (le champ `score` n'existe plus — ne pas le réintroduire).
- Mettre `production` si la doc dit "beta".
- Créer la fiche dans une catégorie improvisée — toujours vérifier `Documentation/general/taxonomie.md`, demander sinon.
- Inventer un tag hors `Documentation/general/tags.md` sans le proposer d'abord.
- Modifier une fiche `status: abandonne` sans demander.
- Réécrire une fiche entière au lieu de patcher la section concernée.
- Modifier un champ d'une fiche existante sans dérouler la *table des effets de bord* de `enrichir-brain` (workflow général, point 5) — un `pitch:` réécrit sans repropager laisse un pitch périmé chez chaque citeur.
- Écrire un retour d'expérience sans date dans `## Pièges`, ou le dupliquer sur les deux briques d'un incident inter-briques.
