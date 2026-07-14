---
galaxie: wiki
type: concept
nom: No Free Lunch theorem
alias: [Théorème No Free Lunch, No Free Lunch, NFL, pas de repas gratuit, théorème du pas de modèle universel]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [learning-theory, no-free-lunch]
---

# No Free Lunch theorem

## Aperçu

- Résultat d'impossibilité : **aucun algorithme d'apprentissage n'est universellement supérieur**. Moyenné sur *toutes* les distributions de problèmes possibles, tous les apprenants ont la même performance.
- Corollaire fondateur : généraliser **exige un a priori** (inductive bias). Sans hypothèse sur la structure du problème, voir des données ne dit rien sur les données non vues.

## Concepts clés

### Deux énoncés à distinguer
- **NFL pour l'optimisation** (Wolpert & Macready, 1997) : moyennée sur toutes les fonctions objectif, aucune stratégie de recherche ne bat la recherche aléatoire.
- **NFL pour l'apprentissage supervisé** (Wolpert, 1996) : moyenné sur tous les concepts cibles, aucun classifieur n'a une erreur de généralisation attendue meilleure qu'un autre.

### Le rôle de l'a priori (inductive bias)
- Si toutes les étiquetages du non-vu sont équiprobables, l'échantillon n'informe pas. La performance réelle vient de ce que les problèmes du monde **ne sont pas uniformément distribués** : régularité, parcimonie, lissité. Choisir un modèle, c'est parier sur ces régularités.
- Ce pari est exactement le choix de la classe d'hypothèses $\mathcal H$ du [[PAC learning]] : restreindre $\mathcal H$ = injecter un a priori = rendre l'apprentissage possible.

### Conséquence pratique
- Pas de « meilleur algorithme » dans l'absolu : la supériorité est toujours **relative à une famille de problèmes**. D'où l'importance d'essayer plusieurs modèles et de valider empiriquement.

## Les maths, simplement

- Formellement : pour deux algorithmes $A_1, A_2$, $\sum_{f} P(\text{erreur}\mid f, A_1) = \sum_{f} P(\text{erreur}\mid f, A_2)$, la somme portant sur toutes les fonctions cibles $f$ équiprobables.
- Lecture : tout gain sur une classe de problèmes est **compensé** par une perte exacte sur une autre. Le « repas » (bonne généralisation) est payé ailleurs par l'a priori.
- Ce n'est pas contradictoire avec les [[Generalization bounds]] : celles-ci sont conditionnelles à une classe $\mathcal H$ fixée (donc à un a priori), pas moyennées sur tous les problèmes.

## En pratique

- Justifie le **pluralisme** méthodologique : tester arbres, linéaires, boosting plutôt que chercher LE modèle (cf. [[Compromis biais-variance]] — le bon biais dépend du problème).
- Met en garde contre les benchmarks sur-généralisés : « X bat Y » n'a de sens que pour une distribution de tâches donnée.
- Rappelle que le **feature engineering** et le choix d'architecture sont l'endroit où l'a priori utile est injecté — souvent plus rentable que le réglage fin.

## Approches voisines & alternatives

- [[PAC learning]] — restreindre $\mathcal H$ (l'a priori que NFL rend obligatoire) est ce qui restaure l'apprenabilité.
- [[Generalization bounds]] — valides parce que conditionnelles à une classe ; NFL en marque la limite globale.
- [[Compromis biais-variance]] — NFL explique pourquoi aucun réglage biais/variance n'est optimal partout.
- [[VC dimension]] — la capacité qu'on choisit de limiter incarne l'a priori imposé par NFL.

## Pour aller plus loin

- Wolpert (1996) — *The Lack of A Priori Distinctions Between Learning Algorithms*.
- Wolpert & Macready (1997) — *No Free Lunch Theorems for Optimization*.
