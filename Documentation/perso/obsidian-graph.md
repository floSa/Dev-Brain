---
galaxie: meta
nom: obsidian-graph
type: perso
created: 2026-06-04
modified: 2026-06-09
tags: [meta, perso, obsidian]
---

# Explorer le brain dans Obsidian

But : naviguer du général au précis (domaine → sous-domaine → fiche), et repérer les niveaux à la couleur.

## 1. Code couleur du graphe

Depuis le lot 2 de la migration v3, la couleur se lit sur `role:` — le champ qui porte la
**nature** de la page. `galaxie:` a été supprimé : il ne servait qu'à ça, et il le faisait
moins bien (il ne distinguait ni un hub d'une notion, ni un comparatif d'une brique).

| Élément | `role:` | Requête | Couleur |
|---------|---------|---------|---------|
| **Métiers** transverses (Data Science, ML Eng, AI Eng, MLOps, Data Eng) | `hub` | `path:Métiers/` | 🟡 or |
| **Hubs** — la page d'un dossier, l'aiguillage | `hub` | `["role":"hub"]` + `path:MOC/` | 🟠 orange |
| **Briques** — ce qu'on déploie ou importe | `brique` | `["role":"brique"]` | 🔵 bleu |
| **Notions** — ce qu'il faut comprendre | `notion` | `["role":"notion"]` | 🟢 vert |
| **Comparatifs** — ce qui départage plusieurs briques | `comparatif` | `["role":"comparatif"]` | 🔴 rouge |
| **Patterns** et **Rules** | `pattern`, `rule` | `["role":"pattern"] OR ["role":"rule"]` | ⚪ gris |

Le bleu et le vert sont **exactement** ceux des anciennes galaxies `dev` et `wiki` : ce sont
les mêmes pages, elles ne changent que de nom de champ.

L'ordre des règles compte : `path:Métiers/` passe **avant** la règle `hub`, sinon les cinq
axes métier prendraient l'orange des hubs — ce sont eux aussi des `role: hub`.

Deux rôles n'ont encore aucune page : `hub` naît au lot 3 (avec l'arborescence), `comparatif`
au lot 5 (quand les `.base` deviennent des pages). Leurs règles sont posées d'avance — elles
ne colorent rien pour l'instant, et coloreront le jour même sans qu'on y retouche. En
attendant, `path:MOC/` tient le rôle de hub.

Bloc exact (clé `colorGroups` de `.obsidian/graph.json`) :

```json
"colorGroups": [
  { "query": "path:Métiers/",              "color": { "a": 1, "rgb": 16766011 } },
  { "query": "[\"role\":\"hub\"] OR path:MOC/", "color": { "a": 1, "rgb": 16749099 } },
  { "query": "[\"role\":\"brique\"]",        "color": { "a": 1, "rgb": 4271325 } },
  { "query": "[\"role\":\"notion\"]",        "color": { "a": 1, "rgb": 8042496 } },
  { "query": "[\"role\":\"comparatif\"]",    "color": { "a": 1, "rgb": 15680580 } },
  { "query": "[\"role\":\"pattern\"] OR [\"role\":\"rule\"]", "color": { "a": 1, "rgb": 9741240 } }
]
```

Vérification des entiers : `16766011` = `#FFD43B` (or) · `16749099` = `#FF922B` (orange) ·
`4271325` = `#412CDD` (indigo, ex-`galaxie: dev`) · `8042496` = `#7AB800` (vert olive,
ex-`galaxie: wiki`) · `15680580` = `#EF4444` (rouge) · `9741240` = `#94A3B8` (gris).

Deux règles de l'ancien bloc ont été **retirées**, et non transposées :

- `path:AI/skills/` — ce dossier n'existe plus, les skills vivent sous `.claude/skills/`.
  Or Obsidian **n'indexe aucun dossier commençant par un point** : la règle ne pouvait pas
  fonctionner sous son nouveau chemin. Son entier valait de surcroît `14701138` = `#E05252`,
  un rouge — il serait entré en collision frontale avec celui des comparatifs.
- `["galaxie":"meta"]` — le champ n'existe plus. Les pages de gouvernance (`Documentation/`,
  `AI/`) sont déjà hors du graphe par `userIgnoreFilters` (cf. lot 0).

> ⚠️ `.obsidian/graph.json` est **gitignoré** → cette config est **locale par machine**, pas
> versionnée. Ce tableau est donc la **seule** source de vérité des couleurs du graphe : à
> réappliquer à la main sur chaque poste. L'extrait CSS `.obsidian/snippets/roles.css`, lui,
> est versionné — il colore l'explorateur, les onglets et le badge de propriété, pas le graphe.

## 2. Hiérarchie de navigation (MOC)

Les pages hub sont générées par `AI/scripts/build_mocs.py` sur 3 étages :
- **`Métiers/`** — un par axe métier (`data-sci`…). Pointe vers les **sous-hubs**, pas vers les ~100 feuilles.
- **`MOC/Concepts/`** — un par sous-domaine de concept encore sous `Wiki/`. **Étage en voie d'extinction** : le lot 4 le vide famille par famille, et il n'en reste qu'**une** au 2026-09-05, `Machine learning (notions)`, dernière famille non rangée. Liste ses feuilles.
- **les hubs de l'arbre** — un par dossier de domaine et de sous-domaine (`Bases de données`, `Machine Learning`…), zone `AUTO` remplie depuis le contenu du dossier. Ils ont remplacé `MOC/Categories/`, vide depuis le lot 3.

Résultat : `Data Science` → `Machine Learning` / `Statistiques & inférence` / … → feuilles. On descend par étages au lieu de noyer l'écran. Les deux premiers étages pointaient vers `MOC/Concepts/` tant que les notions vivaient sous `Wiki/` ; ils pointent vers les hubs de l'arbre à mesure que le lot 4 les descend.

## 3. Se balader en profondeur (graphe local)

1. Ouvre une note → clic droit → **« Ouvrir la vue graphique autour du fichier courant »** (= graphe **local**).
2. **Ancre ce panneau à droite** (glisse l'onglet) : page à gauche, graphe à droite. Il **suit la note active**.
3. Roue ⚙️ → curseur **Profondeur** (1 = enfants directs, 2+ = plus loin).
4. Navigation : **clic sur un nœud** = la page s'ouvre à gauche **et** le même graphe se re-centre dessus (on descend). **`Alt+←`** = on remonte.

## 4. Couleurs dans le graphe LOCAL (plugin)

Le graphe **local n'hérite pas** des couleurs du global (config séparée). Solution : plugin communautaire **« Sync Graph Settings »** (xallt).
- Installé + activé.
- Avec un graphe local actif : `Ctrl+P` → **« Sync Graph Groups Settings to Local Graph »** → applique les couleurs du global.
- À relancer pour un nouveau graphe local (assigner un raccourci clavier pour aller vite). Avec le panneau **ancré** (§3), une seule synchro suffit tant qu'il reste ouvert.

## 5. Bruit CRLF (git)

`git config core.autocrlf true` est posé sur le repo → Obsidian peut écrire en CRLF sans que git le voie comme une modification. Évite les faux « fichiers modifiés » qui bloquaient les `git pull`/FF.
