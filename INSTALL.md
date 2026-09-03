---
nom: INSTALL
role: gouvernance
created: 2026-05-20
modified: 2026-09-05
tags: [meta]
---

# Guide d'installation — DevBrain

Ce guide t'accompagne pas à pas pour installer DevBrain et le connecter à Claude Code (ou n'importe quel agent compatible MCP).

> **Durée estimée :** 15-20 minutes.
> **Captures :** Obsidian 1.12.7 en français sur Windows 11. Les libellés en anglais sont entre parenthèses quand c'est utile.

---

## Sommaire

1. [Aperçu — à quoi ça ressemble une fois installé](#1-aperçu--à-quoi-ça-ressemble-une-fois-installé)
2. [Pré-requis](#2-pré-requis)
3. [Cloner le dépôt](#3-cloner-le-dépôt)
   - 3.5. [Activer les hooks git — **obligatoire**](#35-activer-les-hooks-git--obligatoire)
4. [Ouvrir DevBrain comme coffre Obsidian](#4-ouvrir-devbrain-comme-coffre-obsidian)
5. [Activer les modules complémentaires](#5-activer-les-modules-complémentaires)
6. [Installer les 4 plugins requis](#6-installer-les-4-plugins-requis)
   - 6.1. [Local REST API & MCP Server](#61-local-rest-api--mcp-server)
   - 6.2. [Templater](#62-templater)
   - 6.3. [Dataview](#63-dataview)
   - 6.4. [File Hider](#64-file-hider)
7. [Récupérer la clé API et l'endpoint MCP](#7-récupérer-la-clé-api-et-lendpoint-mcp)
8. [Configurer Templater pour pointer sur `Templates/`](#8-configurer-templater-pour-pointer-sur-templates)
9. [Cacher `AI/` avec File Hider](#9-cacher-ai-avec-file-hider)
10. [Connecter Claude Code via MCP](#10-connecter-claude-code-via-mcp)
11. [Installer les Skills Obsidian (kepano)](#11-installer-les-skills-obsidian-kepano)
   - 11.5. [Activer le code couleurs des rôles](#115-activer-le-code-couleurs-des-rôles)
12. [Personnaliser les fichiers `CLAUDE.md`](#12-personnaliser-les-fichiers-claudemd)
13. [(Optionnel) Hook Stop pour la mémoire de session](#13-optionnel-hook-stop-pour-la-mémoire-de-session)
14. [Vérifier que tout marche](#14-vérifier-que-tout-marche)
15. [Dépannage](#15-dépannage)

---

## 1. Aperçu — à quoi ça ressemble une fois installé

Une fois DevBrain installé, ton coffre Obsidian aura cette structure :

![Vue d'ensemble du vault DevBrain](docs/install/img/24-vault-overview.png)

À gauche : l'arborescence du vault — **un dossier par domaine**, à la racine. À droite : un
*Comparatif* `.base` qui se remplit tout seul en lisant le frontmatter des fiches de sa
catégorie (ici, les frameworks LLM open-source).

Chaque fiche de brique (`role: brique`) utilise un frontmatter dense, lisible par Claude comme
par toi en mode lecture :

![Frontmatter d'une fiche de brique](docs/install/img/19-postgres-fiche-properties.png)

C'est la combinaison **frontmatter + Bases** qui permet à Claude (et à toi) de poser des
questions comme « liste mes bases vectorielles open-source encore en production » sans rien
indexer.

> Les captures de ce guide datent de la v2, où les fiches vivaient sous `Dev/Services/`. Le
> lot 3 de la v3 les a descendues dans l'arbre des 20 domaines : les images montrent encore
> les anciens chemins, le texte donne les vrais.

---

## 2. Pré-requis

Installe d'abord :

| Outil | Version mini | Vérification |
|-------|--------------|--------------|
| [Obsidian](https://obsidian.md/download) | 1.10+ | Ouvrir l'app |
| [Git](https://git-scm.com/downloads) | — | `git --version` |
| [Node.js](https://nodejs.org/) | 18+ | `node --version` |
| [Python](https://www.python.org/downloads/) | 3.10+ | `python --version` |
| [`uv`](https://docs.astral.sh/uv/getting-started/installation/) | — | `uvx --version` |
| [Claude Code](https://docs.claude.com/en/docs/claude-code) | — | `claude --version` |

> `uv` n'est pas Python. C'est un installateur de paquets Python ultra-rapide, on s'en sert pour lancer le serveur MCP `mcp-obsidian` sans polluer ton environnement Python.

---

## 3. Cloner le dépôt

```bash
git clone https://github.com/floSa/DevBrain.git ~/DevBrain
cd ~/DevBrain
```

Sur Windows tu peux remplacer `~/DevBrain` par `%USERPROFILE%\Documents\Projets\DevBrain` ou n'importe quel emplacement persistant (évite `Desktop` ou `Downloads`).

---

## 3.5. Activer les hooks git — **obligatoire**

À faire **une fois par clone**, juste après le `git clone`, et avant le premier commit.

```bash
git config core.hooksPath .githooks
```

Vérifier que c'est pris :

```bash
git config core.hooksPath        # doit répondre : .githooks
```

### À quoi ça sert

DevBrain est un dépôt **personnel**. Claude Code annonce à chaque conversation l'adresse
e-mail qui identifie l'utilisateur auprès de l'outil — et cette adresse peut être une adresse
**professionnelle**. Une conversation a déjà signé cinq commits du vault avec l'adresse pro.
Une fois poussés, ces commits font entrer l'adresse dans les **contributeurs GitHub** du dépôt,
d'où elle ne se retire pas sans réécriture d'historique.

La consigne écrite existait déjà dans `CLAUDE.md`. Elle n'a pas suffi. Deux hooks, versionnés
dans `.githooks/`, la tiennent désormais mécaniquement :

| Hook | Ce qu'il fait |
|---|---|
| `pre-commit` | refuse un commit dont l'**auteur** ou le **committer** contient `aosis.net`. Lit l'identité effective (`git var`), donc couvre aussi `-c user.email=…`, `--author=…` et `GIT_AUTHOR_EMAIL=…` |
| `pre-push` | refuse de **pousser** un commit fautif, quelle que soit son origine : `--no-verify`, un `rebase` qui rejoue une identité, un commit importé d'un autre clone ou d'un worktree où les hooks n'étaient pas actifs |

**Git ne lit `.githooks/` qu'après la commande ci-dessus.** Sans elle, les hooks sont bien dans
le dépôt mais ne s'exécutent pas — et c'est pire qu'aucun garde-fou, parce qu'on le croit actif.
Un **worktree** frais hérite de la config du dépôt principal, mais un **clone** neuf, non :
refaire la commande.

### Poser l'identité du dépôt

Les hooks vérifient ; ils ne configurent rien. L'identité, elle, se pose une fois :

```bash
git config --local user.name  "floSa"
git config --local user.email "<ton adresse perso>"
```

`--local` est important : la config **du dépôt** prime sur la config globale de la machine,
qui peut très bien porter une adresse pro pour d'autres projets.

### Si un hook refuse

Ce n'est pas un incident à contourner, c'est la règle qui fonctionne. Le message dit quelle
identité a été refusée et laquelle est attendue. **Ne pas utiliser `--no-verify`** : corriger
l'identité, puis recommencer.

```bash
git commit --amend --reset-author --no-edit   # ré-attribue le dernier commit
```

Pour plusieurs commits déjà faits, en parler à floSa avant de réécrire quoi que ce soit — une
réécriture d'historique ne se décide pas seule (cf.
`.claude/skills/cloturer-brain/SKILL.md`, *Politique git du vault*).

---

## 4. Ouvrir DevBrain comme coffre Obsidian

Lance Obsidian. Au premier démarrage (ou via *File → Open Vault*), le sélecteur de coffre s'affiche :

![Sélecteur de coffre Obsidian](docs/install/img/02-welcome-vault-picker.png)

Clique sur **Ouvrir** *(Open)* à droite de "Ouvrir un dossier comme coffre" *(Open folder as vault)*. Une boîte Windows s'ouvre — navigue jusqu'au dossier `DevBrain` que tu viens de cloner :

![Sélecteur de dossier sur DevBrain](docs/install/img/02b-folder-picker-devbrain.png)

Tu peux soit naviguer manuellement, soit coller le chemin dans le champ **Dossier :** puis cliquer **Sélectionner un dossier**.

Une fois ouvert, l'arborescence du vault apparaît dans la barre latérale gauche :

![Vault DevBrain ouvert dans Obsidian](docs/install/img/03-vault-opened.png)

Tu dois voir les dossiers `AI`, `Dev`, `docs`, `Documentation`, `MOC`, `Projects`, `Templates`, `Wiki` et les fichiers `CHANGELOG.md`, `CLAUDE.md`, `CLAUDE-build.md`, `CLAUDE-project.md`, `CONTRIBUTING.md`, `Home.md`, `Inbox.md`, `README.md`.

> 💡 **À la première ouverture du vault, Obsidian peut afficher un message "Faire confiance à l'auteur" puisque DevBrain contient des fichiers `.base`. Accepte.**

---

## 5. Activer les modules complémentaires

Par défaut, Obsidian protège ton coffre avec le **mode restreint** : aucun plugin tiers ne peut tourner. On va le désactiver pour ce vault uniquement (les autres coffres ne sont pas affectés).

Ouvre les paramètres avec `Ctrl + ,` *(Cmd+, sur Mac)*. La vue **Général** s'affiche :

![Settings → Général](docs/install/img/01-settings-general.png)

Clique sur **Modules complémentaires** *(Community plugins)* dans la barre de gauche. Le mode restreint est actif :

![Mode restreint activé](docs/install/img/04-restricted-mode.png)

Clique sur **Activer les modules complémentaires** *(Turn on community plugins)*.

Le panneau se met à jour : `Mode restreint` passe à *désactivé* et le bouton **Parcourir** *(Browse)* devient cliquable :

![Modules complémentaires activés](docs/install/img/05-community-plugins-enabled.png)

---

## 6. Installer les 4 plugins requis

Clique sur **Parcourir** *(Browse)*. Le catalogue communautaire s'ouvre :

![Catalogue des plugins](docs/install/img/06-plugins-browser.png)

Tu vas installer ces 4 plugins. Pour chacun : tape son nom dans la barre de recherche, clique sur la carte du résultat, puis **Installer** *(Install)* puis **Activer** *(Enable)*. Le détail de chaque plugin est expliqué juste après le tableau.

| # | Plugin | Auteur (id repo) | Rôle dans DevBrain |
|---|--------|------------------|---------------------|
| 1 | **Local REST API & MCP Server** | Adam Coddington (`coddingtonbear`) | Expose le vault via HTTPS sécurisé. Sans lui, **Claude Code ne peut rien lire ni écrire** dans ton brain. |
| 2 | **Templater** | SilentVoid13 | Remplit automatiquement les nouvelles fiches (Service, Concept, Pattern) avec le bon frontmatter, la date du jour, l'arborescence cible. |
| 3 | **Dataview** | blacksmithgu | Permet d'écrire des requêtes type SQL sur le frontmatter (`LIST FROM "Bases de données" WHERE maturite = "production"`). Sert de fallback si tu n'utilises pas encore les `.base`. |
| 4 | **File Hider** | Oliver Akins (`eldritch-oliver`) | Cache `AI/` (mémoire et hooks de l'agent) et autres dossiers techniques de la sidebar, pour que ta vue reste propre. |

### 6.1. Local REST API & MCP Server — le pont avec Claude

**À quoi ça sert :** ce plugin transforme ton Obsidian en *serveur local* qui répond en HTTPS sur `127.0.0.1:27124`. Quand Claude Code (ou Claude Desktop, Codex, n'importe quel agent compatible MCP) veut lire une fiche ou en écrire une, il interroge ce serveur. C'est **la fondation** de tout DevBrain : sans lui, l'IA voit le repo Git mais pas le vault vivant (frontmatter, Bases, etc.).

Le plugin expose deux interfaces sur le même port :
- une **REST API** classique (`GET /vault/...`, `POST /vault/...`) pour les scripts custom
- un **endpoint MCP** (`/mcp`) que les agents IA parlent nativement depuis Claude 3.5+

Tape `Local REST API` dans la recherche. Le bon résultat est **Local REST API with MCP** par Adam Coddington (`coddingtonbear`, ~490k téléchargements). Attention : il y a d'autres résultats (« MCP REST » par swarogan, « Local REST API Second Brain MCP Extension ») — **pas** ceux qu'on veut.

![Recherche Local REST API](docs/install/img/07-search-local-rest-api.png)

Clique sur la carte, puis **Installer** :

![Page détail Local REST API](docs/install/img/08-local-rest-api-detail.png)

Une fois installé, le bouton devient **Activer**. Clique dessus :

![Local REST API activé](docs/install/img/09-local-rest-api-activated.png)

Dès qu'il est activé, le serveur tourne. Tu peux le vérifier dans n'importe quel navigateur en allant sur `https://127.0.0.1:27124/` (le navigateur va râler sur le certificat auto-signé — c'est normal).

> 🔐 **Note sécurité :** le serveur n'écoute que sur `127.0.0.1` (loopback), donc inaccessible depuis ton réseau local ou Internet. Il faut aussi la clé API pour faire quoi que ce soit. Tu ne peux pas te faire pirater par défaut.

### 6.2. Templater — les fiches qui s'auto-remplissent

**À quoi ça sert :** Templater est un moteur de templates dynamiques. Quand tu crées une nouvelle fiche Service avec le skill `enrichir-brain`, ce n'est pas un fichier markdown vide qui apparaît — c'est une fiche pré-remplie avec :

- le **frontmatter standardisé** (`nom`, `categorie`, `pitch`, `licence_type`, etc. — ~14 champs, cf. `Templates/Service-Dev.md`)
- les **sections markdown obligatoires** (`## Pourquoi`, `## Quand l'utiliser`, `## Pièges`, `## Liens`)
- des **wikilinks pré-remplis** vers les pages liées

Sans Templater, tu devrais recopier ces lignes à la main à chaque nouvelle fiche. Les autres gabarits (`Concept-Wiki.md`, `Pattern.md`, `Rule.md`) fonctionnent pareil.

Reviens à la liste *(flèche ← en haut à gauche, ou clique sur la barre de recherche puis efface)*, retape `Templater`. Le bon résultat est de **SilentVoid13** (~4M téléchargements). Clique sur sa carte → **Installer** → **Activer**.

> ℹ️ On configurera son dossier de templates à l'étape 8 (sinon il ne saura pas où chercher).

### 6.3. Dataview — requêtes sur le brain

**À quoi ça sert :** Dataview lit le frontmatter de toutes les notes et te laisse les interroger avec un mini-langage type SQL. Exemple concret :

````markdown
```dataview
LIST FROM "Bases de données"
WHERE categorie = "database/relationnel" AND licence_type = "open-source"
SORT file.name ASC
```
````

…te renvoie la liste de toutes les bases relationnelles open-source du brain. Le champ `score`
de la v1 n'existe plus : il n'était jamais fiable. Les critères qui trient réellement sont
`maturite`, `licence_type` et `famille`.

Depuis Obsidian 1.10, le format `.base` natif fait pareil (et c'est ce que DevBrain utilise par défaut dans les `Comparatif - *.base`, rangés **dans le dossier de leurs membres**). Mais Dataview reste utile pour :
- les **requêtes ad-hoc inline** dans une fiche (le format `.base` est un fichier séparé)
- la **rétrocompatibilité** si tu ouvres le vault avec une version d'Obsidian < 1.10
- les **scripts Claude** qui génèrent du markdown dynamique : Dataview est plus simple à écrire pour l'IA que `.base`

Pareil. Retape `Dataview`. Choisis le plugin de **blacksmithgu** (~4M téléchargements). **Installer** + **Activer**.

### 6.4. File Hider — sidebar propre

**À quoi ça sert :** DevBrain a un dossier `AI/` qui contient des trucs techniques que tu ne dois pas voir 24h/24 :
- `AI/sessions/` — résumés auto des conversations passées avec Claude
- `AI/prompts/` — prompts réutilisables
- `AI/scripts/` — scripts d'index et d'hygiène
- `AI/index/` — index généré (`brain-index.json`), ne s'édite jamais à la main

Tout ça pollue ta sidebar et te distrait quand tu cherches une vraie fiche. File Hider permet de **cacher** ces dossiers de l'explorateur Obsidian — les fichiers sont toujours là, Claude peut toujours les lire, mais toi tu ne les vois plus.

Le plugin ajoute simplement une option **"Hide Folder"** / **"Hide File"** au clic droit dans la sidebar. On l'utilisera à l'étape 9 pour cacher `AI/`.

⚠️ **Attention au choix exact** : la recherche `File Hider` renvoie 2 résultats. Tu veux **File Hider** par **eldritch-oliver** (Oliver Akins, ~43k téléchargements), **pas** *Explorer Hider* (mara-li). Les deux font le même genre de chose mais on a calibré DevBrain pour File Hider.

Retape `File Hider`. Choisis le plugin d'eldritch-oliver. **Installer** + **Activer**.

### État final attendu

Ferme la page Parcourir et reviens à **Modules complémentaires**. Tu dois voir tes 4 plugins listés et tous les toggles violets (activés) :

![Tous les plugins installés et activés](docs/install/img/12-all-plugins-enabled.png)

---

## 7. Récupérer la clé API et l'endpoint MCP

C'est l'étape qui permettra à Claude Code de lire/écrire dans ton vault.

Dans **Modules complémentaires** → ligne **Local REST API & MCP Server** → clique sur l'icône engrenage à droite.

Le panneau d'options s'ouvre. Note :

- **URL HTTPS** : `https://127.0.0.1:27124/` (port par défaut **27124**)
- **API key** : chaîne `Bearer ...` (~64 caractères). C'est ta clé secrète — traite-la comme un mot de passe.

![Options Local REST API avec clé masquée](docs/install/img/10-local-rest-api-options.png)

> ⚠️ **Sécurité :** ne commit jamais cette clé. Elle donne un accès complet en lecture/écriture à tout ton vault. Si tu la fuites, regénère-la (voir plus bas, *Re-generate certificates* ou *Reset all crypto*).

Scrolle plus bas. La section **How to access via MCP** te donne directement le bloc JSON à coller dans la config Claude Code :

![Endpoint MCP + exemple JSON](docs/install/img/13-mcp-endpoint-json-config.png)

L'endpoint MCP est `https://127.0.0.1:27124/mcp` — c'est ce que tu utiliseras à l'étape 10.

Plus bas encore, des options avancées (regénérer le certificat, reset crypto, activer le HTTP non chiffré) :

![Options avancées Local REST API](docs/install/img/14-local-rest-api-advanced.png)

> 🔒 Laisse **Enable non-encrypted (HTTP) server** désactivé. Le HTTPS auto-signé suffit en local et ne dégrade pas la sécu.

Copie ta clé API (le bouton **Copier** à droite). On l'utilisera à l'étape 10.

---

## 8. Configurer Templater pour pointer sur `Templates/`

Sans cette étape, Templater ne saura pas où chercher les templates de DevBrain.

Toujours dans Settings → barre latérale → bas → clique sur **Templater** (sous "Modules complémentaires") :

![Templater settings (vide)](docs/install/img/22-templater-settings.png)

Dans le champ **Template folder location**, tape `Templates`. Obsidian autocomplète. Sélectionne `Templates` (pas `Templates/ServiceDocs`) :

![Templater configuré](docs/install/img/23-templater-folder-set.png)

C'est tout pour Templater. Les autres options (syntax highlighting, jump to cursor) sont en valeurs par défaut OK.

---

## 9. Cacher `AI/` avec File Hider

`AI/` contient ta mémoire de session, tes prompts, tes hooks. C'est l'espace de l'agent — pas le tien. On le masque pour ne pas polluer la sidebar.

File Hider ne se configure pas dans les Options du plugin — il fonctionne par clic droit dans l'explorateur.

Ferme Settings (`Échap`). Dans la sidebar du vault, **clic droit sur le dossier `AI`** :

![Menu contextuel File Hider sur AI/](docs/install/img/16-file-hider-context-menu.png)

Clique sur **Hide Folder**. Le dossier disparaît de la sidebar :

![Vault sans le dossier AI/ visible](docs/install/img/17-file-hider-after-hidden.png)

Refais la même chose pour `.obsidian/` si tu veux (mais Obsidian le masque déjà par défaut dans la sidebar — pas indispensable).

> ↩️ **Annuler :** Settings → File Hider → toggle **Hidden File Visibility** sur ON pour réafficher tous les fichiers cachés temporairement.

---

## 10. Connecter Claude Code via MCP

Maintenant on branche Claude Code sur le MCP server qui tourne dans Obsidian.

**Méthode 1 — Via `claude mcp add`** (recommandée) :

```bash
claude mcp add devbrain \
  --command uvx \
  --args mcp-obsidian \
  --env OBSIDIAN_API_KEY=<colle_ta_cle_ici> \
  --env OBSIDIAN_HOST=127.0.0.1 \
  --env OBSIDIAN_PORT=27124
```

> Sur Windows PowerShell, remplace les `\` de fin de ligne par des backticks `` ` ``, ou mets tout sur une ligne.

**Méthode 2 — Via `.claude/settings.json` direct** (utilise le JSON déjà fourni par le plugin) :

Récupère le bloc JSON exact depuis le panneau Local REST API (capture en 7). Copie-le dans `.claude/settings.json` à la racine de ton vault DevBrain (ou dans le projet où tu veux que Claude ait accès au brain).

Vérifie ensuite :

```bash
claude mcp list
```

Tu dois voir une ligne `devbrain` avec status `✓ Connected`. Si c'est ✗, va à la section [Dépannage](#15-dépannage).

---

## 11. Installer les Skills Obsidian (kepano)

**À quoi ça sert :** Claude ne connaît pas la syntaxe Obsidian par défaut. Si tu lui demandes de créer une fiche, il va écrire du markdown générique : pas de wikilinks (`Postgres`), pas de Bases, des callouts mal formés, des Canvas inconnus. Les skills officiels [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) de Steph Ango (CEO d'Obsidian) lui apprennent ces conventions.

Concrètement, après cette étape, Claude saura :
- linker entre fiches avec `Nom` (et utiliser les alias frontmatter)
- écrire un bloc `.base` valide avec filtres et colonnes
- formater des callouts (`> [!info]`, `> [!warning]`, `> [!example]`)
- générer du Canvas si tu lui demandes un schéma
- comprendre les properties typées (multi-select, date, lien)

Le second skill, `kepano/defuddle`, est un parseur HTML→markdown propre — utile quand tu colles un article web et veux que Claude le nettoie au format Obsidian.

```bash
npx skills add kepano/obsidian-skills
npx skills add kepano/defuddle
```

> ℹ️ La commande `npx skills` est l'installeur officiel des skills Claude. Elle clone le repo skill dans `~/.claude/skills/<nom>/` et l'enregistre. Vérifie après : `npx skills list` doit montrer les deux.

Les **skills custom DevBrain** (`enrichir-brain`, `planifier-projet`) sont déjà dans `.claude/skills/` du repo — pas besoin de les installer séparément, Claude Code les charge automatiquement quand il est lancé depuis le dossier du vault.

---

## 11.5. Activer le code couleurs des rôles

Depuis le lot 2 de la migration v3, la couleur se lit sur **`role:`** — le champ qui porte la
**nature** d'une page. `galaxie:` a été supprimé : il ne servait qu'à ça, et il le faisait
moins bien (il ne distinguait ni un hub d'une notion, ni un comparatif d'une brique).

| Élément | `role:` | Couleur |
|---|---|---|
| **Métiers** transverses (Data Science, ML Eng, AI Eng, MLOps, Data Eng) | `hub` | 🟡 or |
| **Hubs** — la page d'un dossier, l'aiguillage | `hub` | 🟠 orange |
| **Briques** — ce qu'on déploie ou importe | `brique` | 🔵 bleu |
| **Notions** — ce qu'il faut comprendre | `notion` | 🟢 vert |
| **Comparatifs** — ce qui départage plusieurs briques | `comparatif` | 🔴 rouge |
| **Patterns** et **Règles** | `pattern`, `rule` | ⚪ gris |

Le bleu et le vert sont **exactement** ceux des anciennes galaxies `dev` et `wiki` : ce sont
les mêmes pages, elles ne changent que de nom de champ.

Deux choses à activer côté Obsidian : le **snippet CSS** (couleurs dans la sidebar, les
onglets, les notes) et le **graph view avec groupes** (couleurs dans le graphe).

### A. Activer le snippet CSS

Le fichier `.obsidian/snippets/roles.css` est versionné dans le repo. Pour l'activer :

1. **Settings** → **Apparence** *(Appearance)*
2. Scrolle tout en bas jusqu'à la section **Extraits CSS** *(CSS snippets)*
3. Cherche **roles** dans la liste
4. Clique sur le toggle à droite — il devient violet/actif

![Extrait CSS activé dans Apparence → Extraits CSS](docs/install/img/27-snippet-galaxies-active.png)

Le toggle passe au violet et l'effet est immédiat dans la sidebar.

Effets visuels immédiats (recharge le vault si besoin, `Ctrl+R`) :
- **Sidebar** : dossiers et fichiers ont une barre verticale colorée + titres de dossiers en gras coloré
- **Onglets** : un fin trait coloré au-dessus de l'onglet selon le rôle de la note ouverte
- **Note ouverte** : bord gauche coloré selon le champ `role:` du frontmatter
- **Property** `role:` dans le panneau Properties : rendue en pastille colorée

> La capture ci-dessus date de la v2, quand l'extrait s'appelait `galaxies.css` et que la
> sidebar montrait `Wiki/` en vert. Le mécanisme est identique ; seuls le nom du fichier et le
> champ lu ont changé.

### B. Activer le module Graph et configurer les groupes

> ⚠️ Si tu ne vois pas **Affichage du graphique** dans tes Settings, c'est que le module natif Obsidian est désactivé. Active-le d'abord :
>
> 1. **Settings** → **Modules principaux** *(Core plugins)*
> 2. Cherche **Affichage du graphique** *(Graph view)* dans la liste
> 3. Clique sur le toggle (à droite) pour l'activer
>
> Une icône en forme de petit graphe nodal apparaît alors dans la **barre latérale gauche**.

Une fois le module activé, configurer les groupes :

1. Clique sur l'icône **Affichage du graphique** dans la sidebar gauche pour ouvrir le graphe
2. Dans le panneau du graphe, clique sur l'icône **engrenage** (en haut à droite, dans le panneau du graphe lui-même)
3. Va dans l'onglet **Groupes** *(Groups)*
4. Clique 6 fois sur **Nouveau groupe** *(New group)* et configure chacun **dans cet ordre** :

| # | Requête (à coller telle quelle) | Couleur (hex — RGB) |
|---|---|---|
| 1 | `path:Métiers/` | 🟡 or `#FFD43B` — 255/212/59 |
| 2 | `["role":"hub"] OR path:MOC/` | 🟠 orange `#FF922B` — 255/146/43 |
| 3 | `["role":"brique"]` | 🔵 indigo `#412CDD` — 65/44/221 |
| 4 | `["role":"notion"]` | 🟢 vert olive `#7AB800` — 122/184/0 |
| 5 | `["role":"comparatif"]` | 🔴 rouge `#EF4444` — 239/68/68 |
| 6 | `["role":"pattern"] OR ["role":"rule"]` | ⚪ gris `#94A3B8` — 148/163/184 |

Pour la couleur : à droite de la requête, clique sur le petit carré de couleur → un sélecteur s'ouvre. Dans Obsidian 1.12.7, le plus simple est de saisir les trois champs **R / G / B** en bas du sélecteur (valeurs ci-dessus), puis `Entrée`.

> ⚠️ **L'ordre des règles compte.** `path:Métiers/` doit passer **avant** la règle `hub`, sinon les cinq axes métier prendraient l'orange des hubs — ce sont eux aussi des `role: hub`. Obsidian applique la première règle qui matche.

> 💡 **Pourquoi une règle mixte en 2 ?** `MOC/Concepts/` porte les 10 MOC de notions, seule porte d'entrée de 30 d'entre elles ; ce ne sont pas encore des `role: hub`, et elles vivent jusqu'au **lot 4**. La règle `["role":"hub"] OR path:MOC/` couvre les deux le temps de la migration, sans qu'il faille y retoucher le jour où `MOC/` disparaît.

> 💡 **Deux règles ne colorent encore rien** : `comparatif` naît au **lot 5**, quand les `.base` deviendront des pages. La règle est posée d'avance — elle coloriera le jour même, sans intervention.

> ℹ️ Deux règles de l'ancien bloc v2 ont été **retirées** et non transposées. `path:AI/skills/` : ce dossier n'existe plus, les skills vivent sous `.claude/skills/`, et Obsidian **n'indexe aucun dossier commençant par un point** — la règle ne pouvait pas fonctionner sous son nouveau chemin. `["galaxie":"meta"]` : le champ n'existe plus, et les pages de gouvernance (`Documentation/`, `AI/`) sont déjà hors du graphe par `userIgnoreFilters`.

Une fois les 6 groupes saisis, le panneau **Groupes** ressemble à ça, et le graphe se colorie en direct :

![Panneau Groupes du graphe](docs/install/img/25-graph-groupes-config.png)

Le graphe affiche alors tes notes coloriées par nature (métiers en or, hubs en orange, briques en bleu, notions en vert) :

![Graphe DevBrain colorié par rôle](docs/install/img/26-graph-colore.png)

> Ces deux captures datent de la v2 (7 groupes, requêtes en `galaxie:`). Le résultat visuel est le même ; les requêtes du tableau ci-dessus font foi.

Si tu ne vois pas l'effet, refais "Reload app" (`Ctrl+R`).

> ℹ️ Le détail de ce code couleur (et la navigation en graphe local) vit dans `Documentation/perso/obsidian-graph.md`, la source de référence. Comme `.obsidian/graph.json` est gitignoré, **cette config est locale par machine** : à réappliquer sur chaque poste.

### C. Exclure les Roadmaps du graphe (optionnel)

`Wiki/Roadmaps/` était un scaffold vide prévu pour des documents de référence à fort volume de wikilinks fantômes (héritage v1 : `Roadmap.md` ~1500 items, `Roadmap-AI.md`), jamais remigrés. **Il a été supprimé le 2026-09-05** avec le reste de `Wiki/` : la v3 n'a plus de galaxie, et une roadmap qui reviendrait se rangerait par son domaine comme tout le reste. Rien à exclure aujourd'hui, donc — cette section reste pour le jour où un document de ce genre revient et noie le graphe sous un nuage gris déconnecté :

1. Toujours dans les **Settings** du panneau graphe → onglet **Filtres** *(Filters)*
2. Dans le champ **Recherche** *(Search)*, coller :

   ```
   -path:<le dossier du document>
   ```

   Le `-` exclut.

> 💡 Cette exclusion est par-graphe (vue locale ou globale). Tu peux aussi simplement décocher **Existing files only** *(Fichiers existants uniquement)* dans Filters pour masquer tous les wikilinks vers des notes non-créées — utile en général au-delà du Roadmap.

---

## 12. Personnaliser les fichiers `CLAUDE.md`

Avant ta première vraie session, édite ces 3 fichiers pour remplacer les placeholders (`<ton_nom>`, `<tes_domaines>`, etc.) :

- `CLAUDE.md` — routeur (mode brain vs mode projet). Il porte aussi la **règle d'identité git** (cf. §3.5) : la lire avant d'y toucher.
- `CLAUDE-build.md` — contexte du mode brain (conventions de fiches, gabarits par rôle)
- `CLAUDE-project.md` — **template** à copier dans tes futurs projets (pas à modifier en place)

Exemple minimal dans `CLAUDE.md` :

```markdown
## Identité utilisateur

Je suis floSa, dev full-stack. Domaines : Python (FastAPI, ML), TypeScript
(Next.js), DevOps (Docker, GitHub Actions). Je travaille seul ou en petite
équipe.
```

---

## 13. (Optionnel) Hook Stop pour la mémoire de session

**À quoi ça sert :** Claude Code peut exécuter un script à des moments précis (avant un tool call, après un edit, à la fin d'une session). Le hook **Stop** se déclenche quand tu fermes la conversation (Ctrl+D ou "fin de session"). Le script `AI/scripts/session_to_devbrain.py` lit la transcription de la session, en extrait un résumé structuré, et l'écrit dans `AI/sessions/YYYY-MM-DD-HHmm.md`.

Le but : la prochaine fois que tu ouvres Claude dans le vault, il lit automatiquement les 3 derniers résumés de session (instruction dans `CLAUDE.md`) et a le contexte de "où tu en étais". Tu évites de devoir re-briefer à chaque ouverture.

Sans ce hook, tu peux toujours obtenir le même résultat en disant **"fin de session"** explicitement à Claude — il écrira le résumé lui-même avant de te quitter. Le hook automatise juste le geste.

**Configuration** (à faire une seule fois, dans `~/.claude/settings.json` ou `.claude/settings.json` du vault) :

```json
{
  "hooks": {
    "Stop": [{
      "command": "python",
      "args": ["AI/scripts/session_to_devbrain.py"]
    }]
  }
}
```

Le script `session_to_devbrain.py` est déjà dans le repo. Adapte le chemin Python (`python3` sur Mac/Linux, chemin absolu si nécessaire).

---

## 14. Vérifier que tout marche

### a) Obsidian — Bases fonctionnent

Ouvre `LLM & IA générative/Comparatif - Frameworks LLM.base`. Tu dois voir un tableau des frameworks LLM (LangChain, LangGraph, LlamaIndex, DSPy, LiteLLM…) qui se remplit tout seul depuis le frontmatter :

![Comparatif LLM frameworks](docs/install/img/21-comparatif-llm-frameworks.png)

Si ça apparaît comme du texte brut au lieu d'un tableau, vérifie que ta version d'Obsidian est ≥ 1.10 (Bases est natif depuis cette version).

### b) Claude Code se connecte au vault

Dans un terminal, dans le dossier du vault :

```bash
cd ~/DevBrain
claude
```

Claude devrait :

1. Détecter le `CLAUDE.md` et te demander **"Mode build ou mode projet ?"**.
2. Pouvoir lister tes fiches Services. Teste :

```
> Liste-moi 5 fiches Services au hasard.
> Quelle est la note Postgres ? (devrait répondre "5")
```

Si tu obtiens des réponses cohérentes (pas une erreur MCP), tout est bon. 🎉

---

## 15. Dépannage

### `claude mcp list` n'affiche pas `devbrain` comme Connected

- Obsidian est-il lancé avec le vault DevBrain ouvert ? Le serveur Local REST API ne tourne **que pendant ce temps**.
- Le port 27124 est-il libre ? `netstat -an | findstr 27124` doit montrer `LISTENING` sur 127.0.0.1.
- La clé API est-elle correcte ? Re-copie depuis le panneau Local REST API (étape 7).
- Le plugin est-il bien **activé** (toggle violet) ? Settings → Modules complémentaires.

### Certificate error / SSL handshake failure

Local REST API utilise un certificat auto-signé. Le client `mcp-obsidian` est configuré pour l'accepter, mais si tu utilises un client custom :

- Soit télécharge le certificat depuis le lien *this certificate* du panneau d'options (capture en 7), et ajoute-le aux CA de confiance.
- Soit régénère-le : panneau Local REST API → **Re-generate certificates** (capture en 14). L'API key reste la même.
- En dernier recours, tu peux activer le HTTP non chiffré (même panneau, capture en 14) mais **uniquement sur ta machine locale** — jamais exposé sur le réseau.

### `npx skills add` échoue

Vérifie Node 18+ : `node --version`. Les anciennes versions de `npm` ne gèrent pas le CLI `skills`.

### Le `.base` apparaît comme du texte brut au lieu d'une table

Ta version d'Obsidian est trop ancienne. Bases est natif à partir d'Obsidian **1.10** (octobre 2025). Mets à jour Obsidian, ou utilise Dataview comme fallback (cf. §6.3).

### Un commit est refusé : « identité professionnelle sur un dépôt personnel »

C'est le hook `pre-commit` (§3.5), et il fait son travail. Le message nomme l'adresse refusée et
celle attendue. Pose l'identité locale du dépôt puis recommence — **pas de `--no-verify`** :

```bash
git config --local user.email "<ton adresse perso>"
git commit --amend --reset-author --no-edit
```

### Les hooks ne se déclenchent jamais

`git config core.hooksPath` ne répond rien : la commande de §3.5 n'a pas été passée sur ce
clone. Les hooks sont dans le dépôt, mais git ne regarde pas `.githooks/` par défaut.

```bash
git config core.hooksPath .githooks
```

Sous Windows, vérifie aussi que `.githooks/pre-commit` est bien en **LF** et non en CRLF : un
`#!/bin/sh` suivi d'un CR fait chercher un interpréteur `/bin/sh
` qui n'existe pas.
`.gitattributes` épingle `.githooks/** text eol=lf` pour l'éviter ; si le fichier a été édité
hors de git, `git checkout -- .githooks/` le remet d'aplomb.

### Templater n'insère pas les templates

Vérifie que **Template folder location** est bien réglé sur `Templates` (étape 8). Le champ est sensible à la casse.

### Le dossier `AI/` reste visible alors que j'ai cliqué Hide Folder

Vérifie que **Hidden File Visibility** est sur OFF dans les options File Hider. S'il est ON, le plugin sait que `AI/` doit être caché mais l'affiche quand même (mode "voir tout").

### Reset complet — je veux tout recommencer

- Désinstalle les 4 plugins (Settings → Modules complémentaires → corbeille).
- Réactive le mode restreint.
- Supprime `~/DevBrain/.obsidian/` (config du vault).
- Recommence depuis l'étape 4.

---

Tu es prêt. Pour la suite, consulte le [README](README.md) (concept, workflow, conventions), le
[CONTRIBUTING](CONTRIBUTING.md) (anatomie du repo, règles de modification), ou plonge directement
dans `CLAUDE-build.md` si tu veux commencer à enrichir le brain.
