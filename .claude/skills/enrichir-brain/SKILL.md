---
name: enrichir-brain
description: |
  Use this skill to capture knowledge into the DevBrain v2 (galaxies Dev/ and Wiki/).
  Triggers: "ajoute <techno/sujet> au brain", "documente <X>", "ajoute le service Y",
  "ajoute le concept Z", or, at the end of a conversation, "mets à jour DevBrain" /
  "enrichis le brain" (sweep mode). Creates the requested page AND the missing
  connected pages (parent concept, alternatives, comparatif), wires links, keeps
  alternatives and pitches in sync bidirectionally, then regenerates the index.
---

# Skill — enrichir-brain

Skill de **capture** du DevBrain v2. Implémente le workflow W1 de `AI/design/brain-v2.md` (§2, §7.1). Exigence cardinale : **faire les choses bien, sans rien oublier** — la page demandée *et* ses pages connexes, les liens, la synchro bidirectionnelle, l'index.

## Quand l'utiliser

- **Mode ciblé** : ajouter une brique précise. « ajoute Weaviate », « ajoute le concept bases vectorielles ».
- **Mode balayage** : en fin de conversation, « mets à jour DevBrain » → repérer tout ce qui mérite une page et tout traiter.

Distinct de :
- `planifier-projet` (consomme le brain pour cadrer un projet, n'écrit pas de fiches).

## Pré-requis

Mode build (pages Dev/) ou mode wiki (pages Wiki/). Ne jamais toucher au réservoir v1 (`Services/`, `Patterns/`, `Rules/`, `Bugs/` à la racine) — c'est de la référence en lecture seule.

## Appuis (à lire AVANT d'écrire)

- `AI/index/brain-index.json` — catalogue courant (pitch, tags, alternatives, categorie, galaxie). **Ne jamais le charger en entier** : l'interroger par tranches via `AI/scripts/query_index.py` (existence, candidats d'une catégorie, pages d'un tag). C'est la règle qui tient quand le brain devient grand — la sortie est bornée par le nombre de correspondances, pas par la taille du brain.
- `Documentation/general/tags.md` — vocabulaire de tags **fermé**. Piocher ici, ne jamais inventer.
- `Documentation/general/taxonomie.md` — catégories `categorie:` autorisées.
- `Documentation/general/themes.md` — vocabulaire `domaines:`.
- `Templates/Service-Dev.md`, `Templates/Concept-Wiki.md` — gabarits stricts (§5).

## Conventions v2 non négociables


- **Rangement par NATURE, pas par audience** : tout ce qui est **technique** → `Dev/` (jamais `Wiki/`). Brique à déployer (service, framework, lib, BDD) → `Dev/Services/` ; **outil technique** que l'on utilise (client GUI, CLI, utilitaire — DBeaver, pgAdmin, uv…) → `Dev/Outils/` (`galaxie: dev`, `categorie: tooling/<famille>`). `Wiki/` = **notions** (`Concepts/`) + **skills/extensions de pratique perso** (`Outils/` : Claude Code, Obsidian, MCP). Doute « Dev ou Wiki ? » → est-ce technique ? alors Dev.
- **Ton impersonnel** partout : ni « tu » ni « vous ». Phrases courtes, hiérarchie parties + bullets.
- **Frontmatter exact** selon le gabarit (§5) : ni plus, ni moins de champs.
- **Pitch unique** : chaque page Dev porte SON `pitch:` (une ligne), écrit une seule fois. La section *Alternatives* des autres pages **réinjecte** ce pitch tel quel. Une donnée, trois usages (frontmatter, alternatives, propositions de `planifier-projet`).
- **Liens qualifiés en cas de collision** : si un nom existe aussi dans le réservoir v1 (ex. `Services/VectorDB/Qdrant.md`), lier en `[[Dev/Services/Qdrant|Qdrant]]` pour viser le v2 sans ambiguïté. Sinon, lien nu.
- **Catégorie ou tag manquant → demander**, jamais inventer. L'ajout se fait d'abord dans `Documentation/general/`.
- **Faits vérifiés sur le web, d'office (sans demander la permission)** : avant d'écrire une fiche, vérifier en ligne (WebSearch / WebFetch) les champs factuels — `licence_type`, `langage`, `maturite`, `hosted`, `scaling`, `url_docs` / `url_repo`, statut actuel (actif / déprécié / racheté). Ne jamais demander l'autorisation de vérifier : le faire directement. Info introuvable ou ambiguë → laisser le champ vide, ne pas inventer.

## Procédure — mode ciblé

1. **Interroger l'état (par tranches, jamais l'index entier)** :
   - existence (nom + alias) : `uv run AI/scripts/query_index.py --name "<X>"` ;
   - candidats alternatives : `uv run AI/scripts/query_index.py --categorie "<cat>"` ;
   - vocabulaire de tags : `Documentation/general/tags.md` ; catégories : `taxonomie.md` (fichiers bornés).
2. **Vérifier l'existence** de la page (nom + `alias`). Si elle existe en v2 → proposer une mise à jour plutôt qu'une création. Si elle n'existe qu'en réservoir v1 → créer la version v2 (ne pas modifier le v1).
3. **Identifier les pages connexes nécessaires** :
   - concept parent côté Wiki (un service vectoriel → `Bases de données vectorielles`) ;
   - comparatif `.base` de la catégorie ;
   - alternatives à citer (même `categorie:`).
   Lister celles qui manquent.
4. **Vérifier les faits sur le web (d'office), puis créer / mettre à jour chaque page** depuis le bon gabarit :
   - service → `Templates/Service-Dev.md` dans `Dev/Services/` ;
   - concept → `Templates/Concept-Wiki.md` dans `Wiki/Concepts/`.
5. **Poser les tags** depuis `tags.md` uniquement. Besoin d'un tag absent → le proposer, l'ajouter au vocabulaire, puis l'utiliser.
6. **Câbler les wikilinks** dans les deux sens du couple Dev↔Wiki (le service lie son concept ; le concept liste le service dans *Approches voisines*), plus le `.base` du comparatif.
7. **Synchroniser bidirectionnellement** :
   - **Alternatives** : si A liste B, alors B doit lister A. Mettre à jour le frontmatter `alternatives:` **et** la section *Alternatives* de chaque page concernée.
   - **Pitches** : la ligne affichée pour une cible dans une section *Alternatives* doit être exactement le `pitch:` courant de cette cible. Re-synchroniser si un pitch a changé.
8. **Régénérer l'index puis valider** :
   ```bash
   uv run AI/scripts/build_index.py   # met à jour brain-index.json + brain-index.md (doc humain)
   uv run AI/scripts/build_mocs.py    # régénère les pages hub (MOC) — liens à jour, aucun oublié
   uv run AI/scripts/build_links.py   # carte des liens + sujets à créer (AI/index/liens.md)
   uv run AI/scripts/check_brain.py   # DOIT passer : réciprocité, liens, tags, catégorie, gabarit
   ```
9. **Corriger jusqu'au vert** : toute violation dure signalée par `check_brain` se corrige et on relance. Ne pas clore tant que ce n'est pas OK.
10. **Commit + push + intégration dans `main` (d'office, sans demander)** : `check_brain` vert → commit (Conventional Commits) → `git push` de la branche → **intégrer dans `main`** : `git -C <vault-principal> merge --ff-only <branche-courante>` puis `git -C <vault-principal> push origin main`. Fast-forward uniquement ; si la divergence empêche le FF, le signaler — jamais de `--force`. Ne jamais répondre « à toi de committer / merger ».

## Procédure — mode sujet / balayage (plan d'abord, PUIS go)

Déclencheurs : « fais-moi les pages sur les statistiques », « ajoute le sujet RAG », ou en fin de conversation « mets à jour DevBrain ».

1. **Cadrer le périmètre** → dresser la liste des pages candidates : concept(s) Wiki + services/patterns Dev. Pour chacune : nom, galaxie, type, catégorie pressentie, tags pressentis (du vocabulaire), alternatives pressenties, et si elle existe déjà (`query_index.py`). Au besoin, ouvrir l'ancienne page du sujet dans `Archive-v1/` (voir `Archive-v1/_inventaire.md`) pour en réutiliser le contenu.
2. **Présenter le plan et ATTENDRE le GO.** Ne rien créer avant validation. L'utilisateur ajoute / retire / renomme des pages.
3. **Écrire la file validée** dans `AI/backlog.md` (une page par ligne).
4. **Drainer la file une page à la fois**, chacune via la procédure ciblée ci-dessus. Cocher au fur et à mesure.
5. **Clôturer** : `build_index.py`, `build_mocs.py`, `build_links.py`, `check_brain.py` (doit passer), puis **commit + push + intégration dans `main` d'office** (cf. étape 10). Repassable tant qu'il reste des items → rien d'oublié.

## Anti-patterns

- Créer la page demandée mais oublier le concept parent ou la réciprocité des alternatives.
- Inventer une catégorie, un tag ou un score (le score n'existe plus en v2).
- Recopier un pitch divergent au lieu de réinjecter le `pitch:` de la cible.
- Modifier une fiche du réservoir v1.
- Oublier `uv run AI/scripts/build_index.py` à la fin.

## Voir aussi

- `planifier-projet` — consomme l'index produit ici.
- `AI/design/brain-v2.md` §2, §5, §7.1 — spec de référence.
