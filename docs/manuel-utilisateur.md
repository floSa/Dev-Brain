# DevBrain — Manuel d'utilisateur

Ce document explique **ce que tu as sous les yeux** quand tu ouvres le vault, et comment y
retrouver quelque chose. Pour l'installer, va dans [INSTALL.md](../INSTALL.md). Pour
l'enrichir, va dans [guide-enrichissement.md](guide-enrichissement.md).

---

## 1. Le vault en une phrase

**Un dossier par domaine à la racine, et une page qui dit ce qu'elle est.**

Il n'y a rien d'autre à comprendre. Pas de galaxie, pas de hiérarchie parallèle, pas de
dossier d'attente. 20 dossiers de domaine, plus trois dossiers que le domaine ne range pas —
`Métiers/`, `Patterns/`, `Rules/` — et `Comparatifs/`, qui ne range rien non plus mais
rassemble.

---

## 2. Les six natures de page

C'est le champ `role:` du frontmatter qui porte la nature d'une page. Il ne se devine pas
depuis le chemin : une notion et la brique du même sujet vivent dans le même dossier, et `ls`
ne les distingue pas.

| `role:` | Ce que c'est | La question à laquelle ça répond | Le test qui tranche |
|---|---|---|---|
| **brique** | un outil qu'on installe et qu'on fait tourner | « comment ça marche, qu'est-ce que ça coûte » | ça s'installe ? |
| **notion** | un concept qu'il faut comprendre | « c'est quoi, pourquoi » | ça ne s'installe pas, ça s'apprend |
| **comparatif** | ce qui départage plusieurs briques d'un même thème | « laquelle je prends ? » | il compare, il ne décrit pas |
| **hub** | la page d'aiguillage d'un dossier | « qu'est-ce qu'il y a là-dedans » | elle ne dit rien, elle oriente |
| **pattern** | un assemblage de briques déjà éprouvé | « comment on monte ça ensemble » | ça combine plusieurs briques |
| **rule** | une contrainte transverse à tous les projets | « qu'est-ce qu'on s'impose » | ça ne dépend d'aucun outil |

**Pourquoi ces mots-là.** « Brique » et « notion » ne sont pas jolis, ils sont *disjoints* :
une page est l'un ou l'autre, jamais les deux, et le test tient en une question. C'est ce qui
permet au validateur de contrôler le gabarit sans jamais avoir à interpréter.

Les couleurs du graphe sont ce même axe, en visuel : 🔵 briques, 🟢 notions, 🔴 comparatifs,
🟠 hubs, 🟡 métiers, ⚪ patterns et règles.

---

## 3. Où vit une page

**Personne ne choisit un dossier.** Le chemin se dérive du champ `categorie:` — le domaine,
94 valeurs regroupées en 20 préfixes. `AI/scripts/arbo.py` porte la dérivation,
`check_arbo.py` la vérifie, et aucune page n'y échappe.

Un sous-dossier apparaît quand un sous-domaine atteint **5 pages**, sauf s'il ne laisserait
aucune page au niveau du domaine — un dossier fils qui redouble son parent n'apporte rien.

```
Bases de données/                 ← le domaine
├── Bases de données.md           ← role: hub, porte le nom de son dossier
├── Vectoriel/                    ← sous-domaine promu (11 pages)
│   ├── Vectoriel.md              ← role: hub
│   ├── Qdrant.md                 ← role: brique
│   ├── Comparatif - Bases vectorielles.md    ← role: comparatif
│   └── Comparatif - Bases vectorielles.base  ← le moteur du tableau
├── Postgres.md                   ← une brique restée au niveau du domaine
└── Bases de données vectorielles.md          ← une notion, à côté des briques
```

---

## 4. Lire une fiche de brique

Une brique suit toujours le même gabarit. De haut en bas :

| Section | Ce qu'elle contient | Ce qu'elle ne contient pas |
|---|---|---|
| **Le bandeau** `<!-- AUTO -->` | Nature, Licence, Exécution, Maturité | rien d'écrit à la main — il est **généré** depuis le frontmatter |
| `## Définition` | 4 à 6 lignes de prose | ni la licence ni la maturité, elles sont au-dessus |
| `## Prendre si / Écarter si` | un tableau à deux colonnes | des redirections « pour X, prends Y » — ça, c'est le comparatif |
| `## Mise en œuvre` | cinq étiquettes fixes | de la prose |
| `## Écosystème` | `### Alternatives` (à la place) et `### Compléments` (avec) | — |
| `## Ressources` | liens externes, étiquetés | des liens vers le vault |
| `## Voir aussi` | liens internes — la notion parente, le hub, les pairs | des liens externes |

**Une cellule vide est un fait, pas un oubli.** Le lot 6 a converti les 337 fiches sous une
règle dure : rien ne s'écrit qui ne soit sourcé dans la fiche d'origine. Une case vide dit
« l'information n'existe pas », pas « on a oublié ».

---

## 5. Lire un comparatif

Deux fichiers portent le même nom : la **page** `.md` et le **moteur** `.base`.

- Le `.base` est une requête. Il liste les briques qui remplissent son filtre et affiche leur
  frontmatter en tableau. Il se remplit tout seul — une brique ajoutée y entre sans que
  personne ne touche au comparatif.
- La page embarque ce tableau, et ajoute ce que le tableau ne peut pas dire : la section
  **`## Ce qui départage`**. Une puce par brique, avec le fait qui la distingue.

C'est là qu'est la valeur. Le tableau dit que Neptune et MLflow sont tous deux en
`maturite: production` — c'est vrai et ça n'apprend rien. La page dit que Neptune a été
racheté et que son service s'arrête.

Les 47 comparatifs sont rassemblés par [[Comparatifs]], la page qui les liste par domaine.

---

## 6. Trouver quelque chose

Par ordre d'efficacité :

1. **Tu sais quoi chercher** → `Ctrl+O`, tape le nom. Les liens sont nus (`[[Postgres]]`),
   Obsidian résout par nom de fichier.
2. **Tu hésites entre deux outils** → ouvre le comparatif du dossier, va directement à
   `## Ce qui départage`.
3. **Tu explores un sujet** → ouvre le hub du domaine. Sa zone `<!-- AUTO -->` liste tout ce
   que le dossier contient ; son corps, écrit à la main, dit ce qui départage les
   sous-dossiers.
4. **Tu pars d'un métier** → `Métiers/` porte six axes (Data Science, Data Engineering,
   MLOps, ML Engineering, AI Engineering, Infrastructure & Ops). C'est le seul axe qui
   traverse l'arbre technique.
5. **Tu veux voir les liens** → le graphe, coloré par `role:`.

---

## 7. Ce qui est généré, et qu'on ne touche pas

| Quoi | Généré par |
|---|---|
| Les zones `<!-- AUTO -->` des hubs | `build_mocs.py` |
| Le bandeau en tête de chaque fiche | `build_bandeau.py` |
| `Métiers/` | `build_mocs.py`, depuis le champ `domaines:` |
| `Comparatifs/Comparatifs.md` | `build_mocs.py`, depuis `role: comparatif` |
| `AI/index/` | `build_index.py`, `build_links.py` |

Éditer l'un de ces blocs à la main, c'est écrire quelque chose que la prochaine régénération
effacera. Le **corps** d'un hub, lui, s'écrit à la main — c'est la zone AUTO qui est
intouchable, pas la page.
