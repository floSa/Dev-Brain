---
galaxie: meta
nom: migration-v3
type: gouvernance
created: 2026-09-04
modified: 2026-09-06
status: clos
tags: [meta, migration, v3]
---

# Migration v2 → v3 — document pilote

> [!success] **MIGRATION CLOSE le 2026-09-06.** Les huit lots sont faits. Le vault est en v3 :
> 764 pages dans l'arbre des 20 domaines, `role:` à la place de `galaxie:`/`type:`, les 47
> comparatifs en pages, les 337 fiches au gabarit, les skills à jour, et les dix règles du §10
> écrites et mesurées. `Dev/`, `Wiki/` et `MOC/` n'existent plus.
>
> Ce document reste comme **journal**, pas comme plan. Ce qui a été délibérément **reporté**
> est nommé plus bas, avec son motif — rien n'est laissé ouvert sans décision.

Ce dossier orchestre le passage du DevBrain à la structure v3. **Un lot = une conversation.**
Ce document est le seul à garder l'état d'avancement ; chaque brief est autonome.

Cible : [[AI/design/brain-v3|brain-v3]] · Inventaire et arbre : [[AI/design/v3-arborescence|v3-arborescence]]

---

## Pourquoi une conversation par lot

Le vault fait 646 pages dans `Dev/` et `Wiki/` (mesure corrigée au lot 2). Une seule conversation qui déplacerait les fichiers, réécrirait les
scripts, recatégoriserait 205 notions et convertirait 336 fiches sature son contexte avant la
moitié, et la qualité tombe sans que rien ne le signale.

C'est le schéma qui a fonctionné pour l'audit en six axes : un brief fermé, une conversation
dédiée, un livrable vérifiable, et ce document qui arbitre entre deux lots.

**Règle non négociable** : une conversation ne sort **jamais** du périmètre de son brief. Ce
qu'elle découvre hors périmètre part dans la section *Remontées* de ce document, pas dans son
propre travail.

---

## État d'avancement

| Lot | Objet | Brief | Prêt à lancer | Fait |
|-----|-------|-------|---------------|------|
| 0 | Réglages Obsidian — graphe et propriétés | `lot-0-reglages.md` | oui | **fait le 2026-09-04** |
| 1 | Spec et arborescence | — | — | **fait le 2026-09-04** |
| 2 | `role:` remplace `galaxie:`/`type:` ; nettoyage du frontmatter | `lot-2-role.md` | oui | **fait le 2026-09-04** — 646 pages, validateur vert, 0 lien non résolu. Écarts au brief et pertes assumées : cf. *Remontées* |
| 3 | Déplacement des fichiers, domaine par domaine | `lot-3-arborescence.md` | après lot 2 | **fait le 2026-09-05** — 20 domaines, 682 fichiers déplacés, `Dev/` n'existe plus |
| 4 | Recatégorisation des 205 notions | `lot-4-notions.md` | après lot 3 | **fait le 2026-09-05** — 297 notions rangées, 10 MOC supprimées sur mesure, `Wiki/` et `MOC/` n'existent plus |
| 5 | Comparatifs `.base` → pages `.md` | `lot-5-comparatifs.md` | après lot 3 | **fait le 2026-09-06** — les 47 sont des pages `role: comparatif`, 258 puces toutes sourcées, les 47 `.base` conservés à côté de leur page. Quatre sessions, 27 *Remontées* |
| 6 | Conversion des fiches au nouveau gabarit | `lot-6-gabarit.md` | après lot 2 | **fait le 2026-09-06** — les 337 briques au gabarit v3, 149 → 28 avertissements (les 121 fermés sont tous des R15). **Seul lot mené en parallèle** : un pilote seul, puis 17 conversations simultanées, puis une intégration. Zéro conflit, 20 *Remontées* consolidées dans le journal du brief |
| 7 | Skills et règle de propagation | `lot-7-skills.md` | après lots 2 et 3 | **fait** — `enrichir-brain` et `cloturer-brain` scindés, mode wiki dissous |
| 8 | Durcissement des règles du validateur | `lot-8-durcissement.md` | en dernier | **fait le 2026-09-06** — les dix règles du §10 écrites et mesurées : sept dures, trois en avertissement à motif écrit, **deux réécrites** (5 et 8) parce qu'inatteignables telles qu'elles étaient formulées. R8e comble l'angle mort de R8a, R14b rend visible l'absence de `famille:`. 28 → 111 avertissements, dont 83 par des règles neuves. Hooks git durcis contre `Co-Authored-By`, 25 branches `claude/` supprimées côté origin, `verifier_fraicheur` branché sur les comparatifs. **La migration est close** |

**Une conversation à la fois, jamais deux en parallèle** — sauf sous le protocole du lot 6.
Les fichiers sources de 4, 5 et 6 sont bien disjoints, mais chaque lot se clôt par
`cloturer-brain`, qui régénère `AI/index/`, commit et pousse : deux clôtures simultanées se
percutent sur les fichiers générés et sur le push.

Le lot 6 a levé cette contrainte en **retirant la clôture** des conversations de conversion :
dix-sept branches, six interdits (pas de régénération, pas de `cloturer-brain`, pas de fichier
partagé, un dossier entier par conversation, remontées dans son propre fichier, push sur sa
branche seulement), puis une conversation d'intégration qui régénère et clôt une fois. Résultat
mesuré : 322 fiches, zéro collision, zéro conflit de merge. Le protocole et ses trois manques
sont écrits dans `lot-6-gabarit.md` — il est réutilisable, mais seulement pour un lot qui **ne
déplace ni ne renomme rien**.

~~**Le lot 7 est prioritaire dès que le 3 est fait.**~~ — sans objet, le lot 7 est fait. La
raison reste vraie en général et vaut d'être retenue : tant que les skills suivent d'anciennes
règles, toute page ajoutée entre-temps dégrade la structure neuve.

---

## Comment lancer un lot

1. Vérifier dans le tableau que ses prérequis sont faits.
2. Ouvrir une conversation neuve **dans le dossier du vault**.
3. Coller le prompt qui se trouve en fin de brief. Rien d'autre.
4. À la fin, la conversation clôt avec le skill `cloturer-brain` — c'est lui qui régénère,
   valide, vérifie la divergence et commit.
5. Revenir ici : cocher, et reporter ce qui est remonté.

### Entre deux lots, à vérifier soi-même

```bash
uv run AI/scripts/check_brain.py
git log --oneline -3
git status -sb
```

Le validateur doit être au vert et l'arbre de travail propre avant de lancer le lot suivant.
Si un lot laisse le validateur rouge, on ne passe pas au suivant : on ouvre une conversation
de correction avec le périmètre du lot fautif.

---

## Invariants — vrais pour tous les lots

1. **Un lot par commit**, message conventionnel, jamais de `--force`, jamais de `rebase`.
2. **Vérifier la divergence avec `origin/main` avant tout commit** — `git fetch origin` puis
   `git log HEAD..origin/main --oneline`. La machine de travail peut changer en cours de
   chantier ; un `main` local obsolète est le risque numéro un.
3. **Ne jamais éditer à la main** ce qui est généré : `AI/index/`, les zones `<!-- AUTO -->`.
4. **Ne rien supprimer sans que le contenu soit ailleurs.** Un `git mv` n'est pas une
   suppression ; un `rm` en est une, et aucun lot n'en autorise.
5. **Le validateur au vert en fin de lot**, sans exception ajoutée pour le faire passer.
6. Français, ton impersonnel, phrases courtes, **aucun émoji** — y compris dans les messages
   de commit.

---

## Remontées

Ce qu'une conversation découvre hors de son périmètre s'écrit ici, et **seulement ici**.

| Date | Lot | Constat | Décision |
|------|-----|---------|----------|
| 2026-09-04 | 0 | **Lot 0 clos sur pièces ; vérifications visuelles abandonnées.** Les deux réglages sont constatés dans `.obsidian/app.json` (`AI/index/` dans `userIgnoreFilters`, `propertiesInDocument: "hidden"`) — c'est le fichier qui fait foi, pas l'écran. Le vault réellement ouvert dans Obsidian est la copie WSL `~/Projets/DevBrain`, deux commits en retard au moment du constat. Le test du bloc `base` n'a jamais été exécuté ; le brouillon `_orphans/test-bloc-base.md` a été supprimé. | Aucun lot n'en dépend. Le lot 5 applique la variante prudente : les 47 `.base` sont **conservés**. Décision ouverte n°5 close. |
| 2026-09-04 | 2 | **Le vault fait 646 pages sous `Dev/` + `Wiki/`, pas 682.** Le brief du lot 2 et la spec v3 annoncent 682 « pages du vault » — le compte inclut vraisemblablement les 47 `.base` et les 39 `MOC/`. Aucune conséquence sur le travail. | Chiffre corrigé dans les commits du lot 2. À reprendre dans `brain-v3.md` §1 et dans les briefs suivants s'ils s'appuient dessus. |
| 2026-09-04 | 2 | **`remplace_par:` n'était PAS vide sur 297 fiches sur 297.** 4 fiches le portaient : `Fanalysis` → Prince, `Neptune` → MLflow + W&B, `TorchServe` → BentoML + Triton, `Vanna` → WrenAI + DB-GPT. Vérifié avant suppression : les 7 cibles étaient **déjà** dans l'`alternatives:` de leur fiche **et** nommées dans son corps. | Supprimé sans perte. La mesure « vide sur 297/297 » de `brain-v3.md` §5 et du brief est fausse — le chiffre juste est 293/297. |
| 2026-09-04 | 2 | **`status: en-eval` perd de l'information sur 4 fiches**, non transposée : `Dev/Outils/Maka.md`, `Dev/Outils/swarm-forge.md`, `Dev/Outils/t3code.md` (aucune `maturite:` — le gabarit `outil` n'avait pas le champ) et `Dev/Services/pykan.md` (`maturite: experimental`). `en-eval` décrivait l'état d'évaluation de floSa, pas la maturité du produit : lui donner une `maturite` aurait fabriqué une affirmation sur l'amont. | Non transposé, décision validée par floSa. Le seul report effectué est `Dev/Outils/osint4all.md` (`abandonne` sans `maturite`) → `maturite: deprecated`, fait sourcé par son propre pitch (« sans commit depuis juillet 2022 »). Si floSa veut retenir « je suis en train de l'évaluer », il faudra un champ pour ça — ce n'est pas `maturite`. |
| 2026-09-04 | 2 | **Trois corps de page citent `status:`, champ désormais inexistant** : `Dev/Outils/Maka.md:53`, `Dev/Outils/t3code.md:48`, `Dev/Outils/osint4all.md:54`. Les trois sont dans `## Pièges`. | Volontairement **non corrigées** — le corps est hors périmètre du lot 2, et `## Pièges` est dissoute au lot 6. **Le lot 6 ne doit pas les recopier telles quelles** : elles justifient un choix de champ qui n'existe plus. |
| 2026-09-04 | 2 | **La spec écrit `hosted: [self, managé]`** (§5), avec accent. L'énumération en vigueur porte `managed`, sans accent, sur 10 fiches que le lot ne touche pas. Deux orthographes dans un champ fermé se paient au premier filtre. | `managed` retenu partout. **`AI/design/brain-v3.md` §5 est à corriger** — c'est le seul endroit où `managé` subsiste. |
| 2026-09-04 | 2 | **`Wiki/Outils/Obsidian.md` est classé `role: brique`, contre la lettre du brief** (qui mappait `Wiki/Outils/*` → `notion`). C'est la seule des 646 pages où le dossier et le `type:` divergent. Sa fiche porte un frontmatter de brique (`pitch`, `licence_type`, `os`, `alternatives`, `url_docs`) : la classer `notion` aurait rendu cinq champs hors gabarit, donc obligé à affaiblir le validateur — ce que le brief interdit. | Mapping fait sur `type:` et non sur le dossier. Validé par floSa après relecture du frontmatter. **Le lot 3 doit décider où cette page atterrit** dans l'arborescence par domaine : sa `categorie` est `skill/knowledge`, hors des 20 préfixes de `DOM_LABEL`. |
| 2026-09-04 | 2 | **La règle souple R15 passe de 297 à 337 pages contrôlées** (les ex-`outil` deviennent des briques) : 121 avertissements « aucun lien vers Wiki/Concepts » au lieu de ~102. Le passif grossit avant de se résorber, c'est le prix de la fusion des deux gabarits. | Assumé. Total : 153 avertissements, 0 violation dure. À traiter comme un sujet d'enrichissement, pas comme un résidu de migration. |
| 2026-09-04 | 2 | **`AI/scripts/audit_mesures.py` plante sur une console Windows cp1252** (`UnicodeEncodeError` sur `→`, ligne 262). Défaut **antérieur** au lot 2 — vérifié sur `HEAD~1`, le script n'a jamais eu le garde `sys.stdout.reconfigure` que porte `sync_reservoir.py`. Contournement : `PYTHONIOENCODING=utf-8`. | Non corrigé — hors périmètre, et sans rapport avec la migration. Deux lignes à ajouter quand quelqu'un repassera dessus. |
| 2026-09-04 | 2 | **Les 7 scripts PowerShell de `AI/scripts/` lisent `galaxie`** (`audit-vault.ps1`, `report-ghosts.ps1`, `find-connexes.ps1`, `discover-links.ps1`, `audit-links.ps1`, `add-wikilinks.ps1`, `gen-stubs-batch.ps1`). Ils sont déjà périmés bien au-delà de ce champ : ils ciblent des chemins v1 (`Services/`, `Bugs/`) et des champs v1 (`sous_categories`). | Laissés en l'état, décision de floSa. Ils ne tournent plus depuis la v2 ; les réparer pour `role:` serait réparer un outil mort. À supprimer ou à réécrire, comme sujet propre. |
| 2026-09-04 | 2 | **Le hook Stop mourait à l'installation de ses dépendances** : `uv` pose ses paquets par hardlink depuis son cache, et OneDrive refuse l'opération (`os error 396`). Le résumé de session n'était plus écrit, en silence. | Corrigé hors lot, commit `e068744` : `--link-mode=copy` sur les deux hooks de `.claude/settings.json`. |
| 2026-09-06 | 5 | **Le vault n'a qu'un seul solveur d'optimisation, et c'est ce que `R8b` signale depuis le début.** `Comparatif - Solveurs d'optimisation` a un membre, `PuLP`, dont la fiche nomme onze briques absentes en clair — Pyomo, CVXPY, `scipy.optimize`, CBC, GLPK, HiGHS, SCIP, Gurobi, CPLEX, MOSEK, XPRESS. La conversion en page ne rend PAS l'avertissement silencieux, contrairement à ce que le brief prédisait deux fois : la variante à deux fichiers garde le `.base`, donc garde le contrôle qui porte sur lui. | Hors périmètre du lot 5, qui convertit et ne crée pas de brique. Entrée ouverte dans `AI/backlog-enrichissement-brain.md` avec les onze, leur `categorie:` et une priorité à trois pages (Pyomo, CVXPY, HiGHS) qui éteindraient `R8b`. La page le dit aussi en clair, pour que le lecteur ne prenne pas une puce unique pour une comparaison. |
| 2026-09-06 | 8 | **`ANTHROPIC_API_KEY` n'est pas positionnée sur cette machine, et la moitié « résumé de session » du hook Stop ne produit donc rien.** C'est la cause du trou dans `AI/sessions/`, qui s'arrête au 2026-09-03 alors que les lots 5, 6 et 7 ont tourné depuis. Vérifié en exécutant les deux hooks avec un payload réel : `stop_check_brain.py` tourne et rapporte correctement ; `session_to_devbrain.py` est branché, résout bien le vault, et sort proprement en 0 faute de clé. Ce n'est pas un bug — c'est une configuration absente. | Hors périmètre : la clé est une donnée personnelle, elle va dans `settings.local.json` ou dans l'environnement, et elle appartient à floSa. **Le hook est prêt ; il lui manque une clé.** Tant qu'elle n'est pas posée, `AI/sessions/` reste à écrire à la main en fin de session, comme `CLAUDE.md` le prévoit déjà. |
| 2026-09-06 | 8 | **La décision 6 du lot 6 — « `famille:` devrait être requis, le correctif est d'une ligne » — contredit une décision écrite de `Documentation/general/taxonomie.md`**, qui dit noir sur blanc que `check_brain` « accepte un champ vide : c'est le seul signal prévu pour "l'arbre n'a pas tranché, à arbitrer". Une famille inventée est une faute, un champ vide est une question ouverte. » Rendre le champ requis supprimerait le seul moyen qu'a le vault de dire qu'il ne sait pas, et pousserait à inventer une valeur — ce que la même page interdit. | **Non appliquée telle quelle.** Ce qu'il fallait corriger n'était pas la permissivité mais le SILENCE : une brique sans `famille:` échappait à R14 sans que rien ne le dise. R14b, souple, le dit maintenant. Une seule brique concernée, `Outils de développement/Obsidian.md`. |
| 2026-09-06 | 8 | **Le dépôt local porte 54 branches `claude/` et 27 worktrees encore montés**, dont beaucoup pointent sur des branches d'un lot clos. Côté `origin`, les 25 branches intégrées ont été supprimées après vérification une par une qu'elles sont bien ancêtres de `main` — il ne reste que `main` et la branche du lot 8. | Le nettoyage **local** n'a pas été fait : supprimer une branche encore montée dans un worktree casserait ce worktree, et démonter 27 worktrees n'était pas dans le brief. À faire par floSa quand il veut, avec `git worktree remove` puis `git branch -d` — le `-d` minuscule refusera toute branche non intégrée, ce qui est le garde-fou voulu. |
| 2026-09-06 | 8 | **Quatre entrées mortes dans `.git/worktrees/` ne peuvent pas être élaguées** : chaque `git fetch` et chaque `git commit` affiche « failed to delete … Permission denied » sur `festive-euler-269d34`, `inspiring-vaughan-f64682`, `lot-4-quatre-domaines-bce336` et `nervous-cerf-959102`. Le dossier de travail a disparu, git veut nettoyer la métadonnée, et OneDrive refuse la suppression. Purement cosmétique : aucune commande n'échoue, seule la sortie est polluée. | Non corrigé — c'est un verrou OneDrive, pas un état git. `git worktree prune` une fois les fichiers réellement libérés (OneDrive fermé, ou après redémarrage) suffira. Même famille que le défaut CRLF de `Documentation/perso/obsidian-graph.md` §5 : un artefact du support, pas du dépôt. |
| 2026-09-06 | 8 | **`MOC/` et `Wiki/` existent encore comme dossiers VIDES et non suivis** à la racine de chaque copie du vault. Git ne suit pas les dossiers vides : les `git mv` des lots 3 et 4 ont vidé leur contenu sans que le dossier disparaisse du disque. `check_brain` et `check_arbo` ne s'y trompent pas — `MOC` est dans leur `NON_PAGES` — mais Obsidian les affiche, et un lecteur peut croire la migration inachevée. | Non supprimés : le brief interdit tout `rm` sur le vault pendant la migration, et la règle n'a pas d'exception pour un dossier vide. Six `rmdir` à passer par floSa — les deux dossiers portent encore leurs sous-dossiers vides (`MOC/Concepts`, `Wiki/Concepts`, `Wiki/Outils`, `Wiki/Roadmaps`, `Wiki/Workflows`) —, ce qui lui fera voir du même coup qu'ils sont bien vides : `find MOC Wiki -type f` ne rend rien. |
| 2026-09-04 | 2 | **Le vault principal portait 24 fichiers « modifiés » qui ne l'étaient pas** — pur bruit CRLF (contenu identique, `git diff --numstat` vide), et il était resté 2 commits derrière `origin/main`. Il bloquait le fast-forward d'intégration. | Résolu par `git add --renormalize .`, sans rien écraser : `git diff` était vide sur les 24 fichiers, vérifié avant. C'est le défaut décrit dans `Documentation/perso/obsidian-graph.md` §5 ; à refaire tel quel s'il revient. |

---

## Décisions restées ouvertes — **aucune, au 2026-09-06**

> **Vérifié une par une à la clôture du lot 8.** Les cinq entrées ci-dessous sont toutes
> tranchées ou explicitement reportées avec leur motif. Le titre est conservé pour ne pas
> casser les liens entrants ; la section est désormais un relevé de décisions, pas une file
> d'attente. Ce qui a été **reporté**, et qui est donc la seule chose à savoir pour la suite :
>
> - **Renommer le champ `domaines:`** — reporté sciemment. Le mot « domaine » désigne déjà
>   l'axe de l'arbre ; ce que le champ porte, ce sont les six **métiers**. Le renommer
>   toucherait 374 pages, l'index, `build_mocs.py` et six hubs : une migration à part
>   entière, et celle-ci se clôt ici. La désambiguïsation de vocabulaire, elle, est écrite
>   dans `brain-v3.md` §14, question 1.
> - **Ouvrir le vocabulaire de `## Ressources`** à `Site` et à `Poids` — reporté parce que
>   c'est un arbitrage qui appartient à **floSa**, pas au lot. Cinq pages concernées, la
>   règle R23 reste en avertissement sur cette moitié jusque-là.
> - **Les sept entrées de contenu** versées par le lot 8 à
>   `AI/backlog-enrichissement-brain.md` — cinq comparatifs manquants, onze filtres de vue
>   trop étroits, 89 briques hors de toute vue, 39 champs vides, six `alternatives:`
>   démenties par leur propre fiche, une trentaine de briques nommées mais non fichées, deux
>   notions citant une catégorie disparue. Ce sont des sujets d'enrichissement, pas des
>   décisions en attente.

Elles n'empêchaient aucun lot de démarrer. Elles sont ici pour l'historique.

0. ~~**Trois corrections à porter dans `AI/design/brain-v3.md`**~~ — **closes, vérifiées le
   2026-09-06 dans le fichier** : le compte de 682 ne figure plus dans la spec ; §5 porte
   « vide sur 293 fiches sur 297 (mesure corrigée au lot 2) » ; §5 porte `[self, managed]`
   « sans accent, orthographe de l'énumération en vigueur ».

1. ~~**`MOC/Themes`** (5 pages)~~ — **tranché le 2026-09-05 : gardés.** Descendus à la racine
   dans « Métiers/ », `role: hub`, régénérés depuis `domaines:`. Les deux dettes qu'ils
   laissaient sont tranchées à la clôture du lot 8 : le champ **garde son nom** (renommage
   reporté, motif ci-dessus) et **reste facultatif** sur `role: brique` — 307 des 337 briques
   ne le portent pas, le rendre requis serait un travail de contenu sur 307 fiches.
2. ~~**Les 18 notions sans domaine évident**~~ — **close le 2026-09-05, à la clôture du
   lot 4.** Les 297 notions sont dans l'arbre, les 18 comprises, arbitrées page par page.
   Méthode à retenir : cinq d'entre elles ont d'abord été **remontées** plutôt que déplacées,
   parce qu'elles appelaient un domaine hors du périmètre du lot qui rangeait leur famille ;
   elles sont descendues dans un second passage pris par domaine d'accueil.
3. ~~**Les 9 comparatifs sans filtre `categorie`**~~ — **close.** Les 9 ont été rangés à la
   clôture du lot 3, et le lot 5 a supprimé la question elle-même : une page de comparatif
   porte une `categorie:`, dont `check_arbo` dérive le dossier. Plus aucun dossier ne se
   pose à la main. Le dernier des 9, `Comparatif - Frontends web légers`, garde sa liste de
   cinq noms codée en dur (`R8d`) — mesuré au lot 5 : aucun tag ne capture ces cinq membres
   et rien d'autre, et le motif est désormais écrit dans le `.base` et dans la page.
4. ~~**Le seuil de promotion à 5 pages**~~ — **tranché le 2026-09-04 : il reste à 5**, mais il
   est **plafonné** — un sous-domaine ne se promeut pas s'il ne laisse aucune page au niveau
   du domaine. Le plafond vit dans `arbo.py` à côté du seuil, et a été appliqué
   rétroactivement à `Stockage/Stockage objet/` et `Automatisation no-code/No-code/`.
5. ~~**Variante « comparatif en un seul fichier »**~~ — **close le 2026-09-04** sans test : le lot 5
   conserve les 47 `.base`. Rouvrable plus tard, elle ne bloque rien.
