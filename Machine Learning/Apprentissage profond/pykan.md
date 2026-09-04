---
role: brique
nom: pykan
alias: [KAN python, kindxiaoming pykan]
pitch: "Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: []
complements: ["[[PyTorch]]"]
tags: [deep-learning]
url_docs: https://kindxiaoming.github.io/pykan/
url_repo: https://github.com/KindXiaoming/pykan
---

# pykan

<!-- AUTO:BANDEAU:START -->
> Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental |
<!-- AUTO:BANDEAU:END -->

## Définition

L'implémentation de référence des [[Kolmogorov-Arnold Networks]], écrite par les auteurs du papier sur [[PyTorch]]. Au lieu des poids linéaires et des activations fixes d'un MLP, un KAN place des **fonctions univariées apprenables** — des B-splines — sur les arêtes. pykan expose toute la mécanique de l'article : raffinement de grille (*grid extension*), régularisation et élagage, fixation de symboles, puis **extraction d'une formule symbolique** lisible. C'est ce dernier point qui en fait un outil de ML scientifique — régression de fonctions, EDP — plutôt qu'une brique de calcul. Le coût de la construction est assumé par l'auteur : l'évaluation de splines rend le **coût par paramètre** plus élevé qu'un MLP, l'entraînement est nettement plus lent, et les gains de paramètres ne se voient guère hors des cibles structurées. L'amont renvoie lui-même vers des réimplémentations plus rapides (efficient-kan, FastKAN, non référencées ici) pour qui cherche le débit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Explorer l'architecture KAN sur des problèmes structurés : régression de fonctions, physique et EDP, découverte de formules | Tâches de perception à grande échelle (vision, langage) : MLP et transformeurs restent devant, plus rapides et mieux outillés → [[Transformer architectures]] |
| Tirer parti de l'interprétabilité : visualiser ce que chaque arête calcule, simplifier vers une expression analytique | Besoin de débit ou de production : l'amont privilégie la clarté scientifique à l'efficacité, et renvoie vers efficient-kan ou FastKAN |
| Reproduire ou prolonger les expériences du papier KAN / KAN 2.0 | Pipeline ML standard sur données tabulaires → [[Scikit-Learn]] ou du gradient boosting, matures et éprouvés |

## Mise en œuvre

- Installation — `uv add pykan`
- Point d'entrée — import Python, au-dessus de [[PyTorch]]
- Prérequis — PyTorch ; version v0.2.x (KAN 2.0), API encore mouvante d'une version à l'autre, à épingler
- Exécution — single-node, CPU ou GPU via PyTorch
- Coût — gratuit, MIT ; le coût réel est le temps d'entraînement, plus élevé qu'un MLP à paramètres égaux

## Écosystème

### Alternatives

- Pas de substitut direct référencé dans le brain : les réimplémentations communautaires (efficient-kan, FastKAN) remplacent les B-splines par des bases moins coûteuses sans changer l'idée, et pour les tâches usuelles le MLP ou le transformeur restent les défauts.

### Compléments

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche. — le socle sur lequel pykan est bâti.

## Ressources

- Documentation — https://kindxiaoming.github.io/pykan/
- Dépôt — https://github.com/KindXiaoming/pykan

## Voir aussi

- [[Kolmogorov-Arnold Networks]] — le concept dont pykan est l'implémentation de référence
- [[Apprentissage profond]] — le hub du domaine
