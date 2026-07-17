---
galaxie: wiki
type: concept
nom: Probing
alias: [Probe, Probes, Sonde linéaire, Linear probe, Sondage, Diagnostic classifier, Probing classifier]
categorie: concept/dl
domaines: [data-sci, ai-eng]
tags: [explainability, deep-learning, representation-learning]
---

# Probing

## Aperçu

- Technique pour savoir **ce qu'une couche encode** : geler le modèle, extraire ses activations, et entraîner un petit classifieur (la *sonde*) à prédire une propriété connue depuis ces activations. Si la sonde y arrive, l'information est là.
- L'inversion est astucieuse : au lieu d'ouvrir le modèle, on **teste ce qu'on peut lire dedans**. Simple, rapide, et applicable à n'importe quelle couche de n'importe quel réseau.

## Concepts clés

### Le protocole
1. Geler le modèle — on ne le réentraîne jamais.
2. Faire passer des données, capter les activations d'une couche donnée.
3. Entraîner une sonde (souvent une [[Régression logistique|régression logistique]]) à prédire une propriété étiquetée : partie du discours, sentiment, langue, véracité d'une affirmation.
4. Lire l'exactitude de la sonde. Élevée → la propriété est **linéairement accessible** à cette couche.

### Pourquoi la sonde doit rester faible
- **Le piège fondateur du domaine.** Une sonde puissante (un MLP profond) atteindra une bonne exactitude même sur des activations aléatoires — elle aura *appris la tâche elle-même* au lieu de *lire* le modèle.
- D'où la règle : sonde **linéaire**, de préférence. Ce qu'on mesure alors est l'accessibilité linéaire de l'information, pas la capacité de la sonde.
- La question « la sonde lit-elle ou apprend-elle ? » n'a pas de réponse parfaite. C'est la limite structurelle de la méthode.

### Le contrôle indispensable
- Une exactitude de 85 % ne veut rien dire seule. Il faut une **baseline de contrôle** : la même sonde sur des activations aléatoires, ou sur des étiquettes permutées.
- La *selectivity* formalise ça : écart entre l'exactitude sur la vraie tâche et sur une tâche de contrôle aux étiquettes aléatoires. Une sonde qui réussit les deux ne prouve rien.

### Sonder les couches, pas juste le modèle
- L'intérêt réel est le **profil par couche** : sonder chaque couche et regarder où l'information apparaît, culmine, disparaît.
- Résultat classique sur les Transformers : les couches basses portent la syntaxe, les couches hautes la sémantique — et certaines informations sont *perdues* en fin de réseau parce qu'elles ne servent plus à la tâche.

### Les variantes
- **Linéaire** — régression logistique. Le défaut, et le plus défendable.
- **Par centroïdes** — direction = différence des moyennes entre classes. Encore plus contraint, souvent suffisant, et directement interprétable comme une direction dans l'espace.
- **Non linéaire (MLP)** — mesure ce qui est *présent*, pas ce qui est *accessible*. À manier avec la plus grande méfiance.

### Corrélation, jamais causalité
- **La limite qui compte.** Une sonde réussie prouve que l'information est *présente et lisible*. Elle ne prouve pas que le modèle **s'en sert**.
- Un modèle peut encoder le genre grammatical sans jamais l'utiliser pour sa prédiction. Pour conclure à un usage, il faut intervenir — patcher l'activation, la supprimer, et voir si la sortie change ([[Interprétabilité mécaniste]]).

## Les maths, simplement

- Soit $h_\ell(x) \in \mathbb{R}^d$ les activations de la couche $\ell$. La sonde ajuste $g_\theta$ pour prédire $y$ (la propriété) depuis $h_\ell(x)$ : $\min_\theta \sum_i \mathcal{L}\big(y_i, \, g_\theta(h_\ell(x_i))\big)$ — **sans jamais toucher aux poids du modèle**.
- Sonde linéaire : $g_\theta(h) = \text{softmax}(W h + b)$. Le vecteur $w_k$ appris est une **direction** dans l'espace d'activations, celle qui porte la propriété.
- Sonde par centroïdes, encore plus dépouillée : $w = \mu_{+} - \mu_{-}$, la différence des moyennes des deux classes. Pas d'optimisation du tout, et la direction est interprétable telle quelle.
- Selectivity $= \text{Acc}(\text{tâche réelle}) - \text{Acc}(\text{tâche de contrôle})$. C'est ce nombre qu'il faut regarder, pas l'exactitude brute.

## En pratique

- **Toujours poser une baseline de contrôle.** Une sonde sur activations aléatoires. Sans ce chiffre en face, l'exactitude de la sonde n'est pas interprétable — c'est l'erreur la plus fréquente du domaine.
- **Rester linéaire.** Dès qu'on complexifie la sonde, on mesure la sonde et non le modèle.
- **Sonder toutes les couches, pas une seule.** Le profil est l'information ; un point isolé ne dit rien.
- **Ne pas conclure à la causalité.** Ce que la sonde trouve est présent, pas forcément utilisé. C'est là que [[Superposition|superposition]] et [[Sparse autoencoders|SAE]] prennent le relais : le probing cherche une direction **connue d'avance**, les SAE **découvrent** les directions inconnues. Les deux sont complémentaires, pas concurrents.
- **Attention à la fuite** : les activations sont de très grande dimension et $n$ est souvent petit. Régulariser la sonde et valider proprement ([[Validation croisée]], [[Data leakage]]).
- Usage industriel réel : détecter en temps réel qu'un LLM encode un état problématique (toxicité, hallucination) en lisant une direction connue de ses activations — bien moins coûteux qu'un modèle de garde ([[Guardrails]]).
- Outils : [[Dev/Services/interpreto|interpreto]] (sondes linéaires et par centroïdes, avec l'outillage de concepts autour), [[Dev/Services/nnsight|nnsight]] / [[Dev/Services/TransformerLens|TransformerLens]] pour capter les activations, [[Dev/Services/Scikit-Learn|sklearn]] pour la sonde elle-même.

## Approches voisines & alternatives

- [[Sparse autoencoders]] — le pendant non supervisé : découvrir les directions au lieu d'en chercher une connue.
- [[Superposition]] — pourquoi une direction, et non un neurone, est la bonne unité d'analyse.
- [[Interprétabilité mécaniste]] — le chapeau, et l'étape d'après : intervenir pour établir la causalité.
- [[Attribution par gradient]] — l'autre versant : quelle **entrée** a pesé, plutôt que ce que le modèle **encode**.
- [[Régression logistique]] — la sonde par défaut.
- [[embeddings]] — les représentations que le probing interroge.
- [[Explicabilité des modèles]] — le versant tabulaire et post-hoc.
- [[Transfer learning vision]] — le *linear probing* y désigne le même geste, employé pour évaluer un backbone plutôt que pour l'interpréter.

## Pour aller plus loin

- Alain & Bengio (2016) — *Understanding intermediate layers using linear classifier probes* : l'article fondateur.
- Hewitt & Liang (2019) — *Designing and Interpreting Probes with Control Tasks* : l'origine de la selectivity, et la critique des sondes trop puissantes.
- Belinkov (2022) — *Probing Classifiers: Promises, Shortcomings, and Advances* : la synthèse critique du domaine.
