---
role: brique
nom: Zoo Code
alias: [zoo-code, Zoo-Code-Org/Zoo-Code]
pitch: "Extension VS Code open source (Apache-2.0, TypeScript), suite communautaire de Roo Code : modes Code, Architect, Ask, Debug et personnalisés, serveurs MCP, et le fournisseur de modèles de son choix dont Ollama et LM Studio."
categorie: llm/agent-de-code
famille: extension
domaines: [ai-eng]
licence_type: open-source
os: "Windows, macOS, Linux"
langage: TypeScript
alternatives: ["[[Cline]]", "[[Continue]]", "[[Kilo Code]]"]
complements: []
tags: [code-assistant, code-generation, llm, agents, mcp, local-llm]
url_docs: https://docs.zoocode.dev
url_repo: https://github.com/Zoo-Code-Org/Zoo-Code
---

# Zoo Code

<!-- AUTO:BANDEAU:START -->
> Extension VS Code open source (Apache-2.0, TypeScript), suite communautaire de Roo Code : modes Code, Architect, Ask, Debug et personnalisés, serveurs MCP, et le fournisseur de modèles de son choix dont Ollama et LM Studio.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension TypeScript | open-source | dans le moteur hôte, rien à héberger | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de code qui s'installe comme extension de VS Code. Il reprend le projet Roo Code : d'après son README, l'équipe de Roo a cessé de travailler sur Roo Code pour se concentrer sur un autre produit, et d'anciens contributeurs poursuivent le développement sous le nom Zoo Code (dépôt créé le 2026-04-23). On y travaille par **modes** : Code pour les éditions courantes, Architect pour planifier, Ask pour les questions, Debug pour tracer un défaut, plus des modes personnalisés par équipe. Le README annonce depuis la scission une recherche sémantique de code à la demande (Semble), une orchestration de sous-tâches renforcée, un garde-fou qui bloque les commandes dangereuses (Destructive Command Guard) et de nouveaux fournisseurs. Il ne fournit aucun modèle : il faut un fournisseur, et le code source déclare Ollama et LM Studio comme fournisseurs locaux.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent dans VS Code avec des modes distincts (planifier, coder, déboguer) et des modes sur mesure | Un autre éditeur que VS Code : Zoo Code est une extension de VS Code, JetBrains n'est pas cité par le README |
| Reprendre un usage de Roo Code, dont une page de migration documente le passage | Une équipe stable derrière le projet est exigée : le projet est né en 2026-04 d'un arrêt de Roo Code, avec une équipe de volontaires |
| Un modèle servi sur place (Ollama, LM Studio) ou le fournisseur de son choix | Le mode proxy de Zoo Code Cloud, proposé comme fournisseur, fait transiter le code par les serveurs de l'éditeur, qui dit le supprimer après relais (politique de confidentialité) ; une clé propre l'évite |

## Mise en œuvre

- Installation — extension VS Code (Marketplace, éditeur `ZooCodeOrganization`)
- Point d'entrée — panneau latéral de l'éditeur, avec le sélecteur de mode ; fournisseur et modèle déclarés dans les réglages
- Prérequis — VS Code et un accès à un modèle : API d'un fournisseur ou serveur local
- Exécution — sur le poste, dans le processus de l'éditeur ; v3.86.0 du 2026-10-03
- Coût — gratuit (Apache-2.0) ; la dépense est celle du modèle, et la documentation prévient que l'outil coûte plus cher à l'usage que ses alternatives, parce qu'il appelle des modèles de pointe avec accès aux fichiers et au terminal

## Écosystème

### Alternatives

- [[Cline]] — Agent de code autonome pour VS Code : modes Plan/Act avec validation pas-à-pas et support MCP de première classe.
- [[Continue]] — Assistant IA open-source pour VS Code et JetBrains : chat, autocomplétion, édition et agent, avec le modèle de ton choix (local ou API).
- [[Kilo Code]] — Agent de code open source (MIT, TypeScript) pour VS Code, JetBrains et le terminal, bâti sur le code d'OpenCode : agents Code, Plan, Ask et Debug, plus de 30 fournisseurs par clé propre et les serveurs locaux Ollama et LM Studio.

## Ressources

- Documentation — https://docs.zoocode.dev
- Dépôt — https://github.com/Zoo-Code-Org/Zoo-Code

## Voir aussi

- [[Agents de code]] — le hub du dossier
- [[Comparatif - Assistants de code IA]] — ce qui départage les briques du dossier
- [[Harnais d'agent]] — la couche qui entoure le modèle et exécute la boucle
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
