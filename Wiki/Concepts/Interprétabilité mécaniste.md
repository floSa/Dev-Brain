---
galaxie: wiki
type: concept
nom: Interprétabilité mécaniste
alias: [Mechanistic interpretability, Mech interp, Interpretabilite mecaniste, Circuits, Transformer circuits, Activation patching, Causal tracing]
categorie: concept/dl
domaines: [ai-eng, data-sci]
tags: [explainability, deep-learning, llm]
---

# Interprétabilité mécaniste

## Aperçu

- Programme de **rétro-ingénierie** des réseaux : ne pas se contenter de pondérer les entrées, mais reconstituer les **algorithmes** que le modèle a appris — quels composants font quoi, et comment ils s'enchaînent.
- La différence de nature avec le reste de l'[[Explicabilité des modèles|explicabilité]] : celle-ci décrit un **comportement** (« ce token a pesé 0,3 »), celle-là cherche un **mécanisme** (« ces têtes d'attention copient le token précédent, puis celle-ci en fait une induction »). L'ambition est de lire le programme, pas de résumer les sorties.

## Concepts clés

### L'ambition, et le pari
- Un réseau entraîné est un programme écrit par la descente de gradient dans un langage que personne n'a conçu. Le pari du domaine : ce programme est **compréhensible**, si l'on trouve la bonne unité d'analyse.
- Motivation dominante : la **sécurité**. Détecter une capacité dangereuse ou une tromperie exige de regarder le mécanisme — les tests de comportement ne montrent que ce qu'on a pensé à tester.

### Circuits
- L'unité d'analyse : un **sous-graphe** de composants (têtes d'attention, neurones MLP) qui, ensemble, implémentent une fonction identifiable.
- L'exemple canonique, les **induction heads** : une paire de têtes qui, ayant vu `[A][B]`, complètent un `[A]` ultérieur par `[B]`. Découvertes dans de petits Transformers, elles sont aujourd'hui reconnues comme le socle de l'apprentissage en contexte (*in-context learning*) — un résultat majeur du domaine.

### L'obstacle fondateur
- On voudrait qu'un neurone = un concept. C'est faux : les neurones sont **polysémantiques**, parce que le modèle entasse plus de features qu'il n'a de dimensions ([[Superposition]]).
- Conséquence : la base des neurones n'est pas la base des concepts. Il faut donc d'abord **démêler** — c'est le rôle des [[Sparse autoencoders|SAE]] — avant d'espérer lire quoi que ce soit.

### Corrélation vs causalité — la ligne de partage
- C'est ce qui sépare ce domaine du reste de l'explicabilité. Une [[Attribution par gradient|attribution]] ou un [[Probing|probe]] établissent une **corrélation** : l'information est là, elle covarie avec la sortie.
- L'interprétabilité mécaniste **intervient** : on modifie une activation et on regarde si la sortie change. Si oui, le composant est causalement impliqué. C'est une expérience, pas une observation.

### Les techniques d'intervention
- **Activation patching** (*causal tracing*) : remplacer l'activation d'un composant par celle obtenue sur une autre entrée, et mesurer l'effet sur la sortie. La technique centrale du domaine.
- **Ablation** : mettre un composant à zéro (ou à sa moyenne) et voir ce qui casse. Attention — l'ablation à zéro sort le modèle de sa distribution et produit des artefacts ; l'ablation à la moyenne est plus honnête.
- **Steering** : ajouter un vecteur de direction aux activations pour infléchir le comportement. La preuve causale la plus forte — et le début d'un usage pratique (contrôle, [[Guardrails|garde-fous]]).

### La chaîne méthodologique
1. **[[Superposition]]** — comprendre pourquoi les neurones ne sont pas la bonne unité.
2. **[[Sparse autoencoders]]** — démêler les activations en directions candidates.
3. **[[Probing]]** — vérifier qu'une direction connue est présente et lisible.
4. **Intervention** (patching, ablation, steering) — établir qu'elle est **utilisée**.

Sauter l'étape 4 est l'erreur la plus courante : on conclut à un mécanisme sur la foi d'une corrélation.

## Les maths, simplement

- **Décomposition du flux résiduel** — la lecture qui structure tout le domaine : dans un Transformer, chaque bloc *ajoute* au flux résiduel plutôt que de le remplacer. On peut donc écrire la sortie comme une somme des contributions de chaque composant : $x_{\text{final}} = x_0 + \sum_{\ell} \text{Attn}_\ell(x_\ell) + \sum_{\ell} \text{MLP}_\ell(x_\ell)$.
  - Conséquence : le flux résiduel est un **canal de communication** partagé, où chaque composant lit et écrit. C'est ce qui rend l'analyse par composant possible.
- **Activation patching**, formellement : soit $x_{\text{clean}}$ et $x_{\text{corrupt}}$ deux entrées ne différant que par un détail. On exécute sur $x_{\text{corrupt}}$ en remplaçant l'activation du composant $c$ par celle relevée sur $x_{\text{clean}}$. L'effet mesuré est $\Delta = f_{\text{patché}}(x_{\text{corrupt}}) - f(x_{\text{corrupt}})$.
  - $\Delta$ grand → le composant $c$ **porte causalement** l'information qui distingue les deux entrées.
- **Steering** : $h' = h + \alpha \, v$, où $v$ est une direction (issue d'un [[Probing|probe]] ou d'un [[Sparse autoencoders|SAE]]) et $\alpha$ son intensité. Si la sortie change dans le sens attendu, la direction est causale — et devient un levier de contrôle.

## En pratique

- **Domaine de recherche, pas d'ingénierie.** Pour expliquer une prédiction à un métier ou à un régulateur, utiliser [[Explicabilité des modèles|SHAP]] ou une [[Attribution par gradient|attribution]]. L'interprétabilité mécaniste sert à auditer un modèle, chercher une capacité, comprendre un échec.
- **Ne s'applique presque qu'aux Transformers** — et surtout à des modèles petits ou moyens. L'essentiel des résultats vient de GPT-2 small et de modèles jouets. Le passage à l'échelle est le défi ouvert.
- **Coûteux en temps humain** : identifier un circuit se compte en semaines d'analyse. Il n'y a pas de bouton.
- **Le doute est de rigueur.** Beaucoup de résultats sont fragiles : circuits qui ne se retrouvent pas d'un modèle à l'autre, SAE dont les features paraissent interprétables même entraînés sur du bruit. Le domaine est jeune et se corrige vite ; se méfier des conclusions définitives.
- **La retombée pratique existe déjà** : le *steering* par vecteur d'activation est un moyen de contrôle bien plus léger qu'un fine-tuning ou qu'un modèle de garde, et il commence à sortir des labos ([[Guardrails]], [[AI security]]).
- Outils : [[Dev/Services/TransformerLens|TransformerLens]] (la référence pour l'analyse de circuits), [[Dev/Services/nnsight|nnsight]] (intervention sur modèles distants ou volumineux), [[Dev/Services/SAELens|SAELens]] (SAE), [[Dev/Services/interpreto|interpreto]] (le pipeline concept de bout en bout).

## Approches voisines & alternatives

- [[Superposition]] — l'obstacle fondateur : pourquoi les neurones ne sont pas la bonne unité d'analyse.
- [[Sparse autoencoders]] — l'outil de démêlage, aujourd'hui central dans le domaine.
- [[Probing]] — la brique corrélationnelle, à compléter par l'intervention.
- [[Attribution par gradient]] — la question voisine mais distincte : quelle **entrée** a pesé, pas quel **mécanisme** opère.
- [[Explicabilité des modèles]] — le versant post-hoc et tabulaire, qui décrit sans rétro-concevoir.
- [[Transformer architectures]] / [[Self-attention]] — l'objet d'étude, et sa structure résiduelle qui rend l'analyse possible.
- [[AI security]] / [[Guardrails]] — la motivation dominante, et le débouché du steering.
- [[Reasoning models]] — le comportement que le domaine cherche aujourd'hui à expliquer.

## Pour aller plus loin

- Elhage et al. (2021) — *A Mathematical Framework for Transformer Circuits* (Anthropic) : la décomposition du flux résiduel. Le texte fondateur.
- Olsson et al. (2022) — *In-context Learning and Induction Heads* (Anthropic).
- Meng et al. (2022) — *Locating and Editing Factual Associations in GPT* (ROME) : le causal tracing appliqué aux faits.
- Wang et al. (2022) — *Interpretability in the Wild* (le circuit IOI de GPT-2) : un circuit complet, disséqué de bout en bout.
- *Transformer Circuits Thread* (transformer-circuits.pub) — la publication de référence du domaine.
