---
galaxie: dev
type: outil
nom: OpenCut
alias: [OpenCut-app/OpenCut, opencut]
pitch: "Éditeur de montage vidéo open-source (MIT), alternative déclarée à CapCut : cœur Rust, frontend TypeScript/Next.js, médias traités en local. Réécriture en cours — serveur MCP, mode headless et plugins sont annoncés, pas livrés."
categorie: tooling/video
famille: application
domaines: []
licence_type: open-source
os: "Navigateur (aujourd'hui) ; desktop et mobile annoncés, non livrés"
langage: TypeScript, Rust
status: actif
alternatives: []
tags: [video-editing, privacy]
url_docs: 
url_repo: https://github.com/OpenCut-app/OpenCut
---

# OpenCut

## Pourquoi

**Avertissement de rangement, à lire en premier** : ce brain documente des briques data, ML et IA. Un éditeur de montage vidéo n'en relève pas. La page est classée en `tooling/video`, catégorie créée faute de mieux, et son champ `domaines:` est **volontairement vide** — aucune des six valeurs du vocabulaire (`data-sci`, `data-eng`, `mlops`, `ml-eng`, `ai-eng`, `infra-ops`) ne la couvre. À lire comme une fiche périphérique, pas comme une brique choisissable dans un plan projet.

Ce qui justifie malgré tout sa présence : la feuille de route annonce un **serveur MCP** (pilotage de l'éditeur depuis un agent) et un **mode headless** pour le rendu par lots. Un éditeur vidéo scriptable et pilotable par agent, c'est le seul angle par lequel OpenCut touche au périmètre du brain. **Ces deux fonctions n'existent pas** à ce jour — cf. *Pièges*.

Ce qui existe aujourd'hui : un éditeur de montage dans le navigateur, sous licence MIT, où les médias ne quittent pas la machine. Timeline, prévisualisation, bac à médias, keyframes, masques, effets par clip, jeu d'outils volontairement restreint. Le positionnement affiché par le dépôt est « the open-source CapCut alternative » ; l'argument mis en avant côté projet est le passage de fonctions de base derrière un paywall chez CapCut. Environ 88 400 étoiles GitHub au 2026-09-02.

## Quand l'utiliser

- Coupe, assemblage et récit rapides, sans compte ni téléversement chez un tiers.
- Montage d'un support où les rushes ne doivent pas sortir du poste (démo client, capture d'écran interne).
- Veille sur l'arrivée effective du serveur MCP et du rendu headless, qui rendraient l'outil réellement automatisable.

## Quand NE PAS l'utiliser

- VFX, étalonnage, audio avancé, multipiste complexe : hors cible, le jeu d'outils est minimal par choix.
- Chaîne de production qui dépend d'une fonctionnalité de la feuille de route : rien de ce qui est annoncé n'est livré.
- Rendu automatisé aujourd'hui : pour du batch scriptable, `ffmpeg` reste la réponse.
- Génération de vidéo par modèle : sujet différent, cf. [[Wiki/Concepts/Video generation|Video generation]].

## Installation & plateformes

- **Usage direct** : `opencut.app`, dans le navigateur. Ce site fait tourner la version *classic*, pas la réécriture.
- **Auto-hébergement** : dépôt `opencut-app/opencut-classic` — application Next.js, Bun, plus Postgres et Redis via Docker Compose. Ce dépôt est **archivé**.
- **Réécriture** (`OpenCut-app/OpenCut`) : monorepo Moon, outils épinglés par proto, Bun ; `moon run web:dev` (port 5173), `api:dev` (8787), `desktop:dev`. Prévisualisation sur `new.opencut.app`.
- **Aucun binaire téléchargeable** : les releases v0.1.0 à v0.3.0 (dernière le 2026-04-15) ne portent aucun asset — ce sont des jalons de l'application web. Le desktop natif (GPUI) est annoncé « in progress », le mobile seulement annoncé.

## Pièges

- **La roadmap n'est pas la fiche produit.** Serveur MCP, mode headless, architecture à plugins, Editor API et onglet de scripting figurent tous sous « What's coming » dans le README. Aucun n'est utilisable. C'est le point à vérifier avant toute décision fondée sur cette page.
- **Deux bases de code coexistent** : la version *classic* (archivée, plus maintenue) est celle qui sert le site public ; la réécriture est la seule active mais n'est pas prête à prendre le relais.
- **Contributions externes fermées** le temps de la refonte de l'architecture — pas de correctif tiers à espérer à court terme.
- **Aucun site de documentation** : `opencut.app/docs` renvoie 404, `docs.opencut.app` ne répond pas. Le champ `url_docs:` est donc laissé vide ; le README et le dossier `docs/` du dépôt archivé sont la seule doc.
- **Les tags `mcp` et `agents` anticipent.** Ils décrivent l'intérêt de la page pour ce brain, pas une capacité livrée. Une recherche par tag `mcp` remontera donc un outil sans serveur MCP.
- **`domaines: []` a un effet de bord assumé** : la page n'apparaîtra dans aucun hub de `MOC/Themes/`.

## Alternatives

- Aucune. Le brain ne contient aucun autre outil de montage vidéo, et fabriquer une alternative pour remplir le champ serait faux.

## Liens

- [[Dev/Outils/SmartTube|SmartTube]] — l'autre page `tooling/video` du brain ; nature différente (lecture, pas montage), même inconfort de rangement
- [[Dev/Outils/Claude Video|Claude Video]] — le cas inverse et déjà fonctionnel : une vidéo donnée en entrée à un agent
- [[Wiki/Concepts/mcp-protocol|mcp-protocol]] — le protocole que le serveur MCP annoncé exposerait
- [[Wiki/Concepts/Video generation|Video generation]] — synthèse de vidéo par modèle : sujet distinct du montage
- Repo : https://github.com/OpenCut-app/OpenCut
- Site : https://opencut.app
