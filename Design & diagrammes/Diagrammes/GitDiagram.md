---
role: brique
nom: GitDiagram
alias: [gitdiagram]
pitch: "Service web open-source (MIT, TypeScript) qui génère par LLM un diagramme d'architecture interactif d'un dépôt GitHub depuis son URL : composants liés au code, export PNG/Mermaid, serveur MCP pour les agents."
categorie: design/diagramme
famille: application
domaines: [ai-eng]
licence_type: open-source
os: "Web"
langage: TypeScript
hosted: [self, managed]
alternatives: ["[[Archify]]"]
complements: []
tags: [diagram, mcp, llm]
url_docs: https://github.com/ahmedkhaleel2004/gitdiagram/tree/main/docs
url_repo: https://github.com/ahmedkhaleel2004/gitdiagram
---

# GitDiagram

<!-- AUTO:BANDEAU:START -->
> Service web open-source (MIT, TypeScript) qui génère par LLM un diagramme d'architecture interactif d'un dépôt GitHub depuis son URL : composants liés au code, export PNG/Mermaid, serveur MCP pour les agents.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé | — | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

GitDiagram lit un dépôt GitHub — arborescence, README, extraits de code — et en tire un
**diagramme d'architecture interactif** produit par un LLM : groupes, composants et flèches,
chaque composant renvoyant à son fichier ou à son dossier sur GitHub. Le modèle rend un graphe
strict, que le serveur valide contre le dépôt réel puis compile de façon déterministe en
Mermaid ; le rendu se fait dans le navigateur. Le point d'entrée est l'URL : remplacer `hub`
par `diagram` dans celle du dépôt. Le même service expose un serveur MCP et une version
Markdown de chaque diagramme, lisibles par un agent, et génère des vidéos explicatives d'une
minute. Le projet se dit inspiré de Gitingest.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comprendre vite un dépôt inconnu, sans installer ni configurer : une URL suffit | Code confidentiel : la génération envoie des extraits du dépôt, jusqu'à 40 fichiers, à un fournisseur LLM (OpenAI ou OpenRouter) |
| Livrer à un humain un schéma cliquable, dont chaque composant renvoie au fichier ou au dossier GitHub | Contexte on-prem sans accès sortant : l'auto-hébergement exige Cloudflare R2, Upstash Redis et une clé OpenAI ou OpenRouter, et aucun modèle local n'est documenté |
| Récupérer la source Mermaid ou un export PNG pour un README, ou laisser un agent lire le diagramme par MCP | Schéma qui doit faire foi : c'est une lecture par un modèle, et le banc d'essai du projet mesure encore 17 % de flèches pleines non étayées par le code (5 dépôts, 3 essais chacun) |

## Mise en œuvre

- Installation — aucune sur l'instance publique (gitdiagram.com) ; en auto-hébergement, `git clone`, `bun install`, `cp .env.example .env`, puis `bun run dev` ; un `Dockerfile` est fourni
- Point d'entrée — l'URL du dépôt GitHub avec `hub` remplacé par `diagram` ; serveur MCP public sans clé à `https://gitdiagram.com/mcp` (`claude mcp add --transport http gitdiagram https://gitdiagram.com/mcp`) ; version Markdown à `gitdiagram.com/<owner>/<repo>.md`
- Prérequis — auto-hébergement : Bun, Cloudflare R2, Upstash Redis et une clé OpenAI ou OpenRouter ; dépôt privé : un jeton GitHub ; vidéos explicatives éteintes par défaut, leur création est en accès anticipé sur l'instance publique
- Exécution — sur l'instance de l'éditeur (Vercel, seul runtime en ligne), ou application Next.js auto-hébergée
- Coût — gratuit, MIT ; en auto-hébergement, la clé LLM se paie à chaque génération, R2 et Upstash en plus

## Écosystème

### Alternatives

- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM. — même besoin, autre chaîne : Archify suppose un agent et rend le même schéma à chaque fois, GitDiagram part d'une URL et régénère à chaque visite.

## Ressources

- Documentation — https://github.com/ahmedkhaleel2004/gitdiagram/tree/main/docs
- Dépôt — https://github.com/ahmedkhaleel2004/gitdiagram

## Voir aussi

- [[Graphify]] — l'autre moitié du sujet, côté agent : indexe un dépôt en graphe interrogeable au lieu de le dessiner
- [[Mermaid]] — le format de sortie : GitDiagram compile son graphe en Mermaid et en expose la source
- [[mcp-protocol]] — le protocole du serveur MCP exposé
- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
