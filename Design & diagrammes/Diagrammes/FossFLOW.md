---
role: brique
nom: FossFLOW
alias: [fossflow, isoflow]
pitch: "Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON."
categorie: design/diagramme
famille: application
domaines: []
licence_type: open-source
os: "Web (PWA)"
langage: TypeScript
alternatives: ["[[draw.io]]", "[[Archify]]"]
complements: []
tags: [diagram, isometric]
url_docs: https://github.com/stan-smith/FossFLOW
url_repo: https://github.com/stan-smith/FossFLOW
---

# FossFLOW

<!-- AUTO:BANDEAU:START -->
> Application web open-source (Unlicense, bâtie sur Isoflow) pour des diagrammes d'infrastructure isométriques 3D : PWA locale dans le navigateur, icônes AWS/Azure/GCP/K8s, export JSON.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript | open-source | Web (PWA) | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web pour diagrammes **isométriques 3D** d'infrastructure — le rendu en
perspective des schémas d'architecture cloud. C'est une Progressive Web App bâtie en React
sur la bibliothèque Isoflow, qui tourne **entièrement dans le navigateur**, hors ligne
comprise, avec auto-save. Le système d'icônes est extensible et embarque les jeux standard
AWS, Azure, GCP et Kubernetes. Rien ne part vers un serveur : les données vivent dans le
stockage du navigateur, et la seule façon de les emporter est l'export JSON.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Présenter une infrastructure ou une topologie système avec un rendu isométrique soigné | Périmètre **spécialisé** : hors de l'isométrique d'infra, un généraliste est plus adapté |
| Contexte où la donnée doit rester locale : rien n'est envoyé à un serveur | Stockage navigateur : exporter le JSON, ou perdre son travail en changeant de poste |
| Réutiliser les jeux d'icônes cloud standard pour un schéma présentable rapidement | Écosystème plus jeune et plus petit que celui de draw.io : moins de formes, moins d'intégrations |

## Mise en œuvre

- Installation — rien : PWA installable depuis le navigateur ; auto-hébergement possible en conteneur
- Point d'entrée — application web, édition graphique ; export et import de sauvegardes JSON
- Prérequis — un navigateur récent ; dépôt canonique `stan-smith/FossFLOW`, plusieurs forks circulent
- Exécution — entièrement dans le navigateur, hors ligne comprise ; aucun serveur
- Coût — gratuit ; **Unlicense** (domaine public) pour FossFLOW, MIT pour la bibliothèque Isoflow sous-jacente

## Écosystème

### Alternatives

- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

## Ressources

- Dépôt — https://github.com/stan-smith/FossFLOW

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — ce qui départage les outils du dossier
