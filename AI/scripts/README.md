---
type: doc
created: 2026-05-21
modified: 2026-09-08
tags: [doc, scripts, audit]
---

# AI/scripts — l'outillage du vault

Depuis le **lot 9 de BrainKit** (2026-09-08), le DevBrain est une **instance** du
kit : il ne porte plus son outillage, il le **lit**. Les deux validateurs et les
quatre générateurs de ce dossier sont devenus des **ponts** — une vingtaine de
lignes chacun, qui résolvent la racine du kit, chargent `brain.yml` et appellent
BrainKit. Aucune ligne du kit n'est copiée ici.

`brain.yml`, à la racine du vault, est la **seule source** des valeurs : les 20
préfixes de domaine et leurs 47 sous-libellés, les 9 familles, le seuil de
promotion, les gabarits de frontmatter par rôle, les quatre colonnes du bandeau,
les dix règles et leur sévérité. Un libellé qui manque s'ajoute **là**, plus dans
une table Python.

## Comment ce vault atteint le kit

Tout est écrit dans [`_pont_kit.py`](_pont_kit.py), et se résume à trois pistes,
essayées dans cet ordre :

1. `$BRAINKIT_RACINE`, si la variable est posée ;
2. `AI/scripts/brainkit/` — une instance **figée**, où `brainkit freeze` a copié
   le kit dans le vault (livraison on-prem, plus aucun correctif) ;
3. le **voisinage** : `<parent>/BrainKit`, en remontant depuis la racine du
   vault. C'est le cas nominal — les deux dépôts côte à côte sous `Projets/` — et
   c'est aussi ce qui fait marcher un worktree, qui vit trois niveaux plus bas.

Si aucune ne répond, les ponts **s'arrêtent en 2** et disent les trois pistes.
Ils ne devinent pas : un kit deviné est un verdict rendu par un code qu'on n'a
pas choisi.

## Les six ponts

| Fichier | Ce qu'il appelle | Ce qu'il contrôle ou produit |
|---|---|---|
| [`check_brain.py`](check_brain.py) | `brainkit valider` | le **contenu** : frontmatter, énumérations, réciprocité, résumés réinjectés, liens. Sort en 1 sur une violation dure |
| [`check_arbo.py`](check_arbo.py) | `brainkit valider`, restreint | la **structure** : `chemin_categorie`, `hub_par_niveau`, `frontmatter_lisible` |
| [`build_index.py`](build_index.py) | `brainkit generer --quoi index` | `AI/index/brain-index.json` et `brain-index.md` |
| [`build_mocs.py`](build_mocs.py) | `brainkit generer --quoi hubs` | les zones `<!-- AUTO -->` des 74 hubs, `Métiers/`, `Comparatifs.md` |
| [`build_links.py`](build_links.py) | `brainkit generer --quoi liens` | `AI/index/liens.md`, dont la section « à créer » |
| [`build_bandeau.py`](build_bandeau.py) | `brainkit generer --quoi bandeau` | les zones `<!-- AUTO:BANDEAU -->` des 337 briques |

Plus une **bibliothèque**, [`arbo.py`](arbo.py) : la dérivation
`categorie:` → chemin, que `enrichir-brain` importe pour savoir où ranger une
page avant de l'écrire. Son API publique — `domaine()`, `promotions()`,
`dossier_attendu()` — n'a pas changé ; ses trois tables sont désormais dans
`brain.yml`.

Les quatre générateurs prennent `--check` : ils n'écrivent alors rien et sortent
en **2** s'il reste un écart. C'est la forme vérifiable du contrat *ce qui est
généré n'est jamais édité à la main*.

```bash
# La séquence de clôture. Le skill `cloturer-brain` la porte en entier —
# ceci n'est qu'un rappel de ce qu'elle lance.
uv run AI/scripts/build_index.py
uv run AI/scripts/build_mocs.py
uv run AI/scripts/build_bandeau.py
uv run AI/scripts/build_links.py
uv run AI/scripts/check_brain.py            # doit finir par « OK — aucune violation dure. »
uv run AI/scripts/check_arbo.py
uv run AI/scripts/build_bandeau.py --check  # doit sortir en 0
```

Le kit s'utilise aussi directement, depuis la racine du vault — il y trouve
`brain.yml` tout seul :

```bash
uv run --project ../BrainKit brainkit valider
uv run --project ../BrainKit brainkit generer --check
uv run --project ../BrainKit brainkit mesurer
```

`mesurer` n'a **pas** de pont, et c'est délibéré : il ne fait partie d'aucune
boucle de travail du vault. Il sert quand on se demande ce qu'une règle coûterait
si on la durcissait, et cette question se pose à la main.

## Les autres scripts — propres au vault, pas au kit

Ils n'ont **rien à voir avec BrainKit** et le lot 9 ne les a pas touchés.

| Script | Quand l'utiliser | Sortie |
|---|---|---|
| `query_index.py` | interroger `brain-index.json` par rôle, famille, nom | terminal |
| `stop_check_brain.py` | hook `Stop` de Claude Code — lance `check_brain.py` si la session a touché une page ; silencieux quand c'est vert | `systemMessage` |
| `session_to_devbrain.py` | hook `Stop` — écrit le résumé de session | `AI/sessions/…` |
| `verifier_fraicheur.py` | vérifier la fraîcheur des fiches (versions, dépôts) | `AI/index/fraicheur.json` |
| `audit_mesures.py` | audit des mesures citées dans les fiches | terminal |
| `list_reservoir.py`, `sync_reservoir.py` | le réservoir v1, hors du vault | terminal |
| `audit-vault.ps1`, `report-ghosts.ps1`, `find-connexes.ps1`, `discover-links.ps1`, `audit-links.ps1`, `add-wikilinks.ps1`, `gen-stubs-batch.ps1` | audits PowerShell hérités de la v2 | `AI/audits/…` |

> Les sept scripts PowerShell parlent encore de « galaxies », de `Services/` et
> de `Wiki/` — un vocabulaire et une arborescence qui n'existent plus depuis la
> clôture du lot 4 de la migration v3. Ils n'ont pas été touchés par le lot 9,
> dont l'interdiction est explicite : *un problème hors périmètre s'écrit dans
> les Remontées et ne se corrige pas.* Cf. `AI/migration/lot-9-brainkit.md`.

## Conventions communes

- **Périmètre de lecture** : déclaré une seule fois, dans `brain.yml`, bloc
  `genere.non_pages`. Les ponts n'ont plus chacun leur liste d'exclusions.
- **Encodage** : UTF-8 partout, y compris la sortie console sous Windows.
- **`--link-mode=copy`** est obligatoire pour `uv` sur ce poste : le vault vit
  sur OneDrive, où `uv` échoue à poser ses hardlinks de cache (os error 396).
  C'est déjà le cas dans `.claude/settings.json` pour le hook `Stop`.
