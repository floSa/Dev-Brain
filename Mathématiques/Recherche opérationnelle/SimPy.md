---
role: brique
nom: SimPy
alias: [simpy, SimPy discrete-event simulation, simulation à événements discrets Python]
pitch: "Cadre de simulation à événements discrets en Python pur : les processus sont des générateurs, les ressources partagées (serveurs, files, stocks) des objets du paquet, le temps est simulé, réel ou avancé pas à pas ; MIT."
categorie: math/recherche-operationnelle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [simulation, inventory, scheduling]
url_docs: https://simpy.readthedocs.io/
url_repo: https://gitlab.com/team-simpy/simpy
---

# SimPy

<!-- AUTO:BANDEAU:START -->
> Cadre de simulation à événements discrets en Python pur : les processus sont des générateurs, les ressources partagées (serveurs, files, stocks) des objets du paquet, le temps est simulé, réel ou avancé pas à pas ; MIT.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Cadre de **simulation à événements discrets** fondé sur les processus, en Python standard. Un processus est une
**fonction génératrice** : elle déroule le comportement d'un client, d'un véhicule, d'une machine ou d'un agent,
et rend la main avec `yield` pour attendre un événement (`env.timeout(durée)`, l'obtention d'une ressource).
Les points de congestion, serveurs, caisses, quais, se modélisent par des **ressources partagées**, de trois
familles d'après la documentation : les *Resources* à capacité limitée (avec les variantes à priorité et à
préemption), les *Containers* pour une matière en vrac, continue ou discrète, et les *Stores* pour des objets
Python. Le temps est simulé : la simulation avance d'événement en événement, aussi vite que possible, ou
synchronisée avec l'horloge (`RealtimeEnvironment`), ou pas à pas.

C'est le moyen d'**essayer une politique avant de la déployer** : un stock qu'on réapprovisionne selon
[[Politiques de réapprovisionnement (s,S) et (R,Q)]], un atelier dont on veut comparer les règles de
priorité d'[[Ordonnancement d'atelier (job-shop, flow-shop)]], une file de quai. Là où une formule ne tient plus
(demande variable, pannes, délais aléatoires), la simulation donne le comportement sans le résoudre.

La documentation précise deux bornes : une simulation **continue** est théoriquement possible mais le paquet
n'offre rien pour la faire ; et SimPy est **disproportionné** pour une simulation à pas fixe dont les processus
n'interagissent pas, ni entre eux ni par une ressource.

Relevé le 2026-10-05 : **4.1.2** du 2026-05-24 (PyPI, *Production/Stable*, Python 3.8 et plus), licence MIT ;
le dépôt est sur GitLab, dernière activité le 2026-07-14.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer des politiques de stock ou de file sous une demande et des délais aléatoires, quand la formule n'est plus valable | Une formule ou un quantile suffit : [[Modèle du vendeur de journaux (newsvendor)]], [[Stock de sécurité et taux de service]] |
| Un atelier à ressources partagées, pannes et priorités, où l'on veut voir l'engorgement ([[Ordonnancement d'atelier (job-shop, flow-shop)]]) | Chercher la **meilleure** décision : la simulation évalue, elle ne cherche pas ; un solveur comme [[OR-Tools]] ou [[PuLP]] propose |
| Du Python pur, sans compilateur ni interface graphique, dans un dépôt versionné | Un modèle à pas fixe sans interaction entre processus : un simple `for` suffit |
| Du temps réel ou du pas à pas pour un banc d'essai | Une simulation physique continue (équations différentielles) : le paquet n'apporte rien pour cela |

## Mise en œuvre

- Installation — `uv add simpy`
- Point d'entrée — `import simpy`, `env = simpy.Environment()`, `env.process(ma_fonction(env, ...))`, `env.run(until=...)` ; une ressource se crée par `simpy.Resource(env, capacity=...)`, un stock par `simpy.Container(env, capacity=..., init=...)`
- Prérequis — Python 3.8 minimum ; aucune dépendance
- Exécution — un seul fil, dans le process ; chaque exécution est un tirage, la **répétition** de la simulation sous plusieurs graines est à écrire
- Coût — gratuit, MIT

## Limites à connaître

- **Aucune mesure fournie.** Le guide de la documentation sur le suivi dit que le sujet est complexe et propose des modèles : surveiller les processus, l'usage des ressources, ou tracer tous les événements. Stocker, agréger et tracer les indicateurs reste à écrire ([[Indicateurs de stock (rotation, couverture, rupture)]]).
- **Un tirage n'est pas une réponse.** Le hasard vient du code qu'on écrit autour (génération de la demande, des durées) ; un résultat se lit sur plusieurs répétitions, pas sur une exécution.
- **Pas de recherche.** Optimiser une règle exige de boucler la simulation dans un autre code, ce qui coûte autant d'exécutions que de candidats.

## Écosystème

### Alternatives

Aucune alternative déclarée : le brain n'a pas d'autre outil de simulation à événements discrets.

### Compléments

Aucun complément déclaré : le décideur qui entoure la simulation, une politique ou un solveur, est décrit par les notions du dossier.

## Ressources

- Documentation — https://simpy.readthedocs.io/
- Dépôt — https://gitlab.com/team-simpy/simpy
- Documentation — https://simpy.readthedocs.io/en/latest/topical_guides/resources.html

## Voir aussi

- [[Recherche opérationnelle]] — le hub du dossier
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — la politique à essayer par simulation
- [[Stock de sécurité et taux de service]] — la marge que la simulation vérifie
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — l'atelier à ressources partagées
- [[Optimisation]] — les méthodes de résolution, que la simulation complète sans les remplacer
