---
galaxie: meta
nom: lot-6-gabarit
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 6 — Conversion des fiches au nouveau gabarit

Effort : **25 fiches par conversation au maximum**, **337** fiches au total — soit dix-huit
conversations (le pilote et les dix-sept lots du protocole). C'est le lot le plus long, et le
seul qui touche au texte.

> **337, et non 336.** Recompté le 2026-09-06 par la conversation pilote, sur les pages
> `role: brique` de l'arbre — les deux gabarits de `Templates/` et l'exemple de code de
> `CLAUDE-build.md` exclus. Le 336 de la rédaction initiale traînait dans six phrases de ce
> brief ; elles sont corrigées ci-dessous, chacune avec sa date de mesure.

Mesure du 2026-09-04 : 64 lignes et 407 mots médians par fiche, lues *et* réécrites, soit 3 à
4 k tokens chacune. Au-delà de 25, la conversation sature avant la fin du domaine.

Prérequis : lots 2 et 3 faits. **Jamais en parallèle d'un autre lot** — le 3 déplace les fiches
que le 6 réécrit.

## Contexte

Le gabarit actuel est suivi à 100 % : **337 fiches sur 337** portent `Pourquoi`, `Quand
l'utiliser`, `Quand NE PAS l'utiliser`, `Pièges` et `Liens` (remesuré le 2026-09-06). Ce n'est donc pas un problème de
discipline, c'est le gabarit lui-même qui est en cause. Sept sections pour 407 mots médians,
soit 58 mots par section : les titres pèsent plus que leur contenu.

Trois mesures qui commandent les changements :

| Constat | Mesure |
|---|---|
| `Pièges` ne contient pas de retours d'expérience | 337 sections remplies, **1 seule** avec une entrée datée — `LLM & IA générative/Agents de code/t3code.md` (remesuré le 2026-09-06) |
| `Déploiement & coût` reformule le frontmatter | 84,5 % contiennent « gratuit » (= `licence_type`), 4,4 % mentionnent une plateforme |
| `Liens` fait trois métiers à la fois | sur la page Faker, Mimesis apparaît en `Alternatives` **et** en `Liens` |

Le gabarit cible et le raisonnement complet : [[AI/design/brain-v3|brain-v3]] §6.

## Périmètre

- Le corps des **337** fiches `role: brique` (mesure du 2026-09-06).
- Le bandeau généré des 299 `role: notion` — leur corps, lui, n'est **pas** touché.
- Le nouveau script `build_bandeau.py`.

## Le principe, en une phrase

**Une ligne, une étiquette, une idée.** Aucune prose hors de `## Définition`. C'est le format
de la section `## Alternatives`, la seule que l'usage a validée, généralisé à toute la page.

## Procédure

### 1. Écrire `build_bandeau.py`

Il compose le bandeau de chaque page depuis son frontmatter, dans une zone `<!-- AUTO -->` :
`Nature` (dérivé de `famille:` + `langage:`), `Licence`, `Exécution`, `Maturité`. Idempotent,
relançable, jamais édité à la main.

### 2. Convertir, domaine par domaine

Correspondance de départ, à ne pas appliquer aveuglément :

| Ancienne section | Devient |
|---|---|
| `## Pourquoi` | `## Définition` — prose, 4 à 6 lignes, **sans redire le bandeau** |
| `## Quand l'utiliser` + `## Quand NE PAS l'utiliser` | un tableau `Prendre si / Écarter si` |
| `## Déploiement & coût`, `## Bases & plateformes`, `## Installation & plateformes` | `## Mise en œuvre`, cinq étiquettes fixes |
| `## Pièges` | **dissoute** — voir ci-dessous |
| `## Alternatives` | `## Écosystème` → `### Alternatives` + `### Compléments` |
| `## Liens` | scindée en `## Ressources` (externe, étiqueté) et `## Voir aussi` (interne) |

**La section « déploiement » porte trois noms, pas un.** Mesure du 2026-09-06 : 297 fiches
portent `## Déploiement & coût`, 22 portent `## Bases & plateformes` et 18 `## Installation &
plateformes` — 337 en tout, donc aucune fiche sans. Une conversation qui ne cherche que le
premier nom laissera 40 fiches avec deux sections « mise en œuvre », l'ancienne et la neuve.
Les trois se lisent de la même façon et fusionnent dans la même cible.

Deuxième écart de la même mesure : **334 fiches sur 337 portent `## Alternatives`**. Les trois
qui n'en ont pas sont des fiches sans voisin déclaré — elles n'ont pas de `### Alternatives` à
remplir, et c'est la règle 4 du validateur (voisinage déclaré, souple) qui les signale déjà.

### 3. Dissoudre `Pièges` correctement

C'est l'étape qui demande du jugement, et elle ne se scripte pas. Chaque puce part vers l'un
de trois endroits :

- **une limite de conception qui oriente un choix** → colonne `Écarter si`, avec le lien vers
  l'alternative. Exemple mesuré : « Faker tire les champs indépendamment, email et nom ne
  correspondent pas » n'est pas un piège, c'est le critère qui fait choisir SDV ;
- **une limite qui n'oriente rien mais qu'il faut savoir** → `## Définition` ;
- **un retour d'expérience daté** → section `## Retours`, qui n'existe **que** dans ce cas.
  Une seule fiche du vault est concernée.

Aucune puce n'est supprimée sans avoir trouvé sa destination.

### 4. Remplir `complements:`

Le champ a été ouvert vide au lot 2. Le remplir ici, quand le voisinage de la fiche est sous
les yeux : pgvector et Postgres, Faker et pandas. Réciprocité obligatoire.

## Critères d'acceptation

- [ ] Aucune fiche ne porte plus `Pourquoi`, `Quand l'utiliser`, `Quand NE PAS l'utiliser`,
      `Déploiement & coût` ni `Pièges`.
- [ ] Chaque cellule `Écarter si` contient un wikilink.
- [ ] Chaque puce de `Ressources` porte une étiquette du vocabulaire fermé.
- [ ] `Mise en œuvre` porte ses cinq étiquettes.
- [ ] Aucune cible n'apparaît dans deux sections de la même page.
- [ ] `## Définition` ne recontient ni la famille, ni la licence, ni la maturité.
- [ ] `check_brain.py` au vert.

## Interdictions

- **Ne pas inventer de contenu.** Une cellule `Écarter si` qui n'a pas de source dans la fiche
  d'origine se laisse vide et se signale. Un tableau à moitié rempli honnêtement vaut mieux
  qu'un tableau complet inventé.
- Ne pas supprimer une puce de `Pièges` sans lui avoir trouvé une destination.
- Ne pas toucher au corps des notions.
- Ne pas traiter plus d'un domaine par conversation.

## Réserve connue

Mesure du 2026-09-04, sur 336 fiches et non revérifiée depuis : 331 puces `Liens` portent
déjà une étiquette, mais **286 valent « Doc »**. Le vault ne
contient presque aucun tutoriel, article ou papier. Typer les liens ne les crée pas : la
section `## Ressources` sera souvent réduite à deux lignes, et c'est normal. Les enrichir est
un chantier distinct, à ouvrir plus tard.

## Prompt à coller dans une conversation neuve

```
Lis AI/design/brain-v3.md puis AI/migration/lot-6-gabarit.md.

Écris d'abord AI/scripts/build_bandeau.py, puis convertis les fiches du domaine
<NOM DU DOMAINE> uniquement.

Montre-moi trois fiches converties — une librairie, une plateforme, une application
à interface — avant de dérouler le reste du domaine.

Traite au maximum 25 fiches. Termine en me listant nommément celles qui restent dans
le domaine, pour que la conversation suivante reprenne exactement là.

N'invente aucun contenu : une cellule sans source dans la fiche d'origine reste vide
et tu me la signales. Clôture avec le skill cloturer-brain.
```

---

## Protocole parallèle — arrêté le 2026-09-06

Le lot 6 est le seul assez long pour justifier du parallélisme, et le seul qui s'y
prête : il ne déplace rien, ne renomme rien, et le corps des 337 fiches est **disjoint
par dossier**. Ce qui empêchait le parallélisme aux lots 3, 4 et 5 était la clôture —
`cloturer-brain` régénère `AI/index/`, commit et pousse sur `main` : deux clôtures
simultanées se percutent. On la retire des conversations de conversion et on la fait
une fois, à la fin.

Le harnais donne déjà à chaque conversation son worktree et sa branche. Il n'y a donc
rien à installer : il y a des **interdits** à tenir.

### Les six règles d'une conversation de conversion

1. **Elle ne touche que les fiches `role: brique` des dossiers qui lui sont assignés.**
   Rien d'autre dans le vault : pas un hub, pas une notion, pas un comparatif, pas une
   fiche d'un dossier voisin. Deux conversations ne partagent jamais un dossier.
2. **Elle ne régénère rien** — ni `build_index`, ni `build_mocs`, ni `build_links` —
   **et n'appelle jamais `cloturer-brain`.** C'est la conversation d'intégration qui
   régénère, une fois.
3. **Elle ne modifie aucun fichier partagé** : ni `lot-6-gabarit.md`, ni `CLAUDE*.md`,
   ni `taxonomie.md`, ni `brain-v3.md`, ni `v3-arborescence.md`, ni `arbo.py`, ni aucun
   script — `build_bandeau.py` compris, qu'elle **lance** sans jamais l'éditer, et
   toujours **borné à ses dossiers**.
4. **Ses remontées vont dans son propre fichier**, `AI/migration/lot-6/remontees-<slug>.md`,
   créé par elle. Jamais dans le brief commun. Si elle constate qu'un document partagé
   doit changer, elle l'écrit là et ne le change pas.
5. **Elle peut lancer `check_brain.py` et `check_arbo.py`** pour se vérifier, mais le
   compte d'avertissements de sa branche ne vaut que pour elle : il lui manque le
   travail des autres. Elle mesure son propre écart avant/après et l'explique ; elle
   ne cherche pas à retomber sur le compte de `main`.
6. **Elle commite sur sa branche et la pousse** (`git push -u origin HEAD`). Elle ne
   fait **jamais** `checkout main`, `merge`, `rebase`, ni `push` vers `main`. Elle
   termine en donnant son **nom de branche** et ses SHA.

### La conversation d'intégration

Seule, en dernier. Elle intègre les branches une par une dans `main` — les jeux de
fichiers étant disjoints, aucun conflit n'est attendu ; **un conflit signifie qu'une
règle a été violée**, il s'examine, il ne se force pas. Puis elle lance
`build_bandeau.py` sur tout le vault, régénère les trois index, fusionne les fichiers
de remontées dans `lot-6-gabarit.md`, passe les deux validateurs et clôt avec
`cloturer-brain`.

### Découpage — un dossier entier par conversation, jamais moins

Le pilote (`build_bandeau.py` + « Bases de données/Vectoriel/ » et « Administration/ »)
passe **seul**, avant tout parallélisme : il fixe le gabarit et l'outil.

> **Table corrigée le 2026-09-06 par le pilote**, contre le contenu réel du vault. La
> première rédaction en 14 lots avait trois défauts, tous mesurables : elle laissait
> **11 fiches orphelines** — celles posées directement dans « LLM & IA générative/ », le
> seul domaine dont la table ne nommait pas le niveau domaine, quand elle le nommait pour
> Bases de données, Machine Learning et Data & pipelines ; elle **dépassait le plafond de
> 25** sur deux lots (29 et 27) ; et elle comptait 326 fiches pour 337.
>
> Trois contraintes ont guidé la correction, et elles se vérifient : couverture des 337
> sans orpheline, plafond de 25 **dur**, dossier entier jamais coupé en deux. Le nombre de
> lots, lui, est libre — ils tournent en parallèle, un lot de plus ne coûte rien, alors
> qu'un lot à 30 coûte une conversation ratée. La règle appliquée là où un domaine
> débordait : **le niveau domaine fait son propre lot**. C'est ce qui donne les lots 1, 10
> et 13, et ce qui ferme le trou LLM.

| # | Périmètre | Fiches |
|---|---|---|
| — | *pilote* — Bases de données : `Vectoriel/`, `Administration/` | 18 |
| 1 | Bases de données : niveau domaine | 17 |
| 2 | Bases de données : `Relationnel/`, `Recherche/` | 12 |
| 3 | Machine Learning : `Vision/`, `Serving/`, `Non supervisé/` | 22 |
| 4 | Machine Learning : `Apprentissage profond/`, `Interprétabilité/`, `Socle/`, `Évaluation de modèles/` | 19 |
| 5 | Machine Learning : `Séries temporelles/`, `Suivi d'expériences/`, `Tabulaire/` | 20 |
| 6 | Machine Learning : `Apprentissage par renforcement/`, `NLP/`, niveau domaine | 24 |
| 7 | LLM : `Agents de code/`, `Agents/` | 22 |
| 8 | LLM : `Runtimes/`, `Assistants/`, `Fine-tuning/` | 19 |
| 9 | LLM : `Observabilité des LLM/`, `Passerelles/`, `RAG & retrieval/`, `Sortie typée/`, `Text-to-SQL/`, `Évaluation/` | 22 |
| 10 | LLM : niveau domaine | 11 |
| 11 | Data & pipelines : `Scraping/`, `Parsing/` | 19 |
| 12 | Data & pipelines : `Orchestration/`, `DataFrames/`, `Visualisation/` | 16 |
| 13 | Data & pipelines : niveau domaine | 11 |
| 14 | Outils de développement (entier, `Notebooks/` compris) | 20 |
| 15 | Statistiques & inférence (entier), Design & diagrammes (entier), Calcul distribué | 24 |
| 16 | Web & API, Stockage, Automatisation no-code, Médias, Interfaces & apps data | 25 |
| 17 | Sécurité, Signal & audio (entier), Observabilité, Réseau, Documents, DevOps, `Mathématiques/Optimisation/` | 16 |

Total : **18 + 319 = 337**, zéro fiche orpheline, aucun lot au-dessus de 25. Les comptes ne
sont **pas** indicatifs : ils sont mesurés, et un lot qui n'en trouve pas le nombre annoncé
doit s'arrêter et le signaler plutôt que déborder sur un dossier voisin.

Deux lots portent un domaine dont un autre lot porte les sous-dossiers (1 et 2 pour Bases de
données, 9 et 10 pour LLM, 12 et 13 pour Data & pipelines). Ce n'est pas un dossier coupé en
deux : « Bases de données/ » et « Bases de données/Relationnel/ » sont deux dossiers distincts,
et aucune fiche n'appartient aux deux. Le point d'attention est ailleurs — la réciprocité
d'`alternatives:` et de `complements:` traverse ces frontières dans 66 arêtes sur 798 (8 %,
mesuré le 2026-09-06). Une conversation qui remplit `complements:` vers une fiche **hors de
son périmètre** écrit une moitié de couple : elle pose sa moitié, et **inscrit l'autre dans
ses remontées** au lieu d'aller éditer la fiche du voisin. C'est l'intégration qui referme.

Ce découpage suit les **dossiers**, pas un compteur : c'est ce qui garantit qu'aucune
fiche n'appartient à deux conversations.

---

## Trois règles nées des lots 1 à 5 — arrêtées le 2026-09-06

### 1. Un wikilink dans une cellule de tableau est NU

`[[Triton]]`, jamais `[[NVIDIA Triton|Triton]]`. Un wikilink à alias dans une cellule
coupe la ligne du tableau ; l'échapper répare le rendu Obsidian et fait **échouer
`check_brain` en violation dure** (« lien mort »). Mesuré par le lot 4, qui a vérifié
sur la vraie expression régulière. Les deux formes cassent, la nue est la seule qui
passe.

### 2. Où va une puce « besoin -> [[concurrent]] » : ça dépend du comparatif

Les cinq premiers lots l'ont traitée de trois façons, et chacun avait raison **dans son
cas**. La règle qui les réconcilie :

- **La brique est membre d'une vue `.base`** → la puce vit dans le comparatif, et la
  cellule `Écarter si` de la fiche ne porte que des **bornes dures de la brique seule**.
  C'est le cas du pilote et des lots 1, 2 et 5.
- **La brique n'est membre d'AUCUNE vue** → la puce **reste** en `Écarter si`, avec son
  wikilink. L'écarter la supprimerait. C'est le cas des lots 3 et 4 : un dossier peut
  n'avoir aucun comparatif (`Apprentissage profond/`, 8 briques), et une vue filtrant par
  tag rate des briques de son propre dossier (Kornia, timm, torchvision, hdbscan,
  Featuretools, category_encoders, imbalanced-learn).

Vérifier l'appartenance, ne pas la supposer : `AI/scripts/mesure_membres_bases.py` la
donne. La conversation d'intégration normalise ce qui a divergé.

### 3. `complements:` n'est pas « tout ce avec quoi ça s'intègre »

Un couple ne se pose que si la fiche **énonce l'appariement comme une recommandation**,
et il s'écrit **dans les deux sens**. « MLflow s'intègre à PyTorch, Scikit-Learn,
XGBoost, Optuna » n'ouvre aucun couple : sinon les sept trackers du lot 5 en ouvrent
une quinzaine et le champ devient du bruit. Une moitié de couple dont la cible est hors
périmètre se pose de son côté et se **signale dans les remontées** ; l'intégration ferme
l'autre moitié.
