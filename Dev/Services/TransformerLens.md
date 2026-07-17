---
galaxie: dev
type: service
nom: TransformerLens
alias: [transformer_lens, HookedTransformer, TransformerBridge]
pitch: "Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/nnsight|nnsight]]", "[[Dev/Services/SAELens|SAELens]]"]
remplace_par: []
status: actif
tags: [explainability, llm]
url_docs: https://transformerlensorg.github.io/TransformerLens/
url_repo: https://github.com/TransformerLensOrg/TransformerLens
---

# TransformerLens

## Pourquoi

L'outil de référence de l'[[Interprétabilité mécaniste|interprétabilité mécaniste]], créé par Neel Nanda et aujourd'hui maintenu par Bryce Meyer et Jonah Larson. La quasi-totalité des résultats publiés du domaine sont sortis de cette bibliothèque.

Sa valeur n'est pas d'exposer des activations — n'importe quel hook PyTorch le fait — mais de **réécrire les poids en notation canonique**. Là où HuggingFace fusionne les têtes d'attention dans une seule matrice pour l'efficacité, TransformerLens les **sépare** et donne accès aux `W_Q`, `W_K`, `W_V`, `W_O` de chaque tête individuellement, ainsi qu'au flux résiduel décomposé par composant.

C'est ce qui rend le raisonnement en circuits praticable : on peut enfin poser « que fait la tête 5 de la couche 3 » et obtenir une réponse, plutôt que de démêler un tenseur fusionné.

## Quand l'utiliser

- **Analyse de circuits** : identifier ce que fait un composant, tracer un mécanisme (induction heads, circuit IOI). C'est son terrain, et il n'a pas d'égal dessus.
- **Activation patching / ablation** : le système de hooks est fait pour intervenir en cours de passe.
- Raisonner en **têtes d'attention séparées** ou en flux résiduel décomposé — la notation canonique est l'argument décisif.
- Modèles GPT-style de taille petite à moyenne (GPT-2, Pythia, Llama…) : plus de 9 000 modèles portés, 50+ familles d'architectures.
- Reproduire un résultat publié du domaine — l'écosystème et les notebooks sont écrits pour elle.

## Quand NE PAS l'utiliser

- **Modèle trop gros pour la machine** : elle charge tout localement. Pour intervenir sur un très gros modèle sans l'infrastructure, [[Dev/Services/nnsight|nnsight]] et son exécution distante.
- **Simple attribution** : hors sujet. [[Dev/Services/Captum|Captum]] ou [[Dev/Services/interpreto|interpreto]].
- **Entraîner ou analyser des SAE** : depuis la v2, cette partie a été **sortie** de TransformerLens et déplacée vers [[Dev/Services/SAELens|SAELens]] (`HookedSAETransformer`). Ne pas la chercher ici.
- **Production** : outil de recherche, coûteux en mémoire (elle conserve les activations).
- **Architecture exotique non portée** : le portage vers la notation canonique est fait modèle par modèle.

## Déploiement & coût

- `pip install transformer_lens` — bibliothèque Python. Gratuit (MIT). Dépendances : `torch`, `transformers`, `einops`.
- Exécution **single-node**. Le coût dominant est la **mémoire** : conserver les activations de toutes les couches pour analyse multiplie l'empreinte par rapport à une inférence ordinaire.
- Pensée pour le chercheur indépendant : l'essentiel du domaine se fait sur GPT-2 small, qui tourne sur un GPU grand public — voire en CPU.

## Pièges

- **La v3 a changé l'interface** : `TransformerBridge` est désormais le point d'entrée, `HookedTransformer` est déprécié tout en restant disponible. Beaucoup de tutoriels et notebooks en ligne visent encore l'ancienne API. Épingler la version.
- **Les SAE ne sont plus ici** : `HookedSAETransformer` a migré vers [[Dev/Services/SAELens|SAELens]] à la v2. Source de confusion fréquente dans la documentation ancienne.
- **Mémoire** : `run_with_cache` garde tout. Sur un modèle moyen et un batch un peu large, la saturation arrive vite. Ne mettre en cache que les hooks nécessaires.
- **Les poids sont retraités**, pas ceux de HuggingFace tels quels. C'est l'intérêt (notation canonique) et le risque : les valeurs numériques peuvent différer légèrement. La v3 préserve mieux les poids bruts.
- **Le piège méthodologique n'est pas dans l'outil** : l'ablation à zéro sort le modèle de sa distribution et fabrique des artefacts. Préférer l'ablation à la moyenne ([[Interprétabilité mécaniste]]).

## Alternatives

- [[Dev/Services/nnsight|nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).
- [[Dev/Services/SAELens|SAELens]] — Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens.

## Liens

- [[Interprétabilité mécaniste]] — le concept parent : circuits, patching, ablation, steering.
- [[Superposition]] — l'obstacle que l'analyse par composant rencontre.
- [[Sparse autoencoders]] — le démêlage, désormais confié à SAELens.
- [[Transformer architectures]] / [[Self-attention]] — l'objet d'étude, et la structure que la notation canonique rend lisible.
- [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/HuggingFace|HuggingFace]] — le socle requis.
