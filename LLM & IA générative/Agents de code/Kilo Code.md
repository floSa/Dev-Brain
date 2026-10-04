---
role: brique
nom: Kilo Code
alias: [kilo, kilocode, Kilo-Org/kilocode]
pitch: "Agent de code open source (MIT, TypeScript) pour VS Code, JetBrains et le terminal, bâti sur le code d'OpenCode : agents Code, Plan, Ask et Debug, plus de 30 fournisseurs par clé propre et les serveurs locaux Ollama et LM Studio."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[Cline]]", "[[OpenCode]]", "[[Zoo Code]]"]
complements: []
tags: [code-assistant, code-generation, llm, agents, mcp, local-llm]
url_docs: https://kilo.ai/docs
url_repo: https://github.com/Kilo-Org/kilocode
---

# Kilo Code

<!-- AUTO:BANDEAU:START -->
> Agent de code open source (MIT, TypeScript) pour VS Code, JetBrains et le terminal, bâti sur le code d'OpenCode : agents Code, Plan, Ask et Debug, plus de 30 fournisseurs par clé propre et les serveurs locaux Ollama et LM Studio.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension TypeScript | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de code décliné en extension VS Code, plugin JetBrains et CLI (`kilo`), avec en plus un agent dans le nuage et des revues de code automatiques de pull requests, hébergés par l'éditeur. Il fournit des agents spécialisés : Code, Plan, Ask, Debug, et des agents sur mesure. Le dépôt est sous licence MIT (fichiers LICENSE de la racine et des sous-paquets) ; ses fichiers LICENSE reprennent le copyright du projet OpenCode, dont le code sert de socle (dossier `packages/opencode`, version amont épinglée `v1.18.26`). La documentation distingue le fournisseur intégré de Kilo, qui ne demande aucune configuration, des clés propres : plus de 30 fournisseurs, dont les serveurs locaux Ollama, LM Studio et tout endpoint compatible OpenAI. Le cœur du produit n'est donc pas payant : le fournisseur intégré est une commodité, pas un passage obligé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le même agent dans VS Code, JetBrains et le terminal | Aucun compte chez l'éditeur toléré : le démarrage sans clé passe par le fournisseur intégré et un compte chez Kilo, d'après le README ; la clé propre ou le modèle local l'évitent |
| Un modèle servi sur place (Ollama, LM Studio) : la politique de confidentialité dit qu'on peut exécuter des modèles en local pour qu'aucune donnée ne parte chez un tiers | Un projet stable à l'échelle d'un trimestre : les versions se suivent vite (v7.8.3 le 2026-10-01, des préversions chaque semaine) |
| Le socle d'[[OpenCode]] avec des extensions d'éditeur par-dessus | Une extension seule pour VS Code, plus simple : [[Cline]] ou [[Zoo Code]] |

## Mise en œuvre

- Installation — extension VS Code (Marketplace), plugin JetBrains, ou CLI : `npm install -g @kilocode/cli`, Homebrew, ou binaire des releases GitHub
- Point d'entrée — le panneau de l'éditeur ou la commande `kilo` dans le dossier du projet
- Prérequis — un modèle : fournisseur intégré (compte chez Kilo), clé d'un des fournisseurs pris en charge, ou serveur local
- Exécution — sur le poste ; v7.8.3 du 2026-10-01
- Coût — logiciel gratuit (MIT) ; la dépense est celle du modèle. Le README affirme que le fournisseur intégré facture au tarif du fournisseur de modèles sans marge : affirmation de l'éditeur, non vérifiée ici. Tarifs de l'agent dans le nuage et des revues de code : non vérifiés

## Écosystème

### Alternatives

- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[OpenCode]] — Agent de code open source (MIT, TypeScript) pour le terminal, avec une application desktop en bêta : plus de 75 fournisseurs de modèles et les serveurs locaux Ollama, llama.cpp, LM Studio et vLLM par endpoint compatible OpenAI.
- [[Zoo Code]] — Extension VS Code open source (Apache-2.0, TypeScript), suite communautaire de Roo Code : modes Code, Architect, Ask, Debug et personnalisés, serveurs MCP, et le fournisseur de modèles de son choix dont Ollama et LM Studio.

## Ressources

- Documentation — https://kilo.ai/docs
- Dépôt — https://github.com/Kilo-Org/kilocode

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
