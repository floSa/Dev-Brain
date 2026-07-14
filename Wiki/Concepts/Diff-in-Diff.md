---
galaxie: wiki
type: concept
nom: Diff-in-Diff
alias: [DiD, difference-in-differences, différence des différences, doubles différences]
categorie: concept/stats
domaines: [data-sci]
tags: [causal-inference, hypothesis-testing]
---

# Diff-in-Diff

## Aperçu

- Méthode quasi-expérimentale : estimer l'effet d'un traitement en comparant l'**évolution** d'un groupe traité à celle d'un groupe témoin, avant et après l'intervention.
- Soustraire l'évolution du témoin retire ce qui serait arrivé sans traitement (tendance commune) → on isole l'effet propre.
- Recours quand la randomisation d'un [[A-B testing|A/B test]] est impossible (changement de loi, déploiement régional, prix appliqué à tous).

## Concepts clés

### Les deux différences
- 1re différence : avant → après, dans chaque groupe (élimine ce qui est fixe par groupe).
- 2e différence : traité − témoin de ces évolutions (élimine la tendance commune à toute la période).

### Hypothèse des tendances parallèles
- Cœur de la méthode : sans traitement, traité et témoin auraient suivi des trajectoires **parallèles**. Invérifiable directement, on l'étaye en montrant des tendances pré-traitement parallèles.
- Si elle casse (les groupes divergeaient déjà), l'estimation est biaisée.

### Groupes et périodes
- Besoin d'au moins deux groupes et deux périodes. Généralisation : panels multi-périodes, adoptions échelonnées (designs récents : Callaway-Sant'Anna, problèmes des effets hétérogènes en TWFE).

## Les maths, simplement

- Estimateur 2×2 : $\widehat{\text{DiD}} = \big(\bar{Y}^{traité}_{après} - \bar{Y}^{traité}_{avant}\big) - \big(\bar{Y}^{témoin}_{après} - \bar{Y}^{témoin}_{avant}\big)$.
- Forme régression : $Y = \beta_0 + \beta_1\,\text{Traité} + \beta_2\,\text{Après} + \beta_3\,(\text{Traité}\times\text{Après}) + \varepsilon$.
- L'effet causal est le coefficient d'interaction $\beta_3$ ; son [[Tests d'hypothèse|test]] et son IC se lisent directement dans la régression (écarts-types groupés/clusterisés).
- Tendances parallèles ⇔ en l'absence de traitement, $\beta_3 = 0$ serait l'attendu.

## En pratique

- Toujours tracer les séries pré-traitement des deux groupes : des trajectoires parallèles avant l'intervention rendent l'hypothèse crédible (test de placebo / event study).
- Clusteriser les écarts-types au niveau du groupe randomisé/observé (sinon faux positifs).
- Méfiance avec l'adoption échelonnée et les effets variables dans le temps : l'estimateur TWFE classique peut être trompeur → estimateurs modernes.
- Vérifier l'absence de chocs concomitants ne touchant qu'un seul groupe (sinon confondu avec l'effet).

## Approches voisines & alternatives

- [[Inférence causale]] — le cadre général (DAG, confounding, identification) ; DiD en est une stratégie quasi-expérimentale.
- [[A-B testing]] — l'étalon-or causal par randomisation ; DiD prend le relais quand randomiser est impossible.
- [[Tests d'hypothèse]] — l'effet DiD se teste via le coefficient d'interaction de la régression.
- Méthodes de contrôle synthétique, régression sur discontinuité, variables instrumentales — autres designs d'inférence causale observationnelle, selon la source d'identification disponible.
- [[Dev/Services/CausalImpact|CausalImpact]] — séries temporelles structurelles bayésiennes : prédit le contrefactuel à partir de séries de contrôle, sans groupe témoin observé à proprement parler.

## Pour aller plus loin

- Réf : Card & Krueger (1994, salaire minimum) ; Angrist & Pischke — *Mostly Harmless Econometrics*.
- Avancées : Callaway & Sant'Anna (2021), Goodman-Bacon (2021) sur les biais du TWFE.
- Outils : [[Dev/Services/statsmodels|statsmodels]] / `linearmodels` (PanelOLS), `pyfixest` (effets fixes + clustering) ; [[Dev/Services/CausalImpact|CausalImpact]] pour l'approche série temporelle bayésienne.
