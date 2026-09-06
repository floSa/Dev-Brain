---
role: brique
nom: OpenCut
alias: [OpenCut-app/OpenCut, opencut]
pitch: "Éditeur de montage vidéo open-source (MIT), alternative déclarée à CapCut : cœur Rust, frontend TypeScript/Next.js, médias traités en local. Réécriture en cours — serveur MCP, mode headless et plugins sont annoncés, pas livrés."
categorie: media/video
famille: application
domaines: []
licence_type: open-source
os: "Navigateur (aujourd'hui) ; desktop et mobile annoncés, non livrés"
langage: TypeScript, Rust
alternatives: []
complements: []
tags: [video-editing, privacy]
url_docs: 
url_repo: https://github.com/OpenCut-app/OpenCut
---

# OpenCut

<!-- AUTO:BANDEAU:START -->
> Éditeur de montage vidéo open-source (MIT), alternative déclarée à CapCut : cœur Rust, frontend TypeScript/Next.js, médias traités en local. Réécriture en cours — serveur MCP, mode headless et plugins sont annoncés, pas livrés.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application TypeScript, Rust | open-source | Navigateur (aujourd'hui) ; desktop et mobile annoncés, non livrés | — |
<!-- AUTO:BANDEAU:END -->

## Définition

**Avertissement de rangement, à lire en premier** : ce brain documente des briques data, ML et
IA. Un éditeur de montage vidéo n'en relève pas. La page est classée en `media/video`, catégorie
retenue faute de mieux, et son champ `domaines:` est **volontairement vide** — aucune des six
valeurs du vocabulaire ne la couvre, ce qui a pour effet assumé de ne la faire apparaître dans
aucun hub de `Métiers/`. À lire comme une fiche périphérique, pas comme une brique
choisissable dans un plan projet.

Ce qui existe aujourd'hui : un éditeur de montage **dans le navigateur** où les médias ne
quittent pas la machine — timeline, prévisualisation, bac à médias, keyframes, masques, effets
par clip, avec un jeu d'outils volontairement restreint. Le dépôt se présente comme
l'alternative ouverte à CapCut, l'argument mis en avant étant le passage de fonctions de base
derrière un paywall chez ce dernier. Environ 88 400 étoiles GitHub au 2026-09-02.

Ce qui justifie sa présence ici est ailleurs : la feuille de route annonce un **serveur MCP**
— pilotage de l'éditeur depuis un agent — et un **mode headless** pour le rendu par lots. Un
éditeur vidéo scriptable et pilotable par agent, c'est le seul angle par lequel OpenCut touche
au périmètre du brain. Ces deux fonctions **n'existent pas** à ce jour.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Coupe, assemblage et récit rapides, sans compte ni téléversement chez un tiers | **La feuille de route n'est pas la fiche produit** : serveur MCP, mode headless, architecture à plugins, Editor API et onglet de scripting sont tous sous « What's coming ». Aucun n'est utilisable |
| Montage d'un support dont les rushes ne doivent pas sortir du poste — démo client, capture interne | **Deux bases de code coexistent** : la version *classic*, archivée et plus maintenue, est celle qui sert le site public ; la réécriture est la seule active mais n'est pas prête à prendre le relais |
| Veille sur l'arrivée effective du serveur MCP et du rendu headless, qui rendraient l'outil réellement automatisable | VFX, étalonnage, audio avancé, multipiste complexe : hors cible, le jeu d'outils est minimal par choix |
| | Rendu automatisé aujourd'hui : pour du batch scriptable, `ffmpeg` reste la réponse |
| | **Contributions externes fermées** le temps de la refonte : aucun correctif tiers à espérer à court terme |
| | **Aucun site de documentation** : `opencut.app/docs` renvoie 404 et `docs.opencut.app` ne répond pas — d'où le champ `url_docs:` laissé vide |
| | Génération de vidéo par modèle : sujet différent → [[Video generation]] |

## Mise en œuvre

- Installation — aucun binaire téléchargeable : les releases v0.1.0 à v0.3.0 (la dernière le 2026-04-15) ne portent aucun asset, ce sont des jalons de l'application web. Le desktop natif (GPUI) est annoncé « in progress », le mobile seulement annoncé
- Point d'entrée — `opencut.app` dans le navigateur, qui fait tourner la version *classic*, pas la réécriture
- Prérequis — pour l'auto-hébergement de la *classic* (`opencut-app/opencut-classic`, dépôt **archivé**) : Next.js, Bun, plus Postgres et Redis par Docker Compose. Pour la réécriture (`OpenCut-app/OpenCut`) : monorepo Moon, outils épinglés par proto, Bun — `moon run web:dev` sur 5173, `api:dev` sur 8787, `desktop:dev` ; prévisualisation sur `new.opencut.app`
- Exécution — dans le navigateur ; les médias restent sur la machine
- Coût — gratuit, MIT

## Écosystème

### Alternatives

<!-- Aucune : le brain ne contient aucun autre outil de montage vidéo, et en fabriquer une pour remplir le champ serait faux. -->

## Ressources

- Dépôt — https://github.com/OpenCut-app/OpenCut
- Site — https://opencut.app

## Voir aussi

- [[Médias]] — le hub du domaine
- [[SmartTube]] — l'autre page `media/video` du brain ; nature différente (lecture, pas montage), même inconfort de rangement
- [[Claude Video]] — le cas inverse, et déjà fonctionnel : une vidéo donnée en entrée à un agent
- [[mcp-protocol]] — le protocole que le serveur MCP annoncé exposerait
