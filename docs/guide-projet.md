# DevBrain — S'en servir depuis un projet

Le brain n'est pas fait pour être lu, il est fait pour **contraindre l'IA qui code**. Ce
document explique comment. Pour lire le vault, va dans
[manuel-utilisateur.md](manuel-utilisateur.md) ; pour l'enrichir,
[guide-enrichissement.md](guide-enrichissement.md).

---

## 1. La règle qui commande tout : on ne travaille pas dans le vault

Un projet se développe dans **son propre dossier**, avec Claude Code lancé là-bas — jamais
dans le vault. Le vault est une source, pas un plan de travail.

```bash
cd ~/Projets/mon-projet
claude
```

Ce dossier porte son propre `CLAUDE.md`, issu du gabarit `CLAUDE-project.md` du vault. Ce
gabarit dit une chose essentielle à l'IA qui code : **aucune écriture dans l'arbre des
domaines**. Depuis un projet, le brain se lit et ne s'écrit pas.

---

## 2. Ce que le brain apporte au démarrage

Sans lui, une IA à qui on demande « fais-moi une appli de recherche sémantique » propose la
stack qu'elle a vue le plus souvent sur internet. Avec lui, elle propose **ce que tu as déjà
évalué**, avec le fait qui t'avait fait choisir.

C'est le rôle du skill `planifier-projet`, appelé depuis le dossier du projet :

```
propose-moi un plan pour <ce que tu veux faire>
quel stack pour ce projet
aide-moi à cadrer
```

Ce qu'il fait, dans l'ordre :

1. **Il identifie l'archétype** du projet — `Documentation/perso/archetypes.md` en porte la
   liste. Un pipeline de données et une démo ML locale ne posent pas les mêmes questions.
2. **Il ne pose que les questions qui comptent** pour cet archétype
   (`Documentation/general/questions-projet.md`).
3. **Il interroge `AI/index/brain-index.json`** et sort, pour chaque brique à choisir, 2 ou 3
   candidates avec leur pitch d'une ligne — sous forme de question à choix, pas de
   recommandation imposée.
4. **Il produit un cahier des charges sourcé** : chaque choix pointe vers la fiche du vault
   qui le justifie.

Ce cahier des charges est ce qui contraint l'IA de dev ensuite. C'est là qu'est le gain :
elle ne redécouvre pas ce que tu sais déjà.

---

## 3. Interroger l'index directement

Le skill passe par là, mais tu peux aussi le faire à la main. `query_index.py` filtre sur les
champs indexés :

```bash
uv run AI/scripts/query_index.py --categorie database/vecteur --famille paquet
uv run AI/scripts/query_index.py --categorie data/synthetique --langage Python
```

Une réserve mesurée au lot 4 : `langage:` est une énumération **ouverte**. Un filtre exact
rate une brique déclarée « C++ / Python » — `Stan` est dans ce cas.

---

## 4. Le chemin de lecture, quand tu cherches toi-même

| Tu veux | Va voir |
|---|---|
| choisir entre deux outils | le **comparatif** du dossier, section `## Ce qui départage` |
| savoir ce qu'un outil coûte à exploiter | la fiche, `## Mise en œuvre` → `Prérequis` |
| savoir pourquoi écarter un outil | la fiche, colonne `Écarter si` |
| comprendre le concept sous-jacent | la **notion** du même dossier |
| monter un assemblage déjà éprouvé | `Patterns/` — 5 patterns, chacun combinant plusieurs briques |
| savoir ce que tu t'imposes sur tous les projets | `Rules/` — 5 règles transverses (toolchain, structure, qualité, config typée, packaging) |

---

## 5. Ce qui remonte du projet vers le brain

Un projet produit deux choses qui méritent de revenir :

- **Un retour d'expérience daté.** Il s'écrit dans la section `## Retours` de la fiche
  concernée, au format `- YYYY-MM-DD — <symptôme> : <correctif>.` La date est ce qui
  distingue le vécu du piège documenté. Sans date, ce n'est pas un retour mais une borne, et
  ça va en `Écarter si` ou en `Prérequis`.
- **Une brique découverte.** Elle se capture avec `enrichir-brain`, **depuis le vault**, pas
  depuis le projet.

Un incident né entre deux briques s'inscrit **sous celle qui a porté le correctif**, une
seule fois, les autres nommées en clair dans la ligne. Une entrée dupliquée serait une
seconde chose à synchroniser.

> À la clôture de la v3, le vault ne portait **aucune** entrée datée : la section `## Retours`
> n'existe encore nulle part. C'est le premier vrai retour de projet qui la créera.

---

## 6. Installer le gabarit dans un nouveau projet

Copie `CLAUDE-project.md` du vault vers le `CLAUDE.md` du projet, et renseigne les deux
lignes qu'il attend : le chemin du vault, et l'archétype retenu. Le reste du fichier dit à
l'IA de dev ce qu'elle a le droit de faire — et surtout ce qu'elle n'a pas le droit de faire
dans le brain.
