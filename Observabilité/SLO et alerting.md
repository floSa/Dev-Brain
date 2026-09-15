---
role: notion
nom: SLO et alerting
alias: [SLO, SLI, SLA, service level objective, budget d'erreur, error budget, burn rate, taux de consommation, alerting, alerte sur les SLO]
categorie: observability/supervision
domaines: [infra-ops, mlops]
tags: [observability, alerting, slo]
---

# SLO et alerting

## Aperçu

- Un **SLO** fixe le niveau de service visé, un **SLI** le mesure, un **SLA** en fait un contrat. L'**alerting** décide ensuite quand un humain doit être prévenu : il ne devrait l'être que lorsque l'objectif est réellement menacé.
- Sans objectif, une alerte est un seuil arbitraire sur une métrique. Avec un objectif, elle devient une question chiffrée : à quelle vitesse le service consomme-t-il la marge d'erreur qu'il s'est accordée ?

## Concepts clés

### SLI, SLO et SLA
- SLI, *Service Level Indicator* : « une mesure quantitative soigneusement définie d'un aspect du niveau de service fourni ». SLO, *Service Level Objective* : « une valeur cible, ou une plage de valeurs, pour un niveau de service mesuré par un SLI ». SLA, *Service Level Agreement* : « un contrat, explicite ou implicite, avec les utilisateurs, qui comporte des conséquences si les SLO qu'il contient sont respectés ou manqués » (livre SRE de Google).
- Le SLI s'écrit comme un rapport : événements **bons** divisés par événements **valides** — par exemple les requêtes HTTP réussies divisées par toutes les requêtes (*SRE Workbook*).
- Le *Workbook* distingue la **spécification** du SLI (« ce qui compte pour l'utilisateur », par exemple charger la page d'accueil en moins de 100 ms) de son **implémentation** (la spécification plus une méthode de mesure : journaux serveur, sondes externes, instrumentation côté client), qui change la qualité, la couverture et le coût de la mesure.

### Le budget d'erreur
- Le budget d'erreur est le taux auquel l'objectif peut être manqué. Le livre SRE conseille de le suivre à l'échelle du jour ou de la semaine ; c'est ce qui permet d'arbitrer entre livrer plus vite et fiabiliser.
- Un SLO de 99,9 % sur 30 jours autorise 0,1 % d'échecs, soit 43,2 minutes de panne totale (calcul : $30 \times 24 \times 60 \times 0{,}001$).
- La **politique de budget d'erreur** écrite doit nommer ses auteurs, réviseurs et approbateurs, sa date d'approbation et de revue, décrire le service, et surtout lister « les actions à mener à l'épuisement du budget », avec une procédure d'escalade en cas de désaccord.

### Choisir des objectifs
- Le livre SRE donne quatre conseils : ne pas prendre la performance actuelle comme cible, sous peine de s'enfermer dans un système qui demande des efforts héroïques ; garder les agrégations simples, car des agrégations compliquées masquent les changements et se raisonnent mal ; choisir « juste assez » de SLO pour couvrir les attributs du système ; commencer par une cible lâche et la resserrer, plutôt que d'en poser une trop stricte à assouplir.
- Fenêtre de mesure : le *Workbook* recommande une fenêtre **glissante**, plus proche de l'expérience des utilisateurs, d'un nombre entier de semaines pour qu'elle contienne toujours autant de week-ends ; quatre semaines glissantes conviennent pour un usage général.

### Alerter sur les symptômes
- Règle de Prometheus, reprise d'observations de Rob Ewaschuk chez Google : alerter sur les symptômes qui touchent l'utilisateur, plutôt que sur chaque cause possible ; avoir aussi peu d'alertes que possible ; laisser de la marge aux petits accrocs.
- Le livre SRE pose la question de tri d'une page : la règle détecte-t-elle une condition par ailleurs non détectée, **urgente**, **actionnable**, et visible ou sur le point de l'être par l'utilisateur ? Une alerte qui n'appelle qu'une réponse mécanique n'a pas à réveiller quelqu'un.
- Deux angles de mesure : la **boîte noire** teste le comportement visible de l'extérieur — c'est le côté symptôme, actif, celui d'[[Uptime Kuma]] —, la **boîte blanche** s'appuie sur des métriques et des logs internes, et détecte les défaillances imminentes et aide au débogage.

### Le taux de consommation (burn rate)
- Le *burn rate* mesure la vitesse à laquelle le service consomme le budget d'erreur, relativement au SLO : un taux d'erreur constant égal à la marge du SLO vaut 1 et épuise exactement le budget sur la période.
- Alerter quand le taux d'erreur dépasse simplement le seuil du SLO a une mauvaise précision : le *Workbook* calcule qu'on pourrait recevoir jusqu'à 144 alertes par jour, chaque jour, n'en traiter aucune, et tenir quand même le SLO. Allonger la fenêtre d'alerte a un très mauvais temps de retour : après une panne totale, l'alerte part au bout d'environ deux minutes et **reste active pendant 36 heures**. Exiger une durée minimale a un mauvais rappel et un mauvais délai de détection, puisque la durée ne dépend pas de la gravité et qu'une fluctuation de la métrique remet le compteur à zéro.

## Les maths, simplement

- Burn rate, pour un SLO de niveau $s$ (par exemple $s = 0{,}999$) :
  $$\text{burn rate} = \frac{\text{taux d'erreur observé}}{1 - s}$$
  Un taux d'erreur de 0,1 % pour $s = 99{,}9\ \%$ donne un burn rate de 1.
- Part du budget consommée : $\text{burn rate} \times \dfrac{\text{fenêtre}}{\text{période}}$. Un burn rate de 36 tenu une heure sur une période de 30 jours (720 h) consomme $36 / 720 = 5\ \%$ du budget.
- Réglage recommandé par le *Workbook* pour un SLO de 99,9 %, avec deux fenêtres par alerte — une longue pour la significativité, une courte pour que l'alerte s'éteigne vite une fois le problème réglé :

  | Sévérité | Fenêtre longue | Fenêtre courte | Burn rate | Budget consommé |
  |---|---|---|---|---|
  | Page | 1 h | 5 min | 14,4 | 2 % |
  | Page | 6 h | 30 min | 6 | 5 % |
  | Ticket | 3 j | 6 h | 1 | 10 % |

- Vérification : $14{,}4 \times 1/720 = 2\ \%$ ; $6 \times 6/720 = 5\ \%$ ; $1 \times 72/720 = 10\ \%$. À 14,4, le budget entier disparaît en $720 / 14{,}4 = 50$ heures.

## En pratique

- Chaîne courante sur site : [[Prometheus]] évalue les règles et envoie les alertes à [[Alertmanager]], qui les regroupe, les inhibe, les met en silence et les route vers le bon récepteur. L'alerting intégré de [[Grafana]] évalue et notifie dans le même outil, ce qui économise un composant sur un petit parc.
- Une alerte de type « page » est réservée au symptôme urgent ; le reste va dans un ticket. Le tableau ci-dessus fait cette séparation par le burn rate : une consommation rapide réveille, une consommation lente ouvre un ticket.
- Compléter par une sonde de l'extérieur : [[Uptime Kuma]] mesure ce qu'un utilisateur voit, là où les métriques internes disent où chercher. Un déclencheur [[Zabbix]] est une règle d'alerte au même titre : il se juge sur le symptôme, pas sur la cause qu'il nomme.
- Ne pas décider de l'objectif à partir de ce que le service fait déjà, ni multiplier les SLO : en poser peu, les serrer avec le temps.

## Approches voisines & alternatives

- [[Métriques, logs et traces]] — les signaux dont un SLI est tiré, et ce que chacun coûte.
- [[Monitoring de modèle en production]] — la même logique d'alerte appliquée à la dérive d'un modèle, qui ne se mesure pas en disponibilité.
- [[Alertmanager]] et [[Prometheus]] — l'outillage qui exécute la règle.

## Pour aller plus loin

- Google, *Site Reliability Engineering*, chapitre « Service Level Objectives », https://sre.google/sre-book/service-level-objectives/ (définitions du SLI, du SLO et du SLA ; conseils de choix de cibles).
- Google, *Site Reliability Engineering*, chapitre « Monitoring Distributed Systems », https://sre.google/sre-book/monitoring-distributed-systems/ (boîte noire et boîte blanche ; ce qui mérite une page).
- Google, *The Site Reliability Workbook*, chapitre « Implementing SLOs », https://sre.google/workbook/implementing-slos/ (SLI comme rapport, spécification et implémentation, fenêtres, politique de budget d'erreur).
- Google, *The Site Reliability Workbook*, chapitre « Alerting on SLOs », https://sre.google/workbook/alerting-on-slos/ (burn rate, alertes multi-fenêtres et multi-taux, défauts des approches simples).
- Prometheus — *Alerting*, https://prometheus.io/docs/practices/alerting/ (alerter sur les symptômes).
