---
role: hub
nom: Méthodes causales
alias: [causal methods, méthodes causales, inférence causale et découverte causale]
pitch: Passer de « ces deux choses varient ensemble » à « celle-ci fait varier celle-là » — estimer un effet sans randomisation simple, par individu, ou retrouver le graphe qui le porte.
domaines: [data-sci]
tags: [causal-inference, statistical-inference]
---

# Méthodes causales

> Passer de « ces deux choses varient ensemble » à « celle-ci fait varier celle-là » — estimer un effet sans randomisation simple, par individu, ou retrouver le graphe qui le porte.

## Ce qu'il faut comprendre

- **Cinq pages, et l'ordre compte.** [[Inférence causale]] pose le cadre : résultats potentiels, DAG, confondeurs, ce qu'il faut ajuster. Les trois autres pages en dérivent : [[Diff-in-Diff]] et [[CausalImpact]] estiment un effet **moyen** sans randomisation, [[Modélisation d'uplift]] l'estime **par individu**, [[Découverte causale]] cherche le **graphe** que la première suppose connu.
- **Les trois hypothèses reviennent partout, sous des noms différents.** Ignorabilité (pas de confondant non observé), chevauchement (chaque profil peut recevoir chaque traitement), et pour les méthodes de découverte, fidélité et suffisance causale. Aucune ne se teste sur les données seules : c'est ce qui sépare ce dossier d'un simple outil statistique.
- **La randomisation reste l'étalon.** [[A-B testing]], au niveau du domaine, la fournit par construction ; les pages d'ici servent quand elle est impossible, trop coûteuse, ou qu'on veut savoir *pour qui* l'action marche.
- **La découverte causale ne remplace pas l'expert.** Les données d'observation ne retrouvent qu'une classe de graphes équivalents, et les benchmarks simulés ont été montrés faciles à tromper (varsortability). [[Découverte causale]] propose, un expert dispose, [[Inférence causale]] estime.
- **Frontière avec [[Statistiques & inférence]], au niveau du domaine** : concevoir et arrêter une expérience contrôlée ([[A-B testing]], [[CUPED]], [[Sequential testing]], [[Multi-armed bandits]]) reste au niveau du domaine ; ici, l'objet est l'effet causal lui-même.

## Choisir

- Poser le problème : quoi ajuster, quoi ne pas ajuster → [[Inférence causale]].
- Une intervention datée, un groupe traité, un groupe témoin, avant et après → [[Diff-in-Diff]].
- Un effet sur une série unique, sans groupe témoin randomisé → [[CausalImpact]].
- À qui adresser l'action, effet par individu, courbes de Qini → [[Modélisation d'uplift]].
- Retrouver ou tester un graphe causal à partir de données → [[Découverte causale]].
- Planifier l'expérience elle-même → [[A-B testing]], au dossier [[Statistiques & inférence]].

<!-- AUTO:START -->
<!-- AUTO:END -->
