---
galaxie: dev
type: service
nom: pykan
alias: [KAN python, kindxiaoming pykan]
pitch: "Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: experimental
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: en-eval
tags: [deep-learning]
url_docs: https://kindxiaoming.github.io/pykan/
url_repo: https://github.com/KindXiaoming/pykan
---

# pykan

## Pourquoi

Implémentation **officielle de référence** des [[Kolmogorov-Arnold Networks]] (KAN), par les auteurs du papier, bâtie sur [[Dev/Services/PyTorch|PyTorch]]. Au lieu des poids linéaires + activations fixes du MLP, un KAN place des **fonctions univariées apprenables** (B-splines) sur les arêtes. pykan expose toute la mécanique de l'article : raffinement de grille (grid extension), régularisation et **élagage**, fixation de symboles et **extraction d'une formule symbolique** lisible — d'où son usage en ML scientifique (régression de fonctions, EDP). C'est une base de recherche, pas un framework de production.

## Quand l'utiliser

- **Explorer** l'architecture KAN sur des problèmes structurés : régression de fonctions, physique / EDP, découverte de formules symboliques.
- Tirer parti de l'**interprétabilité** : visualiser ce que chaque arête calcule, simplifier vers une expression analytique.
- Reproduire ou prolonger les expériences du papier KAN / KAN 2.0.

## Quand NE PAS l'utiliser

- Tâches de **perception à grande échelle** (vision, langage) → MLP et transformeurs ([[Transformer architectures]]) restent devant, plus rapides et mieux outillés.
- Besoin de **débit / production** : l'auteur lui-même privilégie la clarté scientifique à l'efficacité et renvoie vers des variantes plus rapides (efficient-kan, FastKAN, non référencées ici).
- Pipeline ML standard tabulaire → [[Dev/Services/Scikit-Learn|Scikit-Learn]] / gradient boosting, matures et éprouvés.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add pykan`. Dépend de PyTorch.
- **Single-node** (CPU/GPU via PyTorch) ; l'évaluation de splines rend le **coût par paramètre** plus élevé qu'un MLP.
- Version v0.2.x (KAN 2.0), API encore mouvante — épingler la version.

## Pièges

- **Entraînement lent** vs MLP (splines à évaluer), écosystème immature, API instable d'une version à l'autre.
- Gains de paramètres réels surtout sur cibles **structurées / scientifiques** ; peu nets sur les grosses tâches de perception.
- Architecture **récente (2024)** et orientée recherche : à manier comme une piste, pas comme une brique de production.

## Alternatives

Pas de substitut direct référencé dans le brain. Pour la performance, des réimplémentations communautaires (efficient-kan, FastKAN) remplacent les B-splines par des bases moins coûteuses ; pour les tâches usuelles, le MLP ou le transformeur ([[Transformer architectures]]) restent les défauts.

## Liens

- [[Kolmogorov-Arnold Networks]] — le concept dont pykan est l'implémentation de référence.
- [[Dev/Services/PyTorch|PyTorch]] — le socle sur lequel pykan est bâti.
- [[Transformer architectures]] — la brique de deep learning concurrente sur les grosses tâches.
- Doc : https://kindxiaoming.github.io/pykan/ · Repo : https://github.com/KindXiaoming/pykan
