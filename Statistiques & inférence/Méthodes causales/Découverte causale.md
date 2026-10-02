---
role: notion
nom: Découverte causale
alias: [causal discovery, structure learning causale, apprentissage de structure causale, causal structure learning, PC algorithm, algorithme PC, FCI, GES, greedy equivalence search, LiNGAM, NOTEARS, d-séparation, d-separation, CPDAG, classe d'équivalence de Markov, Markov equivalence class, varsortability, fidélité, faithfulness, suffisance causale]
categorie: stats/causal
domaines: [data-sci]
tags: [causal-inference, statistical-inference]
---

# Découverte causale

## Aperçu

- Retrouver un **graphe causal** (qui cause quoi) à partir de données, au lieu de le dessiner à la main avant d'estimer un effet comme le fait l'[[Inférence causale]].
- Le graphe visé est un **DAG** : orienté, sans cycle. Les données d'observation ne suffisent en général qu'à en retrouver une **classe** de graphes équivalents, pas un seul.
- Chaque algorithme tient à des **hypothèses d'identifiabilité** explicites (pas de variable cachée, linéarité, bruit non gaussien…). Hors de ces hypothèses, rien n'est garanti.
- Produit des **hypothèses causales à valider**, pas des effets établis : le résultat se lit avec un expert du domaine.

## Concepts clés

### DAG, d-séparation et hypothèses de base

- **d-séparation** : critère graphique qui dit quelles indépendances conditionnelles le DAG implique. Si $A$ et $B$ sont d-séparés par $S$, alors $X_A \perp X_B \mid X_S$ (Heinze-Deml, Maathuis, Meinshausen, 2018).
- **Hypothèse de Markov causale** : chaque variable est indépendante de ses non-descendants sachant ses parents (Glymour, Zhang, Spirtes, 2019). Elle fait passer du graphe aux indépendances.
- **Fidélité** : la réciproque — toute indépendance observée vient d'une d-séparation. Avec Markov, elle donne une correspondance entre d-séparation et indépendances conditionnelles. Non testable en général (Reisach et al., 2021, citant Zhang et Spirtes).
- **Suffisance causale** : pas de variable latente qui cause deux variables mesurées.

### Classe d'équivalence de Markov

- Deux DAG sont équivalents (mêmes indépendances) s'ils ont le même **squelette** et les mêmes **v-structures** $A \to C \leftarrow B$ avec $A$, $B$ non adjacents (Verma et Pearl, repris par Chickering, 2002).
- La classe se représente par un **CPDAG** : une arête $i \to j$ y figure si elle a cette orientation dans **tous** les DAG de la classe ; une arête non orientée signifie que les deux orientations existent dans la classe.
- Avec bruit gaussien et données i.i.d. d'observation, le DAG n'est en général **pas identifiable** : on identifie sa classe de Markov (Heinze-Deml et al., §3.1). C'est la limite structurelle de la discipline.

### Algorithmes par contraintes : PC et FCI

- **PC** (Spirtes, Glymour, Scheines) : suppose acyclicité, fidélité et suffisance causale. Part du graphe complet, retire une arête dès qu'un **test d'indépendance conditionnelle** trouve un ensemble séparateur (en augmentant la taille de l'ensemble), oriente les v-structures, puis propage les orientations. Renvoie un **CPDAG**. Consistant en haute dimension si le graphe est parcimonieux (Kalisch et Bühlmann, cités par Heinze-Deml et al.).
- **FCI** : lève la suffisance causale (variables latentes en nombre quelconque) et renvoie un **PAG**, qui représente une classe de graphes ancestraux maximaux. Plus de tests, donc plus fragile à taille d'échantillon finie ; variantes RFCI, FCI+.
- Qualité = qualité des tests d'indépendance : une erreur de test se propage dans les orientations.

### Algorithmes par score : GES

- **GES** (Chickering, 2002) : cherche dans l'espace des **classes d'équivalence**, en deux phases — ajout d'arêtes tant que le score monte, puis suppression d'arêtes tant que le score monte.
- Fondement : preuve de la **conjecture de Meek** (si un DAG $H$ est une carte d'indépendance d'un DAG $G$, une suite d'ajouts d'arêtes et de renversements d'arêtes couvertes mène de $G$ à $H$). Optimalité **asymptotique** seulement : distribution génératrice représentable par un DAG parfait, grand échantillon, score localement consistant.
- Limite posée par l'auteur : l'extension aux variables cachées est laissée ouverte.

### Bruit non gaussien : LiNGAM

- **LiNGAM** (Shimizu, Hoyer, Hyvärinen, Kerminen, 2006) : sous trois hypothèses — **linéarité**, **pas de confondant non observé**, **bruits non gaussiens indépendants** — le DAG est **entièrement identifiable**, sans ordre préalable. Il se retrouve par analyse en composantes indépendantes (ICA).
- C'est le contraste avec le cas gaussien : la non-gaussianité fournit l'information qui sépare cause et effet.
- **DirectLiNGAM** (Shimizu et al., 2011) : variante sans paramètres d'algorithme, avec garantie de convergence en un nombre fixe d'étapes si les données suivent strictement le modèle (résumé lu seulement).
- Cas non linéaire à **bruit additif** (Hoyer et al., 2008 ; Peters et al., 2014) : le DAG est identifiable sous des conditions douces (résumés lus seulement).
- **Désaccord laissé tel quel** : Reisach et al. (2021) attribuent à Shimizu et al. (2006) l'hypothèse de fidélité ; le texte de Shimizu et al. (§2) n'en a pas besoin.

### Optimisation continue : NOTEARS

- **NOTEARS** (Zheng, Aragam, Ravikumar, Xing, NeurIPS 2018) : remplace la recherche combinatoire par un problème d'optimisation sur une matrice de poids $W$, avec une contrainte d'acyclicité **lisse et exacte**.
- Cadre : modèle structurel linéaire, perte moindres carrés avec pénalité $\ell_1$, résolu par lagrangien augmenté, puis seuillage des poids.
- Limites que les auteurs énoncent : problème non convexe (seuls des points stationnaires), coût $O(d^3)$ par évaluation de l'exponentielle matricielle, seuil fixé à la main.

### Interventions et contextes multiples

- Des **interventions** (expériences où l'on force une variable) affinent la classe d'équivalence : GIES (Hauser et Bühlmann, 2012) adapte GES aux interventions connues.
- **JCI** (Mooij, Magliacane, Claassen, 2020) : cadre qui traite plusieurs contextes comme des variables supplémentaires, avec n'importe quel algorithme acceptant des connaissances a priori.

## Les maths, simplement

- Factorisation selon le DAG : $f(x) = \prod_i f\big(x_i \mid x_{\mathrm{pa}(i)}\big)$ — chaque variable dépend de ses seuls parents.
- Contrainte d'acyclicité de NOTEARS : $h(W) = \operatorname{tr}\!\big(e^{W \circ W}\big) - d$, nulle si et seulement si $W$ est un DAG ($\circ$ : produit terme à terme, $d$ : nombre de variables).
- LiNGAM : $x = Ae$ avec $A = (I - B)^{-1}$ ; l'ICA estime $A$ à l'échelle et à la permutation des colonnes près, et la permutation unique sans zéro sur la diagonale de $W = A^{-1}$ donne l'ordre causal (démonstration dans l'annexe du papier, non lue ici).
- Varsortability (Reisach et al., 2021) : fraction des chemins dirigés qui partent d'un nœud de variance marginale plus faible que celle du nœud d'arrivée (un demi-point en cas d'égalité). Si elle vaut 1, trier par variance croissante donne un **ordre causal valide**.

## En pratique

- **Ce que les données d'observation ne permettent pas** : orienter les arêtes d'une même classe d'équivalence ; exclure un confondant caché (sauf FCI, au prix de tests plus nombreux) ; remplacer une expérience.
- **Rôle de l'expertise métier** : les bibliothèques savent injecter des connaissances a priori — arêtes interdites ou obligatoires, ordre temporel par niveaux (`causal-learn` : `BackgroundKnowledge`, utilisé par `pc` ; `gCastle` : `PrioriKnowledge` ; `lingam` : matrice `prior_knowledge`). Une arête interdite par la physique du système vaut mieux qu'une arête « découverte ».
- **Critique des benchmarks** : Reisach, Seiler, Weichwald (*Beware of the simulated DAG!*, NeurIPS 2021) montrent que dans les DAG additifs simulés « génériques », la variance marginale **croît le long de l'ordre causal**. Un algorithme qui exploite cet artefact réussit sans rien découvrir. Sur données **standardisées**, NOTEARS et ses proches, excellents sur données brutes, se dégradent fortement ; un baseline sans modèle causal — trier par variance puis régresser — rivalise avec eux sur données brutes. PC, FGES et DirectLiNGAM, invariants d'échelle par construction, sont peu concernés. Sur les données protéiques réelles de Sachs et al., la varsortability moyenne est de 0,57 (écart-type 0,01), proche du hasard.
- **NOTEARS et l'échelle** : Kaiser et Sipos (2021) donnent un contre-exemple à quatre variables où NOTEARS inverse une arête une fois les variables normalisées, que DirectLiNGAM retrouve ; ils concluent que NOTEARS cherche un DAG parcimonieux qui explique la variance résiduelle, pas un graphe causal.
- **Au-delà de la variance** : Reisach et al. (2023) trouvent un motif voisin, invariant d'échelle (le $R^2$ croît le long de l'ordre causal), et un critère de tri qui rivalise avec des méthodes établies. Reisach et al. (arXiv, mai 2026) en signalent un troisième : le nombre de nœuds atteignables par chemins ouverts croît le long de l'ordre causal dans les DAG aléatoires courants. Conséquence pratique : **ne pas conclure d'un bon score sur DAG simulé**.
- **Standardiser n'élimine pas le problème** : les données standardisées gardent des motifs exploitables (Reisach et al., 2021).
- Stratégie raisonnable : algorithme à contraintes ou score pour proposer un squelette, **expert** pour orienter, puis [[Inférence causale]] pour estimer l'effet — et un [[A-B testing|test randomisé]] quand c'est possible.

### Avec des LLM

Kıcıman, Ness, Sharma, Tan (*Causal reasoning and large language models*, arXiv 2305.00050, TMLR) rapportent que GPT-3.5 et GPT-4 atteignent 97 % de réussite sur une tâche de découverte causale **par paires**, à partir des **noms de variables** et non des données ; ils signalent des modes d'échec imprévisibles. Deux prépublications (résumés lus seulement) mettent en cause ce type d'évaluation : Srivastava et al. (arXiv 2510.16530, octobre 2025) soutiennent que les benchmarks ont probablement été vus à l'entraînement, que les modèles font « bien pire » sur des études publiées après leur date limite, et que des a priori LLM injectés dans PC améliorent l'un et l'autre pris seuls ; *CausalArena* (arXiv 2609.11897, septembre 2026) relève que les classements changent beaucoup d'une famille de modèles causaux à l'autre et que le recouvrement entre pré-entraînement et évaluation est un enjeu central. Un LLM propose des hypothèses d'expert ; il ne remplace pas un test sur données.

### En Python

- `causal-learn` (0.1.4.8, 2026-07-11, dépôt py-why) : PC, FCI, GES, LiNGAM, connaissances a priori pour PC.
- `lingam` (1.13.0, 2026-07-22, MIT) : LiNGAM, DirectLiNGAM, `prior_knowledge`.
- `gCastle` (1.0.4, 2025-03-07, Apache 2.0) : PC, GES, DirectLiNGAM, NOTEARS et variantes, GOLEM, nombreuses méthodes neuronales ; README annonçant Python ≤ 3.9.
- `cdt` (0.6.0, 2022-08-23) : quasi gelé sur PyPI.
- Tetrad (v7.6.10, 2026-01-06, Java, GPL-3.0) et son pont Python `py-tetrad`.
- `DoWhy` (0.14, 2025-11-08) : modélisation et estimation causales à partir d'un graphe donné, **pas** de la découverte.

## Approches voisines & alternatives

- [[Inférence causale]] — suppose un graphe connu pour choisir quoi ajuster ; la découverte tente de le fournir.
- [[A-B testing]] — la randomisation fixe l'orientation des effets du traitement sans rien deviner du graphe.
- [[Diff-in-Diff]] — identification par quasi-expérience, graphe supposé connu.
- [[Modélisation d'uplift]] — suppose aussi l'ignorabilité ; la découverte causale peut aider à choisir les covariables d'ajustement.
- [[Inférence bayésienne]] — l'apprentissage de structure bayésien met une loi sur les graphes ; voisin par le score, pas par les hypothèses.
- [[Modèles graphiques probabilistes]] — le cadre des graphes (d-séparation, équivalence de Markov, fidélité) sur lequel s'appuient les algorithmes d'apprentissage de structure.
- Briques du brain : **sans objet** — aucune bibliothèque de découverte causale n'a de fiche.

## Pour aller plus loin

- Spirtes, Glymour, Scheines (2000), *Causation, Prediction, and Search*, 2e éd., MIT Press — notice seule consultée, texte non lu ; une notice indexe décembre 2001 (année à confirmer sur la page éditeur).
- Pearl (2009), *Causality*, 2e éd., Cambridge UP — texte non lu ; la d-séparation est citée ici via Heinze-Deml et al.
- Chickering (2002), *Optimal structure identification with greedy search*, JMLR 3:507–554 : <https://jmlr.org/papers/v3/chickering02b.html>
- Shimizu, Hoyer, Hyvärinen, Kerminen (2006), *A linear non-Gaussian acyclic model for causal discovery*, JMLR 7:2003–2030 : <https://jmlr.org/papers/v7/shimizu06a.html>
- Zheng, Aragam, Ravikumar, Xing (2018), *DAGs with NO TEARS*, NeurIPS : <https://arxiv.org/abs/1803.01422>
- Reisach, Seiler, Weichwald (2021), *Beware of the simulated DAG!*, NeurIPS : <https://arxiv.org/abs/2102.13647> ; Reisach et al. (2023), *A scale-invariant sorting criterion to find a causal order in additive noise models* : <https://arxiv.org/abs/2303.18211> ; Reisach, Chambaz, Blanchard, Weichwald (2026), *A topological sorting criterion for random causal DAGs* : <https://arxiv.org/abs/2605.06288>
- Kaiser & Sipos (2021), *Unsuitability of NOTEARS for causal graph discovery* : <https://arxiv.org/abs/2104.05441>
- Heinze-Deml, Maathuis, Meinshausen (2018), *Causal structure learning*, Annual Review of Statistics and Its Application : <https://arxiv.org/abs/1706.09141> ; Glymour, Zhang, Spirtes (2019), *Review of causal discovery methods based on graphical models*, Frontiers in Genetics : <https://pmc.ncbi.nlm.nih.gov/articles/PMC6558187/>
- Hauser & Bühlmann (2012), GIES, JMLR 13 ; Mooij, Magliacane, Claassen (2020), JCI, JMLR 21(99) : <https://arxiv.org/abs/1611.10351> — résumés seulement.
- Kıcıman, Ness, Sharma, Tan, *Causal reasoning and large language models* : <https://arxiv.org/abs/2305.00050>
- Connexions brain : [[Inférence causale]], [[Modélisation d'uplift]], [[A-B testing]], [[Diff-in-Diff]].
