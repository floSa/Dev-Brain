---
galaxie: meta
nom: migration-v3
type: gouvernance
created: 2026-09-04
modified: 2026-09-04
status: en-cours
tags: [meta, migration, v3]
---

# Migration v2 → v3 — document pilote

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
| 3 | Déplacement des fichiers, domaine par domaine | `lot-3-arborescence.md` | après lot 2 | — |
| 4 | Recatégorisation des 205 notions | `lot-4-notions.md` | après lot 3 | — |
| 5 | Comparatifs `.base` → pages `.md` | `lot-5-comparatifs.md` | après lot 3 | — |
| 6 | Conversion des fiches au nouveau gabarit | `lot-6-gabarit.md` | après lot 2 | — |
| 7 | Skills et règle de propagation | `lot-7-skills.md` | après lots 2 et 3 | — |
| 8 | Durcissement des règles du validateur | `lot-8-durcissement.md` | en dernier | — |

**Une conversation à la fois, jamais deux en parallèle.** Les fichiers sources de 4, 5 et 6 sont
bien disjoints, mais chaque lot se clôt par `cloturer-brain`, qui régénère `AI/index/` et `MOC/`,
commit et pousse : deux clôtures simultanées se percutent sur les fichiers générés et sur le push.

**Le lot 7 est prioritaire dès que le 3 est fait.** Tant qu'il n'a pas tourné, les skills
suivent encore les règles v2 : toute page ajoutée entre-temps dégrade la structure neuve.

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
| 2026-09-04 | 2 | **Le vault principal portait 24 fichiers « modifiés » qui ne l'étaient pas** — pur bruit CRLF (contenu identique, `git diff --numstat` vide), et il était resté 2 commits derrière `origin/main`. Il bloquait le fast-forward d'intégration. | Résolu par `git add --renormalize .`, sans rien écraser : `git diff` était vide sur les 24 fichiers, vérifié avant. C'est le défaut décrit dans `Documentation/perso/obsidian-graph.md` §5 ; à refaire tel quel s'il revient. |

---

## Décisions restées ouvertes

Elles n'empêchent aucun lot de démarrer, mais elles doivent être tranchées avant le lot 7.

0. **Trois corrections à porter dans `AI/design/brain-v3.md`**, relevées par le lot 2 et sans
   effet sur le travail déjà fait : le vault fait **646** pages sous `Dev/` + `Wiki/` et non 682 ;
   `remplace_par:` était vide sur **293** fiches sur 297 et non 297 sur 297 ; `hosted:` prend
   `managed` sans accent, la spec §5 écrit `managé`.

1. **`MOC/Themes`** (5 pages) — seul consommateur du champ `domaines:`. Les garder comme hubs
   transverses à la racine, ou supprimer le champ ?
2. **Les 18 notions sans domaine évident** — listées en fin d'arborescence. La plupart sont en
   fait faciles (`ORM`, `Migrations de schéma`, `Web scraping`, `Notebooks-as-code`) ; le lot 4
   les propose, floSa tranche.
3. **Les 9 comparatifs sans filtre `categorie`** — leur dossier d'accueil se pose à la main.
4. **Le seuil de promotion à 5 pages** — 28 sous-dossiers. À 4 il en donnerait 34, à 8 il en
   donnerait 12. Choix de confort, révisable au lot 3 sans rien casser d'autre.
5. ~~**Variante « comparatif en un seul fichier »**~~ — **close le 2026-09-04** sans test : le lot 5
   conserve les 47 `.base`. Rouvrable plus tard, elle ne bloque rien.
