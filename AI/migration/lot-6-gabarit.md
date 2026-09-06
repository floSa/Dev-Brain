---
galaxie: meta
nom: lot-6-gabarit
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 6 — Conversion des fiches au nouveau gabarit — **CLOS le 2026-09-06**

> Les 337 fiches sont au gabarit v3. Le *Journal du lot 6*, en fin de fichier, porte l'état
> final, les vingt remontées consolidées des dix-huit conversations, et ce qui part au lot 8.
> Ce qui suit est le brief tel qu'il a servi, corrigé au fil du lot.

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
  ~~Une seule fiche du vault est concernée.~~ **Aucune, vérifié le 2026-09-06** : la fiche que
  cette phrase visait portait une date de création de dépôt, pas un retour d'expérience (cf.
  remontée 7 du journal). La section n'a été créée nulle part et n'avait pas à l'être ;
- **une contrainte d'installation ou d'exploitation** → `## Mise en œuvre`, sous l'étiquette
  qui convient — `Installation`, `Point d'entrée`, `Prérequis`, `Exécution` ou `Coût`.
  **Quatrième destination, ajoutée le 2026-09-06** : quatre lots l'ont trouvée indépendamment
  (4, 9, 13, 14). `Écarter si` est réservé à ce qui **disqualifie** le choix ; ce qu'on subit
  une fois le choix fait — volume de traces, cache qui grossit, distribution TeX à installer —
  est un prérequis, pas un critère de décision.

Aucune puce n'est supprimée sans avoir trouvé sa destination.

### 4. Remplir `complements:`

Le champ a été ouvert vide au lot 2. Le remplir ici, quand le voisinage de la fiche est sous
les yeux : pgvector et Postgres, Faker et pandas. Réciprocité obligatoire.

## Critères d'acceptation — **relevés le 2026-09-06, cinq sur sept**

- [x] Aucune fiche ne porte plus `Pourquoi`, `Quand l'utiliser`, `Quand NE PAS l'utiliser`,
      `Déploiement & coût` ni `Pièges` — les **trois** noms de la section déploiement cherchés,
      et `## Alternatives` en `##`. Zéro occurrence sur les 337.
- [ ] ~~Chaque cellule `Écarter si` contient un wikilink.~~ **NON TENU, et le critère est
      inatteignable** : 356 cellules sur 1 388, soit 26 %, de 0 % à 44 % selon le domaine. Il
      cède devant la règle 2 — cf. remontée 3 du journal, et le lot 8.
- [x] Chaque puce de `Ressources` porte une étiquette du vocabulaire fermé — à quatre puces
      près, étiquetées `Site`, un besoin réel que le vocabulaire ne couvre pas (remontée 13).
- [x] `Mise en œuvre` porte ses cinq étiquettes, sur les 337.
- [ ] ~~Aucune cible n'apparaît dans deux sections de la même page.~~ **NON TENU tel qu'écrit,
      et impossible** dès qu'une catégorie n'a pas de comparatif : la règle 2 garde la cible en
      `Écarter si`, R11 l'exige en `### Alternatives`, et R11 est une violation dure. Tenu sous
      la lecture « listes de liens » du lot 9 — cf. remontée 4.
- [x] `## Définition` ne recontient ni la famille, ni la licence, ni la maturité — vérifié
      contre le bandeau **rendu**, pas contre les valeurs brutes.
- [x] `check_brain.py` au vert : 0 violation dure, 28 avertissements contre 149 avant.

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

### 2. Où va une puce « besoin -> [[concurrent]] » : ça dépend de la CIBLE

**Corrigé le 2026-09-06.** La première formulation testait l'appartenance de la *fiche*
à une vue `.base`. Trois lots l'ont trouvée fausse indépendamment (6, 7 et 8) : la
question utile porte sur la **cible du renvoi**, pas sur la brique qui l'écrit.

La règle :

- **La brique ET la cible sont membres de la MÊME vue `.base`** → la puce vit dans le
  comparatif, et la cellule `Écarter si` de la fiche ne porte que des **bornes dures de
  la brique seule**.
- **Sinon — dans tous les autres cas** → la puce **reste** en `Écarter si` avec son
  wikilink. L'écarter la supprimerait, parce qu'aucun comparatif ne peut la porter.

Les quatre cas qui tombent dans « sinon », tous rencontrés — **le quatrième ajouté le
2026-09-06 par les lots 11 et 15** :
  1. le dossier n'a aucun comparatif (`Apprentissage profond/`, 8 briques ; `Assistants/`) ;
  2. la vue filtre par tag et rate des briques de son propre dossier (Kornia, timm,
     torchvision, hdbscan, Featuretools, category_encoders, imbalanced-learn, Evidently,
     Feast, PyTorch Geometric) ;
  3. **la brique est membre mais la cible ne l'est pas** — `datasets -> Polars`,
     `Flyte -> Dagster`, `E2B -> compute/a-la-demande`, `needle -> Outlines`,
     `TRL -> PyTorch`. C'est le cas majoritaire, et celui que la première formulation
     ratait ;
  4. **la cible est une notion.** Un `.base` filtre `role == "brique"` depuis le lot 4 : une
     notion n'est membre d'**aucune** vue, jamais. Toute redirection d'une brique vers une
     notion tombe donc dans « sinon », par construction et non par accident de filtre —
     `CausalImpact -> Diff-in-Diff`, `docTR -> OCR`.

Vérifier, ne pas supposer : `AI/migration/scripts/mesure_membres_bases.py` (et non
`AI/scripts/`). Un sur-comptage possible du script est signalé par le lot 8 : recouper
sur un cas avant de s'y fier en masse. Recoupé depuis par les lots 9, 11, 12, 14, 15 et 16
sur leurs propres périmètres — **aucun sur-comptage constaté**, hors le cas `ONNX Runtime`
que le lot 8 nomme.

`AI/migration/scripts/lot6_regle2_audit.py`, écrit à l'intégration, fait le contrôle dans
l'autre sens : il relit les puces `## Quand NE PAS l'utiliser` d'une fiche **à son commit
d'origine** et dit, renvoi par renvoi, s'il devait rester et s'il est là.

**Deux critères d'acceptation du brief cèdent devant cette règle**, et c'est délibéré :
« un wikilink dans chaque cellule `Écarter si` » et « aucune cible dans deux sections »
supposent tous deux que la redirection a toujours un comparatif d'accueil. Quand elle
n'en a pas, la règle 2 l'emporte : on garde l'information plutôt que de satisfaire un
critère. Les deux critères seront réécrits au lot 8.

### 3. `complements:` n'est pas « tout ce avec quoi ça s'intègre »

Un couple ne se pose que si la fiche **énonce l'appariement comme une recommandation**,
et il s'écrit **dans les deux sens**. « MLflow s'intègre à PyTorch, Scikit-Learn,
XGBoost, Optuna » n'ouvre aucun couple : sinon les sept trackers du lot 5 en ouvrent
une quinzaine et le champ devient du bruit. Une moitié de couple dont la cible est hors
périmètre se pose de son côté et se **signale dans les remontées** ; l'intégration ferme
l'autre moitié.

---

# Journal du lot 6 — CLOS le 2026-09-06

Les **337** fiches `role: brique` sont au gabarit v3. Dix-huit conversations : le pilote,
seul, puis dix-sept en parallèle selon le protocole ci-dessus, puis une conversation
d'intégration qui a réuni les dix-sept branches, normalisé leurs divergences, tranché ce qui
restait ouvert, régénéré et clos.

Ce journal **remplace** les dix-huit fichiers `AI/migration/lot-6/remontees-*.md`, absorbés
ici et supprimés. Chaque remontée numérotée dit quels lots l'ont mesurée : c'est la
convergence de mesures indépendantes qui fait la valeur du constat, pas son nombre
d'occurrences.

## Les dix-huit conversations

| # | Périmètre | Fiches | Branche | Avert. sur sa branche |
|---|---|---|---|---|
| — | *pilote* — `build_bandeau.py`, Bases de données : `Vectoriel/`, `Administration/` | 18 | `claude/lot-6-conversion-fiches-8ec828` | intégrée avant la mesure |
| 1 | Bases de données : niveau domaine | 17 | `claude/lot-6-databases-conversion-1209d0` | 149 → 147 |
| 2 | Bases de données : `Relationnel/`, `Recherche/` | 12 | `claude/lot-2-databases-search-3a7ffa` | 149 → 149 |
| 3 | ML : `Vision/`, `Serving/`, `Non supervisé/` | 22 | `claude/lot-3-machine-learning-f44962` | 149 → 140 |
| 4 | ML : `Apprentissage profond/`, `Interprétabilité/`, `Socle/`, `Évaluation de modèles/` | 19 | `claude/lot-4-machine-learning-57b861` | 149 → 145 |
| 5 | ML : `Séries temporelles/`, `Suivi d'expériences/`, `Tabulaire/` | 20 | `claude/lot-5-ml-fiches-c0933f` | 149 → 142 |
| 6 | ML : `Apprentissage par renforcement/`, `NLP/`, niveau domaine | 24 | `claude/machine-learning-batch-6-6ba45a` | 149 → 144 |
| 7 | LLM : `Agents de code/`, `Agents/` | 22 | `claude/lot-7-llm-ia-agents-cd531c` | 149 → 144 |
| 8 | LLM : `Runtimes/`, `Assistants/`, `Fine-tuning/` | 19 | `claude/lot-8-llm-ia-generative-77e163` | 149 → 145 |
| 9 | LLM : six sous-dossiers — observabilité, passerelles, RAG, sortie typée, text-to-SQL, éval | 22 | `claude/lot-9-llm-six-dossiers-dd3c2b` | 149 → 149 |
| 10 | LLM : niveau domaine | 11 | `claude/lot-10-llm-domaine-f58fec` | 149 → 148 |
| 11 | Data & pipelines : `Scraping/`, `Parsing/` | 19 | `claude/lot-11-data-pipelines-cb7f8e` | 149 → 142 |
| 12 | Data & pipelines : `Orchestration/`, `DataFrames/`, `Visualisation/` | 16 | `claude/lot-12-data-pipelines-fce886` | 149 → 133 |
| 13 | Data & pipelines : niveau domaine | 11 | `claude/lot-13-data-pipelines-0bb213` | 149 → 145 |
| 14 | Outils de développement — entier, `Notebooks/` compris | 20 | `claude/lot-14-outils-dev-121856` | 149 → 133 |
| 15 | Statistiques & inférence, Design & diagrammes, Calcul distribué | 24 | `claude/lot-15-stats-design-distribue-5f95ed` | 149 → 139 |
| 16 | Web & API, Stockage, Automatisation no-code, Médias, Interfaces & apps data | 25 | `claude/lot-16-gabarit-v3-3751de` | 149 → 129 |
| 17 | Sécurité, Signal & audio, Observabilité, Réseau, Documents, DevOps, `Mathématiques/Optimisation/` | 16 | `claude/lot-17-six-domaines-0b1858` | 149 → 138 |

**Les dix-sept lots ont trouvé le compte annoncé par la table du découpage, tous les
dix-sept.** La table corrigée par le pilote était juste : 322 fiches touchées par les
dix-sept, 15 par le pilote seul, 322 + 15 = 337 ; aucune collision, aucun fichier hors de la
liste des briques. Les jeux de fichiers étant disjoints, les dix-sept merges se sont faits
**sans un seul conflit** — c'est la vérification que le protocole parallèle demandait.

## 1. La règle 2 a été trouvée fausse trois fois avant d'être corrigée — et le pilote ne pouvait pas la trouver

La première formulation testait l'appartenance de la **fiche** à une vue `.base`. Les lots 6,
7 et 8 l'ont contredite indépendamment, à quelques heures d'intervalle, chacun avec ses
propres cas : `Maka → E2B`, `ai-memory → Letta`, `PraisonAI → Langflow` (lot 7) ;
`needle → Outlines`, `TRL → PyTorch` (lot 8) ; neuf renvois dont `datasets → Polars` et
`Flyte → Dagster` (lot 6). La question utile porte sur la **cible du renvoi**.

Ce qui mérite d'être retenu n'est pas l'erreur, c'est **pourquoi le pilote ne pouvait pas la
voir**. Mesure faite à l'intégration, en relisant ses 18 fiches d'origine : ses **68** renvois
« besoin → concurrent » visaient **tous** un co-membre de sa propre vue. « Bases vectorielles »
compare onze briques qui s'opposent deux à deux ; la question « et la cible, est-elle
membre ? » ne s'y pose littéralement jamais. Un pilote choisi pour être exemplaire a produit
une règle qui ne valait que pour lui.

> **Ce que ça dit du choix d'un pilote.** Le dossier le plus homogène du vault est celui qui
> teste le moins la règle qu'on lui fait écrire. Un second dossier, hétérogène, aurait coûté
> une conversation et fait tomber la règle 2 avant que six lots ne travaillent dessus.

## 2. Le routage, mesuré lot par lot après intégration

`AI/migration/scripts/lot6_regle2_audit.py`, écrit à l'intégration, relit les puces
`## Quand NE PAS l'utiliser` de chaque fiche **à son commit d'origine**, résout l'appartenance
aux 47 vues par `check_brain.base_match`, et confronte au contenu actuel de la colonne
`Écarter si`. Sur les 1 025 renvois vers une brique du vault :

| | Renvois | Traitement |
|---|---|---|
| brique **et** cible co-membres | 672 | partent au comparatif, qui les porte déjà |
| tous les autres cas | 353 | **restent** en `Écarter si`, avec leur wikilink |

Les six lots écrits avant la correction en avaient perdu **53** — lot 1 : 24 sur 24 ; lot 2 :
7 sur 10 ; lot 3 : 9 sur 22 ; lot 5 : 6 sur 11 ; plus 7 résidus chez les lots 6, 7 et 8. Ils
sont revenus sur la fiche : **42 gestes sur 35 fiches**, texte repris de la puce d'origine,
wikilinks nus, et une cellule qui disait déjà la chose sans le lien a reçu le lien plutôt
qu'une ligne de plus. Après : **0 renvoi manquant**.

Le **lot 4** n'avait rien perdu : il avait gardé ses 44 renvois hors-vue *contre* le pilote,
en argumentant sur la spec (§6 : « chaque exclusion doit pointer vers l'alternative »). Sa
remontée 1 est la première formulation correcte de la règle 2, écrite avant qu'elle n'existe.

Les quatre cas de « sinon » rencontrés, et ils sont tous les quatre nécessaires :

1. **le dossier n'a aucun comparatif** — `Assistants/` (lot 8), `Passerelles/` (lot 9),
   `llm/low-code` et `llm/memoire` (lot 10), `devtools/config` et `devtools/notebook`
   (lot 14), Stockage et Médias (lot 16), quatre dossiers sur sept (lot 17) ;
2. **la vue filtre par tag et rate des briques de son propre dossier** — Kornia, timm,
   torchvision, hdbscan (lot 3) ; Featuretools, category_encoders, imbalanced-learn (lot 5) ;
   Daytona, E2B, Modal (lot 15) ;
3. **la brique est membre, la cible ne l'est pas** — le cas majoritaire. `Dask` concentre à
   lui seul quatre des six renvois survivants du lot 12 : il est l'alternative « à l'échelle »
   de tout le dossier DataFrames sans jamais en être membre, sa `categorie` le rangeant en
   calcul distribué ;
4. **la cible est une notion** — un `.base` filtre `role == "brique"` depuis le lot 4, donc
   une redirection vers une notion tombe *toujours* dans « sinon ». Repéré par le lot 15
   (`CausalImpact → Diff-in-Diff`) et le lot 11 (`docTR → OCR`). Ce quatrième cas ne figurait
   pas dans la règle ; il y est ajouté.

Deux lots sont aux extrêmes, et l'écart s'explique par la **fermeture du dossier**, pas par
une différence de méthode : le lot 11 a 67 renvois sur 70 qui visent un co-membre (Scraping et
Parsing sont fermés sur eux-mêmes), le lot 17 en a 13 fiches sur 16 qui ne sont membres
d'aucune vue.

## 3. La règle dure nº 5 est inatteignable — le chiffre du vault entier

Mesuré à l'intégration, sur les 337 fiches converties :

| | Compte |
|---|---|
| lignes de tableau `Prendre si / Écarter si` | 1 486 |
| cellules `Écarter si` remplies | 1 388 |
| — **dont portant un wikilink** | **356 (26 %)** |
| — dont borne dure de la brique seule, sans cible | 1 032 |
| cellules `Écarter si` laissées vides | 98 |
| cellules `Prendre si` laissées vides | 269 |

Le taux va de **0 %** — Automatisation no-code, DevOps, Interfaces & apps data, trois domaines
dont toutes les briques sont co-membres de leur vue — à **44 %** (Machine Learning). Sur les
branches prises isolément, l'écart était du même ordre : 0 % au pilote, 48 % au lot 10.

**La cause est structurelle, et elle est l'exact revers de la règle 2** : quand la redirection
part au comparatif, ce qui reste sur la fiche est une borne qui ne pointe vers personne — « le
cache n'est jamais purgé seul », « `max_elements` est fixé à l'initialisation », « il n'y a pas
de révocation native ». Le lot 14 nomme la seconde famille : **la cible n'existe pas dans le
vault**. Ses fiches citent dix-neuf outils non fichés — Click, argparse, mypy, conda, Black,
isort… — et le lot 17 en ajoute six, Wireshark, `rsync`, Pyomo, Podman. Exiger un wikilink là
rendrait tous ces outils obligatoires à ficher, ce qui n'est pas une décision de format.

Les deux reformulations proposées disent la même chose de deux façons : « toute cellule dont
le **motif** est une redirection porte un wikilink » (lot 5) et « toute exclusion qui nomme un
besoin **couvert par une autre brique du brain** porte son wikilink » (lot 4). À arbitrer au
lot 8.

## 4. « Aucune cible dans deux sections » est impossible, et le lot 16 en donne la preuve arithmétique

Le mécanisme, décrit indépendamment par les lots 10, 12, 13 et 14 : une cible gardée en
`Écarter si` par la règle 2 est presque toujours aussi une `alternatives:` — et **R11 est une
violation DURE** qui exige qu'elle figure en `### Alternatives`. Les deux contraintes sont
dures et contradictoires ; la règle 2 l'emporte.

Le lot 16 a mesuré la corrélation sur cinq dossiers qui couvrent les deux cas :

| Dossier | Comparatif d'accueil | Cibles dans deux sections |
|---|---|---|
| Stockage/ | aucun | **20** |
| Web & API/ | aucun pour 4 fiches sur 6 | **2** |
| Médias/ | aucun | 0 — aucune fiche n'a d'alternative déclarée |
| Automatisation no-code/ | les 5 membres d'une même vue | **0** |
| Interfaces & apps data/ | les 4 membres d'une même vue | **0** |

Le recouvrement apparaît **exactement** là où aucun comparatif ne peut porter la redirection,
et nulle part ailleurs. Ce n'est pas un défaut de rédaction à nettoyer : c'est la forme que
prend une fiche dont la catégorie n'a pas de comparatif.

Le lot 9 propose la lecture qui sauve le critère et restitue le défaut d'origine — sur la page
Faker, Mimesis apparaissait en `Alternatives` **et** en `Liens`, deux **listes de liens**. Le
critère porte sur `### Alternatives`, `### Compléments` et `## Voir aussi` ; ni la prose de
`## Définition`, ni les cellules du tableau de décision ne sont des listes de liens. Sous cette
lecture, les 337 fiches sont conformes.

Deux cas ne rentrent dans aucune des deux lectures, et sont signalés tels quels :
`docTR → [[OCR]]`, présent en `Écarter si` **et** en `## Voir aussi` (lot 11), et
`jupytext ↔ papermill`, à la fois redirection et complément — « si vous ne voulez qu'exécuter
en CI, prenez papermill » *et* « l'appariement versionne le source, papermill l'exécute »
(lot 14). Les deux phrases sont vraies et ne disent pas la même chose.

## 5. R15 tombe mécaniquement — 121 avertissements fermés, et la somme des mesures indépendantes est exacte

R15 — « une `role: brique` doit porter au moins un lien vers une notion ou un hub » — comptait
**121** avertissements à `d8f81d6`. Il en reste **0**.

La cause n'est pas un chantier de câblage : c'est le gabarit. `## Voir aussi` **oblige** à
nommer la notion parente ou le hub du dossier, là où l'ancienne `## Liens` mêlait navigation,
doublons d'alternatives et URLs, et pouvait n'en citer aucun. Le lot 3 a trouvé les **neuf**
fiches de `Serving/` non câblées à `[[Déploiement de modèles]]`, la notion de leur propre
dossier, présente depuis le lot 4.

Vérification qui vaut d'être notée : la somme des R15 fermés **annoncés séparément par les
dix-sept branches** — 2 + 0 + 9 + 4 + 7 + 5 + 5 + 4 + 0 + 1 + 7 + 16 + 4 + 16 + 10 + 20 + 11 —
vaut **exactement 121**. Dix-sept mesures indépendantes, sur dix-sept copies du vault, qui
totalisent le chiffre intégré au fichier près. C'est la meilleure preuve disponible qu'aucune
branche n'a débordé sur le périmètre d'une autre.

Le lot 6 explique **où** ces R15 vivaient : très majoritairement au **niveau domaine** des
dossiers, là où il n'y a pas de notion chapeau sous la main. Trois de ses cinq portent
`ml/orchestration`, une catégorie sans notion. Et le lot 17 ajoute la contrainte que le lot 8
devra respecter : **quatre domaines n'ont aucune notion** — Observabilité, Réseau, Documents,
DevOps. Si R15 durcit, le **hub** doit rester une cible légitime, sinon ces quatre domaines
deviennent inconvertibles.

## 6. `Pièges` avait une quatrième destination, que le brief ne nommait pas

Le brief en donnait trois — `Écarter si`, `## Définition`, `## Retours`. Quatre lots ont
trouvé la même quatrième, indépendamment : **`## Mise en œuvre`**, sous l'une de ses cinq
étiquettes.

- **lot 4** — environ 25 puces sur 76 : « installer la roue qui correspond au driver CUDA »
  (Installation), « le backend se fixe **avant** d'importer Keras » (Point d'entrée),
  « surveiller les *dead features* » (Exécution). *« Ce sont des contraintes d'installation ou
  d'exécution, pas des critères de choix : les mettre en `Écarter si` aurait pollué la
  décision, les mettre en `Définition` l'aurait noyée. »*
- **lot 13** — 3 puces sur 40, et il les nomme pour ce qu'elles sont : des **prérequis
  déguisés en pièges**.
- **lot 14** — la destination la plus fréquente de son domaine, devant `## Définition` : la
  distribution TeX de Quarto, le démon Docker de testcontainers, le kernel épinglé de
  papermill, le venv de pip.
- **lot 9** — la même puce écrite quatre fois : « le volume de traces, de logs ou de spans
  fait exploser le stockage ». Rangée sous `Prérequis` ; et sous `Coût` pour LangSmith, qui
  écrivait « le volume de traces **facturé** peut surprendre ».

**Arbitrage rendu à l'intégration** : `Écarter si` est réservé à ce qui **disqualifie** le
choix ; ce qu'on subit une fois le choix fait va sous `Prérequis`. Quatre cellules ont été
déplacées à ce titre — Aim, TensorBoard, `datasets`, Docling — et la quatrième destination est
inscrite dans la procédure ci-dessus.

Le même arbitrage donne enfin une destination à la puce que le pilote avait consignée sans en
trouver : « cohérence métrique / modèle d'embedding à surveiller, comme pour tout vector
store », partagée par `Chroma` et `LanceDB`. Le pilote la voyait partir vers la notion, qu'une
conversation de conversion ne touche pas. C'est un prérequis d'exploitation ; elle est sous
`Prérequis` des deux fiches. **Plus aucune puce du lot 6 n'est supprimée sans destination.**

## 7. `## Retours` n'existe nulle part, et la « seule entrée datée du vault » n'en était pas une

Le brief et la spec annonçaient une fiche portant un retour d'expérience daté, et la
nommaient : `LLM & IA générative/Agents de code/t3code.md`. Le lot 7, qui l'avait dans son
périmètre, est allé lire la puce :

> `- Créé le 2026-02-08 : peu de recul terrain, périmètre susceptible de bouger vite.`

C'est la **date de création du dépôt**, écrite `- <texte> le YYYY-MM-DD`, et non
`- YYYY-MM-DD — <symptôme> : <correctif>.`, la convention que `CLAUDE.md` définit. La mesure
qui l'avait désignée cherchait une date dans la section, pas la convention. Le fait a rejoint
la cellule `Écarter si` sur la précocité du projet.

**Conséquence : le vault ne contient AUCUNE entrée REX datée**, et les dix-huit lots l'ont
tous vérifié sur leur périmètre. Aucune section `## Retours` n'a été créée. Le grep de
contrôle est `^- [0-9]{4}-[0-9]{2}-[0-9]{2} —` ; il ne remonte rien sur l'arbre entier, ce que
l'intégration a revérifié après les dix-sept merges. La section reste au gabarit pour les
entrées futures.

Les lots 3 et 17 signalent le contre-effet à surveiller : les fiches portent beaucoup de
**faits datés sur le projet** — archivage de TorchServe le 7 août 2025, bascule BSL de Seldon
le 22 janvier 2024, v2.14.3 de Stirling PDF en août 2026 — et le gabarit v3 n'a pas de case
pour un fait qui se périme. Le lot 17 en a conservé un et perdu deux, sur le même lot : deux
traitements pour un même type de fait, ce qui n'est pas défendable longtemps.

## 8. Le tableau ne s'équilibre pas, et le sens du déséquilibre dit ce qu'est la brique

Le pilote comptait 17 cellules `Écarter si` vides sur 13 fiches et s'en inquiétait. La suite a
montré que **le déséquilibre s'inverse selon le matériau**, et qu'il est informatif :

- **vers la droite** — le lot 7 (3 cellules `Écarter si` vides contre 14 `Prendre si`), le
  lot 8 (six fiches dont cinq d'`Assistants/`), le lot 9 (`OmniRoute` : 4 raisons de le
  prendre contre 7 de l'écarter), le lot 17 (13 `Prendre si` vides contre 6). Ce sont les
  produits **jeunes** ou à forte surface de risque : licence absente, quota, permissions,
  chiffres auto-déclarés. *« La fiche d'un produit jeune penche structurellement vers le
  refus »* (lot 8) ;
- **vers la gauche** — le pilote et le lot 2, dont les dossiers sont des concurrents directs
  adossés à un comparatif : une fois les redirections parties, il ne reste qu'une ou deux
  bornes propres. `DBeaver` est le cas net : ses trois exclusions d'origine étaient toutes des
  redirections, il ne lui reste que l'empreinte mémoire de l'application Java.

Le lot 16 atteint **zéro cellule vide** sur 25 fiches, et prend soin de dire que ce n'est pas
un exploit de rédaction : ses cinq dossiers portaient des `Pièges` massivement faits de bornes
dures. **Aucune cellule n'a été comblée** dans aucun des dix-huit lots. C'est l'interdiction la
plus tenue du brief.

## 9. Le recouvrement fiche ↔ comparatif est toléré — et il se mesure

Le pilote signalait trois faits présents des deux côtés sur 18 fiches et demandait un
arbitrage : recouvrement toléré, ou fiche muette sur son propre discriminant ? Les lots ont
tous tenu « toléré », faute de réponse, et ont compté :

| Lot | Faits des deux côtés | Sur |
|---|---|---|
| pilote | 3 | 18 fiches |
| lot 1 | **13** | 17 fiches — six comparatifs pour 17 briques |
| lot 3 | 2 | 22 fiches |
| lot 6 | 6 | 24 fiches |
| lot 9 | **16** | 22 fiches |
| lot 11 | 3 | 19 fiches |

La règle est claire et elle se lit dans les chiffres : **plus un dossier est comparé finement,
plus le discriminant et la borne coïncident** (lot 1). Le lot 7 donne le contre-exemple utile —
recouvrement faible, parce que les comparatifs de ses dossiers ont été écrits au lot 5 sur un
axe **fonctionnel** quand ses `Écarter si` sont des bornes d'**exploitation** : les deux ne
parlent pas de la même chose et se lisent bien l'un après l'autre.

**Arbitrage rendu à l'intégration : recouvrement toléré**, et pour la raison que le lot 6
donne — *« une fiche muette sur sa propre borne dure oblige à ouvrir le comparatif pour savoir
ce qui mord »*. Les formulations diffèrent par construction : la fiche dit **ce qui va mordre**,
le comparatif dit **ce qui fait choisir**. C'est un coût réel, et il faut le nommer : une
quarantaine de paires à tenir d'accord dans le vault.

## 10. `complements:` — la règle 3 a refusé bien plus qu'elle n'a posé, et c'est le signe qu'elle marche

Le champ était **vide sur les 337 fiches** avant le lot 6. Il porte aujourd'hui **154
demi-arêtes sur 96 fiches**, soit 77 couples, tous réciproques.

Ce qui compte n'est pas ce compte, c'est le taux de refus. La règle 3 — *« un couple ne se pose
que si la fiche énonce l'appariement comme une recommandation »* — a écarté, lot après lot :

- **lot 6** : une dizaine de couples sur 24 fiches, dont `ZenML → MLflow, BentoML, KServe`,
  l'énumération même que la règle condamne. Deux couples déjà écrits ont été **défaits** après
  lecture de la règle ;
- **lot 7** : les six couples `LangGraph ↔ {CrewAI, AutoGen, OpenAI Agents SDK, Agno,
  smolagents, PraisonAI}`, écrits avant la règle et retirés après — ce que les fiches énoncent
  est du **positionnement**, pas un appariement. Conséquence assumée : `LangGraph` a désormais
  `alternatives: []` *et* `complements: []`, et c'est juste — sa fiche dit elle-même n'avoir
  aucun substitut direct ;
- **lot 9** : 19 fiches sur 22 gardent `complements: []`, six candidats écartés nommément ;
- **lot 10** : cinq refusés, un seul posé — *« c'est un domaine où les briques se substituent
  plutôt qu'elles ne s'apparient »* ;
- **lot 16** : quatre candidats de la même forme — la cible est une **dépendance embarquée**,
  pas une brique qu'on choisit d'apparier : `FastAPI → Pydantic`, `Flask → Jinja2`,
  `Dash → plotly`, `Gradio → FastAPI`.

Trois questions restent ouvertes, et elles sont posées par des lots différents sur des cas
différents :

1. **Une brique peut être à la fois alternative et complément.** Le lot 3 en compte cinq dans
   le seul serving (`BentoML` devant `Triton`, `KServe` avec `Triton` comme runtime,
   `ONNX Runtime` qui délègue à `TensorRT`), le lot 12 trois sur seize (`Modin`/`Dask`,
   `seaborn`/`matplotlib`, `pandas`/`numpy`), le lot 13 le cas le plus net —
   `Apache Iceberg`/`Parquet`, où l'appariement est réel et mutuel mais **impossible à poser**,
   chacune figurant en `Écarter si` de l'autre. Le modèle de données ne sait pas le dire.
2. **La dépendance de socle est-elle un complément ?** Le lot 4 s'est donné la règle
   « non » — *« sans cette règle, `PyTorch` héritait de neuf compléments, toutes les briques du
   vault qui importent `torch` »* — et le lot 3 mesure ce que « oui » coûterait : **huit** de
   ses 22 fiches dépendent de PyTorch.
3. **Le sourcing doit-il être des deux côtés ?** Le lot 11 pose 11 couples sur un sourcing
   unilatéral, et dit précisément lesquels tomberaient sous la lecture stricte : six sur onze.
   Le lot 17 fait l'inverse et refuse `PyJWT → FastAPI` pour cette raison exacte. Les deux
   lectures coexistent aujourd'hui dans le vault.

`check_brain.py` ne contrôle **pas** la réciprocité de `complements:` — seul `alternatives:`
la porte. Une moitié orpheline ne casse rien et ne se voit pas ; c'est ce qui a produit la
remontée suivante.

## 11. Les treize moitiés de couple, refermées à l'intégration

Le protocole demandait de poser sa moitié et d'inscrire l'autre dans ses remontées quand la
cible était hors périmètre. Douze moitiés sont restées ouvertes à l'arrivée, mesurées par un
script qui relit les 337 frontmatter et compare A → B à B → A :

| Moitié ouverte | Posée par | Cible du ressort de |
|---|---|---|
| `Evidently → MLflow` | lot 6 | lot 5 |
| `LangChain SQL agent → LangChain` | lot 9 | lot 10 |
| `MongoDB → MongoDB Compass` | lot 1 | **personne** — le pilote était déjà clos |
| `Redis → Redis Insight` | lot 1 | **personne** — idem |
| `SQLModel → FastAPI`, `SQLModel → Pydantic` | lot 1 | lots 16 et 14 |
| `TimescaleDB → Postgres`, `psycopg2 → Postgres` | lot 1 | lot 2 |
| `connectorx → Polars` | lot 13 | lot 12 |
| `jupysql → DuckDB` | lot 14 | lot 1 |
| `plotly → Dash` | lot 12 | lot 16 |
| `xarray → Dask` | lot 12 | lot 15 |

S'y ajoute le seul couple dont **aucun lot n'était propriétaire** : `txtai ↔
sentence-transformers`, ouvert par le lot 2 et posé à l'intégration des deux côtés.

Les treize sont fermées. 14 puces posées sous `### Compléments`, pitch courant de la source
réinjecté ; cinq figuraient déjà en `## Voir aussi` et ont été **déplacées**, pas dupliquées —
précédent posé par le lot 2 sur `pgAdmin` et `MySQL Workbench`. **Asymétries restantes : 0.**

Les deux lignes `MongoDB Compass` et `Redis Insight` méritent d'être vues pour ce qu'elles
sont : le pilote les avait déléguées au lot 1, le lot 1 a posé sa moitié, mais les cibles
étaient dans les dossiers du pilote, **déjà clos et poussés**. Aucun lot restant ne pouvait les
reprendre. C'est le trou que le parallélisme creuse quand un lot passe en premier : il n'a
personne derrière lui pour refermer.

Un arbitrage assumé : le lot 16 refusait `Dash → plotly` comme dépendance embarquée, le lot 12
avait posé `plotly → Dash` en jugeant la réciprocité sourcée des deux côtés. La moitié ouverte
se ferme ; la question générale du lot 16 part au lot 8, avec ses trois autres cas.

## 12. Une brique qui se place AU-DESSUS d'une autre n'en est pas une alternative

Trois fiches du seul lot 7 déclarent en `alternatives:` ce que leur propre texte dit ne pas en
être :

> « **Aucune** des pages ci-dessous n'est un équivalent : t3code se place **au-dessus** de ces
> outils, pas à côté d'eux. » — `t3code`, dont le frontmatter porte
> `alternatives: [Cline, Aider, Continue, Maka]`

`Spec Kit` et `BMAD` sont dans le même cas, et le lot 5 avait déjà dû l'écrire à la main dans
un comparatif (« il pilote, il ne code pas »). Le lot 4 en donne la variante symétrique :
`PyTorch Lightning` et `accelerate` déclarent `DeepSpeed` en `alternatives:` alors que les
trois fiches disent que c'est un **backend**.

Aucun n'a été corrigé, et pour la même raison à chaque fois : défaire une déclaration
réciproque d'`alternatives:` touche la section `### Alternatives` des deux fiches et la
règle R11, ce qui est un ré-arbitrage éditorial et non une conversion de format. **À trancher
hors du lot 6** — le vault en compte au moins six occurrences.

## 13. Le vocabulaire fermé de `## Ressources` manque d'une étiquette

Les lots 16 et 17 ont écrit **quatre puces `- Site —`** hors du vocabulaire du gabarit :
`opencut.app`, `superwhisper.com`, `sniffnet.app`, `getcroc.com` — des sites officiels de
projet, distincts de la doc et du dépôt. Les étiqueter `Documentation` aurait produit deux
puces homonymes sur la même fiche ; les supprimer aurait perdu une URL officielle. Le lot 7 a
rencontré le même besoin et a choisi l'autre voie, `- Documentation — https://t3.codes (site
du projet)`, ce qui donne bien deux lignes `Documentation` sur `t3code`.

Les deux conventions coexistent donc dans le vault. Le lot 3 signale un besoin voisin — une
étiquette `Licence`, l'AGPL étant **le** critère de choix d'`Ultralytics YOLO`, dont la page
de termes est une troisième URL.

Deux cas dégénérés, fréquents et traités de trois façons différentes : `url_docs == url_repo`.
Le lot 2 écrit une seule ligne `Dépôt` « qui tient lieu de documentation », le lot 16 écrit
`- Documentation — le README du dépôt ; il n'existe pas de site séparé`, le lot 6 n'écrit que
`Dépôt`. À unifier au lot 8.

Contre-mesure heureuse à la « réserve connue » du brief : parce qu'`url_repo` est renseigné
presque partout, `## Ressources` porte au minimum **deux** puces là où l'ancienne `## Liens`
n'en portait souvent qu'une. La section n'est pas réduite à une ligne. Mais la réserve tient
sur le fond : sur les périmètres qui l'ont compté, **zéro** puce `Tutoriel`, `Article`,
`Papier`, `Cours` ou `Vidéo`. Le lot 9 mesure 42 puces sur 22 fiches, 22 « Documentation » et
20 « Dépôt ». Typer les liens n'a pas créé les tutoriels qui manquent.

## 14. `## Écosystème` quand `alternatives:` est vide — trois formes, aucune tranchée

Le gabarit ne dit pas ce que devient `### Alternatives` quand il n'y a pas d'alternative. Les
lots ont inventé trois réponses :

- **une puce unique qui dit pourquoi** — la plus répandue, et la meilleure : *« Aucune dans le
  brain : lifelines est la seule bibliothèque d'analyse de survie répertoriée, et son pendant
  ML, scikit-survival, n'y figure pas encore. »* (lot 15, 3 fiches ; lot 4, 4 fiches ; lot 13,
  3 fiches ; lot 17, 11 fiches) ;
- **de la prose sous `### Alternatives`** (lot 9, `RAGatouille`) ;
- **pas de section `## Écosystème` du tout** — lot 14 sur `Ruff`, `Obsidian` et `Quarto,` et
  lot 5 sur `imbalanced-learn`. Quatre fiches sur 337.

Rien ne le vérifie : `check_brain` ne contrôle `### Alternatives` que si `alternatives:` est
non vide. **`## Écosystème` est-elle obligatoire ?** Le lot 8 doit le dire, dans un sens ou
dans l'autre. La forme du lot 15 est la meilleure candidate à généraliser : elle nomme le
concurrent hors brain, ce qui est une information, et non l'absence, qui n'en est pas une.

## 15. Ce que la conversion a rendu visible : cinq comparatifs manquants, et l'angle mort de R8a

Un lot de conversion ne crée pas de comparatif — c'est le travail du lot 5, et la règle 1 le
lui interdit. Mais lire 337 fiches à la file fait apparaître les trous. Les lots en nomment
cinq, chacun avec son axe de départage déjà écrit :

| Manque | Signalé par | L'axe est déjà écrit |
|---|---|---|
| `ml/apprentissage-profond` — **8 briques** | lot 4 | quatre paragraphes « Nuance : … » faisaient mot pour mot le travail d'une section « Ce qui départage » : bas niveau contre structure imposée, moteur contre surcouche |
| `data/format` — 3 briques | lot 13 | Parquet contre Avro, colonnaire contre ligne ; Iceberg au-dessus des deux |
| `data/synthetique` — 3 briques | lot 13 | Faker contre Mimesis, écosystème contre vitesse ; SDV apprend une distribution |
| `llm/assistant` — 5 briques | lot 8 | et `Comparatif - Frameworks LLM` les **exclut explicitement** par un commentaire de son filtre |
| `compute/a-la-demande` — 3 briques | lot 15 | Daytona, E2B, Modal partagent un dossier avec quatre moteurs sans partager leur vue |

Le cas du lot 4 est le plus coûteux : faute de comparatif, ses quatre « Nuance » ont dû être
**repliées en cellules `Écarter si`**, ce qui conserve l'information mais l'éclate en quatre
morceaux qui devront rester d'accord entre eux.

**L'angle mort de R8a, mesuré à l'intégration.** R8a vérifie qu'une *catégorie* a un
comparatif, pas que ses *briques* y entrent. Le décompte exact :

- **89 briques sur 337 (26 %) ne sont membres d'AUCUNE des 47 vues du vault** ;
- **51** relèvent des 13 catégories que R8a signale déjà ;
- **38 sont invisibles à R8a** — leur catégorie *a* un `.base`, elles n'y entrent pas.

Les 38 se répartissent sur 28 catégories, de `ml/tabulaire` (3 : Featuretools,
category_encoders, imbalanced-learn — le cas que le lot 5 avait trouvé) à `ml/vision` (3 :
Kornia, timm, torchvision — celui du lot 3). Le lot 5 propose la correction : **R8a devrait
aussi compter les briques d'une catégorie qu'aucune vue ne retient.**

Un sixième trou, d'une autre nature : le lot 14 a trouvé une redirection sans destination —
`pip → uv` sur la **vitesse**, quand la puce `uv` du comparatif parle d'absorption d'outils et
de `uv.lock`. Reformulée en borne dure de pip seul, ce qui conserve le fait. À trancher :
ajouter la vitesse au comparatif, ou considérer que la borne suffit. **L'intégration retient la
borne** — la fiche dit ce qui va mordre, et le comparatif n'a pas à redire toutes les bornes.

## 16. Une fiche qui nomme sa propre `categorie:` en prose se périme au renommage suivant

Motif systématique, trouvé indépendamment par quatre lots, et jamais signalé par aucun
validateur : **aucun ne contrôle qu'une catégorie citée en prose existe encore**.

| Lot | Fiches | Exemples |
|---|---|---|
| lot 17 | **5 sur 16** | `security/osint` → `security/recon` ; `network/transfer` → `network/transfert` ; `tooling/document` → `docs/pdf` |
| lot 16 | 4 sur 25 | `tooling/api` → `web/api` ; `tooling/video` → `media/video` |
| lot 10 | 2 sur 11 | deux catégories **fantômes** : `llm/context` et `tooling/llm` n'ont jamais existé dans la taxonomie |
| lot 8 | 1 | `OpenMAIC` consacrait trois paragraphes à `llm/app` contre `llm/framework` — **aucune des deux valeurs n'existe plus** |

Le lot 10 donne la bonne parade, et elle est meilleure que la correction : réécrire **sans
nommer aucune catégorie**. *« llmfit y est seul sur ce créneau — décider quel modèle une
machine peut tenir, sans le servir »* ne peut pas se périmer avec la taxonomie. Le gabarit v3
règle le problème par construction — le rangement est dérivé, il n'a plus à se justifier dans
le texte — mais il fallait aller retirer les justifications déjà écrites.

Balayage complet de l'arbre à l'intégration, après les dix-sept merges : **une seule** fiche
restait, `Observabilité/Loki.md`, qui citait `database/search` pour `database/recherche`.
Corrigée. Restent deux **notions** — `Contrats de données & qualité` et `Versionnage de
données` — qui citent `data/quality` et `data/versioning` : ce sont des pages `role: notion`,
on ne les réécrit pas sans demande de floSa.

Motif voisin, également vérifié à l'intégration : plus **aucun** corps de brique ne mentionne
le champ `status:`, supprimé au lot 2. Les lots 7 et 17 avaient trouvé et traité les trois
dernières occurrences.

## 17. 39 bandeaux à cellule vide — et la conjecture du pilote est fausse

`build_bandeau.py`, lancé sur le vault entier à l'intégration : **0 bandeau écrit, 337 déjà à
jour**. Les dix-huit conversations l'avaient donc lancé correctement, chacune bornée à son
périmètre. Le même passage nomme **39 bandeaux à cellule vide** — un champ absent du
frontmatter, jamais une valeur plausible : 34 en Maturité seule, 3 en Exécution + Maturité, 1
en Licence + Maturité, 1 en Nature + Exécution + Maturité.

Le pilote conjecturait que le trou était propre à `famille: application`, ses sept fiches
d'`Administration/` l'étant toutes. **Six lots l'ont testée et elle ne tient pas** : le lot 5
trouve `TensorBoard`, `famille: application`, avec sa maturité ; le lot 10 trouve `llmfit`,
`famille: cli`, sans ; le lot 15 trouve **tout** « Design & diagrammes/ » sans, trois familles
mélangées ; le lot 17 trouve trois familles différentes ; le lot 7 trouve les **13** fiches
d'`Agents de code/` sans, et aucune des 9 d'`Agents/`.

Le trou suit les **dossiers saisis sans ce champ** — Administration/, Agents de code/, Design &
diagrammes/, Médias/ — et les outils de poste de travail, toutes familles confondues. Le
combler est une décision éditoriale de floSa, pas une déduction de conversion.

Deux cellules vides disent en revanche quelque chose de **vrai**, et ne sont pas à
« réparer » : `swarm-forge` n'a pas de licence parce que son dépôt n'en déclare aucune — un
dépôt public sans fichier LICENSE n'accorde aucun droit d'usage —, et `Figma` n'a pas
d'Exécution parce que `famille: saas` sans `hosted:` ne dérive rien.

Un cas est plus dur, et le lot 14 le pose bien : **`Obsidian` n'a pas de `famille:` du tout**.
R14 contraint la valeur quand elle est présente et laisse passer l'absence ; la fiche échappe
donc à R14 *et* à R16, et perd deux colonnes de bandeau sur quatre. **`famille:` devrait être
requis**, pas seulement contraint.

## 18. Le protocole parallèle — ce qui a tenu, et les trois choses qui lui ont manqué

**Ce qui a tenu, et c'est l'essentiel** : dix-sept conversations simultanées, 322 fiches, zéro
collision, zéro conflit de merge, zéro fichier hors périmètre, dix-sept comptes conformes à la
table. Le découpage **par dossier** est ce qui l'achète — un compteur de fiches aurait coupé un
dossier en deux, et deux conversations auraient partagé un voisinage.

Trois manques, tous les trois signalés par les lots eux-mêmes :

1. **Une règle publiée pendant que dix-sept conversations tournent n'atteint que celles qui
   relisent le brief.** Le commit `98f4112` est arrivé en cours de route ; les lots 6, 7 et 8
   l'ont lu par `git show origin/main:…` — sans rebase ni merge, la règle 6 les interdisant —
   et l'ont appliqué. Les lots 1 à 5 avaient fini. **Rien dans le protocole ne demande de
   re-fetcher en cours de route** : c'est ce qui a produit les 53 renvois perdus de la
   remontée 2, et leur réparation à l'intégration.
2. **Un lot « niveau domaine » ne peut pas passer son dossier à `build_bandeau.py`.** Le lot 10
   l'a vu à temps : le scope du script est un chemin, traité en `rglob("*.md")`. Passer
   `"LLM & IA générative"` aurait réécrit les 132 pages des douze sous-dossiers, ceux des
   lots 7, 8 et 9 en train de tourner. **Rien ne refuse** — le dossier est bien dans le vault,
   il existe, il n'est pas de l'outillage. Les trois lots concernés (1, 10, 13) ont énuméré
   leurs fichiers. **À écrire dans le protocole**, pas seulement dans une remontée.
3. **Relever la ligne de base AVANT la première écriture.** Le lot 12 s'y est trompé une fois —
   premier relevé pris après avoir converti un dossier — et a dû la reprendre par
   `git checkout d8f81d6 -- <ses dossiers>`, relevé, puis `git checkout HEAD -- …`, son travail
   étant déjà commité. La gymnastique marche ; ne pas en avoir besoin marche mieux.

Un quatrième point n'est pas un manque du protocole mais un défaut d'outillage, signalé par le
lot 6 : **`AI/scripts/mesure_membres_bases.py` n'existe pas** — le script vit dans
`AI/migration/scripts/`, et la règle 2 le citait au mauvais chemin. Corrigé dans la règle. Le
sur-comptage que le lot 8 soupçonnait a été recoupé à la main par les lots 9, 11, 12, 14, 15
et 16 sur leurs propres cas : **aucun sur-comptage constaté**, hors le cas `ONNX Runtime` que
le lot 8 signale et qui reste à vérifier.

Un cinquième, de méthode : le lot 5 a réécrit sa première fiche **de zéro, frontmatter
compris**, et y a perdu une entrée d'`alternatives:`. Rattrapée avant validation, mais la
conséquence aurait été une **violation dure sur la branche d'un autre lot**, invisible depuis
la sienne. Les fiches suivantes ont été traitées par un script qui ne remplace que ce qui suit
le titre `# `. **Le lot 6 ne modifie pas le frontmatter, à la seule exception de
`complements:`** — et le plus sûr est de ne pas s'en donner la possibilité.

## 19. Ce que l'intégration a tranché

Cinq questions que les lots avaient laissées ouvertes, et qui n'appartenaient à aucun d'eux.

1. **La règle 2 l'emporte sur les deux critères d'acceptation.** « Un wikilink dans chaque
   cellule `Écarter si` » et « aucune cible dans deux sections » supposent tous deux que la
   redirection a un comparatif d'accueil. Quand elle n'en a pas, **on garde l'information**.
   Les deux critères sont marqués comme non tenus ci-dessus, et partent au lot 8.
2. **`Écarter si` est réservé à ce qui disqualifie le choix** ; une contrainte d'exploitation
   qu'on subit ensuite va sous `Prérequis` de `## Mise en œuvre`. Le lot 9 avait raison contre
   les lots 5 et 11 ; quatre cellules déplacées, et la puce orpheline du pilote logée.
3. **Le recouvrement fiche ↔ comparatif est toléré.** La fiche dit ce qui va mordre, le
   comparatif ce qui fait choisir. Une quarantaine de paires à tenir d'accord : c'est le prix,
   il est assumé, et il est écrit.
4. **Les treize moitiés de couple `complements:` sont fermées**, y compris les deux dont aucun
   lot n'était propriétaire et le couple `txtai ↔ sentence-transformers`, ouvert par le lot 2
   et posé ici des deux côtés.
5. **Les 53 renvois perdus par les six lots d'avant `d8f81d6` sont revenus sur la fiche.**
   Mesure avant / après, par script, sur les puces d'origine relues à leur commit.

Ce que l'intégration n'a **pas** fait, et pourquoi : les 54 renvois qui restent en `Écarter si`
alors que leur cible est co-membre (lot 4 : 24, lot 6 : 19, lot 5 : 5, lot 2 : 4, lot 15 : 1)
n'ont pas été retirés. Les retirer supprimerait de l'information d'une fiche pour satisfaire un
critère qui vient de céder. C'est le recouvrement du point 3, vu depuis l'autre bout.

## 20. État final du lot 6

| | Compte |
|---|---|
| fiches `role: brique` au gabarit v3 | **337 / 337** |
| portant `## Définition`, `Prendre si / Écarter si`, `Mise en œuvre`, `Ressources`, `Voir aussi` | **337** |
| portant `## Écosystème` | 333 — quatre fiches sans alternative ni complément (cf. remontée 14) |
| portant `## Retours` | **0**, et c'est conforme : le vault n'a aucune entrée datée |
| portant une section de l'ancien gabarit | **0** — les neuf noms cherchés, `## Alternatives` en `##` compris |
| bandeaux concordant avec leur frontmatter | **337 / 337** |
| `check_brain.py` | **0 violation dure, 28 avertissements** (149 avant) |
| `check_arbo.py` | vert |
| liens non résolus | 0 sur 764 pages |

**Les 121 avertissements fermés sont tous des R15**, et le solde se lit ligne à ligne :

| Règle | Avant (`d8f81d6`) | Après | Écart |
|---|---|---|---|
| R15 — aucun lien vers une notion ou un hub | 121 | **0** | **−121** |
| R8a — catégorie sans comparatif | 13 | 13 | 0 |
| R5 — collisions d'alias | 13 | 13 | 0 |
| R8d — filtre `.base` par liste de noms figée | 1 | 1 | 0 |
| R8b — comparatif à moins de deux membres | 1 | 1 | 0 |
| **Total** | **149** | **28** | **−121** |

Aucun avertissement n'a été **créé**. Les 28 restants sont un passif connu et documenté, dont
aucun n'est du ressort d'un lot de format : 13 collisions d'alias sont du frontmatter (les lots
3, 7, 8, 10, 13 et 14 les ont chacun signalées sans y toucher, la consigne étant de ne modifier
que `complements:`), 13 R8a sont des comparatifs à écrire, R8b et R8d sont deux dettes du
lot 5 déjà documentées sur leurs pages.

**Les critères d'acceptation du brief**, relus un par un :

- ✅ aucune fiche ne porte plus `Pourquoi`, `Quand l'utiliser`, `Quand NE PAS l'utiliser`, les
  **trois** noms de la section déploiement, `Pièges` ni `Liens` ;
- ❌ **chaque cellule `Écarter si` contient un wikilink** — 26 %, et le critère est
  inatteignable (remontée 3) ;
- ✅ chaque puce de `Ressources` porte une étiquette — dont quatre `Site`, hors vocabulaire
  (remontée 13) ;
- ✅ `Mise en œuvre` porte ses cinq étiquettes, sur les 337 ;
- ❌ **aucune cible dans deux sections** — impossible sans comparatif d'accueil, et conforme
  sous la lecture « listes de liens » du lot 9 (remontée 4) ;
- ✅ `## Définition` ne recontient ni la famille, ni la licence, ni la maturité — vérifié par
  script contre le bandeau **rendu** et non contre les valeurs brutes, les lots 4, 10, 14 et 15
  ayant tous montré que « production », « paquet » et « open-source » sont des mots français
  ordinaires (remontée à retenir : ce test ne se scripte que pour `beta`, `experimental` et
  `deprecated`) ;
- ✅ `check_brain.py` au vert.

**Ce qui part au lot 8** est nommé dans `AI/migration/lot-8-durcissement.md`. **Ce qui est du
contenu et non du format** part au backlog d'enrichissement : les cinq comparatifs manquants
(remontée 15), les six déclarations d'`alternatives:` que leur propre fiche dément
(remontée 12), les 39 champs de frontmatter vides (remontée 17), et les briques nommées mais
non fichées — `psycopg 3` et `asyncpg` (lot 1), `scikit-survival` (lot 15), `verl` et `OpenRLHF`
(lot 8), les onze solveurs de `PuLP` (lot 17).
