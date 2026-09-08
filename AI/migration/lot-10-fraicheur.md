---
galaxie: meta
nom: lot-10-fraicheur
type: gouvernance
created: 2026-09-08
modified: 2026-09-08
tags: [meta, migration, brainkit, fraicheur]
---

# Lot 10 — La fraîcheur des briques : sonder l'amont, l'afficher, le signaler

> [!info] **Ce lot n'appartient pas à la migration v3**, close le 2026-09-06. C'est le
> deuxième lot mené depuis le dépôt voisin **BrainKit**, après le lot 9 qui a fait de ce
> vault une instance du kit. Il porte le numéro **10** ici et le numéro **11** là-bas : les
> deux dépôts comptent leurs lots séparément, et ce n'est pas une erreur à corriger — le
> lot 9 de ce vault était déjà le lot 9 du kit par coïncidence.

Le pendant côté kit — l'arbitrage du rangement, les deux sondes, le refus du jeton, les cinq
états, la sixième forme de colonne de bandeau, les arbitrages et les remontées destinées à
BrainKit — est dans `design/11-fraicheur.md` du dépôt BrainKit. Ce fichier-ci dit ce qui a
changé **dans le vault**.

## Ce que le lot fait, en une phrase

Une brique dit maintenant, sur son haut de page et à la date près, si ce dont elle parle est
encore vivant — et le vault le **signale** quand la fiche et l'amont ne disent pas la même
chose, sans jamais corriger ni l'une ni l'autre.

---

## 1. Le problème, tel qu'il se posait

`maturite: production` est **déclaratif**. Écrit une fois à la capture, jamais revérifié.
Rien dans le vault ne disait qu'un dépôt n'avait pas eu de release depuis trois ans, ni
qu'il était archivé.

`AI/scripts/verifier_fraicheur.py` existait et savait sonder GitHub, mais son dernier passage
n'avait produit que des signalements **hors ligne** : `AI/index/fraicheur.json` ne contenait
pas une seule date de release. Son périmètre en ligne existait, il n'avait simplement jamais
tourné jusqu'au bout — 60 appels d'API par heure sans jeton, et 316 dépôts à sonder.

---

## 2. Ce qui a été posé

### 2.1 Dans `brain.yml` — trois déclarations, aucune ligne de code de plus dans le vault

Un bloc **`amont:`** : les rôles concernés (`brique`), le champ qui porte l'URL (`url_repo`),
le champ que l'amont peut contredire (`maturite`), l'hôte et sa sonde (`github.com` →
`github`), le registre de paquets (`pypi`, sur les `famille: paquet`), les deux seuils, le
chemin du side-car, et le nom des deux faits que le bandeau affiche.

Une **cinquième colonne de bandeau**, `Fraîcheur`, déclarée `externe: amont` — la seule des
cinq qui ne lise pas le frontmatter.

Une **règle de socle**, `amont_concorde`, en **avertissement** avec trois `motif:` écrits.

### 2.2 Dans `AI/scripts/` — un septième pont

`sonder_amont.py`, vingt lignes, qui appelle `brainkit sonder`. Comme les six autres : il
résout la racine du kit, charge `brain.yml`, et n'a aucune règle à lui.

C'est le seul pont qui parle à l'extérieur du vault, et le seul qui **déclenche** une étape
de clôture sans en faire partie : après un sondage, la colonne `Fraîcheur` a changé, donc
`build_bandeau.py` doit repasser. La séquence est `sonder_amont.py`, puis la clôture normale.

### 2.3 `verifier_fraicheur.py` a changé de fichier de sortie

Il écrivait `AI/index/fraicheur.json`. Ce fichier est devenu le **side-car de l'amont**,
déclaré par `brain.yml` et composé par le kit ; deux écrivains sur un même fichier, avec deux
formes d'enregistrement, se seraient effacés l'un l'autre **en silence**, et un side-car à
moitié écrit ne se voit pas.

Il écrit donc `AI/index/fraicheur-hors-ligne.json`, et il garde tout ce que le kit ne fait
pas : URL mortes et redirections de domaine, licence constatée contre `licence_type:`,
version majeure affirmée dans le corps contre celle du registre, corps qui décrit un déclin
sous une `maturite:` vive, et le croisement C2' avec les puces de fin de vie des comparatifs.
Le recouvrement entre les deux se limite à **un** fait, l'archivage.

Deux lignes de code changées, un paragraphe d'en-tête ajouté. Rien d'autre de ce script n'a
été touché.

---

## 3. Le sondage — ce qu'il a trouvé, chiffré

Passe complète du **2026-09-08** : 337 briques, **1 128 requêtes HTTP anonymes**, environ neuf
minutes, **aucun jeton**.

| | Compte |
|---|---|
| briques sondées | **337 / 337** — aucune laissée de côté |
| **release datée** (dépôt ou registre) | **312** |
| dont datées par une release de dépôt | 309 |
| dont datées par une version de registre | 161 |
| datées par leur **seul dernier commit** | 4 |
| **dépôts archivés** | **7** |
| **au-delà du seuil** de 730 jours | **13** |
| **sans amont atteignable** | **21** |
| jamais sondées | **0** |

Les 21 sans amont se décomposent : **19** briques ne déclarent aucune `url_repo` — Figma,
AWS S3, Pinecone, Zapier, LM Studio, Postman, Obsidian… ce sont des services propriétaires
qui n'ont pas de dépôt public, et ce n'est pas un trou ; **1** vit sur un hôte que le kit ne
sait pas sonder (Garage, sur `git.deuxfleurs.fr`) ; **1** a un dépôt qui rend 404 (FossFLOW).

Deux cas nommés par le rapport plutôt que passés sous silence :

- **4 pages dont l'archivage n'a pas pu être lu** — cloudscraper, OpenClaw, OmniRoute,
  osint4all. Le marqueur d'archivage n'était pas atteint sous le plafond de lecture. Le
  drapeau reste **absent** du side-car plutôt que posé à « non archivé » : la différence
  entre « non archivé » et « je n'ai pas vu » est celle qu'on refuse de perdre.
- **1 URL qui vise un sous-arbre** — ScaNN, dans le monorepo `google-research`. Le dépôt est
  sondé, et ses dates décrivent le monorepo entier, pas ScaNN.

### 3.1 Les vingt briques dont l'amont est archivé ou ancien

| Brique | État | Date | `maturite:` |
|---|---|---|---|
| Flowise | archivé | 2026-08-13 | production |
| Neptune | archivé | 2026-05-07 | *deprecated* |
| MinIO | archivé | 2026-04-25 | production |
| Vanna | archivé | 2026-03-29 | *deprecated* |
| TGI | archivé | 2026-03-21 | production |
| TorchServe | archivé | 2025-08-07 | *deprecated* |
| albumentations | archivé | 2025-07-10 | production |
| segment-anything | ancien | 2024-09-18 | production |
| Featuretools | ancien | 2024-05-14 | production |
| seaborn | ancien | 2024-01-25 | production |
| TF-Agents | ancien | 2023-12-14 | production |
| Annoy | ancien | 2023-06-14 | production |
| missingno | ancien | 2023-02-26 | production |
| osint4all | ancien | 2022-07-09 | *deprecated* |
| rank-bm25 | ancien | 2022-02-16 | production |
| Detectron2 | ancien | 2021-11-15 | production |
| seqeval | ancien | 2020-10-24 | production |
| LIME | ancien | 2020-06-26 | *deprecated* |
| pytorch-crf | ancien | 2019-02-04 | production |
| Fanalysis | ancien | 2018-06-04 | *deprecated* |

Les six en italique portent déjà `maturite: deprecated` : le vault le savait, et la règle ne
les signale pas. **Rien n'a été corrigé sur aucune de ces vingt pages** — ni une `maturite:`,
ni un `## Retours`, ni une ligne de `## Définition`. Le désaccord est un sujet pour floSa,
pas un défaut à réparer par un script.

---

## 4. Le bandeau — ce qu'il montre maintenant

```
| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
```

```
| Plateforme Go | open-source | self-hébergé · distribué | production | dépôt archivé · 2026-04-25 |
```

La seconde ligne est MinIO, et elle dit tout le lot : la fiche déclare `production`, l'amont
dit archivé depuis avril. Les deux se lisent **sur la même ligne**.

Cinq libellés, un par état, tous déclarés dans `brain.yml` : « à jour », « amont ancien »,
« dépôt archivé », « aucun amont fiché », « amont non sondé ». La cellule n'est **jamais**
vide — le tiret cadratin veut dire « champ absent du frontmatter », et ce serait faux ici.
Le rapport de trous du générateur reste donc à **39**, exactement comme avant, et ces 39 sont
tous des `Maturité` absentes.

Le seuil de 730 jours a été **mesuré avant d'être arrêté** : 180 j → 38 briques au-delà,
365 j → 21, 545 j → 16, **730 j → 13**, 1 095 j → 10, 1 460 j → 8. La courbe est plate après
730, et 730 est le point où la liste reste relisable en une fois. Le chiffre se change dans
`brain.yml`, et `sonder_amont.py --recalculer` rejoue la dérivation sans un appel réseau.

---

## 5. La règle, et ce qu'elle coûte

`amont_concorde`, **avertissement**, trois sous-clés :

| Sous-clé | Ce qu'elle signale | Compte |
|---|---|---|
| `ancien` | dernière trace datée au-delà du seuil, sous une `maturite:` non éliminatoire | **10** |
| `archive` | dépôt archivé, sous une `maturite:` non éliminatoire | **4** |
| `contredit` | l'inverse : amont vivant sous `maturite: deprecated` | **2** |

Les deux `contredit` sont **Marqo** et **AutoGen** : le vault les déclare abandonnées, leur
amont publie encore. C'est le cas auquel personne ne pense, parce qu'on ne relit pas une
fiche qu'on croit enterrée.

**Jamais dure, et ce n'est pas provisoire.** Une violation ici est un désaccord avec un
**tiers**, dont le tiers peut avoir tort — un dépôt miroir archivé pendant que le vrai
développement déménage. Durcir ferait échouer la clôture du vault parce qu'un inconnu a
cliqué sur « archiver » : le brain serait otage de son amont. C'est pour la même raison que
`sonder_amont.py` sort en **0** sur ses constats.

Le dénominateur est le nombre de pages **sondées** (337), pas le nombre de briques. Les deux
coïncident aujourd'hui parce que la passe est complète.

---

## 6. Les vérifications

| Quoi | Avant | Après |
|---|---|---|
| `check_brain.py` | 0 dure, **111** avertissements | 0 dure, **127** avertissements |
| `check_arbo.py` | chemin et catégorie concordent partout | inchangé |
| `build_bandeau.py --check` | 0 | **0** |
| `brainkit generer --check` | 414 artefacts concordent | **414 artefacts concordent** |
| `brainkit mesurer` | 1 (garde-fou 2, deux règles sans motif) | 1, **les deux mêmes** |

Les **seize** avertissements de plus sont **tous** des constats d'`amont_concorde`, une règle
neuve. Aucun compte existant n'a bougé : `voisinage_declare` reste à 62, `collision_alias` à
13, `couverture_des_vues` à 13+1+1+11, `etiquettes_fermees/Ressources` à 5, `anti_repetition`
à 4, `vocabulaire_ferme/axe_vide` à 1. C'est ce qu'il fallait vérifier, et c'est vérifié
règle par règle par `tests/epreuve.py` du kit, lancé sur ce worktree.

Côté kit, les dix jeux d'épreuve passent, dont le nouveau `tests/amont.py` — 6 scénarios, 46
vérifications, **aucun appel réseau**.

### 6.1 Ce que le lot a changé dans les pages

**337 fichiers** de brique, et **uniquement** leur zone `<!-- AUTO:BANDEAU -->` : une colonne
de plus dans l'en-tête, une cellule de plus dans la ligne de valeurs. Aucune autre ligne
d'aucune page. Aucune des **297 notions** n'a été ouverte.

---

## 7. Ce que le lot n'a PAS fait, et c'est volontaire

- **Corriger une `maturite:` que l'amont contredit.** Les 16 désaccords sont signalés,
  aucun n'est réparé. C'est la décision de floSa, page par page.
- **Écrire quoi que ce soit dans un `## Retours`.** Un dépôt archivé n'est pas un retour
  d'expérience daté ; ce n'est pas la même section, et ce n'est pas la même main.
- **Durcir la règle.** `brainkit mesurer` la classe « à réparer » et ne propose rien : une
  règle qui a un passif ne se durcit pas, elle se travaille.
- **Fondre `verifier_fraicheur.py` dans le kit.** Ses règles hors ligne sont bonnes et le kit
  ne les a pas. C'est un lot, pas un effet de bord — cf. *Remontées*.
- **Toucher aux sept scripts PowerShell**, ni à `brain-v3.md`, ni aux skills : remontées 1,
  3 et 5 du lot 9, toujours ouvertes.

---

## Remontées

*Ce qui a été trouvé hors du périmètre du lot, et qui ne s'y corrige pas.*

**1 — La remontée 4 du lot 9 est FERMÉE.** *(fait)* « Le manifeste et le vault se recopient
l'un l'autre, sans contrôle. » `outils/fidelite.py` du kit compare désormais les sha256 de
`exemples/devbrain.brain.yml` et du `brain.yml` du vault, et sort en **1** s'ils ont divergé,
en imprimant les deux empreintes. Vérifié aujourd'hui : identiques
(`7954e3d163b0…`). Ce lot en a eu besoin dès sa première heure — il modifie les deux
manifestes, et c'est exactement le geste où l'un des deux s'oublie.

**2 — Le `main` local porte une modification non commitée qui BLOQUERA l'intégration.**
*(à traiter avant de merger)* `Data & pipelines/missingno.md` est modifié dans la copie
principale : un formateur de tableaux — Obsidian ou un éditeur — a réaligné la zone
`<!-- AUTO:BANDEAU -->` avec des espaces de remplissage. Ce lot réécrit cette même zone sur
les 337 briques, dont celle-là : `git merge --ff-only` refusera de l'écraser. Il faut
**décider** avant de merger : soit `git restore` sur ce fichier (la zone est générée, la
régénération la rendra correcte), soit la commiter d'abord. Ce n'est pas au lot de choisir —
c'est une modification de floSa.

Au passage : un formateur qui réaligne une zone `<!-- AUTO -->` la met en écart avec le
générateur à chaque frappe. Si c'est un réglage d'Obsidian ou d'un plugin, il vaudrait mieux
l'exclure des blocs `AUTO` — sinon `build_bandeau.py --check` sortira en 2 sans raison, un
jour où personne ne s'y attend.

**3 — `brainkit mesurer` sort en 1, et c'était déjà vrai avant ce lot.** *(deux phrases)*
Le garde-fou 2 refuse un `severite: avertissement` sans `motif:` écrit, et deux règles de
socle du manifeste n'en portent pas : `taille_avertissement` et `collision_alias`. Ce n'est
pas un défaut du kit, c'est le garde-fou qui fonctionne. Deux phrases dans `brain.yml` le
ferment, et l'arbitrage — pourquoi ces deux règles restent souples — appartient à floSa.

**4 — Le sondage n'est rappelé par rien.** *(10 lignes)* Il se lance à la main, et un
side-car vieux de six mois ne se distingue d'un side-car frais que par les dates `sonde_le`
qu'il porte — que personne ne lit. Une ligne dans la sortie de clôture (« le side-car de
l'amont a N jours ») coûterait dix lignes, dans `cloturer-brain` ou dans le validateur.

**5 — Les règles hors ligne de `verifier_fraicheur.py` mériteraient d'entrer dans le kit.**
*(un lot)* URL mortes, redirections de domaine, licence constatée contre licence déclarée,
version majeure du corps contre celle du registre : quatre règles génériques que le kit
n'a pas. Les deux dernières — corps qui décrit un déclin, croisement avec les comparatifs —
demandent qu'un manifeste puisse déclarer un motif de texte, ce qui est un mécanisme neuf.
Tant que les deux outils coexistent, il faut se souvenir qu'ils écrivent deux fichiers
différents et qu'aucun ne remplace l'autre.

**6 — L'archivage se lit dans du HTML, et c'est le seul fait fragile du lot.** *(à surveiller)*
Le marqueur `"isArchived"` est un détail d'implémentation de GitHub, pas un contrat. Le jour
où il change, la liste « archivage non lu » passera de **4** à trois cents. Elle existe pour
que ça se voie — encore faut-il la lire. Le kit porte la remontée d'un seuil d'alerte.

---

## Ce que floSa doit lancer pour intégrer

Le lot **n'a rien poussé** : la branche est locale, `main` est intacte, l'intégration est sa
décision. En PowerShell, une commande par ligne — `&&` n'existe pas ici.

**D'abord, régler la remontée 2**, sinon le `merge --ff-only` refusera :

```powershell
cd "C:\Users\FlorianHorellou\OneDrive - Aosis Consulting\Documents\Projets\DevBrain"
git status --short
git restore "Data & pipelines/missingno.md"
```

Puis l'intégration :

```powershell
git fetch origin
git log main..origin/main --oneline
git merge --ff-only claude/devbrain-fraicheur-briques-bad7b1
git push origin main
```

Le deuxième `git log` doit être **vide**. S'il ne l'est pas, s'arrêter : la base a divergé.

Côté BrainKit — dépôt sans remote, rien à pousser : les deux commits du lot y sont déjà sur
`main`.
