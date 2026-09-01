# Axe 5 — Navigation & exploitabilite

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-5-navigation.md`.

## Question centrale

Le brain a **deux consommateurs** aux besoins opposes : un humain qui navigue dans Obsidian
par le graphe et les MOC, et un agent (`planifier-projet`) qui filtre
`AI/index/brain-index.json` sans ouvrir les fiches. **Les sert-il vraiment tous les deux ?**

## Le probleme, tel qu'il est diagnostique

Cote humain : **19 pages ne sont citees par aucune autre**, dont **les 5 Patterns et les
5 Rules — 100 % de ces deux dossiers**. `build_mocs.py` genere 31 MOC (Categories, Concepts,
Themes) mais ne couvre ni `Dev/Patterns/` ni `Dev/Rules/`. Ces pages n'existent donc qu'a
condition d'en connaitre le nom : ni MOC, ni lien entrant, ni graphe local.

Cote agent : `brain-index.json` ne stocke que **dix champs**
(`path, nom, alias, type, galaxie, categorie, domaines, pitch, tags, alternatives`).
`planifier-projet` filtre la-dessus « sans lire 160 fichiers », puis n'ouvre la fiche
qu'apres selection. Une contrainte eliminatoire ecrite en corps de page alimente donc la
justification, **jamais le filtrage** — c'est deja l'entree 1 de `AI/ameliorations-devbrain.md`.

Cote themes : `build_mocs.py` ne construit les MOC de theme qu'a partir des pages
`galaxie: wiki` de categorie `concept/*`. Le `domaines:` des fiches Dev est **inerte** :
le theme `infra-ops`, cree le 2026-09-02 et pose sur trois fiches Dev, n'a produit aucune MOC.

## Faits de depart (cf. `mesures-<date>.md`, a relancer)

- 647 pages, 31 MOC generees, 19 orphelins.
- 5 Patterns, 5 Rules, tous orphelins.
- 1 seule fiche REX (voir axe 6, ne pas empieter).
- `AI/index/liens.md` signale **189 tags sans page concept** : un tag existe, aucun concept
  Wiki ne le porte — donc aucun point d'entree thematique pour ce sujet.
- 75 tags employes une seule fois sur 321.

## Questions a instruire

1. **Le chemin d'acces de chaque type de page.** Pour chacun des 6 types
   (`service`, `outil`, `concept`, `pattern`, `rule`, `rex`), decrire par quel chemin un humain
   qui ne connait pas le nom de la page peut y arriver. Un type sans chemin est un type
   invisible.
2. **Les orphelins : defaut de contenu ou de generation ?** Trancher pour chacun des 19, et
   dire si `build_mocs` doit couvrir Patterns et Rules (et sous quelle forme : une MOC par
   dossier, ou une integration dans les MOC de categorie existantes).
3. **Les 189 tags sans concept.** Est-ce un manque de pages Wiki, ou des tags trop fins qui
   n'auraient jamais du entrer au vocabulaire ? Les 75 tags a usage unique sont un indice.
   Attention : ne pas empieter sur l'axe 1, ici on parle de **navigation**, pas de rangement.
4. **L'index est-il suffisant pour `planifier-projet` ?** Prendre **deux archetypes reels**
   de `Documentation/perso/archetypes.md`, simuler le filtrage sur les dix champs, et dire ce
   qui manque pour ecarter un candidat sans ouvrir sa fiche. Relier a l'entree 1 des
   ameliorations (champ `contraintes:`), sans la re-instruire.
5. **Le champ `domaines:` cote Dev** : le faire lire par `build_mocs`, l'alimenter cote Wiki,
   ou le retirer ? Cet axe le regarde du point de vue de la **navigation** ; l'axe 1 le regarde
   du point de vue du modele. Les deux reponses doivent converger — le signaler si elles diffèrent.
6. **Le graphe Obsidian.** `Documentation/perso/obsidian-graph.md` decrit l'intention.
   Le graphe reel la sert-il, ou 647 nœuds produisent-ils une pelote illisible ?
7. **Que fait un humain qui cherche « par quoi je commence » ?** Il n'existe aucune page
   d'entree unique du vault. Est-ce un manque ?

## Hors perimetre

Le rangement (axe 1), la validation (axe 2), le pilier REX (axe 6). Ne pas proposer de
refonte de taxonomie ici.

## Livrable

Le rapport, plus **en annexe** : le tableau « type de page → chemin d'acces → verdict », et
la liste des 19 orphelins avec pour chacun la cause retenue et le correctif propose.
