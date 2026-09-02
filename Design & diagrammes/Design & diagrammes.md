---
role: hub
nom: Design & diagrammes
alias: [design, diagramme, schema]
pitch: Dessiner — une interface qu'on prototype, ou un système qu'on explique.
domaines: [data-eng, ai-eng]
tags: [design-tool, diagram, whiteboard]
---

# Design & diagrammes

> Dessiner — une interface qu'on prototype, ou un système qu'on explique.

## Ce qu'il faut comprendre

- Deux activités sans rapport partagent ce domaine. **Prototyper une interface** ([[Figma]], [[Penpot]]) produit une maquette destinée à devenir du code. **Faire un schéma** (sous-dossier [[Diagrammes]]) produit une explication destinée à être lue. Les outils ne s'échangent pas.
- Pour un profil data, la seconde activité est celle qui compte : un diagramme d'architecture, un flux de données, un pipeline. C'est là que se joue la question du **diagramme-as-code** contre le **dessin à la main** — voir [[Diagrammes]].
- Un outil de prototypage vaut par son **écosystème** (bibliothèques de composants, plugins, poignées de dev) plus que par ses fonctions de dessin. C'est ce qui rend [[Figma]] difficile à quitter et ce que [[Penpot]] compense par les standards du web (SVG, CSS) et l'auto-hébergement.

## Choisir

- Un schéma à mettre dans un dépôt, une doc ou une PR → [[Diagrammes]], et probablement [[Mermaid]].
- Maquetter une interface, en équipe, avec des composants → [[Figma]].
- Le même besoin sans dépendance à un SaaS, ou avec une contrainte on-prem → [[Penpot]].

<!-- AUTO:START -->
### Sous-domaines
- [[Diagrammes]]

### Briques
- [[Figma]] — Plateforme de design d'interface et de prototypage collaboratif (propriétaire, freemium) : design temps réel multi-utilisateurs, prototypes interactifs, dev mode ; l'outil de référence du design produit.
- [[Penpot]] — Alternative open-source (MPL-2.0) et self-hostable à Figma : design d'interface et prototypage collaboratifs basés sur des standards web (SVG), déployable on-prem — pertinent quand la souveraineté des données compte.

### Comparatifs
- [[Comparatif - Design & prototypage]]
<!-- AUTO:END -->
