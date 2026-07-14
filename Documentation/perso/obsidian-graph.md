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

Quatre niveaux, repérables d'un coup d'œil :

| Élément | Requête | Couleur |
|---------|---------|---------|
| **Domaines** (Data Science, ML Eng, AI Eng, MLOps, Data Eng) | `path:MOC/Themes/` | 🟡 or |
| **Hubs** catégories + sous-hubs concepts (Bases de données, Statistiques, Maths du ML…) | `path:MOC/Categories/` et `path:MOC/Concepts/` | 🟠 orange |
| **Dev** (services, outils techniques) | `["galaxie":"dev"]` | 🔵 bleu |
| **Wiki** (notions / feuilles) | `["galaxie":"wiki"]` | 🟢 vert |

L'ordre des règles compte : `MOC/Themes` et `MOC/Categories/Concepts` sont **avant** la règle `galaxie:wiki` (les MOC sont techniquement `galaxie: wiki`, donc la règle de chemin doit primer pour les colorer en or/orange).

Bloc exact (clé `colorGroups` de `.obsidian/graph.json`) :

```json
"colorGroups": [
  { "query": "path:MOC/Themes/",     "color": { "a": 1, "rgb": 16766011 } },
  { "query": "path:MOC/Categories/", "color": { "a": 1, "rgb": 16749099 } },
  { "query": "path:MOC/Concepts/",   "color": { "a": 1, "rgb": 16749099 } },
  { "query": "path:AI/skills/",      "color": { "a": 1, "rgb": 14701138 } },
  { "query": "[\"galaxie\":\"dev\"]",  "color": { "a": 1, "rgb": 4271325 } },
  { "query": "[\"galaxie\":\"wiki\"]", "color": { "a": 1, "rgb": 8042496 } },
  { "query": "[\"galaxie\":\"meta\"]", "color": { "a": 1, "rgb": 16102400 } }
]
```

> ⚠️ `.obsidian/graph.json` est **gitignoré** → cette config est **locale par machine**, pas versionnée. À réappliquer sur chaque poste.

## 2. Hiérarchie de navigation (MOC)

Les pages hub sont générées par `AI/scripts/build_mocs.py` sur 3 étages :
- **`MOC/Themes/`** — un par domaine (`data-sci`…). Pointe vers les **sous-hubs**, pas vers les ~100 feuilles.
- **`MOC/Concepts/`** — un par sous-domaine de concept (`Statistiques`, `Maths du ML`, `Deep learning`, `NLP (notions)`, `Traitement du signal (notions)`…). Liste ses feuilles.
- **`MOC/Categories/`** — un par famille Dev (`Bases de données`, `Machine Learning`…).

Résultat : `Data Science` → `Statistiques` / `Maths du ML` / … → feuilles. On descend par étages au lieu de noyer l'écran.

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
