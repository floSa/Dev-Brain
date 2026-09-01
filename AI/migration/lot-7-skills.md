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
