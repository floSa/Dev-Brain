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

## Pourquoi

Application web open-source pour créer des **diagrammes isométriques 3D** d'infrastructure — le rendu « en perspective » façon schéma d'architecture cloud. Progressive Web App (PWA) bâtie en React sur la bibliothèque **Isoflow**, qui tourne **entièrement dans le navigateur** avec support hors-ligne et auto-save. Système d'icônes extensible (AWS, Azure, GCP, Kubernetes…) ou icônes maison. Les données restent locales (stockage navigateur) ; export/import de sauvegardes JSON.

## Quand l'utiliser

- Présenter une **infrastructure** ou une topologie système avec un rendu isométrique soigné.
- Contexte où la donnée doit rester locale : rien n'est envoyé à un serveur.
- Réutiliser les jeux d'icônes cloud standard pour un schéma pro rapidement.

## Quand NE PAS l'utiliser

- Diagramme 2D classique (flowchart, UML, séquence) → [[draw.io]].
- Diagramme à versionner comme du code → [[Mermaid]].
- Croquis jetable de réunion → [[Excalidraw]].

## Bases & plateformes

- Licence **Unlicense** (domaine public) pour FossFLOW ; la lib sous-jacente **Isoflow** est MIT. Écrit en TypeScript/React.
- PWA : s'installe et tourne dans le navigateur, hors-ligne ; auto-hébergeable (conteneur).
- Repo canonique `stan-smith/FossFLOW` (plusieurs forks circulent).

## Pièges

- Périmètre **spécialisé** (isométrique d'infra) : hors de ce cas, un outil généraliste est plus adapté.
- Stockage navigateur : penser à exporter le JSON pour ne pas perdre son travail en changeant de poste.
- Écosystème plus jeune et plus petit que draw.io : moins de formes, moins d'intégrations.

## Alternatives

- [[draw.io]] — Éditeur de diagrammes GUI open-source (Apache-2.0, JavaScript) : flowcharts, UML, réseaux, org-charts, BPMN… ; app web ou desktop, stockage sur ton drive, export multi-format, embarquable.
- [[Archify]] — Skill d'agent IA (MIT, JavaScript) pour diagrammes d'architecture : l'agent produit une IR JSON typée, compilée de façon déterministe en HTML autonome validé, avec exports SVG/PNG/WebM.

## Liens

- [[Comparatif - Diagrammes]]
- Repo & doc : https://github.com/stan-smith/FossFLOW
