---
role: meta
nom: remontees-lot-16-web-stockage-nocode-medias-interfaces
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 16

Périmètre : « Web & API/ » (6), « Stockage/ » (6), « Automatisation no-code/ » (5),
« Médias/ » (4) et « Interfaces & apps data/ » (4) — **25 fiches `role: brique`**, le compte
annoncé par la table de découpage, vérifié avant d'écrire.
Branche `claude/lot-16-gabarit-v3-3751de`, base `d8f81d6`.

Écart d'avertissements mesuré sur la branche : **149 → 129**, soit **20 fermés**, tous des
`R15` — aucun des cinq dossiers ne contient de notion, et c'est le lien vers le **hub du
domaine** posé en `## Voir aussi` qui les ferme. Il ne reste qu'un avertissement dans le
périmètre, le `R8d` documenté de la vue « Frontends web légers », qu'il ne fallait pas
corriger. `check_arbo.py` reste vert. Aucun fichier hors des cinq dossiers n'est touché.

---

## 1. La règle 2 se vérifie exactement, et le recouvrement se mesure

Le périmètre était un bon banc d'essai : deux dossiers **sans aucun comparatif** (Stockage,
Médias — plus Web & API pour 4 de ses 6 fiches), deux dossiers dont **toutes** les briques sont
membres d'une même vue (Automatisation no-code, Interfaces & apps data).

Comptage après conversion des 25 fiches, cible présente à la fois en `Écarter si` et en
`### Alternatives` :

| Dossier | Comparatif d'accueil | Cibles dans deux sections |
|---|---|---|
| Stockage/ | aucun | **20** |
| Web & API/ | aucun pour Flask, Jinja2, Uvicorn, public-apis | **2** (FastAPI ↔ Flask) |
| Médias/ | aucun | 0 — aucune de ses fiches n'a d'alternative déclarée |
| Automatisation no-code/ | les 5 membres de la même vue | **0** |
| Interfaces & apps data/ | les 4 membres de la même vue | **0** |

La corrélation est parfaite : **le recouvrement apparaît exactement là où aucun comparatif ne
peut porter la redirection, et nulle part ailleurs.** Ce n'est donc pas un défaut de rédaction,
c'est la conséquence arithmétique de la règle 2 — et la démonstration que le critère « aucune
cible dans deux sections » ne peut être tenu qu'en supprimant de l'information.

Second chiffre pour le lot 8 : sur **80 cellules `Écarter si` non vides**, **18 portent un
wikilink** et **62 sont des bornes dures de la brique seule**. Le critère « un wikilink dans
chaque cellule » demanderait donc de réécrire 62 bornes sous forme comparative — c'est
précisément ce que la remontée 20 du lot 5 condamne.

> Cas de contrôle recoupé à la main avant de me fier au script : FastAPI **est** membre de
> « Frontends web légers », mais Flask **ne l'est pas** — la vue liste cinq noms en dur,
> FastAPI, HTMX, Streamlit, Gradio, Dash. Le renvoi FastAPI → Flask ne peut donc aller nulle
> part et reste sur la fiche. C'est le cas nº 3 du brief, « la brique est membre, la cible ne
> l'est pas », rencontré une fois de plus.

`AI/migration/scripts/mesure_membres_bases.py` n'a pas sur-compté sur ce périmètre : ses trois
vues (5, 4 et 5 membres) concordent avec la lecture manuelle des filtres `.base`.

## 2. Zéro cellule `Écarter si` vide, et ce n'est pas un exploit

Le pilote en comptait 17 sur 13 fiches. Ici : **aucune**. La raison n'est pas une meilleure
rédaction, c'est que la dissolution de `## Pièges` a fourni de quoi remplir : dans ces cinq
dossiers, les puces de `Pièges` sont massivement des **bornes dures** — licences copyleft,
compatibilité S3 partielle, latence réseau de HTMX, re-run global de Streamlit — et non des
« besoin → concurrent ». Le tableau se déséquilibre donc dans l'autre sens : plusieurs fiches
ont deux ou trois « Prendre si » pour six ou sept « Écarter si ». C'est honnête et c'est
lisible ; ça mérite d'être noté avant qu'un lot suivant croie devoir rééquilibrer.

## 3. Quatre corps de fiche citaient une `categorie:` que le lot 4 a renommée

Défaut mesuré, indépendant du gabarit : le lot 4 a renommé des catégories sans propager dans le
**texte** des fiches qui les citent.

| Fiche | Le corps disait | Le frontmatter dit |
|---|---|---|
| `Web & API/public-apis.md` | `tooling/api` | `web/api` |
| `Médias/OpenCut.md` | `tooling/video` | `media/video` |
| `Médias/SmartTube.md` | `tooling/video` | `media/video` |
| `Médias/Superwhisper.md` | `tooling/media` | `media/ingestion` |

Corrigé dans les quatre corps, avec la valeur réelle du frontmatter. **À vérifier sur les autres
domaines** : rien ne laisse penser que ces quatre soient les seules du vault, et aucun
validateur ne contrôle qu'une catégorie citée en prose existe encore.

## 4. Trois affirmations du corps étaient devenues fausses — destinations données

Aucune puce n'est supprimée sans destination ; celles-ci ont pour destination ce document,
parce que leur destination normale aurait été de propager une erreur.

- **`public-apis`, « effet de bord assumé : `Comparatif - Clients d'API` filtre sur
  `categorie == "tooling/api"`, donc cette page y apparaîtra ».** Faux deux fois. Le filtre réel
  de `Outils de développement/Comparatif - Clients d'API.base` est
  `categorie == "devtools/client-api"`, et la page porte `web/api`. Recoupé à la main sur le
  `.base` **et** par `mesure_membres_bases.py`, qui donne deux membres à cette vue, Bruno et
  Postman. Puce retirée.
- **`OpenCut`, « les tags `mcp` et `agents` anticipent ».** La fiche ne porte plus ces tags :
  son frontmatter dit `tags: [video-editing, privacy]`. Puce retirée.
- **`SmartTube`, « son champ `tags:` est volontairement vide, aucun tag du vocabulaire fermé ne
  décrit un lecteur multimédia ».** Plus vrai : `media-player` **est** au vocabulaire
  (`Documentation/general/tags.md`, ligne 342) et la fiche porte
  `tags: [media-player, privacy]`. Puce retirée.

Les trois viennent du même mouvement : le vocabulaire de tags et de catégories s'est enrichi,
et les fiches qui commentaient leur propre absence de tag n'ont pas été relues.

## 5. Un chemin mort cité par deux fiches : `MOC/Themes/`

`OpenCut` et `SmartTube` expliquaient leur `domaines: []` par « la page n'apparaîtra dans aucun
hub de `MOC/Themes/` ». `MOC/` a disparu à la clôture du lot 4. La substance reste vraie — les
hubs transverses sont générés depuis `domaines:` — mais le dossier s'appelle maintenant
`Métiers/`. Corrigé dans les deux fiches.

## 6. Cinq fiches sans `maturite:` — `application` se confirme, `extension` et `annuaire` s'y ajoutent

`build_bandeau.py` les nomme à chaque passage, colonne **Maturité** au tiret cadratin :
`Claude Video`, `OpenCut`, `SmartTube`, `Superwhisper`, `public-apis`.

La remontée 6 du pilote soupçonnait que `famille: application` n'avait jamais reçu ce champ. Le
soupçon se confirme et s'étend : les trois `application` de Médias sont concernées, plus
`Claude Video` (`famille: extension`) et `public-apis` (`famille: annuaire`). Autrement dit,
**aucune des cinq fiches du périmètre qui ne soit ni `paquet`, ni `plateforme`, ni `saas` ne
porte de maturité**, tandis que les vingt autres la portent toutes. Le trou n'est pas
aléatoire, il suit la famille. Combler ces champs est une décision éditoriale de floSa, pas une
déduction de conversion : rien n'est inventé.

## 7. `complements:` — trois couples posés, cinq candidats écartés

**Posés**, parce que les deux fiches énoncent l'appariement comme une recommandation et que les
deux cibles sont dans mon périmètre :

| Couple | Ce que les fiches disent |
|---|---|
| FastAPI ↔ Uvicorn | « s'exécute derrière un serveur ASGI (Uvicorn) » d'un côté, « FastAPI est le framework compagnon, pas une alternative » de l'autre |
| HTMX ↔ Jinja2 | les deux fiches écrivent littéralement « paire usuelle » |
| HTMX ↔ FastAPI | le comparatif du dossier dit « le complément exact du précédent, et non son concurrent » ; la fiche FastAPI présente « FastAPI+HTMX » comme un ensemble |

Trois couples, six moitiés, toutes internes au périmètre. **Aucune moitié orpheline à faire
fermer par l'intégration** — c'est le seul point où ce lot diffère du pilote, dont les cinq
candidats pointaient tous dehors.

**Écartés — et c'est une question à trancher, pas un oubli.** Quatre candidats ont la même
forme : la cible est une **dépendance embarquée**, pas une brique qu'on choisit d'apparier.

| Candidat | Ce que la fiche dit | Pourquoi écarté |
|---|---|---|
| FastAPI → Pydantic | « dépendance forte à Pydantic » | tiré transitivement, jamais choisi |
| Flask → Jinja2 | « embarque Jinja2 comme moteur par défaut » | installé avec Flask |
| Dash → plotly | « on est dans l'écosystème plotly », « moteur de rendu des graphes » | Plotly.js est embarqué dans Dash |
| Gradio → FastAPI | « app ASGI, montable dans FastAPI » | fait de déploiement, énoncé d'un seul côté |

J'ai appliqué la même règle aux quatre plutôt que d'en retenir un ou deux : `complements:` dit
« ce qui s'utilise **avec** », et une dépendance qu'on ne peut pas ne pas utiliser n'est pas un
choix d'appariement. **Si l'intégration tranche dans l'autre sens, elle doit trancher pour les
quatre.** Deux d'entre eux ont leur cible hors de mon périmètre — Pydantic et plotly — donc la
décision ne m'appartenait pas de toute façon.

Cinquième candidat, écarté sans hésitation : `public-apis` → Bruno / Postman. La fiche dit
« avec quoi appeler ce qu'on y trouve », ce qui ressemble à un appariement, mais la même fiche
pose surtout une **redirection** : « chercher un outil pour appeler ces API : ce n'en est
pas un ». Cette redirection est obligatoire en `Écarter si`, `public-apis` n'étant membre
d'aucune vue ; la doubler en `### Compléments` aurait mis la même cible dans deux sections pour
rien. Ni Bruno ni Postman ne mentionnent public-apis.

## 8. Une entorse assumée aux cinq étiquettes de `Mise en œuvre` : le tableau de Superwhisper

`Superwhisper` portait, sous son ancienne section « Installation & plateformes », un tableau de
**13 modèles locaux** — moteur, langues, taille disque, notes de vitesse et de précision,
palier. C'est de la donnée, pas de la prose, et rien dans le gabarit v3 ne l'accueille : les
cinq étiquettes sont des lignes à puce.

Choix fait : conserver le tableau en **`### Modèles locaux disponibles`, sous `## Mise en
œuvre`**, après les cinq étiquettes — qui sont toutes présentes et complètes. Perdre treize
lignes de données sourcées pour tenir une forme aurait été le mauvais arbitrage. À trancher
pour le lot 8 : le gabarit autorise-t-il un `###` de données sous `## Mise en œuvre`, ou
faut-il une section dédiée ?

## 9. Une étiquette de `Ressources` hors du vocabulaire du gabarit : `Site`

Le gabarit énumère `Documentation`, `Dépôt`, `Tutoriel`, `Article`. Deux fiches ont une URL qui
n'entre dans aucune : `OpenCut` (https://opencut.app — l'application elle-même, son `url_docs:`
étant vide parce qu'**aucun site de documentation n'existe**, `opencut.app/docs` renvoie 404) et
`Superwhisper` (https://superwhisper.com — le site commercial, distinct de la page de doc des
modèles).

J'ai employé l'étiquette **`Site`** dans ces deux cas plutôt que de mentir avec `Documentation`
ou de perdre le lien. Le vocabulaire fermé compte donc cinq valeurs sur cette branche. À
entériner ou à corriger à l'intégration.

Cas voisin, résolu autrement : `Claude Video` et `public-apis` ont `url_docs == url_repo` — le
README **est** la documentation. Deux puces portant la même URL auraient été du bruit ; j'ai
écrit `- Dépôt — <url>` puis `- Documentation — le README du dépôt ; il n'existe pas de site
séparé`. L'étiquette est tenue, l'information est juste.

## 10. Le taux de redirections du pilote ne se transporte pas

Le pilote mesurait 89 % de puces « besoin → concurrent » dans `## Quand NE PAS l'utiliser`
(48 sur 54), et les trouvait toutes déjà au comparatif. Sur mon périmètre, la proportion
s'effondre dès qu'un dossier n'a pas de comparatif : Stockage et Médias sont majoritairement
faits de **bornes propres**, et Web & API n'a que deux redirections en tout.

Conséquence pour les lots restants : **ne pas partir du chiffre du pilote.** Il décrit un
dossier de concurrents directs adossé à une vue `.base` — les onze bases vectorielles. Un
dossier d'outils hétérogènes sans comparatif se comporte à l'inverse : les quatre fiches de
Médias n'ont **aucune** alternative déclarée.

## 11. `## Retours` n'a été créée nulle part

Conforme : aucune entrée datée dans le périmètre. La seule du vault reste
`LLM & IA générative/Agents de code/t3code.md`, du ressort du lot 7.

## 12. Rien n'a été inventé — les trois trous laissés en l'état

- Les cinq **Maturité** vides du bandeau (remontée 6) : cellule au tiret cadratin, jamais de
  valeur plausible.
- `Superwhisper` : les colonnes vitesse et précision du tableau sont des **notes auto-déclarées
  par l'éditeur**, sans WER, sans RTF, sans matériel de référence. La phrase qui le dit est
  conservée sous le tableau. De même, l'absence de toute exigence de RAM publiée et l'absence
  de correspondance officielle avec les checkpoints OpenAI sont conservées **en tant
  qu'absences**, en `Écarter si`.
- Trois fiches — `OpenCut`, `SmartTube`, `Claude Video` — portent un **avertissement de
  rangement** écrit par une conversation antérieure : elles sont hors du périmètre thématique
  du brain. Cet avertissement est conservé en tête de `## Définition`, avec sa catégorie
  corrigée. Ce n'est pas au lot 6 de décider si ces pages restent.
