---
role: brique
nom: Kroki
alias: [kroki, yuzutech/kroki, kroki.io]
pitch: "Serveur HTTP (MIT, Java) à héberger qui donne une seule API pour rendre une vingtaine de langages de diagrammes — PlantUML, Mermaid, D2, GraphViz, BPMN, Excalidraw, DBML, Vega — en SVG ou PNG, par une URL ou une requête POST — mais les langages tournent dans des conteneurs compagnons, et l'instance publique kroki.io reçoit vos sources si on la préfère à la sienne."
categorie: design/diagramme
famille: plateforme
domaines: [ai-eng]
licence_type: open-source
hosted: [self]
os: "Linux (conteneurs)"
langage: Java
maturite: production
scaling: single-node
alternatives: []
complements: ["[[PlantUML]]", "[[D2]]"]
tags: [diagram, diagram-as-code, self-hosted]
url_docs: https://docs.kroki.io/
url_repo: https://github.com/yuzutech/kroki
---

# Kroki

<!-- AUTO:BANDEAU:START -->
> Serveur HTTP (MIT, Java) à héberger qui donne une seule API pour rendre une vingtaine de langages de diagrammes — PlantUML, Mermaid, D2, GraphViz, BPMN, Excalidraw, DBML, Vega — en SVG ou PNG, par une URL ou une requête POST — mais les langages tournent dans des conteneurs compagnons, et l'instance publique kroki.io reçoit vos sources si on la préfère à la sienne.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur web qui **rend des diagrammes écrits en texte**, quel que soit le langage : une seule API pour BlockDiag et ses variantes, BPMN, Bytefield, C4 (avec PlantUML), D2, DBML, Ditaa, Erd, Excalidraw, GoAT, GraphViz, Mermaid, Nomnoml, Pikchr, PlantUML, SvgBob, Symbolator, UMLet, Vega, Vega-Lite, WaveDrom et WireViz (liste du README). On envoie la source en `POST` (JSON ou texte brut, format de sortie dans l'en-tête `Accept` ou dans l'URL) ou par `GET` avec la source compressée (deflate puis base64) dans l'adresse.

**Pourquoi il compte.** Un générateur de documentation, un wiki ou une CI n'ont pas à installer Java, Node et Graphviz : ils appellent Kroki, qui s'en charge. Le serveur central est en Java (Vert.x) ; les langages bâtis sur Node.js (Mermaid, BPMN, Excalidraw…) tournent dans des **conteneurs compagnons** facultatifs (`yuzutech/kroki-mermaid`, `kroki-bpmn`…). Seul le conteneur `yuzutech/kroki` est obligatoire ; il suffit à rendre PlantUML, GraphViz et plusieurs autres. Version 0.33.0 du 2026-10-05, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07 ; le numéro de version est toujours inférieur à 1.

**Service tiers.** Le site kroki.io et d'autres instances hébergées (Wovalab, ou des plateformes de déploiement citées par le README) existent ; le README dit que ces offres tierces ne sont pas exploitées par l'équipe Kroki. Pour un schéma interne, héberger sa propre instance évite d'envoyer les sources à un tiers.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Rendre des diagrammes en texte dans un wiki, un site de documentation ou une CI sans installer chaque moteur | Un seul langage à rendre sur un poste : la commande de l'outil suffit ([[D2]], [[PlantUML]]) |
| Un langage de plus à ajouter plus tard sans toucher aux clients : la même API | Rien à héberger : un serveur de plus à tenir, avec ses conteneurs compagnons |
| Un point de rendu partagé pour plusieurs outils internes | Des diagrammes confidentiels envoyés à l'instance publique : à éviter, héberger la sienne |
| Garder le rendu hors des postes : plus d'installation de Java, Node ou Graphviz côté client | Une édition graphique : Kroki rend, il ne dessine pas |

## Mise en œuvre

- Installation — `docker run -d -p 8000:8000 yuzutech/kroki` ; Podman, Kubernetes et une installation manuelle sont décrits dans la documentation
- Point d'entrée — `POST /plantuml/svg` avec la source dans le corps de la requête
- Prérequis — Docker ou Podman ; des conteneurs compagnons selon les langages voulus, reliés par des variables `KROKI_*_HOST`
- Exécution — auto-hébergé, mono-nœud
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- Aucune alternative déclarée : un rendu par serveur n'a pas de pair dans le brain. Le rendu local d'un seul langage se fait avec [[D2]], [[PlantUML]] ou [[Mermaid]].
- voisin : [[Mermaid]] — l'un des langages rendus, par un conteneur compagnon.

### Compléments

- [[PlantUML]] — Outil Java (licences au choix : GPL, LGPL, Apache, EPL ou MIT) qui dessine des diagrammes UML et plus de vingt types — séquence, classes, activité, états, Gantt, carte mentale, JSON, YAML — à partir d'une description textuelle, en ligne de commande, en bibliothèque ou compilé pour le navigateur — mais GitHub ne les rend pas nativement, il faut une extension de navigateur ou un rendu en amont. — rendu par le conteneur principal de Kroki.
- [[D2]] — Outil en ligne de commande (MPL-2.0, Go) qui transforme un langage de description de diagrammes en SVG, PNG, PDF, GIF ou PPTX, avec thèmes, plusieurs moteurs de placement, rendu au trait de crayon et animations — mais le langage lui est propre, aucune forge ne le rend nativement, et le moteur TALA est un module à part. — l'un des langages que Kroki rend.

## Ressources

- Documentation — https://docs.kroki.io/
- Dépôt — https://github.com/yuzutech/kroki

## Voir aussi

- [[Diagrammes]] — le hub du dossier
- [[Comparatif - Diagrammes]] — où ces outils se départagent
- [[Modèle C4]] — le modèle C4 se rend par PlantUML, d'après le README
- [[Design & diagrammes]] — le hub du domaine
