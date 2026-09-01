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

Le vault fait 682 pages. Une seule conversation qui déplacerait les fichiers, réécrirait les
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
| 0 | Réglages Obsidian — graphe et propriétés | `lot-0-reglages.md` | oui | **appliqué le 2026-09-04** — vérifications visuelles et test `base` en attente d'une ouverture du vault dans Obsidian (cf. *Remontées*) |
| 1 | Spec et arborescence | — | — | **fait le 2026-09-04** |
| 2 | `role:` remplace `galaxie:`/`type:` ; nettoyage du frontmatter | `lot-2-role.md` | après validation de la spec | — |
| 3 | Déplacement des fichiers, domaine par domaine | `lot-3-arborescence.md` | après lot 2 | — |
| 4 | Recatégorisation des 205 notions | `lot-4-notions.md` | après lot 3 | — |
| 5 | Comparatifs `.base` → pages `.md` | `lot-5-comparatifs.md` | après lot 3 | — |
| 6 | Conversion des fiches au nouveau gabarit | `lot-6-gabarit.md` | après lot 2 | — |
| 7 | Skills et règle de propagation | `lot-7-skills.md` | après lots 2 et 3 | — |
| 8 | Durcissement des règles du validateur | `lot-8-durcissement.md` | en dernier | — |

Les lots 5 et 6 peuvent tourner en parallèle du 4 : ils ne touchent pas les mêmes fichiers.
Le 3 doit être seul — il déplace tout.

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
| 2026-09-04 | 0 | **Test du bloc de code `base` non exécuté.** Il demande de constater un rendu dans Obsidian ; la conversation tourne sous WSL, sans interface graphique. Brouillon prêt et laissé en place : `_orphans/test-bloc-base.md` (gitignoré), il porte la requête de `Comparatif - Bases vectorielles.base` dans un bloc ```` ```base ````. | Le lot 5 garde l'hypothèse prudente — les 47 `.base` sont **conservés**. À rouvrir si le tableau s'affiche : voir la décision ouverte n°5. Supprimer le brouillon après lecture. |
| 2026-09-04 | 0 | **Aucun Obsidian ne pointe sur ce vault.** Le registre Windows (`AppData/Roaming/obsidian/obsidian.json`) référence `C:\Users\FlorianHorellou\Documents\Projets\DevBrain`, chemin disparu, dernière ouverture le 2026-05-21. Ce `.obsidian/` n'a ni `appearance.json` ni `workspace.json` : il n'a jamais été ouvert par l'application. | Les deux réglages du lot 0 sont écrits dans `.obsidian/app.json` et prendront effet à la première ouverture du vault depuis son chemin actuel. Les deux vérifications visuelles du lot (graphe sans `liens.md`, titre en première ligne) restent donc à faire à ce moment-là, en même temps que le test ci-dessus. |
| 2026-09-04 | 0 | Le réglage « Propriétés dans le document → Masqué » a été appliqué **par le fichier** (`propertiesInDocument: "hidden"` dans `app.json`) et non par l'interface, faute d'accès à celle-ci. Avantage : le réglage devient portable entre machines au lieu de rester local. | À confirmer d'un œil à la réouverture — si le panneau reste visible, le passer par Réglages → Éditeur, Obsidian réécrira la clé lui-même. |

---

## Décisions restées ouvertes

Elles n'empêchent aucun lot de démarrer, mais elles doivent être tranchées avant le lot 7.

1. **`MOC/Themes`** (5 pages) — seul consommateur du champ `domaines:`. Les garder comme hubs
   transverses à la racine, ou supprimer le champ ?
2. **Les 18 notions sans domaine évident** — listées en fin d'arborescence. La plupart sont en
   fait faciles (`ORM`, `Migrations de schéma`, `Web scraping`, `Notebooks-as-code`) ; le lot 4
   les propose, floSa tranche.
3. **Les 9 comparatifs sans filtre `categorie`** — leur dossier d'accueil se pose à la main.
4. **Le seuil de promotion à 5 pages** — 28 sous-dossiers. À 4 il en donnerait 34, à 8 il en
   donnerait 12. Choix de confort, révisable au lot 3 sans rien casser d'autre.
5. **Variante « comparatif en un seul fichier »** — un bloc de code dans la page au lieu d'un
   `.base` à côté. Test de 30 secondes dans Obsidian, à faire avant le lot 5.
