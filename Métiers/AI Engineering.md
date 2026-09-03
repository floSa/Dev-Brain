---
role: hub
nom: AI Engineering
pitch: Construire une application autour d'un modèle de langage — contexte, outils, garde-fous, évaluation.
---

# AI Engineering

> Construire une application autour d'un modèle de langage — contexte, outils, garde-fous, évaluation.

## Ce qu'il faut comprendre

- Le modèle n'est plus ce qu'on fabrique mais ce qu'on **appelle**. Le travail se déplace vers ce qui l'entoure : quel contexte lui donner, quels outils lui laisser, comment vérifier sa sortie, combien elle coûte.
- Son centre est [[LLM & IA générative]], mais l'axe ne tient pas dans ce seul dossier : [[Vectoriel]] pour la récupération, [[Interfaces & apps data]] pour l'exposer, [[Sécurité]] pour ce qu'on refuse de lui laisser faire, [[Observabilité]] pour ce qu'on trace.
- Rien ici ne remplace [[Data Science]] ni [[Machine Learning]] : un prompt ne résout pas un problème de mesure, et un RAG ne corrige pas une donnée fausse.

## Choisir

- Écrire l'application, câbler les outils → [[LLM & IA générative]], sous-dossier [[Agents]].
- Servir un modèle chez soi → [[Runtimes]].
- Retrouver le bon passage à injecter → [[Vectoriel]].
- Spécialiser un modèle sur un domaine → [[Fine-tuning]].
- Interroger une base en langue naturelle → [[Text-to-SQL]].

<!-- AUTO:START -->
Axe métier **AI Engineering** (`ai-eng`) — explorer par sous-domaine, puis descendre via le graphe local.

- [[LLM & IA générative]] — 70 page(s)
- [[Machine Learning]] — 42 page(s)
- [[Sécurité]] — 5 page(s)
- [[Mathématiques]] — 3 page(s)
- [[Bases de données]] — 2 page(s)
- [[Médias]] — 2 page(s)
- [[Outils de développement]] — 2 page(s)
- [[Design & diagrammes]] — 1 page(s)
- [[Documents]] — 1 page(s)
- [[Web & API]] — 1 page(s)
<!-- AUTO:END -->
