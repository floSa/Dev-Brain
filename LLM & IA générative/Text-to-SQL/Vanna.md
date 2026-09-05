---
role: brique
nom: Vanna
alias: [vanna, vanna.ai, vanna-ai]
pitch: "Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable."
categorie: llm/text-to-sql
famille: paquet
licence_type: open-source
maturite: deprecated
langage: Python
alternatives: ["[[WrenAI]]", "[[DB-GPT]]"]
complements: []
tags: [text-to-sql, llm, rag, agents, local-llm]
url_docs: https://vanna.ai/docs/
url_repo: https://github.com/vanna-ai/vanna
---

# Vanna

<!-- AUTO:BANDEAU:START -->
> Framework Python text-to-SQL par RAG (MIT) : s'entraîne sur le DDL, la doc et des paires question/SQL, marche avec n'importe quelle base et n'importe quel LLM (dont Ollama en local), UI web fournie ; OSS archivé en mars 2026 (pivot vers Vanna Cloud hébergé), code toujours forkable.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | deprecated |
<!-- AUTO:BANDEAU:END -->

## Définition

Vanna génère du SQL à partir de questions en langage naturel par **RAG**. On l'« entraîne »
sur trois matières : le **DDL** — les `CREATE TABLE` qui décrivent le schéma —, de la
documentation métier, et des paires question→SQL validées. À l'exécution, il récupère schéma
et exemples pertinents, les injecte dans le prompt, puis demande au LLM de produire la
requête. Il est agnostique de la base (Postgres, MySQL, Snowflake, DuckDB) comme du LLM
(OpenAI, Anthropic, Gemini, Bedrock, Mistral, et **Ollama en local**, ce qui permet de se
passer de tout appel cloud). Longtemps la référence open-source du domaine, environ 23 k
étoiles ; la 2.0, fin 2025, a réécrit l'API autour d'un agent « user-aware » avec permissions,
streaming et UI web `<vanna-chat>` intégrée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Embarquer une brique text-to-SQL dans une app Python custom, sans plateforme lourde | Dépôt OSS archivé le 29 mars 2026 : lecture seule, plus aucun correctif upstream — le code MIT reste forkable, mais forker c'est hériter de la maintenance |
| Cible on-prem avec LLM local : le backend Ollama évite tout appel cloud | La qualité dépend directement de l'entraînement — DDL complet et bons exemples question/SQL ; un schéma mal décrit donne du SQL faux |
| Prototyper vite : quelques appels `train()` sur le DDL et des exemples suffisent à démarrer | Aucune couche sémantique métier : Vanna voit le schéma physique, pas les définitions de métriques |
| | Le magasin de vecteurs devient une dépendance à opérer : persistance, sauvegarde |

## Mise en œuvre

- Installation — bibliothèque Python importée dans l'app
- Point d'entrée — quelques appels `train()` sur le DDL, la doc métier et des paires question→SQL ; UI web `<vanna-chat>` fournie depuis la 2.0
- Prérequis — un magasin de vecteurs pour les données d'entraînement ([[Chroma]], [[Qdrant]], [[pgvector]]) et un LLM au choix ; un 7B quantifié via [[Ollama]] suffit à tester en local
- Exécution — mono-nœud, self-hébergé
- Coût — gratuit sous MIT ; Vanna Cloud, la version hébergée payante, est désormais la seule voie officiellement maintenue par l'éditeur — donc hors périmètre on-prem

## Écosystème

### Alternatives

- [[WrenAI]] — Plateforme GenBI open-source (Apache-2.0) : text-to-SQL gouverné via une couche sémantique MDL qui encode le modèle métier (entités, relations, métriques, contrôle d'accès), produit tableaux de bord et graphiques, self-host Docker ou offre hébergée, 20+ sources.
- [[DB-GPT]] — Framework open-source (MIT) d'agents data IA-natifs : text-to-SQL multi-agent avec langage de workflow AWEL, RAG et fine-tuning Text2SQL intégrés ; très complet mais courbe d'apprentissage raide, self-host Python.

## Ressources

- Documentation — https://vanna.ai/docs/
- Dépôt — https://github.com/vanna-ai/vanna

## Voir aussi

- [[Text-to-SQL]] — la notion du dossier
- [[RAG]] — le mécanisme par lequel il récupère schéma et exemples
- [[Comparatif - Frameworks text-to-SQL]] — ce qui départage les frameworks du dossier
