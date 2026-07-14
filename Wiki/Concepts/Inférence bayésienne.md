---
galaxie: wiki
type: concept
nom: Inférence bayésienne
alias: [Bayesian inference, inference bayesienne, Bayes, statistique bayésienne]
categorie: concept/stats
domaines: [data-sci]
tags: [bayesian, statistical-inference, prior]
---

# Inférence bayésienne

## Aperçu

- Met à jour la probabilité d'une hypothèse (ou d'un paramètre) à mesure que les données s'ajoutent, en combinant une croyance **a priori** avec la **vraisemblance** des données.
- Traite le paramètre comme une variable aléatoire : la sortie est une **distribution** (l'a posteriori), pas un point unique.
- Pendant du cadre fréquentiste des [[Tests d'hypothèse]] : raisonne directement sur $P(\text{hypothèse} \mid \text{données})$.

## Concepts clés

### A priori, vraisemblance, a posteriori
- A priori $P(\theta)$ = croyance avant les données ; vraisemblance $P(D\mid\theta)$ = ce que disent les données ; a posteriori $P(\theta\mid D)$ = croyance mise à jour.
- Tout l'apprentissage tient dans la règle : a posteriori ∝ vraisemblance × a priori.

### Mise à jour séquentielle
- L'a posteriori d'aujourd'hui devient l'a priori de demain : on peut intégrer les données par lots, dans n'importe quel ordre.
- Petit échantillon → l'a priori pèse ; gros échantillon → la vraisemblance domine et l'a posteriori se concentre.

### Distribution a posteriori
- Objet central : résume toute l'incertitude. On en tire un point ([[Estimation MAP|MAP]], moyenne a posteriori) ou un intervalle.

### Intervalle de crédibilité
- 95 % de crédibilité = « le paramètre a 95 % de probabilité d'être dans cet intervalle » — interprétation directe, contrairement à l'[[Intervalles de confiance|IC]] fréquentiste.

## Les maths, simplement

- Théorème de Bayes : $P(\theta \mid D) = \dfrac{P(D \mid \theta)\,P(\theta)}{P(D)}$ — a posteriori = vraisemblance × a priori, normalisé.
- En pratique, la proportionnalité suffit pour la forme : $P(\theta\mid D) \propto P(D\mid\theta)\,P(\theta)$.
- Évidence (le dénominateur) : $P(D) = \int P(D\mid\theta)\,P(\theta)\,d\theta$ — souvent intraitable, d'où le [[MCMC]] ou les [[A priori conjugués]].
- Mise à jour séquentielle : l'a posteriori obtenu après $D_1$ sert d'a priori pour $D_2$.

## En pratique

- Calcul de l'a posteriori : forme fermée si a priori conjugué (cf. [[A priori conjugués]]) ; sinon échantillonnage MCMC ([[Dev/Services/PyMC|PyMC]], [[Dev/Services/Stan|Stan]], NumPyro) ou inférence variationnelle.
- A priori informatif (encode une connaissance) ou faiblement informatif (laisse parler les données) → toujours documenter le choix et tester sa sensibilité.
- Résumés de l'a posteriori : moyenne ou médiane, mode ([[Estimation MAP|MAP]]), intervalle de crédibilité (HDI).
- Atout produit : énonce « proba que B batte A = 92 % », plus lisible qu'une p-value pour décider (cf. [[A-B testing]] bayésien).

## Approches voisines & alternatives

- [[Estimation MAP]] — résumé ponctuel de l'a posteriori (son mode), quand un seul chiffre suffit.
- [[Maximum de vraisemblance]] — cas limite à a priori plat : le MAP rejoint le MLE, sans distribution autour.
- [[A priori conjugués]] — choisir l'a priori dans la famille qui garde l'a posteriori calculable analytiquement.
- [[MCMC]] — échantillonne l'a posteriori quand il n'a pas de forme fermée (le cas général).
- [[KL divergence]] — l'inférence variationnelle remplace l'échantillonnage par la minimisation d'une divergence KL à l'a posteriori.
- [[Tests d'hypothèse]] — le cadre fréquentiste dual ; ici on compare via facteurs de Bayes plutôt que p-values.
- [[Intervalles de confiance]] — l'analogue fréquentiste de l'intervalle de crédibilité, sans l'interprétation probabiliste directe.

## Pour aller plus loin

- Réf : Gelman et al. — *Bayesian Data Analysis* ; McElreath — *Statistical Rethinking*.
- Outils : [[Dev/Services/PyMC|PyMC]], NumPyro, [[Dev/Services/Stan|Stan]] (`cmdstanpy`) ; diagnostics a posteriori avec [[Dev/Services/ArviZ|ArviZ]] ; [[Dev/Services/scipy.stats|scipy.stats]] pour les cas conjugués ; [[Dev/Services/CausalImpact|CausalImpact]] pour l'effet causal d'une intervention.
- Tag-ombrelle `statistical-inference` : sujet « Inférence statistique » à créer un jour comme parent commun (cf. [[Tests d'hypothèse]]).
