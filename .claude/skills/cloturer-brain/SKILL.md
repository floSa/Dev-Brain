---
name: cloturer-brain
description: |
  Use this skill to CLOSE any write into the DevBrain v3: regenerate the derived
  artefacts, run BOTH validators until green, check divergence with origin/main,
  then commit, push and integrate into main. Triggers: after a capture with
  `enrichir-brain`, or after ANY manual edit to a page of the vault — including an
  edit made directly in Obsidian. Idempotent: safe to re-run at any time.
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
  `Métiers/`, `Patterns/`, `Rules/`, `Wiki/Concepts/` — y compris une modification faite
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
refuse d'en pousser un. Activation : `git config core.hooksPath .githooks` (cf. `INSTALL.md`
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

Dans cet ordre, l'index d'abord : les deux suivants le consomment.

```bash
uv run AI/scripts/build_index.py   # brain-index.json + brain-index.md
uv run AI/scripts/build_mocs.py    # zones AUTO des hubs de l'arbre + Métiers/ + MOC/Concepts/
uv run AI/scripts/build_links.py   # carte des liens (AI/index/liens.md)
```

`build_mocs.py` ne remplit pas un dossier `MOC/` : il écrit la zone `<!-- AUTO -->` de chaque
page `role: hub` de l'arbre, les 5 hubs de `Métiers/` (depuis `domaines:`) et, jusqu'au
lot 4, les 10 `MOC/Concepts/`. Le **corps** d'un hub, hors zone AUTO, est écrit à la main :
la régénération ne le touche pas, et ne le répare donc pas non plus.

Fin d'étape vérifiable : `build_links` annonce **0 lien non résolu**. Un lien non résolu à ce
stade est un lien mort que l'étape 2 va confirmer.

### 2. Valider — les DEUX validateurs, et corriger jusqu'au vert

```bash
uv run AI/scripts/check_brain.py   # le contenu : frontmatter, enums, réciprocité, pitchs, liens
uv run AI/scripts/check_arbo.py    # la structure : chemin ↔ categorie, seuil, un hub par dossier
```

Ils ne contrôlent pas la même chose et **aucun ne remplace l'autre**. `check_brain` valide ce
que les pages disent ; `check_arbo` valide qu'elles sont au bon endroit — la règle que le
lot 3 a rendue vérifiable, et qu'une page posée à vue viole sans que `check_brain` s'en
aperçoive.

**Toute violation DURE se corrige, et on relance.** Ne pas clore tant que les deux ne sont
pas verts. Les avertissements (`[WARN]`) ne bloquent pas : ils décrivent un passif connu et
documenté (domaines sans comparatif, `.base` à filtre figé, collisions d'alias, couple
brique↔notion manquant). Ne pas les corriger à la volée sous prétexte de faire baisser le
compteur — un avertissement se traite comme un sujet, pas comme un résidu.

**En revanche, le compte d'avertissements ne doit pas augmenter.** Le relever avant d'écrire
et le comparer après est le seul moyen de voir qu'une écriture a créé une dette souple :

```bash
uv run AI/scripts/check_brain.py 2>&1 | tail -1   # « OK — aucune violation dure. (N avertissement(s)) »
```

Fin d'étape vérifiable : `OK — aucune violation dure` **et** `OK — chemin et catégorie
concordent partout`, avec un code de retour 0 pour les deux.

### 3. Vérifier que la base n'a pas divergé — avant tout commit

```bash
git fetch origin
git log HEAD..origin/main --oneline   # commits distants absents en local
git merge-base HEAD origin/main       # doit renvoyer un ancêtre commun
```

Si `origin/main` porte des commits absents en local, ou si `merge-base` ne trouve **aucun**
ancêtre commun, **s'arrêter et signaler l'écart**. Ne jamais committer ni pousser sur une
base potentiellement obsolète (incident du 2026-07-29 : une session a travaillé des heures
sur un `main` vieux de trois semaines, sur un dépôt republié en snapshot).

**Le `fetch` doit réellement aboutir.** S'il échoue — `could not read Username`,
`expected flush after ref listing` — la vérification de divergence n'a PAS eu lieu, et
l'échec est silencieux si on ne lit pas sa sortie. Passer alors par l'accès qui fonctionne
sur cette machine (cf. `Documentation/perso/machines.md`) et refaire la vérification, plutôt
que de committer sans filet.

### 4. Committer, pousser, intégrer dans `main`

D'office, sans demander — les deux validateurs verts et la divergence vérifiée sont les
conditions, et elles suffisent.

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

**Fast-forward uniquement.** Si la divergence empêche le FF, le signaler — jamais de
`--force`, jamais de `rebase` sans accord explicite. Ne jamais répondre « à toi de
committer / merger » : la clôture fait partie du travail.

Le message de commit dit **pourquoi**, pas seulement quoi : les chiffres avant/après, les
faits vérifiés, les points assumés. Un commit dont le message n'apprend rien à celui qui le
relira dans six mois est un commit à moitié fait.

---

## Politique git du vault — la seule source

Ce fichier est le **seul endroit** où la politique git du DevBrain est écrite, à la seule
exception de la règle d'identité ci-dessus, dupliquée dans `CLAUDE.md` pour la raison qui y
est donnée. Les consignes de `CLAUDE.md` et de `CLAUDE-build.md` renvoient ici au lieu de
redire : trois formulations divergentes coexistaient auparavant, dont deux se contredisaient
frontalement (constat C3 de l'axe 3).

- **Identité** : celle de la config locale du dépôt. Jamais `-c user.email`, jamais `--author`, jamais l'email du harnais. Hooks `.githooks/` activés par `core.hooksPath`.
- Commit et push **d'office** après clôture verte, sans demander.
- **Jamais** de `--force`, de `push --force-with-lease` ni de `rebase` sans accord explicite de l'utilisateur, formulé pour ce cas précis. Une **réécriture d'historique** non plus, y compris pour corriger une identité déjà poussée : c'est une décision de floSa.
- **Jamais** de trailer `Co-Authored-By` : les commits sont attribués à floSa seul.
- **Jamais** de `--no-verify` : les hooks du dépôt portent une règle, pas une gêne.
- Intégration dans `main` en **fast-forward uniquement**.
- Une seule branche vivante à la fois. Les worktrees d'agents se nettoient après intégration.
- **Aucun `rm` sur une page** pendant la migration v3 : un déplacement se fait par `git mv`, qui conserve l'historique. Une suppression se demande.

## Anti-patterns

- Committer sans avoir lu la sortie des validateurs — un vert supposé n'est pas un vert.
- **Ne lancer que `check_brain`** et croire le vault validé : `check_arbo` porte la règle du lot 3, et c'est elle qu'une page mal rangée viole.
- Committer après un `git fetch` qui a échoué : la divergence n'a pas été vérifiée.
- Passer un message de commit multi-lignes en `-m` : les backticks du texte sont exécutés par le shell, et la substitution est silencieuse.
- Contourner un hook avec `--no-verify` au lieu de traiter ce qu'il signale.
- Corriger un avertissement souple à la volée pour faire baisser le compteur, au lieu de le traiter comme un sujet — ou, symétriquement, ne pas voir que le compteur a **augmenté**.
- Régénérer les artefacts dans le désordre : `build_mocs` et `build_links` lisent l'index.
- Éditer une zone `<!-- AUTO -->` de hub à la main : la régénération l'écrase. Le corps du hub, lui, ne se régénère pas — c'est l'inverse qui est vrai, et personne ne le réparera à votre place.
- Utiliser `git checkout -- <fichier>` sur un fichier modifié mais non commité pour annuler une sonde : cela le ramène à `HEAD` et détruit le travail en cours. Défaire la sonde par l'édition inverse.
- Oublier qu'un fichier **créé et non suivi** n'apparaît ni dans `git diff HEAD` ni dans un patch qui en dérive. À l'intégration, compter les trois natures : modifiés, non suivis, supprimés.

## Voir aussi

- `enrichir-brain` — la capture, qui se termine en appelant ce skill. Sa règle de propagation dit **quoi** écrire ; celui-ci dit comment le clore.
- `CLAUDE.md`, section *L'identité git du vault* — la même règle d'identité, là où elle est lue à chaque conversation.
- `AI/audit/rapports/axe-3-skills.md` — les constats C2, C3 et C7 qui ont produit ce découpage.
- `AI/migration/lot-7-skills.md` — le lot qui a écrit cette version.
