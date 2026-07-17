---
galaxie: dev
type: service
nom: SAELens
alias: [sae_lens, SAE Lens, HookedSAETransformer]
pitch: "Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/TransformerLens|TransformerLens]]", "[[Dev/Services/interpreto|interpreto]]"]
remplace_par: []
status: actif
tags: [explainability, llm]
url_docs: https://decoderesearch.github.io/SAELens/
url_repo: https://github.com/jbloomAus/SAELens
---

# SAELens

## Pourquoi

Écosystème spécialisé dans les [[Sparse autoencoders|sparse autoencoders]] appliqués aux modèles de langage — l'outil de référence du domaine, maintenu par Joseph Bloom, Curt Tigges, Anthony Duong et David Chanin.

Il couvre les trois temps du sujet : **entraîner** un SAE (les variantes TopK, JumpReLU, BatchTopK incluses), **charger** un SAE pré-entraîné depuis un catalogue déjà constitué, et **analyser** les features obtenues (visualisations via SAE-Vis, intégration Neuronpedia).

C'est le catalogue qui fait sa valeur pratique : entraîner un SAE coûte des millions d'activations et un entraînement complet. Pouvoir en charger un déjà entraîné sur un modèle connu change la nature du travail — on passe de semaines à quelques lignes.

Historiquement, cette fonction vivait dans [[Dev/Services/TransformerLens|TransformerLens]] ; elle en a été **extraite à la v2** et vit ici désormais.

## Quand l'utiliser

- **Entraîner un SAE** sur les activations d'un modèle de langage, sans réimplémenter la boucle, les variantes de parcimonie et les métriques.
- **Réutiliser un SAE existant** : le catalogue couvre les modèles usuels du domaine (GPT-2, Gemma, Llama…). Le réflexe à avoir avant d'en entraîner un.
- **Analyser les features** : quelles entrées activent une direction, à quoi elle correspond, quel est son effet — avec les visualisations qui vont avec.
- Recherche en [[Interprétabilité mécaniste|interprétabilité mécaniste]] sur les LLM, en complément de TransformerLens pour les circuits.

## Quand NE PAS l'utiliser

- **Analyse de circuits sans SAE** : ce n'est pas son objet. [[Dev/Services/TransformerLens|TransformerLens]].
- **Modèles autres que des LLM** : le domaine et l'outillage sont centrés sur le texte.
- **Attribution ou explication à un métier** : hors sujet. [[Dev/Services/Captum|Captum]], [[Dev/Services/SHAP|SHAP]] ou [[Dev/Services/interpreto|interpreto]].
- **Besoin d'un pipeline concept complet, méthodes de dictionnaire comparées** (NMF, ICA, probes) : c'est le terrain d'[[Dev/Services/interpreto|interpreto]], qui traite les SAE comme une option parmi d'autres. SAELens, lui, ne fait que des SAE — mais les fait à fond.
- **Production** : outil de recherche, coûteux.

## Déploiement & coût

- `pip install sae-lens` — bibliothèque Python. Gratuit (MIT). Dépendances : `torch`, `transformer_lens`, `transformers`.
- **Charger** un SAE pré-entraîné : quasi gratuit, quelques centaines de Mo à télécharger.
- **Entraîner** un SAE : c'est là qu'est le coût réel. Collecter des millions d'activations (stockage et calcul), puis un entraînement complet. Compter des heures de GPU pour un modèle moyen, et un dictionnaire 16× à 64× plus large que la dimension du modèle.
- Exécution **single-node**. GPU nécessaire en pratique pour l'entraînement.

## Pièges

- **Toujours chercher un SAE existant avant d'en entraîner un.** Le catalogue couvre les modèles courants, et l'entraînement est cher.
- **Un SAE par couche et par point d'accroche.** Les features de la couche 5 n'ont rien à voir avec celles de la couche 20 ; charger le mauvais SAE donne des résultats silencieusement absurdes.
- **v6 = refonte majeure** (253 releases). Les tutoriels antérieurs ne s'appliquent pas tels quels. Épingler la version.
- **Le doute méthodologique n'est pas dans l'outil, il est dans la méthode** : rien ne garantit que les features trouvées soient celles du modèle plutôt qu'un artefact du SAE — des SAE entraînés sur du bruit produisent des features d'apparence tout aussi interprétable. Prudence sur les conclusions ([[Sparse autoencoders]]).
- **Surveiller les *dead features*** (unités jamais actives) : le symptôme d'entraînement le plus courant.
- Le curseur reconstruction/parcimonie n'a **pas d'optimum objectif**. C'est un arbitrage, pas un réglage à optimiser.

## Alternatives

- [[Dev/Services/TransformerLens|TransformerLens]] — Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.
- [[Dev/Services/interpreto|interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

## Liens

- [[Sparse autoencoders]] — le concept parent : sur-complétude, parcimonie, variantes TopK/JumpReLU, et comment évaluer.
- [[Superposition]] — le phénomène qui justifie l'existence des SAE.
- [[Interprétabilité mécaniste]] — le chapeau du domaine.
- [[Autoencodeurs]] — l'architecture d'origine, à contrainte inversée.
- [[Dev/Services/TransformerLens|TransformerLens]] — l'intégration étroite (`HookedSAETransformer`), d'où la fonction a migré.
- [[Dev/Services/PyTorch|PyTorch]] — le socle requis.
