# Axe 1 — Rangement & taxonomie

> Lire `AI/audit/README.md` (roles, format de rapport, interdictions) avant de commencer.
> Rapport attendu : `AI/audit/rapports/axe-1-rangement.md`.

## Question centrale

**Ou va une page, et qui le decide ?** Aujourd'hui la reponse depend de qui ecrit la fiche.

## Le probleme, tel qu'il est diagnostique

Un seul champ, `categorie:`, porte **deux questions independantes** :

- une question **thematique** — de quoi ca parle ? (`database`, `llm`, `network`, `data`)
- une question de **nature logicielle** — qu'est-ce que c'est ? (un framework, une
  passerelle, un runtime, un client GUI, une CLI, un annuaire de liens)

D'ou un prefixe `tooling/*` qui n'est pas un domaine mais un fourre-tout de natures
(19 familles), et des domaines qui melangent les natures (`llm/framework` contient a la
fois des passerelles et des frameworks d'agents).

Le champ `type:` porte deja une partie de la nature (`service` = on le deploie,
`outil` = on l'utilise), mais grossierement, et il est en pratique determine par le
**dossier** plutot que par le sujet.

## Faits de depart (cf. `mesures-<date>.md`, a relancer)

- 112 categories declarees, **86 reellement portees** → 26 declarees pour rien.
- **30 categories a une seule page.**
- 6 types de pages, **2 seulement** ont un gabarit controle par `check_brain`.
- Le champ `domaines:` (6 themes) n'est lu par **aucun** script pour les pages Dev :
  `build_mocs.py` ne construit les MOC de theme qu'a partir des concepts Wiki.
- Deux pages sont des **annuaires de liens** ranges en force dans `Dev/Outils/`
  (`public-apis`, `osint4all`), chacune ouvrant sur un « avertissement de rangement ».
  Il n'existe pas de `type: ressource`.
- `licence_type` n'a **aucune valeur pour le domaine public** : CC0-1.0 a ete declare
  `open-source` par defaut.

Contexte de gouvernance : `Documentation/general/taxonomie.md` (autorite),
`themes.md` (vocabulaire `domaines:`), `AI/ameliorations-devbrain.md` entree 3
(les huit incoherences deja relevees — **partir de la, ne pas les re-decouvrir**).

## Questions a instruire

1. **Le double axe tient-il la charge ?** Proposer le couple `domaine:` × `famille:` et
   le **tester contre les 337 fiches Dev existantes** : combien se rangent sans ambiguite,
   combien restent litigieuses, lesquelles. Un modele qui ne classe pas 95 % du vault
   existant n'est pas un modele.
2. **Quelles valeurs pour chaque axe ?** Lister les domaines et les familles, avec pour
   chacune sa frontiere ecrite (« distinct de X parce que Y »). Viser la granularite qui
   evite les singletons : 30 categories a une page signalent soit un axe trop fin, soit
   une famille manquante au-dessus.
3. **Que devient `tooling/*` ?** Ses 19 familles sont-elles des familles au sens de
   l'axe 2, ou un melange a redistribuer ?
4. **Faut-il un `type: ressource`** (annuaire, liste, veille) ? Combien de pages
   actuelles en relevent reellement ?
5. **L'arbre de decision** — le livrable le plus important. Une procedure deterministe
   qui, pour un repo entrant, donne le rangement **sans jugement** : suite de questions
   fermees menant a un couple (domaine, famille) unique. Le tester a blanc sur 10 fiches
   recentes et sur 3 cas volontairement penibles (un annuaire, un outil hors data, une
   brique a la frontiere de deux domaines).
6. **Le cout de migration** : combien de fiches changent de categorie, quels scripts
   suivent (`build_index`, `build_mocs`, `check_brain`), quelles MOC sont renommees,
   et comment faire la bascule sans casser les wikilinks existants.
7. **Le champ `domaines:`** : l'alimenter cote Dev, le faire lire par `build_mocs`, ou le
   retirer des gabarits Dev ? Trancher avec un argument, pas une preference.

## Hors perimetre

La qualite du contenu des fiches, la fraicheur des faits (axe 4), les liens et la
validation (axe 2). Ici on ne parle que de **rangement**.

## Livrable

Le rapport, au format impose par le README, plus **en annexe** : la table complete du
nouveau vocabulaire propose (domaine × famille), et le tableau de correspondance
`ancienne categorie → nouveau couple` pour les 86 categories en usage.
