---
role: meta
nom: remontees-lot-17-six-domaines
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 17 (six petits domaines et l'optimisation)

Périmètre : « Sécurité/ » (3), « Signal & audio/ » (3), « Observabilité/ » (3),
« Réseau/ » (2), « Documents/ » (2), « DevOps/ » (2), « Mathématiques/Optimisation/ » (1).
**16 fiches `role: brique`**, exactement le compte annoncé par la table du découpage.
Branche `claude/lot-17-six-domaines-0b1858`.

Écart de validateur mesuré sur la branche : **149 → 138 avertissements**, soit **11 R15
fermés** et aucun avertissement neuf. Les onze fiches concernées n'avaient aucun lien vers
une notion ou un hub ; le `## Voir aussi` du gabarit v3 en pose un dans chaque. Les cinq
autres fiches du lot en avaient déjà un. `check_arbo.py` reste vert.

## 1. Le lot 17 porte sept dossiers, et quatre d'entre eux n'ont aucune notion

Les seize fiches se répartissent sur sept dossiers dont cinq comptent deux ou trois
briques. Conséquence directe sur le `## Voir aussi` : là où le pilote pouvait écrire « la
notion du dossier », **quatre dossiers sur sept n'ont aucune notion** — « Observabilité/ »,
« Réseau/ », « Documents/ », « DevOps/ ». Le seul lien interne disponible y est le **hub du
domaine**, et c'est celui qui a été posé.

Ce n'est pas une carence de la conversion, c'est la carte du vault : ces quatre domaines
n'ont que des briques. Si le lot 8 veut durcir R15 au-delà de l'avertissement, il devra
accepter le hub comme cible légitime — sinon quatre domaines entiers deviennent
inconvertibles.

## 2. Les trois fiches de « Signal & audio/ » avaient leurs renvois déjà au comparatif

Application de la règle 2 du 2026-09-06, cas « la brique **et** la cible sont co-membres ».
`scipy.signal`, `PyWavelets` et `librosa` sont les **trois** membres de
`Comparatif - Traitement du signal.base` (vérifié par
`AI/migration/scripts/mesure_membres_bases.py`, puis recoupé à la main sur le `.md` du
comparatif). Leurs `## Quand NE PAS l'utiliser` portaient dix puces, dont **neuf** de la
forme « besoin → concurrent ». Sur ces neuf, **sept** visaient un co-membre — deux depuis
`scipy.signal`, trois depuis `PyWavelets`, deux depuis `librosa` : toutes les sept sont déjà
portées par la section « Ce qui départage » du comparatif, écrite au lot 5. Aucune n'a été
recopiée.

Les **deux** autres visaient hors vue et sont **restées** en `Écarter si` avec leur
wikilink : `scipy.signal → [[numpy]]` (la FFT nue) et `librosa → [[HuggingFace]]` (ASR et
TTS). La dixième puce, « traitement temps réel » sur `librosa`, ne nommait aucune cible :
c'est une borne dure, elle est restée aussi.

## 3. Le cas majoritaire du lot est « aucune vue ne peut porter le renvoi »

**13 fiches sur 16 ne sont membres d'aucune vue `.base`** — les quatre dossiers sans
comparatif, plus « Sécurité/ », plus PuLP dont la vue n'a qu'un membre. Pour elles, la
branche « sinon » de la règle 2 s'applique intégralement : **tout** renvoi reste en
`Écarter si` avec son wikilink, parce qu'aucun comparatif ne peut l'accueillir.

Le décompte final des cellules `Écarter si`, mesuré par script sur les 16 fiches :

| Cellules `Écarter si` | Nombre |
|---|---|
| avec wikilink (renvoi vers une brique du vault) | 16 |
| sans wikilink (borne dure de la brique, ou renvoi hors brain) | 53 |
| vides | 6 |

Les 53 sans wikilink ne sont pas un manquement : ce sont des **bornes dures** — « il n'y a
pas de mode terminal » (Sniffnet), « il n'y a pas de révocation native » (PyJWT), « le hub
est mono-nœud » (Beszel) — ou des renvois vers un outil **hors brain** nommé en clair :
Wireshark, `rsync`, Qualys SSL Labs, Pyomo, Podman, Kubernetes. Poser un wikilink y aurait
exigé d'inventer une page. Le critère « un wikilink dans chaque cellule `Écarter si` » est
donc inatteignable sur ce lot, comme le brief l'anticipe.

## 4. Six cellules `Écarter si` et treize cellules `Prendre si` laissées vides

Le tableau ne s'équilibre pas, et c'est dans le sens **inverse** de celui du pilote : ici
**treize cellules `Prendre si`** sont vides contre six côté `Écarter si`. Les fiches de ce
lot sont des outils d'infrastructure très bornés — un annuaire mort, une extension
propriétaire, un transfert point à point — dont la liste des exclusions dépasse la liste
des usages.

Détail des vides côté `Écarter si` : Docker 1, PuLP 1, scipy.signal 2, PyWavelets 2.
Aucune n'a été comblée.

## 5. Deux couples `complements:` posés, deux écartés, un signalé au lot 16

Application de la règle 3 : appariement énoncé **comme une recommandation**, et **dans les
deux sens**.

**Posés** (les deux moitiés sont dans le périmètre, la réciprocité est fermée) :

| Couple | Ce que chaque fiche énonce |
|---|---|
| [[Grafana]] ↔ [[Loki]] | même éditeur ; Loki est « visualisé dans Grafana » jusque dans son `pitch:`, et son confort d'exploration en dépend ; Grafana nomme Loki « source naturelle » |
| [[Docker]] ↔ [[GitHub Actions]] | chacune ne cite **que** l'autre en `Liens` ; « la CI qui construit et publie les images » d'un côté, « images construites et publiées depuis les workflows » de l'autre |

Le second couple est un **jugement**, à confirmer ou infirmer par l'intégration. Il aurait
pu tomber sous la mise en garde de la règle 3 (« s'intègre à » n'ouvre pas un couple), mais
deux faits l'en distinguent : l'appariement est énoncé des deux côtés, et aucune des deux
fiches ne cite d'autre partenaire — le risque de bruit que la règle vise, celui des sept
trackers du lot 5 qui en ouvriraient quinze, n'existe pas ici.

**Écartés**, malgré une apparence de couple :

- **[[Beszel]] ↔ [[Sniffnet]]** — les deux fiches se citent avec le mot « complément » et
  la même formule symétrique (« Beszel dit comment va la machine, Sniffnet ce qui
  circule »). Mais aucune ne recommande de les **utiliser ensemble** : elles disent
  qu'elles répondent à deux questions différentes. C'est du contraste de positionnement,
  exactement ce que la règle 3 exclut. Posé en `## Voir aussi` des deux côtés.
- **[[Web-Check]] ↔ [[osint4all]]** — « à opposer à cette page : l'un s'exécute, l'autre se
  lit ». Contraste explicite, pas appariement.

**Une moitié non posée, à trancher par le lot 16** : `PyJWT` énonce
« [[FastAPI]] consomme PyJWT dans son pattern OAuth2 password bearer ». La fiche
`Web & API/FastAPI.md` ne mentionne **ni PyJWT, ni JWT** — vérifié par `grep`. L'appariement
n'est donc énoncé que d'un seul côté, et la règle en demande deux. Le couple n'a **pas** été
posé, contrairement à ce que « poser sa moitié quand la cible est hors périmètre »
autoriserait : ce n'est pas un problème de périmètre, c'est un appariement qui n'existe pas
dans les deux fiches. Le lot 16, qui aura FastAPI sous les yeux, est le seul à pouvoir juger
si la relation mérite le champ.

## 6. Les fiches sans `maturite:` ne sont pas que des `famille: application`

Extension mesurée de la remontée 6 du pilote, qui supposait le trou propre à
`famille: application`. Trois fiches de ce lot n'ont pas de `maturite:`, et elles portent
**trois familles différentes** :

| Fiche | `famille:` |
|---|---|
| `Réseau/Sniffnet.md` | `application` |
| `Réseau/croc.md` | `cli` |
| `Documents/Page to Markdown.md` | `extension` |

`build_bandeau.py` les nomme à chaque passage et affiche un tiret cadratin. L'hypothèse
« le champ n'a jamais été rempli pour la famille `application` » ne tient donc pas : le trou
suit plutôt les **fiches d'outillage poste de travail**, toutes familles confondues. Le
combler reste une décision éditoriale de floSa.

## 7. L'étiquette « Site » a été ajoutée au vocabulaire de `## Ressources` — à trancher

Le gabarit §6 montre quatre étiquettes (Documentation, Dépôt, Tutoriel, Article) et le
pilote n'en a utilisé que deux. Deux fiches de ce lot ont un **site officiel du projet**
distinct de la doc et du dépôt : `sniffnet.app` et `getcroc.com`. Les supprimer aurait perdu
une URL officielle ; les étiqueter « Documentation » aurait fait deux puces homonymes sur la
même fiche, l'`url_docs` de Sniffnet pointant déjà vers son wiki.

**Deux puces `- Site —` ont donc été écrites.** Décompte des 32 puces du lot :
Documentation 15, Dépôt 15, Site 2. Si le lot 8 ferme le vocabulaire à quatre valeurs, ces
deux puces sont à reclasser — mais le besoin qu'elles couvrent, lui, restera.

> Cas voisin, sans écart : `Sécurité/osint4all.md` porte le **même** URL en `url_docs` et en
> `url_repo`. Une seule puce a été écrite, étiquetée « Dépôt ». C'est la seule fiche du lot
> sans puce « Documentation », et c'est volontaire.

## 8. Cinq fiches nommaient dans leur corps une `categorie:` que leur frontmatter ne porte plus

Reliquat des renommages du lot 3, corrigé dans le texte réécrit, **jamais** dans le
frontmatter (hors périmètre d'une conversion) :

| Fiche | Le corps disait | Le frontmatter porte |
|---|---|---|
| `Sécurité/osint4all.md` | `security/osint` | `security/recon` |
| `Réseau/Sniffnet.md` | `network/analysis` | `network/analyse` |
| `Réseau/croc.md` | `network/transfer` | `network/transfert` |
| `Documents/Page to Markdown.md` | `tooling/capture` | `docs/capture` |
| `Documents/Stirling PDF.md` | `tooling/document` | `docs/pdf` |

Cinq fiches sur seize : le motif est systématique et vaut d'être cherché ailleurs. **Une
fiche qui nomme sa propre catégorie en prose la périme dès le renommage suivant.** Le
gabarit v3 n'y remédie pas — les cinq mentions sont conservées, corrigées, dans la puce
italique de `### Alternatives`, faute d'un meilleur endroit pour dire « seule page de sa
catégorie ».

## 9. Une mention obsolète de champ disparu, dans `osint4all`

Sa section `Pièges` portait : « `status: abandonne` porte sur le dépôt, pas sur la valeur
résiduelle de la liste — la nuance ne se lit pas dans le champ ». Le champ `status:`
n'existe plus depuis le lot 2 ; l'information vit maintenant dans `maturite: deprecated`,
que le bandeau affiche.

La nuance, elle, reste **vraie et utile** : la page est morte, la liste ne l'est qu'en
partie. Elle n'a pas été réécrite en `## Définition`, parce que le critère d'acceptation
interdit d'y recontenir la maturité. Elle a été **reformulée par ses faits** en `Écarter si`
— « huit commits, rien depuis le 9 juillet 2022 » — ce qui dit la même chose sans le mot.
Mais la nuance elle-même, « le dépôt est mort, la liste ne l'est qu'à moitié », n'a **plus
d'endroit** dans le gabarit v3. C'est une vraie perte, petite, et elle est consignée ici.

## 10. Deux puces sans destination dans le gabarit — non reportées

Comme la remontée 8 du pilote, elles sont consignées ici plutôt que logées de force :

- `Sécurité/osint4all.md` — « Un seul tag du vocabulaire fermé s'applique honnêtement
  (`osint`) ; il désigne le sujet, pas la nature de la page. Aucun tag ne dit “annuaire de
  ressources” ». C'est une remontée de **gouvernance du vocabulaire des tags**, pas une
  propriété de l'outil. Elle concerne `Documentation/general/tags.md` et les deux annuaires
  du vault ([[osint4all]] et [[public-apis]]).
- `Documents/Page to Markdown.md` — « Nombre d'utilisateurs, note et date de dernière mise à
  jour non vérifiés : la fiche du Chrome Web Store n'a pas pu être consultée ». C'est une
  **réserve de sourcing** de la conversation qui a écrit la fiche, pas une limite de
  l'extension. Le gabarit v3 n'a pas de section pour ça, et l'inventer aurait été pire.

## 11. Une version datée conservée, deux perdues — l'incohérence est signalée

Trois fiches portaient un numéro de version daté dans leur section de déploiement. Le
gabarit v3 n'a pas de case pour un fait qui se périme :

- `Observabilité/Beszel.md` — « Version au 2026-08-17 : v0.18.8 » : **perdue**. Ce qui
  comptait était la conséquence (`0.x`, compatibilité hub/agent non garantie entre versions
  éloignées) ; elle est en `Mise en œuvre`, ligne Installation.
- `Sécurité/Web-Check.md` — « Version publiée au 2026-07-28 : 2.2.0 » : **conservée** en
  `Mise en œuvre`, ligne Coût, avec sa date.
- `Documents/Stirling PDF.md` — « v2.14.3 en août 2026, environ 91 000 étoiles » :
  **perdue**, sauf la conséquence (« épingler un tag d'image plutôt que `latest` »).

Deux traitements pour un même type de fait, sur le même lot : ce n'est pas défendable
longtemps. Ou le gabarit assume qu'un numéro de version n'a pas sa place dans une fiche — et
les trois se retirent —, ou il lui donne une case. À trancher au lot 8, avec la question plus
large des faits datés : le vault n'a toujours **aucune** entrée datée, et aucune section
`## Retours` n'a été créée ici.

## 12. Le comparatif à un membre : rien n'a été fait, comme demandé

`Mathématiques/Optimisation/Comparatif - Solveurs d'optimisation.base` reste à **un**
membre, `PuLP`, et `R8b` continue d'être émis. La fiche `PuLP` nomme onze solveurs sans
page — Pyomo, CVXPY, `scipy.optimize`, CBC, GLPK, HiGHS, SCIP, Gurobi, CPLEX, MOSEK,
XPRESS. Aucune fiche n'a été créée, aucun manque comblé : l'entrée de backlog existe, et la
page de comparatif porte déjà son propre encart d'explication, écrit au lot 5.

Seul changement côté `PuLP` : la puce italique de `### Alternatives` **nomme le backlog**
comme destination du manque, là où le corps v2 se contentait de « *(Page dédiée non
créée.)* » répété trois fois.

## 13. Vérification des critères d'acceptation — par script, sur les 16 fiches

Mesuré, pas affirmé :

| Critère | Résultat |
|---|---|
| Aucune section `Pourquoi`, `Quand l'utiliser`, `Quand NE PAS l'utiliser`, `Déploiement & coût`, `Bases & plateformes`, `Installation & plateformes`, `Pièges`, `Liens`, `## Alternatives` | **0** occurrence |
| Les sept sections v3 présentes (`Définition`, `Prendre si / Écarter si`, `Mise en œuvre`, `Écosystème`, `### Alternatives`, `Ressources`, `Voir aussi`) | **16/16** |
| `Mise en œuvre` porte ses cinq étiquettes | **16/16** |
| Wikilink **à alias** dans une cellule de tableau (règle 1, violation dure) | **0** |
| Aucune cible n'apparaît dans deux sections de la même page | **0** doublon |
| Chaque puce de `Ressources` porte une étiquette | 32/32, dont 2 hors des quatre du gabarit (cf. remontée 7) |
| `check_brain.py` | vert, 138 avertissements contre 149 avant |
| `check_arbo.py` | vert |

Le critère qui **cède** devant la règle 2, comme le brief l'annonce : « un wikilink dans
chaque cellule `Écarter si` » — 53 cellules sur 75 n'en portent pas, cf. remontée 3.

> Les trois fiches du vault sans `## Alternatives` que le brief signale ne sont pas dans ce
> lot : les 16 en avaient une, et les 16 ont maintenant une `### Alternatives`. Sur **11**
> d'entre elles, `alternatives:` est vide au frontmatter et la sous-section porte une seule
> puce en italique disant pourquoi — première page de sa catégorie, ou candidats non fichés.
> R11 n'a rien à couvrir dans ces cas, et R1 non plus.
