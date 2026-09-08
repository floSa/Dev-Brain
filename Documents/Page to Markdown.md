---
role: brique
nom: Page to Markdown
alias: [page-to-markdown, page to markdown by starterbuild]
pitch: "Extension Chrome qui convertit une page web ou une sélection en Markdown propre, entièrement dans le navigateur, avec copie au presse-papiers ou téléchargement .md."
categorie: docs/capture
famille: extension
domaines: [ai-eng]
licence_type: proprietary
os: "Chrome (Windows, macOS, Linux, ChromeOS)"
langage: 
alternatives: []
complements: []
tags: [browser-extension, markdown-conversion, note-taking, privacy]
url_docs: https://starterbuild.com/page-to-markdown/
url_repo: 
---

# Page to Markdown

<!-- AUTO:BANDEAU:START -->
> Extension Chrome qui convertit une page web ou une sélection en Markdown propre, entièrement dans le navigateur, avec copie au presse-papiers ou téléchargement .md.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension | propriétaire | dans le moteur hôte, rien à héberger | — | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Le geste à l'unité : une page de documentation lue dans le navigateur, un thread, un
article — récupérés en Markdown structuré en deux clics, pour les coller dans un prompt,
une note ou une doc de projet. Le copier-coller brut perd la hiérarchie de titres, casse
les blocs de code et embarque la navigation du site ; c'est ce trou que l'extension
comble. L'éditeur (StarterBuild) annonce trois modes — page nettoyée, page complète,
sélection seule, cette dernière aussi par le menu contextuel — et la conversion préserve
titres, liens, images, listes, citations, tableaux, blocs de code délimités et blocs
dépliants (`details`). La conversion s'exécute **localement dans Chrome** : l'éditeur
déclare que le contenu de la page n'est envoyé ni à StarterBuild ni à un tiers, mais la
déclaration est invérifiable de l'extérieur, le code n'étant pas publié.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Nourrir un prompt ou un contexte LLM avec une page de doc, en gardant une structure exploitable | Extraction à l'échelle, planifiée ou automatisée sur des milliers d'URL → [[Firecrawl]], [[Maxun]] |
| Alimenter des notes ou un wiki personnel à partir de lectures ponctuelles | Conversion de PDF ou de documents bureautiques : c'est une extension de navigateur → [[OpenDataLoader PDF]], [[Docling]] |
| Récupérer un extrait de page — un tableau, un bloc de code — sans écrire un script | Exigence de code auditable ou d'auto-hébergement : l'extension est propriétaire et sans dépôt public, le « tout local » repose sur la parole de l'éditeur |
| Contexte où le contenu de la page ne doit pas transiter par un service distant, sous réserve de faire confiance à cette déclaration | Navigateur autre que Chrome : lui seul est annoncé, la compatibilité Edge, Brave ou Vivaldi n'est pas documentée, et il n'existe ni version Firefox ni version Safari |
| | En faire une dépendance de production : extension gratuite d'un petit éditeur, qui peut changer de modèle économique ou de mainteneur |
| | Page rendue entièrement côté client, ou mise en page atypique : la capture peut être incomplète avant la fin du chargement, et l'heuristique du mode « page nettoyée » retire parfois du contenu utile — comparer avec le mode page complète |

## Mise en œuvre

- Installation — Chrome Web Store, identifiant `abpdjempcbodkeajhfhblcajghbgbdae` ; présentation et lien sur `starterbuild.com/page-to-markdown/`
- Point d'entrée — extension de navigateur : icône de barre d'outils, ou menu contextuel pour une sélection ; sortie au presse-papiers ou en fichier `.md`
- Prérequis — Chrome, sur Windows, macOS, Linux ou ChromeOS ; aucun compte ni clé d'API annoncés. Vérifier les permissions demandées dans le Chrome Web Store avant d'installer, en particulier pour des pages internes ou sous authentification
- Exécution — entièrement dans le navigateur, sur le poste ; rien à héberger
- Coût — gratuite. Aucun code source publié, donc aucun build maison possible

## Écosystème

### Alternatives

- *Aucune alternative déclarée : seule page de la catégorie `docs/capture`. Le voisinage fonctionnel est ailleurs — le scraping programmatique en `data/scraping`, le parsing de documents en `data/parsing` —, pointé dans le tableau ci-dessus.*

## Ressources

- Documentation — https://starterbuild.com/page-to-markdown/

## Voir aussi

- [[Documents]] — le hub du domaine
- [[Comparatif - Scraping]] — ce qui départage les outils de scraping, l'équivalent programmatique et à l'échelle
- [[Comparatif - Parsing de documents]] — la même question pour des documents plutôt que des pages web
