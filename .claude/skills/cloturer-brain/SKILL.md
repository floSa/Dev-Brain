---
name: cloturer-brain
description: |
  Use this skill to CLOSE any write into the DevBrain v2 : regenerate the derived
  artefacts, run the validator until green, check divergence with origin/main, then
  commit, push and integrate into main. Triggers: after a capture with
  `enrichir-brain`, or after ANY manual edit under `Dev/` or `Wiki/` — including an
  edit made directly in Obsidian. Idempotent: safe to re-run at any time.
  This is the ONLY place where the vault's git policy is written.
---

# Skill — cloturer-brain

Clôture mécanique du DevBrain v2. Extrait des étapes 8 à 11 du skill `enrichir-brain`,
où elles étaient **dupliquées trois fois** (mode ciblé, mode mise à jour, mode balayage) —
constat C7 de `AI/audit/rapports/axe-3-skills.md`.

Ce skill ne comporte **aucun choix éditorial**. Il ne décide rien sur le contenu : il
régénère, il valide, il intègre. C'est pour cela qu'il est isolé — la partie mécanisable
d'une procédure ne doit pas être noyée dans la partie qui demande du jugement.

## Quand l'utiliser

- **Après une capture** avec `enrichir-brain`, qui se termine en le nommant.
- **Après toute écriture manuelle** dans `Dev/` ou `Wiki/` — y compris une modification
  faite directement dans Obsidian, hors de toute session d'agent. C'est le cas qui n'était
  couvert par rien : le vault pouvait rester des jours avec un index périmé.
- **Après un correctif** appliqué par un agent, avant d'intégrer son travail.

**Idempotent** : relançable autant de fois que voulu, sans dommage. En cas de doute sur
l'état du vault, le lancer est toujours sûr.

## Procédure — quatre étapes, dans cet ordre

### 1. Régénérer les artefacts dérivés

Dans cet ordre, l'index d'abord : les deux suivants le consomment.

```bash
uv run AI/scripts/build_index.py   # brain-index.json + brain-index.md
uv run AI/scripts/build_mocs.py    # pages hub (MOC/)
uv run AI/scripts/build_links.py   # carte des liens (AI/index/liens.md)
```

Fin d'étape vérifiable : `build_links` annonce **0 lien non résolu**. Un lien non résolu
à ce stade est un lien mort que l'étape 2 va confirmer.

### 2. Valider, et corriger jusqu'au vert

```bash
uv run AI/scripts/check_brain.py
```

**Toute violation DURE se corrige, et on relance.** Ne pas clore tant que ce n'est pas
vert. Les avertissements (`[WARN]`) ne bloquent pas : ils décrivent un passif connu et
documenté (domaines sans comparatif, collisions d'alias, couple Dev↔Wiki manquant). Ne pas
les corriger à la volée sous prétexte de faire baisser le compteur — un avertissement se
traite comme un sujet, pas comme un résidu.

Fin d'étape vérifiable : `OK — aucune violation dure`, et un code de retour 0.

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

D'office, sans demander — `check_brain` vert et divergence vérifiée sont les deux
conditions, et elles suffisent.

```bash
git add -A
git commit                                   # Conventional Commits, message en français
git -C <vault-principal> merge --ff-only <branche-courante>
git -C <vault-principal> push origin main
```

**Fast-forward uniquement.** Si la divergence empêche le FF, le signaler — jamais de
`--force`, jamais de `rebase` sans accord explicite. Ne jamais répondre « à toi de
committer / merger » : la clôture fait partie du travail.

Le message de commit dit **pourquoi**, pas seulement quoi : les chiffres avant/après, les
faits vérifiés, les points assumés. Un commit dont le message n'apprend rien à celui qui le
relira dans six mois est un commit à moitié fait.

## Politique git du vault — la seule source

Ce fichier est le **seul endroit** où la politique git du DevBrain est écrite. Les
consignes de `CLAUDE.md` et `CLAUDE-build.md` y renvoient au lieu de la redire : trois
formulations divergentes coexistaient auparavant, dont deux se contredisaient frontalement
(constat C3 de l'axe 3).

- Commit et push **d'office** après clôture verte, sans demander.
- **Jamais** de `--force`, de `push --force-with-lease` ni de `rebase` sans accord explicite
  de l'utilisateur, formulé pour ce cas précis.
- **Jamais** de trailer `Co-Authored-By` : les commits sont attribués à floSa seul.
- Intégration dans `main` en **fast-forward uniquement**.
- Une seule branche vivante à la fois. Les worktrees d'agents se nettoient après intégration.

## Anti-patterns

- Committer sans avoir lu la sortie de `check_brain` — un vert supposé n'est pas un vert.
- Committer après un `git fetch` qui a échoué : la divergence n'a pas été vérifiée.
- Corriger un avertissement souple à la volée pour faire baisser le compteur, au lieu de le
  traiter comme un sujet.
- Régénérer les artefacts dans le désordre : `build_mocs` et `build_links` lisent l'index.
- Utiliser `git checkout -- <fichier>` sur un fichier modifié mais non commité pour annuler
  une sonde : cela le ramène à `HEAD` et détruit le travail en cours. Défaire la sonde par
  l'édition inverse.
- Oublier qu'un fichier **créé et non suivi** n'apparaît ni dans `git diff HEAD` ni dans un
  patch qui en dérive. À l'intégration, compter les trois natures : modifiés, non suivis,
  supprimés.

## Voir aussi

- `enrichir-brain` — la capture, qui se termine en appelant ce skill.
- `AI/audit/rapports/axe-3-skills.md` — les constats C2, C3 et C7 qui ont produit ce découpage.
