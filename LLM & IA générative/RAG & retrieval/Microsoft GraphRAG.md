---
role: brique
nom: Microsoft GraphRAG
alias: [graphrag (paquet), microsoft/graphrag, GraphRAG de Microsoft, Microsoft Research GraphRAG]
pitch: "Bibliothèque Python de recherche (Microsoft, MIT) qui extrait un graphe d'un corpus par LLM, le découpe en communautés avec un rapport par communauté, puis répond en recherche locale, globale ou DRIFT ; projet en mode maintenance (corrections et mises à jour de dépendances seulement), v3.3.0 en octobre 2026."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[LightRAG]]"]
tags: [rag, knowledge-graph, retrieval, llm]
url_docs: https://microsoft.github.io/graphrag/
url_repo: https://github.com/microsoft/graphrag
---

# Microsoft GraphRAG

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python de recherche (Microsoft, MIT) qui extrait un graphe d'un corpus par LLM, le découpe en communautés avec un rapport par communauté, puis répond en recherche locale, globale ou DRIFT ; projet en mode maintenance (corrections et mises à jour de dépendances seulement), v3.3.0 en octobre 2026.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque Python (`graphrag`) de la méthode décrite par Edge et al. (Microsoft Research, *From Local to Global*, arXiv 2404.16130) : un LLM extrait **entités et relations** de chaque morceau de texte (1 200 tokens par défaut dans la documentation), les fusionne en graphe, le partitionne en **communautés** par l'algorithme de Leiden hiérarchique, puis écrit un **rapport par communauté**. L'index sert quatre modes : la recherche **globale** (raisonner sur tout le corpus à partir des rapports), la recherche **locale** (partir d'une entité et de son voisinage), **DRIFT** (locale enrichie d'informations de communautés) et la recherche **de base** (un RAG vectoriel, gardé pour comparaison). L'extraction des affirmations (*claims*) est désactivée par défaut ; une variante *FastGraphRAG* remplace l'extraction par LLM par du traitement du langage. Licence MIT, version 3.3.0 sur PyPI (2026-10-08), dernier push 2026-10-19.

**Le README annonce un projet « largement en mode maintenance »** : ni nouvelles contributions ni nouvelles fonctions, des corrections de bogues et des mises à jour de dépendances, en particulier pour les CVE. Il dit aussi que le code est une démonstration, pas une offre officiellement supportée par Microsoft.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un corpus **stable** et des questions **globales** (« quels thèmes ressortent ? ») : c'est le cas que le papier évalue | Des **questions factuelles simples** : une étude tierce (Xiang et al., arXiv 2506.05690) rapporte qu'un RAG sur graphe sous-performe souvent un RAG vectoriel sur des tâches réelles ; la recherche de base est là pour le mesurer ([[GraphRAG]]) |
| Une **référence** reconnue pour comprendre la méthode, ses niveaux de communautés et ses modes de recherche | Un **corpus qui change** : l'indexation est lourde et le coût d'une mise à jour n'est pas mesuré dans les sources lues → [[LightRAG]] |
| Des rapports de communauté **lisibles** et un graphe en tables que d'autres outils lisent | Un projet **neuf** à maintenir plusieurs années : le dépôt est en maintenance, sans nouvelles fonctions |
| Une licence **MIT**, Python 3.11 à 3.13 | Un budget d'indexation **non borné** : le README avertit que l'indexation peut coûter cher et conseille de commencer petit |

## Mise en œuvre

- Installation — `uv add graphrag`
- Point d'entrée — l'interface en ligne de commande : `graphrag init --root <dossier>`, puis l'indexation et la requête ; guide de démarrage dans la documentation
- Prérequis — un LLM et un modèle d'embedding à configurer ; **affiner les prompts** à son domaine (guide *Prompt Tuning*, fortement conseillé par le README) ; relancer `graphrag init --root <dossier> --force` entre versions mineures (l'initialisation écrase la configuration et les prompts : les sauvegarder) et le notebook de migration fourni entre versions majeures
- Exécution — local, en bibliothèque ; les appels de modèle se font vers le LLM choisi
- Coût — gratuit sous MIT ; l'indexation consomme des tokens de LLM à chaque morceau, puis pour les rapports de communautés

## Limites à connaître

- **Projet en maintenance** : les évolutions viendront d'ailleurs ; épingler la version et suivre les avis de sécurité.
- **Indexation coûteuse** : le README le dit (« commencer petit »). Aucun coût en euros n'est publié par le projet : mesurer les tokens consommés sur un échantillon avant de passer à l'échelle.
- **Le papier ne mesure que la recherche globale** : la recherche locale, DRIFT et la recherche de base sont des modes de la bibliothèque, pas des résultats du papier. Les taux de victoire du papier viennent d'un LLM-juge, sans vérité terrain.
- **Aucun classement avec [[LightRAG]]** : pas de mesure indépendante sous un protocole commun ; les gains de chacun sont ceux de ses auteurs.

## Écosystème

### Alternatives

- [[LightRAG]] — Framework RAG sur graphe (HKUDS, MIT) — extraction d'entités et de relations par LLM, récupération à deux niveaux (détails et concepts) sur graphe et vecteurs, ajout et suppression incrémentaux de documents ; serveur avec interface web et API, v1.5.7 en septembre 2026. — sans communautés ni rapports, avec un ajout incrémental et un serveur prêt ; pas de recherche globale par rapports.

## Ressources

- Documentation — https://microsoft.github.io/graphrag/
- Dépôt — https://github.com/microsoft/graphrag
- Article — Edge et al., *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, arXiv 2404.16130 : https://arxiv.org/abs/2404.16130
- Vidéo — « RAG vs GRAPH RAG. Lequel choisir ? », Benoit Ferrere, 2 min 46 : https://www.youtube.com/watch?v=ZaOMbq3c0Jg (communautés à 1 min 21, recherche globale à 1 min 40)

## Voir aussi

- [[GraphRAG]] — la notion : RAG sur graphe, recherche locale et globale
- [[Construction de graphes de connaissances]] — l'extraction qui produit le graphe
- [[RAG & retrieval]] — le hub du dossier, avec la comparaison des deux frameworks de graphe
- [[Graphe de connaissances]] — ce qu'est le graphe qu'on construit
