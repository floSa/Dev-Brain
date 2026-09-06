# DevBrain — Enrichir le brain

Comment ajouter une techno ou un concept, et ce que ça déclenche autour. Pour lire le vault,
va dans [manuel-utilisateur.md](manuel-utilisateur.md).

---

## 1. Tu ne crées pas une page, tu déclenches une propagation

C'est le point que la v3 a réglé et qu'il faut avoir en tête : **une page ne s'ajoute jamais
seule**. Une brique nouvelle change au moins cinq autres choses, et si on ne les change pas
le vault ment.

Le skill `enrichir-brain` porte cette règle. On l'appelle en langage naturel, depuis Claude
Code lancé **dans le dossier du vault** :

```
ajoute Qdrant au brain
documente le Change Data Capture
mets à jour DevBrain    ← balayage de fin de conversation
```

---

## 2. Ce que le skill fait, et que tu n'as pas à faire

| Ce qui bouge | Pourquoi |
|---|---|
| La page demandée | évidemment |
| **La notion du dossier** | une brique sans le concept qu'elle implémente est une impasse |
| **Le comparatif du dossier** | il se remplit seul par sa requête, mais sa section « Ce qui départage » ne se remplit pas seule |
| **Les briques pairs** | `alternatives:` est réciproque : si A cite B, B doit citer A |
| **Le hub du dossier et ses parents** | leur zone AUTO se régénère, leur corps peut devoir changer |
| **L'index** | `build_index`, `build_mocs`, `build_links` |

**Le rayon d'une insertion, c'est le dossier d'accueil plus ses hubs parents.** Rien de plus,
rien à deviner à partir des tags : le voisinage d'une page, c'est `ls` de son dossier. C'est
tout ce que l'arbre de la v3 achète.

---

## 3. Les deux valeurs que tu ne devines jamais

Une brique porte **deux** axes de rangement, et aucun des deux ne se choisit à l'intuition :

- **`categorie:`** — le domaine, *de quoi ça parle*. 94 valeurs en 20 préfixes.
- **`famille:`** — la nature technique, *ce que c'est*. 9 valeurs fermées : `paquet`,
  `plateforme`, `application`, `cli`, `saas`, `extension`, `specification`, `modele`,
  `annuaire`.

`Documentation/general/taxonomie.md` porte un **arbre de décision déterministe** : questions
fermées, en ordre strict. On le suit, on ne tranche pas au jugé. Les deux champs sont des
règles dures du validateur et sont indexés.

Un troisième champ, **`role:`**, dit ce que la page *est* — voir le manuel. `famille:` est la
nature technique (est-ce un paquet ou une plateforme ?), `role:` est la nature éditoriale
(est-ce une brique ou une notion ?). Les deux ne se recouvrent pas.

---

## 4. La frontière à connaître : `role: notion`

Une page `role: notion` est **la mémoire perso de floSa**. Elle n'est pas dans un dossier à
part — elle vit à côté des briques, et rien dans le chemin ne la signale. **La frontière se
lit dans le frontmatter, page par page, avant d'écrire.**

- **Créer** une notion : normal, dès qu'une capture en a besoin. `enrichir-brain` écrit la
  brique et sa notion du même geste.
- **Modifier** une notion existante : sur demande explicite. Sinon on propose, on attend.
- **Supprimer** : jamais sans accord.

---

## 5. Mettre à jour une page qui existe

Jamais un patch improvisé. Un champ modifié a des consommateurs :

| Champ modifié | Qui le lit |
|---|---|
| `alternatives:` | les lignes `## Écosystème` des pages citées, en réciproque |
| `categorie:` | le chemin lui-même — la page **déménage** |
| `pitch:` | le bandeau généré, les vues `.base`, les hubs |
| `maturite:`, `licence_type:` | le bandeau, les vues `.base` |

La *Procédure — mode mise à jour* de `.claude/skills/enrichir-brain/SKILL.md` donne pour
chaque champ la liste de ses consommateurs et la commande de vérification.

---

## 6. Clôturer — la seule étape qu'on ne saute pas

**Toute** écriture dans une page du brain se clôt par le skill `cloturer-brain` :

```
cloture le brain
```

Il régénère les artefacts dérivés, passe `check_brain.py` **et** `check_arbo.py` au vert,
vérifie la divergence avec `origin/main`, puis commite et intègre. C'est le **seul** endroit
où la politique git du vault est écrite.

Une exception, et une seule : la **règle d'identité git** vit aussi dans `CLAUDE.md`, parce
qu'elle doit être lue dans chaque conversation. Le dépôt est perso ; l'adresse annoncée par
l'outil est l'adresse pro et n'attribue jamais un commit. Trois hooks versionnés le font
respecter mécaniquement, et un hook qui refuse n'est pas un incident à contourner.

---

## 7. Ce qu'on n'écrit pas

- **Rien qui ne soit sourcé.** Une cellule sans source dans la fiche d'origine reste vide et
  se signale. 337 fiches remplies de plausible seraient pires que 337 fiches vides.
- **Aucune `categorie:` hors de `taxonomie.md`.** Une famille nouvelle se pose dans le
  document de taxonomie, pas dans l'arborescence.
- **Aucun `rm` improvisé.** Un déplacement se fait par `git mv`, sans quoi l'historique de la
  page est perdu.
