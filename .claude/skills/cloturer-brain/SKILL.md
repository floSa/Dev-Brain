---
name: cloturer-brain
description: |
  Use this skill to CLOSE any write into the DevBrain v3: regenerate the derived
  artefacts, run BOTH validators until green, check divergence with origin/main,
  then commit, push and integrate into main. Triggers: after a capture with
  `enrichir-brain`, or after ANY manual edit to a page of the vault — including an
  edit made directly in Obsidian. Idempotent: safe to re-run at any time.
  When origin/main moved meanwhile (parallel conversations), unblocks the closure by a
  MERGE COMMIT in the working branch — never rebase, never force.
  This is the ONLY place where the vault's git policy is written, with one stated
  exception: the git IDENTITY rule also lives in CLAUDE.md, because it must be read
  in every conversation.
---

# Skill — cloturer-brain

Clôture mécanique du DevBrain v3. Extrait des étapes 8 à 11 du skill `enrichir-brain`, où
elles étaient **dupliquées trois fois** (mode ciblé, mode mise à jour, mode balayage) —
constat C7 de `AI/audit/rapports/axe-3-skills.md`.

Ce skill ne comporte **aucun choix éditorial**. Il ne décide rien sur le contenu : il
régénère, il valide, il intègre. C'est pour cela qu'il est isolé — la partie mécanisable
d'une procédure ne doit pas être noyée dans la partie qui demande du jugement.

## Quand l'utiliser

- **Après une capture** avec `enrichir-brain`, qui se termine en le nommant.
- **Après toute écriture manuelle** dans une page du vault — l'arbre des 20 domaines,
  `Métiers/`, `Patterns/`, `Rules/` — y compris une modification faite
  directement dans Obsidian, hors de toute session d'agent. C'est le cas qui n'était couvert
  par rien : le vault pouvait rester des jours avec un index périmé.
- **Après un correctif** appliqué par un agent, avant d'intégrer son travail.

**Idempotent** : relançable autant de fois que voulu, sans dommage. En cas de doute sur
l'état du vault, le lancer est toujours sûr.

---

## Avant tout — l'identité git de ce dépôt

**À vérifier une fois, avant le premier commit de la session.** C'est la seule chose de ce
skill qui n'est pas mécanisable, parce qu'elle contredit une information que le harnais
répète à chaque conversation.

```bash
git config --local user.name    # floSa
git config --local user.email   # l'adresse PERSO
```

Le DevBrain est un dépôt **perso** (`git@github.com-perso:floSa/DevBrain.git`). L'identité de
ses commits est celle de la **config locale du dépôt**, et rien d'autre.

Le harnais annonce à chaque conversation une adresse en `@aosis.net`. **C'est l'adresse PRO
de floSa.** Elle l'identifie auprès de l'outil ; elle n'attribue **jamais** un commit d'ici.

- **Ne JAMAIS passer `-c user.email`, `--author`, ni poser `GIT_AUTHOR_EMAIL` / `GIT_COMMITTER_EMAIL`.** Committer nu : git lit la config locale tout seul, et c'est exactement ce qu'on veut.
- **Ne JAMAIS lire l'email annoncé par le harnais pour attribuer un commit.**
- Config locale absente ou douteuse → **s'arrêter et demander**. Ne pas la deviner, ne pas la « réparer » avec l'adresse qu'on a sous la main.

> Pourquoi : une conversation a déjà signé cinq commits avec l'adresse pro. Une fois poussés,
> l'adresse est entrée dans les contributeurs GitHub, d'où elle ne sort pas sans réécriture
> d'historique — et une réécriture d'historique ne se décide pas seule (cf. *Politique git*).

**Garde-fou mécanique**, parce que la consigne écrite n'a pas suffi : `.githooks/pre-commit`
refuse tout commit dont l'auteur ou le committer porte `aosis.net`, et `.githooks/pre-push`
refuse d'en pousser un. Depuis le lot 8, `.githooks/commit-msg` refuse en plus tout message
portant un trailer `Co-Authored-By`, et `pre-push` refuse d'en pousser un — un hook séparé
parce que `pre-commit` tourne avant que git compose le message. Activation : `git config core.hooksPath .githooks` (cf. `INSTALL.md`
§3.5) — **à vérifier sur un clone neuf ou un worktree frais**, sinon les hooks sont là mais
git ne les lit pas :

```bash
git config core.hooksPath        # doit répondre .githooks
```

Un hook qui refuse n'est pas un incident à contourner : c'est la règle qui fonctionne.
**`--no-verify` ne s'utilise pas ici.**

Cette règle est le **seul** morceau de politique git dupliqué hors de ce fichier : elle est
aussi dans `CLAUDE.md`, qui est chargé dans *chaque* conversation, au même moment que
l'annonce du harnais. Une contre-instruction qui arrive après arrive trop tard. Tout le
reste de la politique git n'est écrit qu'**ici**.

---

## Procédure — quatre étapes, dans cet ordre

### 1. Régénérer les artefacts dérivés

Dans cet ordre.

```bash
uv run AI/scripts/build_index.py     # brain-index.json + brain-index.md
uv run AI/scripts/build_mocs.py      # zones AUTO des hubs de l'arbre + Métiers/
uv run AI/scripts/build_bandeau.py   # zones AUTO:BANDEAU des pages, depuis le frontmatter
uv run AI/scripts/build_links.py     # carte des liens (AI/index/liens.md)
```

**L'ordre compte pour un seul couple, mesuré le 2026-10-01 sur 11 permutations des quatre
scripts : `build_links` doit passer APRÈS `build_mocs`.** La carte des liens lit les
wikilinks que `build_mocs` écrit dans les zones AUTO des hubs ; lancée avant, elle est
composée sur des hubs périmés, et une passe laisse `liens.md` faux (les 4 permutations où
links précède mocs donnent un état différent à l'octet ; les 7 autres, le même).
`build_index`, `build_mocs` et `build_bandeau` sont interchangeables entre eux : même état
final après une seule passe. L'ordre ci-dessus n'est donc pas une obligation
d'index-d'abord — l'index n'est consommé par aucun des trois autres — mais il respecte la
seule contrainte, et c'est celui à suivre. Un ordre défait se rattrape : relancer
l'enchaînement une seconde fois converge toujours (mesuré), et `--check` en est le verdict.

`build_bandeau.py` est entré dans cette liste au **lot 8**, et son absence était un trou :
la règle 9 du §10 — « le bandeau concorde avec le frontmatter » — était déclarée durcissable
et n'était exécutée par rien à la clôture. Un `licence_type:` modifié laissait le bandeau
périmé sans qu'aucune étape ne le dise. Le bandeau est une zone générée, exactement comme la
zone AUTO d'un hub : on le régénère, et la règle devient vraie par construction.

`build_mocs.py` ne remplit plus de dossier `MOC/` — il n'en existe plus depuis la clôture du
lot 4. Il écrit la zone `<!-- AUTO -->` de chaque page `role: hub` de l'arbre et les 6 hubs de
`Métiers/` (depuis `domaines:`). Le **corps** d'un hub, hors zone AUTO, est écrit à la main :
la régénération ne le touche pas, et ne le répare donc pas non plus.

Fin d'étape vérifiable : `build_links` annonce **0 lien non résolu**. Un lien non résolu à ce
stade est un lien mort que l'étape 2 va confirmer.

### 2. Valider — les DEUX validateurs, et corriger jusqu'au vert

```bash
uv run AI/scripts/check_brain.py            # le contenu : frontmatter, enums, réciprocité, pitchs, liens
uv run AI/scripts/check_arbo.py             # la structure : chemin ↔ categorie, seuil, un hub par dossier
uv run AI/scripts/build_bandeau.py --check  # les bandeaux : concordance avec le frontmatter (sort 2 sinon)
```

Ils ne contrôlent pas la même chose et **aucun ne remplace l'autre**. `check_brain` valide ce
que les pages disent ; `check_arbo` valide qu'elles sont au bon endroit — la règle que le
lot 3 a rendue vérifiable, et qu'une page posée à vue viole sans que `check_brain` s'en
aperçoive.

**Toute violation DURE se corrige, et on relance.** Ne pas clore tant que les deux ne sont
pas verts. Les avertissements (`[WARN]`) ne bloquent pas : ils décrivent un passif connu et
documenté (voisinage déclaré R20, domaines sans comparatif ou `.base` à filtre figé R8, collisions
d'alias R5, amont divergent, famille vide R14b, taille de fiche, anti-répétition R26, étiquette
`Ressources` hors vocabulaire R23). Le couple brique↔notion n'en fait plus partie : R15 est dure. Ne pas les corriger à la volée sous prétexte de faire baisser le
compteur — un avertissement se traite comme un sujet, pas comme un résidu.

**En revanche, le compte d'avertissements ne doit pas augmenter.** Le relever avant d'écrire
et le comparer après est le seul moyen de voir qu'une écriture a créé une dette souple. **Un compte
ne s'annonce — message de commit, synthèse — que s'il a été mesuré sur l'état précédent** (jamais
recopié d'un message antérieur ni d'un run filtré par `--regle`, dont la ligne finale ne vaut pas
verdict) :

```bash
uv run AI/scripts/check_brain.py 2>&1 | tail -1   # « OK — aucune violation dure. (N avertissement(s)) »
```

Quand la clôture passe par une fusion d'`origin/main`, le compte **mesuré avant d'écrire**
n'est plus la référence de ce qu'on annonce : voir *Clôture bloquée par une divergence*,
§D — le compte s'annonce sur l'état fusionné, avec un plafond calculé.

Fin d'étape vérifiable : `OK — aucune violation dure`, `OK — chemin et catégorie
concordent partout` **et** `OK — tous les bandeaux concordent avec leur frontmatter`, avec un
code de retour 0 pour les trois.

> **Les dix règles du §10 sont dures depuis le lot 8**, à trois exceptions écrites : la
> règle 4 (voisinage déclaré, R20) reste un avertissement par conception ; la moitié
> `Ressources` de la règle 7 (R23) attend un arbitrage de vocabulaire ; la règle 10 (R26)
> n'est pas scriptable. Les motifs sont dans le code, à côté de chaque règle, et les mesures
> dans `AI/migration/lot-8-durcissement.md`. Une violation dure nouvelle sous R15, R18, R19,
> R21, R23 ou R24 n'est donc pas un faux positif à contourner : c'est une écriture
> incomplète.

### 3. Vérifier que la base n'a pas divergé — avant tout commit

```bash
git fetch origin
git log HEAD..origin/main --oneline   # commits distants absents en local
git merge-base HEAD origin/main       # doit renvoyer un ancêtre commun
```

Deux cas, qui ne se traitent pas pareil :

- **`merge-base` ne trouve aucun ancêtre commun** : historiques divergents ou republiés.
  **S'arrêter et signaler l'écart.** Aucune fusion, jamais de `--allow-unrelated-histories` :
  fusionner deux historiques sans racine commune produirait un dépôt qui n'est celui de
  personne (incident du 2026-07-29 : une session a travaillé des heures sur un `main` vieux
  de trois semaines, sur un dépôt republié en snapshot).
- **`origin/main` porte des commits absents en local, avec un ancêtre commun** : une autre
  conversation a poussé pendant qu'on travaillait. C'est le fonctionnement normal de deux
  conversations en parallèle, pas un incident : suivre *Clôture bloquée par une
  divergence*, plus bas. Ne jamais **pousser** sur une base obsolète — c'est la fusion de
  `origin/main` dans la branche, et non le silence, qui rend la base à jour.

**Le `fetch` doit réellement aboutir.** S'il échoue — `could not read Username`,
`expected flush after ref listing` — la vérification de divergence n'a PAS eu lieu, et
l'échec est silencieux si on ne lit pas sa sortie. Passer alors par l'accès qui fonctionne
sur cette machine (cf. `Documentation/perso/machines.md`) et refaire la vérification, plutôt
que de committer sans filet.

### 4. Committer, pousser, intégrer dans `main`

D'office, sans demander — les deux validateurs verts et la divergence vérifiée sont les
conditions, et elles suffisent.

**Les fichiers de vocabulaire partent dans ce même commit** : si la capture a touché `brain.yml`,
`Documentation/general/taxonomie.md` ou `Documentation/general/tags.md`, ils sont commités avec
les pages qui s'en servent — jamais avant seuls, jamais après (cf. *Procédure — nouvelle valeur de
catégorie* dans `enrichir-brain`). `git add -A` les prend déjà ; la règle interdit de les scinder.

```bash
git add -A
git commit -F <fichier-message>              # Conventional Commits, message en français
git -C <vault-principal> merge --ff-only <branche-courante>
git -C <vault-principal> push origin main
```

**Message par fichier (`-F`), pas par `-m`.** Un message multi-lignes passé en `-m` traverse
le shell : les backticks y sont interprétés et remplacent silencieusement un morceau du texte
par la sortie d'une commande. Écrire le message dans un fichier et le passer par `-F` supprime
le problème à la racine.

**Fast-forward uniquement, dans `main`.** Si la divergence empêche le FF, ou si le `push`
est refusé, la branche de travail absorbe `origin/main` par un commit de fusion et on
recommence : voir *Clôture bloquée par une divergence*. Jamais de `--force`, jamais de
`rebase`. Ne jamais répondre « à toi de committer / merger » : la clôture fait partie du
travail.

Le message de commit dit **pourquoi**, pas seulement quoi : les chiffres avant/après, les
faits vérifiés, les points assumés. Un commit dont le message n'apprend rien à celui qui le
relira dans six mois est un commit à moitié fait.

---

## Clôture bloquée par une divergence

**Cas** : à l'étape 3, `git log HEAD..origin/main` n'est pas vide, avec un ancêtre commun.
Une autre conversation a clos avant celle-ci. Le fast-forward est impossible tant que la
branche ne contient pas les commits distants ; on les **intègre dans la branche de travail
par un commit de fusion**, puis `main` avance en fast-forward comme d'habitude. L'historique
déjà poussé n'est jamais réécrit.

**Interdits, ici comme partout** : `rebase`, `--force`, `--force-with-lease`, `--no-verify`,
`-c user.email`, `--author`, un trailer `Co-Authored-By`. La fusion se fait **dans la branche
de travail**, jamais dans le `main` du vault principal. Les hooks (`pre-commit`,
`commit-msg`) tournent sur un commit de fusion comme sur un autre — constaté par trace —
et `pre-push` ne lit que les commits réellement poussés : aucun n'a besoin d'être
contourné, et un refus se traite.

Quand il faut s'arrêter pendant une fusion en cours, la sortie est toujours la même :
`git merge --abort` (la branche retrouve **exactement** son état d'avant, vérifié par SHA),
puis dire où on s'est arrêté et pourquoi. Jamais `git reset --hard`, jamais
`git checkout -- .` pour « repartir de zéro ». Une fusion déjà commitée à un tour
précédent reste dans la branche : elle est de l'histoire locale non poussée, pas un état à défaire.

### A. Constater, et se mettre en état

```bash
git fetch origin                        # doit aboutir : lire la sortie (cf. étape 3)
git log HEAD..origin/main --oneline     # ce que l'autre conversation a poussé
git merge-base HEAD origin/main         # doit renvoyer un SHA — sinon, arrêt (étape 3)
git status --short                      # doit être vide
```

Arbre non propre : **committer d'abord le travail de la conversation** (étape 4, sans
intégrer). Les validateurs sont déjà verts à ce stade, et un commit *local* sur une base
obsolète ne fait aucun dommage : c'est le push qui en ferait.

### B. Fusionner sans commiter

```bash
git merge --no-commit --no-ff origin/main
git -c core.quotepath=off diff --name-only --diff-filter=U     # les fichiers en conflit
git status --short | grep -E '^(DU|UD|AA|AU|UA|DD)'            # conflits de suppression/ajout
```

- `--no-commit` : la régénération part dans **le même** commit de fusion. `--no-ff` : pas de fast-forward silencieux.
- `-c core.quotepath=off` : sans lui, les noms accentués sortent échappés (`"R\303\251seau/…"`) et aucun script ne les ouvre.
- Un conflit de suppression ou d'ajout (`DU`, `UD`, `AA`, `AU`, `UA`) : **arrêt**. Une page supprimée ou renommée d'un côté est une décision éditoriale.
- **Sans conflit non plus, on ne commite pas avant l'étape D.** Une fusion textuellement propre d'un fichier généré peut être fausse : mesuré, `brain-index.json` est sorti « sans conflit » avec `"count": 970` pour 971 pages, les deux côtés ayant écrit la même ligne (970).

### C. Résoudre, famille par famille

Le critère n'est pas « ce qui a l'air facile », c'est **qui écrit le fichier** :

| Famille | Fichiers | Qui l'écrit | Résolution |
|---|---|---|---|
| Entièrement générés | `AI/index/brain-index.json`, `brain-index.md`, `liens.md` | `build_index`, `build_links` | garder un côté (n'importe lequel), **puis régénérer** |
| Zones générées d'un fichier écrit à la main | zone `<!-- AUTO -->` des hubs (hub de chaque dossier, `Métiers/*`, `Comparatifs/Comparatifs.md`) ; zone `<!-- AUTO:BANDEAU -->` des briques | `build_mocs`, `build_bandeau` | **si tous les marqueurs tombent entre les balises** : garder un côté des seuls blocs en conflit, **puis régénérer**. Un marqueur hors balises = corps écrit à la main → dernière ligne du tableau |
| Vocabulaire et compteurs, écrits à la main | `brain.yml`, `Documentation/general/taxonomie.md`, `Documentation/general/tags.md`, `Home.md` | personne d'autre que les conversations | **garder les ajouts des deux côtés**, selon les règles ci-dessous |
| Tout le reste, écrit à la main | corps d'un hub (hors zone), briques, notions, patterns, règles, tout autre fichier de `Documentation/`, `AI/index/fraicheur.json` (écrit par `verifier_fraicheur.py`, hors clôture : rien ne le régénère ici) | — | **s'arrêter et demander** : `git merge --abort` |

**Distinguer zone et corps** — à lancer sur chaque fichier de la deuxième ligne, avant de toucher à quoi que ce soit :

```bash
awk -v F="$f" '/<!-- AUTO(:BANDEAU)?:START -->/{z=1} /<!-- AUTO(:BANDEAU)?:END -->/{z=0}
  /^(<<<<<<<|=======|>>>>>>>)/{print F": ligne "FNR": "(z?"zone":"HORS ZONE")}' "$f"
```

Un seul `HORS ZONE` suffit à ranger le fichier dans la dernière ligne du tableau.

**Garder un côté des seuls blocs en conflit** (côté `HEAD`, la branche) :

```bash
keep_ours() { awk '/^<<<<<<< /{s=1;next} s==1&&/^=======$/{s=2;next} s==2&&/^>>>>>>> /{s=0;next} s!=2{print}' "$1" > "$1.tmp" && mv "$1.tmp" "$1"; }
```

> **Ne pas résoudre un hub par `git checkout --ours -- <hub>`.** Il restitue le fichier
> entier de la branche, et jette au passage les éditions de corps de l'autre côté que git
> avait fusionnées sans conflit (mesuré : une ligne de corps ajoutée par l'autre conversation
> disparaît). Pour les trois fichiers entièrement générés, c'est sans conséquence ; pour un
> hub, ça ne l'est pas. `keep_ours` ne retire que les blocs en conflit.

**Vocabulaire et compteurs — les cinq pièges mesurés :**

1. **Deux ajouts au même endroit** (deux lignes de tableau dans `tags.md` ou `taxonomie.md`, deux blocs YAML sous la même clé dans `brain.yml`) : garder les deux. L'ordre est sans importance.
2. **La ligne « Démarrage » de `tags.md`** est un paragraphe unique de plus de 15 000 caractères : un ajout de chaque côté donne un conflit sur la ligne **entière**, et en garder « les deux côtés » la dupliquerait. Prendre la ligne côté `origin/main`, puis y insérer à la main le segment propre à la branche (`git diff $(git merge-base HEAD origin/main) HEAD -- Documentation/general/tags.md` le donne).
3. **`Home.md` : les lignes `— N briques` sont adjacentes.** Deux conversations sur deux domaines voisins conflictent sur un bloc de deux lignes, bien qu'aucune ne touche la ligne de l'autre. Pour **chaque ligne**, prendre la version du côté qui l'a modifiée. Une même ligne modifiée des deux côtés : recompter depuis le hub du domaine, pas deviner.
4. **Un compteur modifié des deux côtés fusionne sans conflit, et faux.** Les deux côtés ont écrit « 111 » : git y voit un changement identique et garde 111, quand la bonne valeur est base + 2 = 112. Concerne `valeurs_declarees` et `valeurs_portees` (`brain.yml`, bloc `mesure:`), l'en-tête de `taxonomie.md` (« N valeurs sous le bloc `domaine` ») et les compteurs de `Home.md`.
5. **Aucun validateur ne contrôle ces compteurs** : mesuré, une valeur fausse a été commitée avec les trois validateurs verts, et `brainkit mesurer` ne les lit pas. Le contrôle est humain, et il tient en une commande :

   ```bash
   git diff origin/main -- brain.yml Documentation/general/ Home.md
   ```

   **Ce diff ne doit montrer que les ajouts de cette branche**, ligne par ligne : chaque compteur passe de la valeur d'`origin/main` à cette valeur + les incréments propres à la branche, et rien d'autre. Une ligne qui appartient à l'autre conversation, ou un compteur qui n'a pas bougé de la bonne quantité, est une erreur. **Relire ce diff avant de commiter** ; une correction au `sed` qui écrit `\1` suivi d'un chiffre (`\112`) lit `\11` suivi de `2`, et a écrit `12` au lieu de `112` pendant un test — le diff le montrait.

### D. Régénérer, valider, commiter la fusion

```bash
uv run AI/scripts/build_index.py ; uv run AI/scripts/build_mocs.py        # dans l'ordre de l'étape 1 : links en dernier
uv run AI/scripts/build_bandeau.py ; uv run AI/scripts/build_links.py
git grep -nE '^(<<<<<<<|>>>>>>>) ' -- ':!*.base'                           # aucun marqueur de conflit restant
git add -A
uv run AI/scripts/check_brain.py 2>&1 | tail -1
uv run AI/scripts/check_arbo.py 2>&1 | tail -1
uv run AI/scripts/build_bandeau.py --check 2>&1 | tail -1                  # les trois verts, comme à l'étape 2
```

On **régénère toujours après la fusion**, conflit ou non (§B). Les zones générées d'un fichier
sorti en conflit sont réécrites par le script : c'est lui qui rend la résolution vraie, pas
le choix du côté gardé.

**Verts sur chacun des deux parents, rouge sur la fusion = conflit sémantique.** Un
validateur qui échoue après la fusion alors que la branche et `origin/main` passaient
chacun seuls signale une interaction entre les deux apports, que la régénération ne répare pas.
Mesuré : deux conversations ajoutent chacune une brique dans `network/analyse`, qui passe de
3 à 5 pages — le seuil de promotion — sans `libelle` déclaré, d'où `[FAIL]` sur
`check_arbo` et `check_brain`. Choisir de promouvoir le sous-dossier est une décision
éditoriale : **`git merge --abort`, arrêt, demander.**

**Le compte d'avertissements se mesure sur l'état fusionné, et seulement là.** Le compte
de la branche avant fusion décrit un état qui n'existera jamais sur `main` ; l'annoncer
serait annoncer un état faux. Quatre relevés, aucun recopié d'un message de commit :

| | Où | Comment |
|---|---|---|
| `N_base` | la base de la branche, avant d'écrire | déjà relevé au début du travail (étape 2) |
| `N_branche` | la branche, après ses écritures, **avant** la fusion | déjà relevé à l'étape 2 |
| `N_origin` | `origin/main` | checkout jetable : `git worktree add --detach <dossier-jetable> origin/main`, lancer `check_brain.py` dedans, puis `git worktree remove --force <dossier-jetable>` (27 s mesurés) |
| `N_fusion` | l'état fusionné, **après** régénération | `uv run AI/scripts/check_brain.py 2>&1 \| tail -1`, **c'est le seul compte qui s'annonce** |

Verdict : `N_fusion ≤ N_origin + (N_branche − N_base)`. Mesuré : base 152, A seul 154, B
seul 155, fusion 157 ; base 157, 159 et 159, fusion 161 — l'égalité, sur des domaines
différents. **Au-dessus de ce plafond** : les deux apports interagissent (collision d'alias,
voisinage déclaré…) — le dire, **ne pas corriger à la volée**, et traiter comme un sujet. Le
message de fusion porte `N_fusion` et le détail du plafond.

Commiter la fusion — message par fichier, relu en entier :

```bash
git commit -F <fichier-message>        # pas de --no-edit : git composerait son propre message
```

Le message dit : quels fichiers ont conflité, comment chacun a été résolu, les comptes
mesurés. Pas de trailer, identité de la config locale (cf. *Avant tout*).

### E. Intégrer et pousser — la boucle

```bash
git fetch origin ; git log HEAD..origin/main --oneline    # doit être VIDE
git -C <vault-principal> merge --ff-only <branche-courante>
git -C <vault-principal> push origin main
```

- **`git log HEAD..origin/main` non vide** : une autre conversation a poussé pendant la résolution. Un **tour de plus** : retour à B, sur `origin/main` tel qu'il est maintenant. Mesuré : B résout, C pousse, B voit le log non vide et refait B-D, puis intègre.
- **Le `push` est refusé** (`non-fast-forward`) : quelqu'un a poussé entre le `fetch` et le `push`, depuis un autre clone, donc sans que le `main` local du vault bouge. Le `--ff-only` local a déjà avancé `main` : il est alors **devant** `origin/main` de nos commits et **derrière** de ceux de l'autre (« 2 devant, 1 derrière » mesuré). Ce n'est pas à réparer à la main : un tour de plus (B-D) rend la branche descendante de `origin/main` **et** du `main` local, le `--ff-only` suivant passe, le `push` aussi. Jamais `--force`, jamais `git reset` sur le `main` du vault.
- **`--ff-only` refusé alors que `HEAD..origin/main` est vide** : le `main` local du vault porte des commits que ni la branche ni `origin/main` n'ont. Rien à fusionner côté branche : **arrêt, demander.**
- **Au plus trois tours.** Un tour = fetch, fusion, régénération, validation, tentative d'intégration. Si `origin/main` a encore bougé après le troisième : **arrêt, demander.** Rien n'est poussé, la branche porte ses fusions, et le fait que trois conversations poussent en rafale est une information pour floSa, pas une raison d'insister.

### Conversations parallèles

Deux conversations d'enrichissement peuvent clore à quelques minutes d'écart si chacune :

1. **travaille dans son propre worktree**, sur sa propre branche ;
2. **sur un domaine différent de l'autre** — ce qui garde les conflits dans les familles ci-dessus ; deux conversations dans le même dossier se disputent son hub, le voisinage de leurs briques et le seuil de promotion de leurs sous-domaines, et le conflit sémantique de §D n'est alors plus l'exception ;
3. **fait le `git fetch` et la vérification d'ancêtre commun au début** (protocole de session de `CLAUDE.md`) ;
4. **clôt dès qu'elle a terminé, sans attendre l'autre** : l'ordre de clôture ne compte pas, c'est la boucle qui rattrape. Attendre ne réduit pas les conflits, il retarde seulement un travail terminé.

> **Ce que le protocole a été mesuré à tenir** (clone jetable, remote nu local, hooks actifs,
> le 2026-10-01) : deux briques dans deux domaines (seul `liens.md` conflite) ; deux valeurs de
> catégorie et deux tags dans les trois fichiers de vocabulaire (7 fichiers conflictent) ;
> deux éditions du corps d'un même hub (arrêt) ; une troisième branche qui pousse pendant la
> résolution (deux tours) ; deux compteurs adjacents de `Home.md` ; une fusion qui rend
> rouge deux parents verts (arrêt) ; un push refusé après un `--ff-only` réussi (un tour de
> plus). Ce qui n'a **pas** été testé : trois tours sans issue (l'arrêt au troisième),
> un refus de `commit-msg` sur un commit de fusion portant un trailer.

---

## Politique git du vault — la seule source

Ce fichier est le **seul endroit** où la politique git du DevBrain est écrite, à la seule
exception de la règle d'identité ci-dessus, dupliquée dans `CLAUDE.md` pour la raison qui y
est donnée. Les consignes de `CLAUDE.md` et de `CLAUDE-build.md` renvoient ici au lieu de
redire : trois formulations divergentes coexistaient auparavant, dont deux se contredisaient
frontalement (constat C3 de l'axe 3).

- **Identité** : celle de la config locale du dépôt. Jamais `-c user.email`, jamais `--author`, jamais l'email du harnais. Hooks `.githooks/` activés par `core.hooksPath`.
- Commit et push **d'office** après clôture verte, sans demander.
- **Jamais** de `--force`, de `push --force-with-lease` ni de `rebase` sans accord explicite de l'utilisateur, formulé pour ce cas précis. Une **réécriture d'historique** non plus, y compris pour corriger une identité déjà poussée : c'est une décision de floSa. Une divergence avec `origin/main` ne rend rien de cela caduc : elle se traite par un **commit de fusion dans la branche de travail** (*Clôture bloquée par une divergence*), qui n'écrit aucun historique déjà poussé.
- **Jamais** de trailer `Co-Authored-By` : les commits sont attribués à floSa seul. Tenu par `.githooks/commit-msg` et `.githooks/pre-push` depuis le lot 8.
- **Jamais** de `--no-verify` : les hooks du dépôt portent une règle, pas une gêne.
- Intégration dans `main` en **fast-forward uniquement**. La fusion d'`origin/main` se fait dans la **branche de travail**, jamais sur place dans `main` : c'est la branche, déjà fusionnée, qui avance `main` en fast-forward.
- **Une branche par conversation, un worktree par branche.** Plusieurs conversations peuvent vivre en parallèle, sur des domaines différents (*Conversations parallèles*). Les worktrees d'agents se nettoient après intégration.
- **Un déplacement se fait par `git mv`**, qui conserve l'historique — jamais par `rm` + création. Une suppression se demande. L'interdiction absolue de tout `rm`, elle, valait pendant la migration v3, close le 2026-09-06.

## Anti-patterns

- Committer sans avoir lu la sortie des validateurs — un vert supposé n'est pas un vert.
- **Ne lancer que `check_brain`** et croire le vault validé : `check_arbo` porte la règle du lot 3, et c'est elle qu'une page mal rangée viole.
- Committer après un `git fetch` qui a échoué : la divergence n'a pas été vérifiée.
- Passer un message de commit multi-lignes en `-m` : les backticks du texte sont exécutés par le shell, et la substitution est silencieuse.
- Contourner un hook avec `--no-verify` au lieu de traiter ce qu'il signale.
- Corriger un avertissement souple à la volée pour faire baisser le compteur, au lieu de le traiter comme un sujet — ou, symétriquement, ne pas voir que le compteur a **augmenté**.
- Régénérer `build_links` **avant** `build_mocs` : la carte des liens lit les wikilinks que `build_mocs` écrit dans les hubs, et une passe laisse `liens.md` périmé (mesuré). L'ancienne justification — « `build_mocs` et `build_links` lisent l'index » — était fausse depuis le lot 9.
- Après une divergence : commiter la fusion **sans régénérer** parce qu'elle s'est faite sans conflit (le compteur du catalogue sort faux, mesuré) ; résoudre un hub par `git checkout --ours -- <hub>` (les éditions de corps de l'autre côté disparaissent) ; annoncer le compte d'avertissements d'**avant** la fusion ; commiter un compteur fusionné sans avoir relu `git diff origin/main` ; forcer un push refusé au lieu de refaire un tour.
- Éditer une zone `<!-- AUTO -->` de hub à la main : la régénération l'écrase. Le corps du hub, lui, ne se régénère pas — c'est l'inverse qui est vrai, et personne ne le réparera à votre place.
- Utiliser `git checkout -- <fichier>` sur un fichier modifié mais non commité pour annuler une sonde : cela le ramène à `HEAD` et détruit le travail en cours. Défaire la sonde par l'édition inverse.
- Oublier qu'un fichier **créé et non suivi** n'apparaît ni dans `git diff HEAD` ni dans un patch qui en dérive. À l'intégration, compter les trois natures : modifiés, non suivis, supprimés.

## Voir aussi

- `enrichir-brain` — la capture, qui se termine en appelant ce skill. Sa règle de propagation dit **quoi** écrire ; celui-ci dit comment le clore.
- `CLAUDE.md`, section *L'identité git du vault* — la même règle d'identité, là où elle est lue à chaque conversation.
- `AI/audit/rapports/axe-3-skills.md` — les constats C2, C3 et C7 qui ont produit ce découpage.
- `AI/migration/lot-7-skills.md` — le lot qui a écrit cette version.
