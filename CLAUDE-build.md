---
nom: CLAUDE-build
role: gouvernance
created: 2026-05-19
modified: 2026-09-05
tags: [meta, mode-brain]
---

# CLAUDE-build.md — Mode brain du DevBrain

Tu es en mode **BRAIN** : on enrichit le brain. Lecture/écriture légitime sur **l'arbre des
20 domaines** à la racine, `Métiers/`, `Patterns/`, `Rules/`, `Templates/`, `Documentation/`
et `AI/`. Suis ces conventions strictement.

Spec de référence : `AI/design/brain-v3.md` (ce que la v2 a établi et qui reste vrai :
`AI/design/brain-v2.md`).

> **Le nom du mode a changé au lot 7.** « Mode build » et « mode wiki » désignent tous deux
> ce mode-ci : ils séparaient deux galaxies qui ont fusionné au lot 3. Ce qui reste de la
> distinction n'est pas un mode mais une **frontière sur le rôle** — une page `role: notion`
> est la mémoire perso de floSa : la **créer** dans une capture est normal, la **réécrire**
> demande son accord (cf. `CLAUDE.md`).

> **Les zones `<!-- AUTO -->` des hubs, `Métiers/` et `AI/index/` sont
> générées.** Ne pas les éditer à la main : `cloturer-brain` les régénère et écraserait la
> modification. Le **corps** d'un hub, hors zone AUTO, s'écrit à la main — et ne se répare
> donc pas tout seul.

## Deux axes de rangement, et un troisième champ

Une page se range sur **deux axes indépendants**, tous deux à vocabulaire fermé, et porte un
troisième champ qui dit ce qu'elle **est**. Ne jamais choisir ces valeurs à l'intuition :
`Documentation/general/taxonomie.md` porte un arbre de décision déterministe pour chacune.

| Champ | Question | Valeurs |
|---|---|---|
| `categorie:` | **De quoi ça parle** — le domaine | 94 valeurs en 20 préfixes, arbre D1→D14 |
| `famille:` | **Ce que c'est** techniquement | 9 valeurs fermées, arbre F1→F9 |
| `role:` | **Ce que la page est** éditorialement | `brique`, `notion`, `pattern`, `rule`, `hub` |

**Le dossier ne se choisit pas : il se dérive de `categorie:`.** `AI/scripts/arbo.py` porte la
dérivation, `check_arbo.py` la vérifie, et une page posée « là où ça semble logique » fait
échouer le validateur. Un sous-dossier apparaît dès qu'un sous-domaine atteint 5 pages, sauf
s'il ne laisserait aucune page au niveau du domaine.

## Modèle de rôles (champ frontmatter `role:`)

`role:` a remplacé `galaxie:` et `type:` au lot 2 : le premier ne servait qu'à la couleur du
graphe, le second ne décrivait que le dossier d'accueil (57 fiches de nature identique étaient
réparties 34 `outil` / 23 `service`, sans discriminant). Les `SKILL.md` suivent le frontmatter
Anthropic strict — pas de champ `role:`.

| `role:` | Ce que c'est | Où | Mode d'écriture |
|---|---|---|---|
| **`brique`** | ce qu'on déploie ou importe : service, outil, librairie | `<Dossier>/<Nom>.md`, dérivé de `categorie:` | à la main |
| **`notion`** | ce qu'il faut comprendre : définitions, maths, mécanismes | `<Dossier>/<Nom>.md`, dérivé de `categorie:` — **le même dossier qu'une brique** | à la main, création libre / modification sur accord |
| **`pattern`** | une architecture éprouvée | `Patterns/Pattern - <nom>.md` | à la main |
| **`rule`** | une règle transverse | `Rules/Rule - <nom>.md` | à la main |
| **`hub`** | la page d'un dossier, l'aiguillage | `<Dossier>/<Dossier>.md` + les 6 de `Métiers/` | corps à la main, **zone AUTO générée** |
| **`comparatif`** | ce qui départage plusieurs briques | aucune page encore — arrive au **lot 5**, les comparatifs sont des `.base` | — |

`role: hub`, `pattern` et `rule` ne portent **pas** de `categorie:`, et c'est délibéré : un hub
*est* le rangement (son domaine est son chemin), un pattern enjambe plusieurs domaines par
construction, une règle est transverse par définition. C'est `role:` qui les groupe.

Les pages de gouvernance (docs racine, `Documentation/`, `AI/`) n'ont pas de `role:` de brain :
elles ne sont pas des pages du brain, et le validateur ne les contrôle pas.

## Workflow général

L'utilisateur va te demander :

1. **D'ajouter une brique ou une notion** (« ajoute le service X », « documente Y ») → invoque le skill `enrichir-brain` (mode ciblé). **Il porte la règle de propagation** : le rayon d'une insertion est le dossier d'accueil plus ses hubs parents, et la table P1→P6 nomme tout ce qui doit bouger autour.
2. **De faire un balayage en fin de conversation** (« mets à jour DevBrain ») → `enrichir-brain` en mode balayage : repère tout ce qui mérite une page, draine la file dans `AI/backlog.md`.
3. **De créer un Pattern ou un Comparatif** (« compare X et Y », « fais une base pour… ») → `enrichir-brain` crée/met à jour `<Dossier>/Comparatif - <thème>.base` (**dans le dossier de ses membres**) ou `Patterns/Pattern - <nom>.md`.
4. **De traiter l'Inbox** (« traite mon inbox ») → il n'existe pas de skill dédié à `Inbox.md` (le `process-inbox` v1 n'a pas été porté). Traite manuellement : lis `Inbox.md`, propose une destination par item, demande confirmation, crée la fiche via `enrichir-brain`.
5. **D'enrichir une fiche existante** depuis un article web ou une expérience → **jamais un patch improvisé** : suivre la *Procédure — mode mise à jour* de `.claude/skills/enrichir-brain/SKILL.md`. Une page qui existe a des **consommateurs** (lignes `## Alternatives` des citeurs, comparatifs `.base`, zones AUTO des hubs, index) ; la procédure fournit, pour chaque champ modifié, la liste des consommateurs à repropager et la commande qui le vérifie. Modifier un champ sans dérouler cette table est l'origine mesurée des pitchs périmés du vault (constat C1 de `AI/audit/rapports/axe-2-integrite.md`).
6. **De refactorer une partie du brain** (« réorganise X », « audite Y ») → opération en lot ; `AI/scripts/check_brain.py`, `check_arbo.py` et `audit-vault.ps1` peuvent aider.

**Toute écriture se clôt par `cloturer-brain`** — y compris une modification faite à la main
dans Obsidian.

## Conventions de fiche `role: brique` (strictes)

Une brique va dans le dossier que sa `categorie:` désigne : `<Dossier>/<Nom>.md`. Pour
connaître ce dossier, ne pas deviner — dériver (cf. `enrichir-brain`, *Trouver le dossier
d'accueil*).

### Champs du frontmatter

**Un seul gabarit.** Les anciens `Dev/Services/` et `Dev/Outils/` avaient deux jeux de champs ;
le lot 2 les a fusionnés en `role: brique`, et `check_brain.py` n'applique plus qu'une liste —
l'union des deux (`os` et `domaines` venaient d'`outil` ; `hosted`, `scaling` et `maturite` de
`service`).

```yaml
---
role: brique
nom: <Nom>                            # identique au nom du fichier (R9)
alias: []
pitch: "<une ligne, réutilisée dans les Alternatives des autres pages et par planifier-projet>"
categorie: <domaine>/<sous-domaine>   # cf. taxonomie.md, arbre D1→D14 — décide du DOSSIER
famille: <nature>                     # 9 valeurs fermées, arbre F1→F9
domaines: [<data-sci, data-eng, mlops, ml-eng, ai-eng>]   # cf. themes.md — alimente Métiers/
licence_type: open-source | source-available | proprietary | open-core
maturite: production | beta | experimental | deprecated
langage: <langage d'implémentation>
os: "Windows, macOS, Linux"           # si la brique s'installe sur un poste
# hosted et scaling : SEULEMENT si famille ∈ {plateforme, saas, application}.
# Une bibliothèque ne s'héberge pas — le validateur refuse le champ (R16).
# hosted: [self, managed]             # LISTE, jamais un scalaire
# scaling: single-node | distributed | serverless
alternatives: ["[[X]]", ...]          # ce qui s'utilise À LA PLACE — liens NUS
complements: []                       # ce qui s'utilise AVEC
tags: [...]                           # pioche dans Documentation/general/tags.md, jamais inventé
url_docs:
url_repo:
---
```

Champs **requis non vides** : `role`, `nom`, `pitch`, `categorie`. Tout champ **hors de la
liste ci-dessus** fait échouer le validateur en dur (R3).

> **Champs volontairement absents** (v1 → v2) : `score`, `mes_projets`, `sous_categories`, `licence` (SPDX), `clients_officiels`, `plateforme`, `remplace`, `url_officiel`, `created`/`modified`. Décision actée dans `AI/design/brain-v2.md` §5.1/§11 : ces champs n'étaient jamais fiables (jamais remplis, ou mentaient). Ne les recrée pas.
>
> **Champs supprimés au lot 2 de la v3** : `galaxie`, `type` (→ `role`), `status` (redondant avec `maturite` : 272 fiches sur 336 étaient `actif` + `production`), `remplace_par` (vide sur 293 des 297 fiches ; les 4 restantes portaient déjà leurs cibles dans `alternatives:`). Ne les recrée pas non plus.

### Taxonomie autorisée pour `categorie`

Voir **`Documentation/general/taxonomie.md`** — c'est la source de vérité, ne la duplique pas
ici de mémoire.

- Toute brique, quelle que soit sa nature : `<domaine>/<sous-domaine>`, **un seul vocabulaire de 94 valeurs**, 20 préfixes de tête (`ml`, `llm`, `database`, `data`, `devtools`, `stats`, `compute`, `design`, `storage`, `web`, `automation`, `media`, `ui`, `observability`, `security`, `signal`, `network`, `devops`, `docs`, `math`). Il n'y a **pas** de préfixe `tooling/` : un outil prend le domaine de son **sujet** (DBeaver → `database/admin`, uv → `devtools/paquet`, Aider → `llm/agent-de-code`).
- Le domaine se **dérive** de l'arbre D1→D14, il ne se choisit pas. Le dossier se dérive du domaine.
- `role: notion` → **le même vocabulaire de domaine qu'une brique**, sans exception. Les douze valeurs `concept/*` de la galaxie wiki sont sorties du vocabulaire le 2026-09-05, à la clôture du lot 4 : `taxonomie.md` en garde le journal, pas la liste. Une notion se range donc comme une brique, et souvent dans son dossier.

Catégorie qui ne correspond à rien de listé → **demander avant d'inventer**. Une nouvelle
famille se pose dans `taxonomie.md`, pas dans l'arborescence.

### Valeurs autorisées pour `maturite`

`production`, `beta`, `experimental`, `deprecated` — sur `role: brique` seulement.

`maturite:` porte **seul** le fait qu'une brique est morte depuis la suppression de `status:`.
`deprecated` est éliminatoire : `planifier-projet` ne propose pas une brique qui le porte, et
`verifier_fraicheur.py` signale toute brique `deprecated` sans `alternatives:`.

### Corps de la fiche brique

Sections types (cf. `AI/design/brain-v3.md` §6, `Templates/Service-Dev.md`) :

```markdown
# <Nom>

## Pourquoi          (2-3 lignes : ce qu'il fait, sa différence)
## Quand l'utiliser  (bullets)
## Quand NE PAS      (bullets + wikilinks vers alternatives)
## Déploiement & coût (self-host vs managé, prix, scaling — si la brique s'héberge)
## Pièges            (pièges connus et retours d'expérience de la brique)
## Alternatives
- [[X]] — reprend le pitch de X
## Liens
```

> Le gabarit v3 (§6) remplace `Quand l'utiliser` / `Quand NE PAS` par un tableau
> `## Prendre si / Écarter si`, dont chaque cellule d'exclusion porte un wikilink. **Aucune
> fiche ne le porte encore** : c'est le **lot 6** qui convertira les fiches, domaine par
> domaine. Écrire une fiche neuve dans l'ancien découpage reste donc la norme aujourd'hui.

**Mécanique du pitch (anti-duplication)** : chaque page porte SON `pitch:` dans le
frontmatter, écrit une seule fois. La ligne affichée dans la section *Alternatives* d'une
autre page, et dans les propositions de `planifier-projet`, est **réinjectée** depuis ce
pitch — jamais retapée à la main. `enrichir-brain` synchronise.

**Convention unique de réinjection** (arbitrée le 2026-09-02 — cf. `AI/design/brain-v2.md` §5.1) :

| Cas | Règle | Exemple |
|---|---|---|
| Cible listée en frontmatter `alternatives:` | la ligne **commence par** le `pitch:` courant de la cible (normalisation : `**` retirés, espaces réduits, casse ignorée) ; **suffixe libre autorisé après** | `- [[Qdrant]] — <pitch de Qdrant> — plus simple à self-host ici.` |
| Cible **absente** du frontmatter `alternatives:` | mention de voisinage : ligne libre, **préfixée de `voisin :`** | `- [[SDV]] — voisin : autre nature, synthèse par modèles appris.` |
| Prose comparative à la place du pitch | **interdit** : soit la prose devient le suffixe du cas 1, soit la cible sort de `alternatives:` et passe au cas 2 | — |

**Wikilinks nus, toujours** : `[[Qdrant]]`, jamais `[[Bases de données/Vectoriel/Qdrant|Qdrant]]`.
Le pipe ne sert qu'à changer le texte affiché. Un lien qualifié porte un chemin, donc casse au
déplacement — le lot 3 a déplacé 682 fichiers sans toucher un seul lien, et les lots 4 à 6 en
déplaceront encore. Contrepartie : **vérifier que le nom de fichier d'une page neuve est
unique dans le vault**, à la casse près.

**Important** : les **retours d'expérience et bugs rencontrés** vont dans la section
`## Pièges` de la fiche concernée. Il n'y a pas de dossier séparé.

| Convention | Format / règle |
|---|---|
| **Entrée d'expérience datée** (`## Pièges`) | `- YYYY-MM-DD — <symptôme> : <correctif>.` — la date distingue le vécu du piège documenté ; sans date, c'est un piège générique |
| **Imputation d'un incident inter-briques** | il s'inscrit **sous la brique qui a porté le correctif**, une seule fois, les autres briques nommées **en clair** dans la ligne. La fiche de l'autre brique **ne le mentionne pas** — une entrée dupliquée devient une seconde chose à synchroniser ; le nom en clair suffit à la retrouver par `grep` |

Exemple d'entrée inter-briques, dans `DevOps/Docker.md` (le correctif a porté sur la
configuration Docker, WSL2 et le runtime GPU sont nommés) :

```markdown
- 2026-09-02 — GPU invisible du conteneur sous WSL2 (nvidia-container-toolkit) : déclarer
  le runtime NVIDIA côté Docker Desktop, WSL2 ne le propage pas seul.
```

## Conventions Comparatifs (`.base`)

Un comparatif vit **dans le dossier de ses membres** : `<Dossier>/Comparatif - <thème>.base`.
C'est ce qui le rend trouvable par `ls`, et c'est la ligne P3 de la règle de propagation.

```yaml
filters:
  and:
    - categorie == "<categorie>"
views:
  - type: table
    name: "<titre>"
    order: [file.name, pitch, hosted, licence_type, maturite, alternatives]
```

**Filtrer par `categorie`, pas par chemin ni par liste de noms.** Un filtre
`file.path.startsWith("Dev/Services/")` a cassé au lot 3 ; une liste de noms codée en dur
signifie qu'une brique qui entre dans le thème **n'entrera jamais** dans la vue
(`check_brain` le sort en `[WARN] R8d`). Un comparatif doit garder **≥ 2 membres** (`R8b`).

## Conventions Patterns (`Patterns/`)

Un pattern architectural opinionné : `Patterns/Pattern - <nom>.md`.

```yaml
---
role: pattern
contexte: <quand l'appliquer>
services_cles: ["[[A]]", "[[B]]"]
tags: [pattern, ...]
---
```

Champs autorisés : `role`, `tags`, `contexte`, `services_cles`, `projets_appliques`. **Pas de
`nom:` ni de `categorie:`** — un pattern enjambe plusieurs domaines.
Corps : Contexte → Décisions clés → Stack récap → Pièges → Voir aussi.

## Conventions Rules (`Rules/`)

Une règle = un fichier `Rules/Rule - <nom>.md`.

```yaml
---
role: rule
domaine: <git | docs | tests | code-style | security | logging | dependencies | ...>
applicable: global | type-cli | type-web | stack-python-fastapi
strictness: must | should | nice-to-have
tags: [rule, ...]
---
```

Champs autorisés : `role`, `tags`, `domaine`, `applicable`, `strictness`. **Pas de `nom:` ni
de `categorie:`** — une règle est transverse par définition. Attention : `domaine:` (au
singulier) est ici le sujet de la règle, pas un domaine de l'arbre.
Corps : Principe (1 phrase) → MUST → SHOULD → NICE-TO-HAVE → Exemples (bon/mauvais) →
Exceptions → Voir aussi.

## Conventions Hubs (`role: hub`)

Tout dossier de l'arbre porte une page à son nom, plus les 5 de `Métiers/`.

```yaml
---
role: hub
nom: <Nom du dossier>
pitch: <une ligne — de quoi parle ce dossier>
domaines: [...]                       # facultatif
---
```

Champs autorisés : `role`, `nom`, `alias`, `pitch`, `domaines`, `tags`. **Pas de
`categorie:`** — un hub ne se range pas, il *est* le rangement.

Corps : `## Ce qu'il faut comprendre` et `## Choisir`, **écrits à la main**, puis la zone
`<!-- AUTO:START -->` / `<!-- AUTO:END -->`, **générée** par `build_mocs.py` depuis le
contenu du dossier. Le budget d'écriture d'un hub suit les **confusions à lever**, pas le
nombre de pages.

## Conventions `role: notion`

```yaml
---
role: notion
nom: <Nom>
alias: []
categorie: <domaine>/<sous-domaine>
domaines: [<data-sci, data-eng, mlops, ml-eng, ai-eng>]
tags: [...]
---
```

Champs autorisés : `role`, `nom`, `alias`, `categorie`, `domaines`, `tags` — et rien d'autre.
Requis non vides : `role`, `nom`, `categorie`, `domaines`.

Corps (ton impersonnel, technique vulgarisé — cf. `AI/design/brain-v3.md` §7,
`Templates/Concept-Wiki.md`) : Aperçu → Concepts clés → Les maths, simplement (si pertinent) →
En pratique → Approches voisines & alternatives → Pour aller plus loin.

Emplacement : `<Dossier>/<Nom>.md`, où `<Dossier>` se **dérive** de `categorie:` comme pour
une brique — le plus souvent le dossier où vivent déjà les briques du sujet. Aucun dossier à
choisir, aucun sous-dossier à créer : `AI/scripts/arbo.py` calcule le chemin, `check_arbo.py`
le vérifie.

## Workflow d'ajout depuis l'Inbox

`Inbox.md` à la racine, format checkboxes `- [ ]` avec hints de type (`brique`, `concept`,
`pattern`…). Aucun skill ne l'automatise (cf. Workflow général, point 4) — traiter
manuellement en attendant.

## Workflow d'ajout depuis URL

Si l'utilisateur fournit une URL : utilise le skill `defuddle` (kepano) pour extraire le
contenu propre, puis lance `enrichir-brain` sur le contenu extrait.

## Mémoire de session

À la fin de chaque session, écris dans `AI/sessions/YYYY-MM-DD-HHmm-brain.md` :
- Pages ajoutées/modifiées (chemin)
- Décisions de catégorisation
- À reprendre

(Idéalement automatisé par hook Stop — voir `AI/scripts/session_to_devbrain.py`.)

## Git

**La politique git n'est pas écrite ici.** Elle vit dans un seul fichier,
`.claude/skills/cloturer-brain/SKILL.md`, section *Politique git du vault*. Trois formulations
divergentes coexistaient auparavant dans ce document, dans `CLAUDE.md` et dans
`enrichir-brain`, dont deux se contredisaient frontalement sur le commit automatique (constat
C3 de `AI/audit/rapports/axe-3-skills.md`). Toute écriture dans une page du brain se clôt en
invoquant `cloturer-brain`, y compris une modification faite à la main dans Obsidian.

**Une seule exception, et elle est nommée** : la règle d'**identité git** est aussi dans
`CLAUDE.md`, parce qu'elle doit être lue à chaque conversation, au même moment que l'annonce
du harnais. L'identité de ce dépôt est celle de sa config locale — jamais `-c user.email`,
jamais `--author`, jamais l'email annoncé par le harnais.

## Anti-patterns à éviter

- **Poser un fichier « là où ça semble logique »** au lieu de dériver son dossier de `categorie:` — `check_arbo.py` le refuse, et il le fait après coup.
- **Écrire une brique sans dérouler la table P1→P6** de `enrichir-brain` : le hub, le comparatif, la notion et les pairs du dossier ne se mettent pas à jour tout seuls, et une insertion sans propagation dégrade la structure au lieu de l'enrichir.
- **Éditer une zone `<!-- AUTO -->`** de hub à la main : la clôture l'écrase.
- Inventer un score ou une note (le champ `score` n'existe plus — ne pas le réintroduire).
- Mettre `production` si la doc dit « beta ».
- Créer la fiche dans une catégorie improvisée — toujours vérifier `taxonomie.md`, demander sinon.
- Inventer un tag hors `Documentation/general/tags.md` sans le proposer d'abord.
- Écrire un wikilink qualifié par chemin : il casse au prochain `git mv`.
- Créer un comparatif filtré par chemin ou par liste de noms codée en dur.
- Modifier une fiche `maturite: deprecated` sans demander.
- Réécrire une fiche entière au lieu de patcher la section concernée.
- Réécrire une `role: notion` existante sans que floSa l'ait demandé.
- Modifier un champ d'une fiche existante sans dérouler la *table des effets de bord* de `enrichir-brain` (workflow général, point 5) — un `pitch:` réécrit sans repropager laisse un pitch périmé chez chaque citeur.
- Écrire un retour d'expérience sans date dans `## Pièges`, ou le dupliquer sur les deux briques d'un incident inter-briques.
- Supprimer une page : pendant la migration v3, **aucun `rm`** — un déplacement se fait par `git mv`, une suppression se demande.
