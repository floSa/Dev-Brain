---
role: brique
nom: SAELens
alias: [sae_lens, SAE Lens, HookedSAETransformer]
pitch: "Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[TransformerLens]]", "[[interpreto]]"]
complements: []
tags: [explainability, llm]
url_docs: https://decoderesearch.github.io/SAELens/
url_repo: https://github.com/jbloomAus/SAELens
---

# SAELens

<!-- AUTO:BANDEAU:START -->
> Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

L'outil de référence des [[Sparse autoencoders|sparse autoencoders]] appliqués aux modèles de langage, maintenu par Joseph Bloom, Curt Tigges, Anthony Duong et David Chanin. Il couvre les trois temps du sujet : **entraîner** un SAE — variantes TopK, JumpReLU, BatchTopK incluses —, **charger** un SAE pré-entraîné depuis un catalogue déjà constitué, et **analyser** les features obtenues (visualisations SAE-Vis, intégration Neuronpedia). C'est le catalogue qui fait sa valeur pratique : entraîner coûte des millions d'activations et un entraînement complet, charger prend trois lignes. Deux points de méthode commandent l'usage : un SAE vaut **pour une couche et un point d'accroche donnés**, et charger le mauvais produit des résultats silencieusement absurdes ; et rien ne garantit que les features trouvées soient celles du modèle plutôt qu'un artefact du SAE — des SAE entraînés sur du bruit produisent des features d'apparence tout aussi interprétable. Le curseur reconstruction/parcimonie n'a d'ailleurs pas d'optimum objectif : c'est un arbitrage, pas un réglage à optimiser. Cette fonction vivait historiquement dans [[TransformerLens]] ; elle en a été extraite à la v2.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Entraîner un SAE sur les activations d'un modèle de langage, sans réimplémenter la boucle, les variantes de parcimonie et les métriques | Analyse de circuits sans SAE : ce n'est pas son objet → [[TransformerLens]] |
| Réutiliser un SAE existant : le catalogue couvre les modèles usuels (GPT-2, Gemma, Llama…) — le réflexe à avoir avant d'en entraîner un | Modèles autres que des LLM : le domaine et l'outillage sont centrés sur le texte |
| Analyser les features : quelles entrées activent une direction, à quoi elle correspond, quel est son effet | Attribution, ou explication destinée à un métier : hors sujet → [[Captum]] ou [[SHAP]] |
| Recherche en interprétabilité mécaniste sur les LLM, en complément de l'analyse de circuits | Pipeline concept complet, avec méthodes de dictionnaire comparées (NMF, ICA, probes) → [[interpreto]] : SAELens ne fait que des SAE, mais les fait à fond |
| | Production : outil de recherche, coûteux |

## Mise en œuvre

- Installation — `uv add sae-lens` ; la **v6 est une refonte majeure** (253 releases), les tutoriels antérieurs ne s'appliquent pas tels quels — épingler la version
- Point d'entrée — import Python : charger un SAE du catalogue, ou lancer un entraînement
- Prérequis — `torch`, `transformer_lens`, `transformers` ; un GPU en pratique dès qu'on entraîne
- Exécution — single-node ; surveiller les *dead features* (unités jamais actives), symptôme d'entraînement le plus courant
- Coût — gratuit, MIT ; **charger** un SAE est quasi gratuit (quelques centaines de Mo), **entraîner** coûte des heures de GPU, la collecte de millions d'activations et un dictionnaire 16× à 64× plus large que la dimension du modèle

## Écosystème

### Alternatives

- [[TransformerLens]] — Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

## Ressources

- Documentation — https://decoderesearch.github.io/SAELens/
- Dépôt — https://github.com/jbloomAus/SAELens

## Voir aussi

- [[Sparse autoencoders]] — le concept parent : sur-complétude, parcimonie, variantes TopK et JumpReLU, et comment évaluer
- [[Superposition]] — le phénomène qui justifie l'existence des SAE
- [[Interprétabilité mécaniste]] — le chapeau du domaine
- [[Autoencodeurs]] — l'architecture d'origine, à contrainte inversée
- [[Comparatif - Explicabilité]] — ce qui départage les outils du dossier
