---
galaxie: meta
nom: lot-7-skills
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 7 — Les skills et la règle de propagation

Effort : **une session**. C'est le lot qui rend la v3 durable : sans lui, la structure est
neuve mais la prochaine page ajoutée la dégrade.

Prérequis : lots 2 et 3 faits. À lancer **avant** de reprendre l'usage normal du vault.

## Contexte

C'est la demande centrale de floSa : quand on ajoute une base de données, tout ce qui doit lui
répondre doit être mis à jour, sans rien oublier.

En v2, c'était impossible à garantir. « Quelles sont les pages connexes ? » n'a **aucune
réponse mécanique** : le skill doit les deviner à partir des tags et de l'index. C'est le
mécanisme derrière le constat de l'audit axe 3 — **sept étapes sur onze** d'`enrichir-brain`
ne laissent aucune trace vérifiable, et les omissions constatées tombent toutes dedans.

La v3 change la donne, parce que le dossier porte désormais le domaine.

## La règle, en une ligne

> **Le rayon de propagation d'une insertion est le dossier d'accueil, plus ses hubs parents.**

Insérer Qdrant dans `Bases de données/Vectoriel/` détermine mécaniquement, sans deviner :

| À mettre à jour | Comment il est trouvé | Qui le fait |
|---|---|---|
| Le hub du dossier | c'est le dossier d'accueil | généré |
| Les hubs parents | remontée de chemin | généré |
| Le comparatif du dossier | le fichier `role: comparatif` du dossier | vue : automatique ; « Ce qui départage » : à écrire |
| La notion du dossier | le fichier `role: notion` du dossier | à écrire |
| Les briques pairs | les autres `role: brique` du dossier | à écrire, réciprocité obligatoire |
| Les pitchs réinjectés | `alternatives:` et `complements:` des pairs | script de resynchronisation |

Le voisinage cesse d'être une intuition : c'est le contenu du dossier.

## Périmètre

- `.claude/skills/enrichir-brain/SKILL.md`
- `.claude/skills/planifier-projet/SKILL.md`
- `.claude/skills/cloturer-brain/SKILL.md`
- `CLAUDE.md`, `CLAUDE-build.md`, `CLAUDE-project.md`
- `Documentation/general/taxonomie.md`, pour le vocabulaire des rôles

**Hors périmètre** : les pages de contenu, les scripts (faits aux lots 2 et 3).

## Procédure

### `enrichir-brain`

Sa procédure d'insertion est réécrite autour de la table ci-dessus. Ce qui était une intention
— « identifier les pages connexes » — devient une **liste fermée et vérifiable** : lister le
dossier d'accueil, remonter les hubs, traiter chaque ligne de la table.

Ajouter une étape finale de contrôle explicite : la conversation énumère ce qu'elle a touché
et le compare au contenu du dossier. Un écart se signale, il ne se tait pas.

La procédure de **mise à jour** d'une page existante suit la même règle : un champ modifié se
propage au dossier, pas au vault entier.

### `planifier-projet`

Trois gains à câbler :

- `famille:` et `langage:` deviennent des critères affichables — « pour fabriquer de la
  donnée : Faker, librairie Python ». C'est la demande explicite de floSa ;
- le tableau `Prendre si / Écarter si` lui donne des critères structurés au lieu de prose à
  interpréter ;
- le **hub de domaine** devient sa porte d'entrée quand il ne connaît pas le nom de la brique
  cherchée.

### `cloturer-brain`

Inchangé dans son principe — il reste le seul endroit où la politique git du vault est écrite.
Il gagne l'appel à `build_bandeau.py` et les nouvelles règles du validateur.

### Les fichiers `CLAUDE*.md`

Purger tout le vocabulaire v2 : `galaxie`, `Dev/`, `Wiki/`, `MOC/`, « mode build », « mode
wiki ». Les trois modes d'entrée de session n'ont plus de sens une fois les galaxies fusionnées
— il reste **deux** usages : enrichir le brain, et l'utiliser depuis un projet.

## Critères d'acceptation

- [ ] `enrichir-brain` porte la table de propagation, et chacune de ses lignes est une étape
      vérifiable.
- [ ] Aucun fichier `CLAUDE*.md` ni skill ne mentionne plus `galaxie`, `Dev/`, `Wiki/`, `MOC/`.
- [ ] `planifier-projet` filtre sur `famille:` et `langage:`.
- [ ] Le vocabulaire des rôles est dans `taxonomie.md`.
- [ ] Un test réel : ajouter une brique dans un dossier peuplé, et vérifier que les pairs, le
      hub, la notion et le comparatif ont bougé.

## Interdictions

- Ne pas laisser deux documents formuler la même règle. La politique git reste dans
  `cloturer-brain` et nulle part ailleurs — c'est la leçon du constat C3 de l'audit axe 3,
  où trois documents se contredisaient.
- Ne pas ajouter de garde-fou qui interdit : ils se contournent. Ajouter des contrôles qui
  **signalent**.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md (surtout §10 et §12) puis AI/migration/lot-7-skills.md.

Réécris les trois skills et les fichiers CLAUDE*.md pour la structure v3, en mettant
la règle de propagation au centre d'enrichir-brain.

Termine par le test réel décrit dans les critères d'acceptation : ajoute une brique
dans un dossier peuplé et montre-moi tout ce qui a bougé autour.
```

---

## Remontées — exécution du lot, 2026-09-05

### 1. Deux interdictions du lot ont été enfreintes sciemment, sur arbitrage de floSa

Le lot posait deux interdictions. Toutes deux ont sauté, et il faut que ce soit écrit ici
plutôt que découvert plus tard comme une négligence.

**« Ne pas laisser deux documents formuler la même règle. »** La règle d'**identité git** est
écrite dans `CLAUDE.md` **et** dans `cloturer-brain`. Raison : `CLAUDE.md` est le seul
document chargé dans **chaque** conversation, au même moment que l'annonce du harnais
(« The user's email address is … »). Une contre-instruction qui arrive au moment où l'agent
va committer arrive après que l'information fausse a été lue. Les deux documents nomment
l'exception et se renvoient l'un à l'autre ; le **reste** de la politique git n'est toujours
écrit qu'à un seul endroit. C'est une exception nommée, pas une dérive.

**« Ne pas ajouter de garde-fou qui interdit : ils se contournent. Ajouter des contrôles qui
signalent. »** floSa a demandé un hook **bloquant**, et l'a motivé : la consigne écrite
existait déjà dans `CLAUDE.md`, et cinq commits ont quand même été signés avec l'adresse pro.
Un contrôle qui signale n'aurait rien changé — au moment où il aurait parlé, le commit
existait. La différence avec l'interdiction du lot est que le dommage ici est
**irréversible sans réécriture d'historique** : une fois poussée, l'adresse est dans les
contributeurs GitHub. L'interdiction du lot visait les garde-fous **structurels**, dont le
contournement ne coûte rien ; celui-ci protège une identité.

L'objection « ils se contournent » a été prise au sérieux plutôt qu'écartée : les trois voies
de contournement ont été **testées**, et les trois sont refusées.

| Voie | Résultat |
|---|---|
| `git -c user.email=…@aosis.net commit` | refusé |
| `git commit --author="… <…@aosis.net>"` | refusé |
| `GIT_AUTHOR_EMAIL=…@aosis.net git commit` | refusé |

`pre-commit` lit `git var GIT_AUTHOR_IDENT` / `GIT_COMMITTER_IDENT`, donc l'identité
**effective** du commit à venir, pas la config. Restent `--no-verify` et un commit fabriqué
ailleurs : c'est ce que couvre `pre-push`, ajouté pour ça — il relit les commits réellement
poussés, et le push est le moment où le dommage devient réel.

### 2. `langage:` n'est pas indexé — le critère d'acceptation n'est atteint qu'à moitié

Le lot demandait que `planifier-projet` **filtre** sur `famille:` **et** `langage:`.

- `famille:` : fait. Le champ est indexé, `query_index.py --famille` existe, le skill l'utilise comme critère.
- `langage:` : **impossible en l'état.** `brain-index.json` porte `alias, alternatives, categorie, complements, domaines, famille, maturite, nom, path, pitch, role, tags`. Pas `langage`.

Le skill a donc été écrit sur ce qui marche : lecture du frontmatter, **bornée aux 2-3
candidates déjà retenues par l'index**, jamais un balayage. Le coût réel est nul (la fiche
retenue est ouverte de toute façon, pour son `## Pièges`), mais le champ ne **filtre** pas —
on ne peut pas demander « les paquets Python de cette catégorie » en une requête.

Le correctif tient en un mot ajouté à `build_index.FIELDS`. Il n'a **pas** été fait : le lot
7 déclare les scripts hors périmètre, et élargir le périmètre sans le dire est exactement ce
qui rend un lot ininspectable. **À trancher** — lot 8, ou un commit isolé de trois lignes.

### 3. `Prendre si / Écarter si` n'existe sur aucune page — c'est le lot 6

Le lot voulait que `planifier-projet` s'appuie sur ce tableau comme critère structuré.
Mesure : **zéro page du vault le porte**. C'est le gabarit `brain-v3.md` §6, et c'est le
**lot 6** qui convertira les fiches, domaine par domaine.

Le skill porte donc les **deux** lectures, avec la date : le tableau après le lot 6, et
`## Quand l'utiliser` / `## Quand NE PAS l'utiliser` aujourd'hui — qui portent déjà les
wikilinks vers les alternatives, donc la règle de fond (une exclusion se justifie **et** nomme
la suite) s'applique dès maintenant. Écrire le skill comme si la section existait aurait été
écrire une fiction utilisable dans zéro cas sur 337.

Même traitement dans `CLAUDE-build.md`, dont la section « corps de la fiche » montre le
découpage actuel avec l'encadré qui annonce le suivant.

### 4. `build_bandeau.py` n'existe pas — l'appel demandé n'a pas pu être ajouté

Le lot demandait que `cloturer-brain` gagne « l'appel à `build_bandeau.py` ». Le script est
listé comme **nouveau** dans `brain-v3.md` §11 : il n'a jamais été écrit. Aucune page ne porte
de bandeau généré, et la règle 9 du validateur (« bandeau à jour ») n'est pas implémentée.

Rien n'a été ajouté à `cloturer-brain` : appeler un script absent aurait fait échouer la
clôture à chaque exécution. À reprendre quand le bandeau existera — probablement avec le
**lot 6**, qui pose le gabarit dont le bandeau est la tête.

### 5. Le test réel a corrigé la table de propagation : P2 ne bouge pas toujours

Insertion de `USearch` dans `Bases de données/Vectoriel/` (11 briques, 1 comparatif, 1 hub),
procédure déroulée telle qu'écrite, puis retrait.

Ce qui a bougé, et ce qui n'a pas bougé :

| Ligne | Fichier | Effet |
|---|---|---|
| P1 | `Vectoriel/Vectoriel.md` | zone AUTO régénérée **et** une ligne ajoutée à la main dans `## Choisir` |
| P2 | `Bases de données/Bases de données.md` | **inchangé, au bit près** |
| P3 | `Comparatif - Bases vectorielles.base` | filtre `categorie` : entrée automatique, 11 → 12 membres |
| P4 | `Wiki/Concepts/Bases de données vectorielles.md` | brique ajoutée aux bibliothèques ANN ; lien retour dans `## Liens` de la brique |
| P5 | Faiss, hnswlib, Annoy, ScaNN | `alternatives:` réciproque + puce `## Alternatives`, des deux côtés |
| P6 | les 4 mêmes | puce commençant par le `pitch:` courant — `[V1]` : 4 `OK`, 0 à traiter |

**P2 n'a pas bougé parce que la zone AUTO d'un hub de domaine liste les sous-hubs, pas les
feuilles.** La table du lot laissait croire l'inverse. C'est le cas type de la « ligne sans
objet » : à déclarer, pas à taire. Le skill porte désormais l'encadré qui l'explique, avec la
mesure, et précise deux choses que le test a rendues visibles : il faut quand même relire le
**corps** du hub parent (il décrit le sous-domaine en une phrase, qui peut vieillir), et si la
brique atterrit **directement** dans le dossier de domaine, P1 et P2 désignent la même page.

Mesures avant / après / après retrait, aucune supposée :

| | avant | après insertion | après retrait |
|---|---|---|---|
| `check_brain` | vert, 149 `[WARN]` | vert, 149 | vert, 149 |
| `check_arbo` | vert | vert | vert |
| `[V1]` vault entier | 20 | 20 | 20 |
| briques indexées | 337 | 338 | 337 |
| liens non résolus | 0 | 0 | 0 |

Après retrait, `git diff --stat 6e09e19` sur `Bases de données/`, `Wiki/`, `MOC/`, `Métiers/`,
`Patterns/` et `Rules/` est **vide** : le vault est identique à la clôture du lot 3. Un cycle
insertion + propagation + retrait est donc **réversible à l'octet près**, et c'est ce qui rend
la règle vérifiable plutôt que promise.

### 6. Le critère « aucune mention de `galaxie`, `Dev/`, `Wiki/`, `MOC/` » est écrit contre la cible, pas contre aujourd'hui

Pris à la lettre, il ne peut pas être atteint tant que le lot 4 n'est pas passé :
`Wiki/Concepts/` (297 notions) et `MOC/Concepts/` (10 MOC, seule porte d'entrée de 30 notions)
**existent**, et un document qui les tairait décrirait un vault qui n'est pas celui-là.

État réel des mentions restantes dans les `CLAUDE*.md` et les trois skills :

| Mention | Occurrences | Nature |
|---|---|---|
| `Wiki/Concepts`, `MOC/Concepts`, les scaffolds `Wiki/` vides | 21 | **dossiers qui existent**, tous datés du lot 4 ou signalés vides |
| `galaxie` / `galaxies` | 9 | **historique** — « `galaxie:` a été supprimé au lot 2 », « les galaxies ont fusionné » |
| `Dev/Services`, `Dev/Outils`, `Dev/` | 4 | **historique** — « `Dev/` n'existe plus », « les anciens `Dev/Services/` », « ce filtre a cassé au lot 3 » |

Aucun document ne décrit plus `Dev/` comme un dossier vivant, ni `galaxie:` comme un champ
courant. Le critère est atteint dans son intention ; sa formulation littérale sera atteinte au
lot 4, sans autre travail que la disparition des deux dossiers.

### 7. Trois modes deviennent deux, et les anciens noms restent acceptés

`brain-v3.md` §12 et le périmètre de ce lot demandaient de purger « mode build » et « mode
wiki ». Fait : `CLAUDE.md` annonce **mode brain** ou **mode projet**.

Ce que le mode « wiki » protégeait n'a pas disparu, il a changé de nature : ce n'est plus un
mode mais une **frontière sur le rôle** — créer une `role: notion` est normal en mode brain,
la **modifier** demande l'accord de floSa. Formuler ça sur le rôle était de toute façon
nécessaire : le mode devait déjà s'excepter lui-même pour `enrichir-brain`, qui écrit brique
et notion du même geste.

Le routeur **accepte « mode build » et « mode wiki »** comme noms d'avant le lot 7 et ne
redemande pas. floSa les a tapés pendant des mois ; lui renvoyer une question pour un
renommage interne aurait été une régression d'usage, pas une clarification.

### 8. Un message de commit multi-lignes passé en `-m` exécute ses backticks

Constaté sur le **premier commit de ce lot**. Le message citait le nom d'une variable git
entre backticks ; le shell les a interprétés, et le commit enregistré portait à la place la
sortie de la commande — une identité et un horodatage. Aucun signal, aucune erreur : le
message était simplement faux.

Corrigé par `--amend -F`, et la règle est écrite là où elle sert : `cloturer-brain`
(procédure, étape 4, et anti-patterns) et `CONTRIBUTING.md`. **Un message de commit se passe
par `-F <fichier>`.**

### 9. Le message de la règle R15 cite un numéro d'étape qui n'existe plus

`check_brain.py` sort, 137 fois, `« le couple Dev<->Wiki de l'étape 6 du skill n'est pas
câblé »` (ligne 470, plus le commentaire ligne 452). Deux choses y sont périmées depuis ce
lot : « Dev<->Wiki » nomme deux galaxies fusionnées au lot 3, et « l'étape 6 » désigne une
étape de la procédure v2 — le câblage brique↔notion est désormais la ligne **P4**, traitée à
l'**étape 7**.

La règle elle-même est juste et son signal reste bon : c'est la formulation qui envoie le
lecteur chercher une étape 6 qui parle de tags. Rien n'a été corrigé — c'est un script, et
les scripts sont hors du périmètre du lot 7, comme pour la remontée 2. Deux chaînes à
reformuler, à joindre au même passage que `langage:` dans l'index.

Sans correctif, le coût est faible mais réel : quelqu'un qui lit un `[WARN] R15` ouvre le
skill et ne trouve pas ce que le message annonce.

## Le lot 7 est clos

Les cinq critères d'acceptation sont traités, un avec une réserve nommée :

- [x] `enrichir-brain` porte la table de propagation, et chacune de ses lignes est une étape vérifiable — plus l'étape 8 de contrôle, qui confronte `git status` au `ls` du dossier.
- [x] Aucun `CLAUDE*.md` ni skill ne décrit `galaxie`, `Dev/`, `Wiki/`, `MOC/` comme courants (cf. remontée 6 pour la lettre du critère).
- [~] `planifier-projet` filtre sur `famille:` — **et lit** `langage:`, qui n'est pas indexé (remontée 2, à trancher).
- [x] Le vocabulaire des rôles est dans `taxonomie.md`, section *Axe `role:`*.
- [x] Test réel fait, mesuré, et retiré (remontée 5).

Reste ouvert et daté : `langage:` dans l'index et les deux chaînes périmées de R15 (remontées 2 et 9) · `Prendre si / Écarter si`, qui
arrive avec le **lot 6** (remontée 3) · `build_bandeau.py`, à écrire avant que
`cloturer-brain` puisse l'appeler (remontée 4) · la formulation littérale du critère de purge,
qui tombera au **lot 4** (remontée 6).
