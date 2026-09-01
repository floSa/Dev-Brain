# Rapport d'audit — Axe 1 : Rangement & taxonomie

Auditeur : conversation `audit-axe1-rangement-taxonomie`, le 2026-09-02.
Socle : `AI/audit/mesures-axe1.md`, relancé le 2026-09-02 (`uv run AI/scripts/audit_mesures.py`).
Le rapport `axe-2-integrite.md` n'existe pas encore : ce modèle n'a donc pas pu en tenir compte.

**Écart au socle** : aucun. `diff mesures-2026-09-02.md mesures-axe1.md` ne renvoie rien.
Trois écarts de **définition** entre le brief et le vault sont signalés en C8.

## Synthèse

`categorie:` porte deux questions à la fois, et trois valeurs absorbent 33 % des fiches Dev.
Le vault a déjà contourné le problème quatorze fois : quatorze comparatifs `.base` renoncent à
filtrer sur `categorie` — douze passent par des **tags** — et six fiches
documentent en corps de page leur propre erreur de rangement. Le couple `domaine:` × `famille:`
range **326 des 336 fiches Dev sans jugement (97,0 %)**, dissout `ml/framework` (64 pages)
en 17 domaines et `tooling/*` (86 pages) en 31. La seule chose à faire si on n'en fait qu'une :
adopter l'axe `famille:` à 9 valeurs et éclater les trois fourre-tout, dans cet ordre.

## Constats

### C1. Trois catégories absorbent un tiers du vault Dev — gravité : bloquant

- **Constat** : `ml/framework` (64 pages), `llm/framework` (33) et `tooling/code-assistant` (13)
  totalisent 110 des 336 fiches Dev, soit **32,7 %**. Ces trois valeurs ne décrivent pas un
  sujet : elles décrivent « une bibliothèque quelque part dans le ML / le LLM / l'IA de code ».
  `ml/framework` contient PyTorch, SHAP, librosa, SDV, spaCy, Gymnasium et docTR.
- **Preuve** :
  ```
  $ python3 -c "…compte les categorie: de Dev/**/*.md…"
  top3 anciennes categories : [('ml/framework', 64), ('llm/framework', 33),
                               ('tooling/code-assistant', 13)] = 110 (32.7 %)
  ```
  (script reproduit en annexe A ; il relit le frontmatter des 347 `.md` de `Dev/`.)
- **Portée** : 110 fiches Dev, plus les 3 fichiers `Comparatif - *.base` qui filtrent sur ces
  trois valeurs et affichent donc des tableaux inexploitables.
- **Cause** : `categorie:` est un champ unique à deux niveaux. Quand le sujet est fin
  (`ml/vision`) mais que la valeur n'existe pas, le rédacteur retombe sur la valeur générique
  du domaine. Rien n'oblige à créer la valeur fine, et créer la valeur fine oblige à
  recatégoriser l'existant — coût dissuasif à chaque lot.
- **Recommandation** : appliquer le vocabulaire d'annexe B. `ml/framework` se répartit en
  17 domaines, `llm/framework` en 10, `tooling/code-assistant` devient `llm/agent-de-code`.
  Après application, le domaine le plus peuplé fait **13 pages** et le top 3 tombe à **10,1 %**.
- **Effort** : **L**. Décomposé : réécriture de `Documentation/general/taxonomie.md` (M) ;
  table de migration `nom → (domaine, famille)` de 336 lignes + script d'application (M) ;
  reprise des 34 `.base` (M, cf. C7) ; passage des scripts (M, cf. C6).

### C2. `tooling/*` n'est pas un domaine mais 31 domaines — gravité : bloquant

- **Constat** : les 19 familles de `tooling/*` portent 86 fiches. Reclassées sur le sujet réel,
  elles se répartissent en **31 domaines** relevant de **11 préfixes de tête distincts**.
  `tooling/data` contient à lui seul des DataFrames (`numpy`, `pandas`, `Polars`, `Modin`,
  `xarray`), un générateur de données factices (`Faker`, `Mimesis`), un connecteur SQL
  (`connectorx`) et deux bibliothèques de traitement du signal (`PyWavelets`, `scipy.signal`).
- **Preuve** :
  ```
  tooling/* : 86 pages -> 31 domaines
  prefixes de tete issus de tooling/* : ['data', 'database', 'design', 'devtools', 'docs',
                                         'llm', 'math', 'media', 'signal', 'stats', 'web']
  ```
- **Portée** : 86 fiches, 19 valeurs de taxonomie, 1 MOC (`MOC/Categories/Outils & libs.md`,
  qui agrège aujourd'hui ces 86 pages sous un seul hub).
- **Cause** : la règle historique « un Outil porte `categorie: tooling/<famille>` » a fait de
  `tooling/` le préfixe par défaut de tout ce qui n'était pas une base, un modèle ou un pipeline.
  La taxonomie a ensuite dû assouplir sa propre règle (note en section *Outils Dev*) sans
  reprendre les pages déjà rangées.
- **Recommandation** : supprimer le préfixe `tooling/`. Créer `devtools/*` (12 pages : ce qui
  sert à **fabriquer** du logiciel), `stats/*` (10), `design/*` (7), `media/*` (4),
  `signal/*` (3), `docs/*` (2), `math/*` (1), `web/*` (6) ; renvoyer le reste vers les
  préfixes existants (`data`, `database`, `llm`).
- **Effort** : **M** une fois C1 engagé (même script de migration, même table). Isolément : M.

### C3. Treize comparatifs contournent déjà la taxonomie par les tags — gravité : sérieux

- **Constat** : sur 47 fichiers `Comparatif - *.base`, 33 filtrent sur `categorie ==`
  (36 lignes de filtre, deux fichiers en cumulant plusieurs) et **14 ne le peuvent pas**.
  Douze d'entre eux filtrent sur des `file.hasTag(...)`, un (`Comparatif - Frontends web
  légers.base`) code en dur une liste de cinq noms de fichiers, un dernier se rabat sur
  `categorie.startsWith("automation/")`. Les treize tags utilisés sont exactement les domaines
  qui manquent : `boosting`, `explainability`, `forecasting`, `nlp`, `signal-processing`,
  `package-manager`, `eda`, `text-to-sql`, `dimensionality-reduction`, `anomaly-detection`,
  `object-detection`, `segmentation`, `cli`.
- **Preuve** :
  ```
  $ ls Dev/Patterns/*.base | wc -l                             → 47
  $ grep -l "categorie ==" Dev/Patterns/*.base | wc -l          → 33
  $ grep -h "categorie ==" Dev/Patterns/*.base | wc -l          → 36
  $ for f in Dev/Patterns/*.base; do grep -q "categorie ==" "$f" || echo "$f"; done | wc -l  → 14

  Comparatif - Boosting.base            → file.hasTag("boosting")        3 pages, cat unique ml/framework
  Comparatif - Explicabilité.base       → file.hasTag("explainability")  7 pages, cat unique ml/framework
  Comparatif - Forecasting.base         → file.hasTag("forecasting")     6 pages, cat unique ml/framework
  Comparatif - Frontends web légers.base→ file.name == "FastAPI" or …    5 noms en dur
  …
  ```
- **Portée** : 14 fichiers `.base` sur 47, soit **30 % des comparatifs du vault**.
- **Cause** : un comparatif a besoin d'un groupe homogène. Quand `categorie:` ne le fournit
  pas, l'auteur du comparatif prend le premier champ qui marche — le tag. Le tag devient
  alors un second axe de rangement de fait, non déclaré et non contrôlé.
- **Recommandation** : c'est la validation empirique la plus forte du vocabulaire proposé.
  Onze de ces treize tags correspondent à un domaine unique en annexe B ; après migration,
  ces comparatifs redeviennent des filtres `domaine == "…"`. Reprendre les deux restants
  (`dimensionality-reduction` et `anomaly-detection` tombent tous deux dans
  `ml/non-supervise`) en filtre `domaine + tag`, et `Frontends web légers` en
  `famille == "paquet" and domaine in (web/backend, web/frontend, ui/data-app)`.
- **Effort** : **S** par fichier, **M** pour les 14. À faire dans la même passe que C7.

### C4. Six fiches documentent en corps de page leur propre erreur de rangement — gravité : sérieux

- **Constat** : six fiches ouvrent sur un « avertissement de rangement », une « note de
  rangement » ou une formule « faute de … » : `public-apis`, `osint4all`, `OpenCut`,
  `SmartTube`, `Superwhisper`, `t3code`. Le brief n'en relevait que deux.
- **Preuve** :
  ```
  $ grep -rl "vertissement de rangement\|ote de rangement\|faute de catégorie\|faute de type\|faute de case\|faute de mieux" Dev/*/*.md
  Dev/Outils/Superwhisper.md  Dev/Outils/t3code.md  Dev/Outils/public-apis.md
  Dev/Outils/osint4all.md     Dev/Outils/OpenCut.md Dev/Outils/SmartTube.md
  ```
  Extrait (`Dev/Outils/t3code.md:25`) : « la catégorie retenue est `tooling/code-assistant`
  faute de case "orchestration / supervision d'agents" : c'est le rangement le moins faux,
  pas le rangement juste. »
- **Portée** : 6 fiches sur 336 (1,8 %), **toutes** dans `Dev/Outils/` — soit 15 % des
  39 fiches de ce dossier, contre 0 sur les 297 fiches de `Dev/Services/`. Le rangement casse
  du côté des outils, pas des services.
- **Cause** : la taxonomie est fermée et `check_brain` la fait respecter (bien). Faute de
  pouvoir créer une valeur, le rédacteur range de travers puis s'en excuse dans le corps.
  Le corps de fiche sert de champ de débordement à la taxonomie.
- **Recommandation** : trois des six cas sont résolus par le modèle (`t3code` →
  `llm/agent-de-code` × `application` ; `public-apis` et `osint4all` → `famille: annuaire`).
  Trois relèvent du périmètre, pas de la taxonomie (cf. Questions ouvertes). Une fois rangées,
  ces six notes de bas de page doivent être supprimées du corps.
- **Effort** : **S** (6 fiches, à faire après C1).

### C5. `domaines:` est un champ mort côté Dev — gravité : sérieux

- **Constat** : 31 fiches Dev portent un `domaines:` renseigné, 8 le portent vide, 297 ne le
  portent pas (`check_brain` l'interdit sur `type: service`). Aucune des 39 ne produit de MOC :
  `build_mocs.py:131` ne retient que les pages `galaxie: wiki` dont la `categorie` commence par
  `concept/`. Le thème `infra-ops` est déclaré dans `themes.md`, posé sur 3 fiches Dev, et
  `MOC/Themes/` ne contient que 5 fichiers.
- **Preuve** :
  ```
  31 ('Dev','outil','champ present','non vide')
   8 ('Dev','outil','champ present','vide')    → draw.io, Mermaid, OpenCut, Penpot,
                                                  FossFLOW, Figma, Excalidraw, SmartTube
  297 ('Dev','service','absent','vide')
  $ ls MOC/Themes/ | wc -l
  5      # AI Engineering, Data Engineering, Data Science, ML Engineering, MLOps
  ```
- **Portée** : 39 fiches Dev, 1 vocabulaire (`themes.md`, 6 valeurs), 1 script.
- **Cause** : le champ a été conçu pour la galaxie Wiki puis étendu aux Outils par convention,
  sans que le script suive. Une convention non consommée par un script ne se corrige jamais.
- **Recommandation** : **retirer `domaines:` des gabarits Dev**, plutôt que l'alimenter.
  Argument : après C1, le préfixe de tête de `domaine:` porte déjà la thématique, et une table
  `domaine → thème` de 94 lignes dans `build_mocs.py` produit les MOC de thème par dérivation.
  Un champ dérivable est un champ qu'on n'a pas à décider à chaque fiche — c'est 336 arbitrages
  supprimés. Le maintenir à la main coûte un jugement par page pour une information qu'aucun
  consommateur ne lit et qu'aucun contrôle ne valide (`check_brain` ne vérifie pas ses valeurs).
- **Effort** : **S** pour le retrait des gabarits ; **M** pour la table de dérivation dans
  `build_mocs.py` et la génération des MOC de thème côté Dev.

### C6. `type:` ne décrit pas la nature, il décrit le dossier — gravité : sérieux

- **Constat** : croisé avec la famille réelle, `type:` n'est pas discriminant. 52 fiches
  relèvent des familles `application`, `cli` ou `extension` : 35 sont `type: outil`, 17 sont
  `type: service`. `Marimo` (notebook à interface, `type: service`) et `DBeaver` (client à
  interface, `type: outil`) ont la même nature et des types opposés. Symétriquement, 11 des
  13 fiches `saas` sont `type: service`.
- **Preuve** :
  ```
  croisement type x famille (336 fiches) :
     outil   x application  : 18      service x application  :  9
     outil   x cli          :  7      service x cli          :  7
     outil   x extension    : 10      service x extension    :  1
     outil   x saas         :  2      service x saas         : 11
     (service x paquet 181, service x plateforme 80, service x modele 4, service x specification 4)
  ```
- **Portée** : 52 fiches à type ambigu sur 336 (15,5 %). Aucun gabarit ne contrôle
  `type: outil` : `ALLOWED` (`check_brain.py:52`) ne couvre que `service` et `concept`.
- **Cause** : `type:` est posé par le dossier d'accueil (`Dev/Services/` vs `Dev/Outils/`),
  jamais par une question sur l'objet. Le dossier a été choisi avant que la nature soit établie.
- **Recommandation** : ne pas supprimer `type:` (il porte la distinction galaxie/gabarit), mais
  **cesser de lui faire porter la nature** : c'est le rôle de `famille:`. Corollaire immédiat et
  indépendant de C1 : ajouter un gabarit `outil` dans `check_brain.ALLOWED`, aujourd'hui absent.
- **Effort** : **S** pour le gabarit `outil` (≈ 15 lignes dans `check_brain.py`).
  **M** si l'on décide en plus de réaligner les 52 fiches sur leur dossier.

### C7. Le coût réel de migration est dans les 34 `.base`, pas dans les fiches — gravité : sérieux

- **Constat** : 266 des 336 fiches changent de valeur de rangement, et les 336 changent de
  forme de frontmatter. Mais les fiches sont migrables par script. Ce qui ne l'est pas :
  **34 fichiers `.base` référencent `categorie:` en dur** — 33 par `categorie == "<valeur>"`
  (36 lignes de filtre, deux fichiers en cumulant plusieurs) et 1 par
  `categorie.startsWith("automation/")`. Sept d'entre eux ne se renomment pas, ils se
  réécrivent, parce que leur catégorie source éclate en plusieurs domaines (`Comparatif - Outils stats`, `- Visualisation`, `- Calcul distribué`,
  `- Frameworks LLM`, `- Manipulation de données`, `- Clients d'API`, `- Reinforcement learning`).
- **Preuve** :
  ```
  $ grep -l "categorie ==" Dev/Patterns/*.base | wc -l          → 33
  $ grep -l "categorie.startsWith" Dev/Patterns/*.base | wc -l  → 1
  $ grep -rho "\[\[MOC/Categories/[^]|]*" Dev Wiki MOC AI Documentation | wc -l
  0        # aucun wikilink entrant vers les MOC de catégorie : les renommer ne casse rien
  ```
- **Portée** : 34 `.base` à reprendre (dont 7 à réécrire), 336 fiches à migrer, 3 MOC à
  supprimer (`Auth`, `Frameworks`, `Outils & libs`), 8 à créer, 12 régénérées — soit
  15 → 20 fichiers dans `MOC/Categories/`. **Zéro wikilink cassé** : `categorie:` est un champ
  de frontmatter, il n'apparaît dans aucun lien, et rien ne pointe vers les MOC de catégorie.
- **Cause** : les `.base` sont des requêtes figées sur un vocabulaire mouvant. Aucun script ne
  les valide (`check_brain` ne lit pas les `.base`).
- **Recommandation** : séquencer la bascule en quatre passes, dans cet ordre, avec
  `check_brain.py` vert entre chacune : (1) taxonomie + gabarits + `check_brain` acceptant
  **les deux** formes ; (2) migration scriptée des 336 fiches depuis la table d'annexe C ;
  (3) reprise des 34 `.base` et des 14 comparatifs sans filtre `categorie` (C3) ; (4) retrait de l'ancienne
  forme de `check_brain`, `build_index`, `build_mocs`, `query_index`.
- **Effort** : **L**. Fichiers impactés, comptés : 336 fiches Dev, 47 `.base` (34 à reprendre,
  13 à revalider),
  6 scripts Python (`check_brain`, `build_index`, `build_mocs`, `query_index`, `build_links`,
  `audit_mesures`), 4 scripts PowerShell (`audit-links`, `discover-links`, `find-connexes`,
  `gen-stubs-batch`), 3 gabarits (`Service-Dev.md`, `Concept-Wiki.md`, + `Outil-Dev.md` à créer),
  2 skills (`enrichir-brain`, `planifier-projet`), 2 documents de gouvernance
  (`taxonomie.md`, `tags.md`) — soit **400 fichiers**, dont 387 modifiables par script.

### C8. Trois écarts de définition entre le brief et le vault — gravité : mineur

- **Constat** : le socle de mesures est identique au brief, mais trois chiffres du brief se
  lisent autrement dans le vault. (a) « 337 fiches Dev » : `audit_mesures.py:221` compte les
  `type ∈ {service, outil}` **de tout le vault**, ce qui inclut `Wiki/Outils/Obsidian.md`.
  `Dev/` en contient **336**. (b) « 30 catégories à une seule page » : 29 dans `Dev/`, la
  trentième étant `skill/knowledge`, portée par cette même page Wiki. (c) « deux pages ouvrant
  sur un avertissement de rangement » : six (cf. C4).
- **Preuve** :
  ```
  $ python3 -c "…" ; # comptage restreint a Dev/
  fiches Dev (categorie non vide) : 336
  repartition type : Counter({'service': 297, 'outil': 39})
  anciennes categories a 1 page (Dev seul) : 29
  $ sed -n '218,222p' AI/scripts/audit_mesures.py
          if fm.get("type") not in ("service", "outil"):
              continue
          counts["fiches Dev"] += 1
  ```
- **Portée** : 1 ligne de `audit_mesures.py`, et tous les briefs qui citent « 337 ».
- **Cause** : le libellé « fiches Dev » désigne un type, pas un chemin. `Wiki/Outils/Obsidian.md`
  est un `type: outil` de `galaxie: wiki` — un cas légitime que le compteur ne distingue pas.
- **Recommandation** : renommer le compteur en « fiches à faits périssables » ou ajouter le
  filtre `galaxie == "dev"`. **Le vault fait foi : le périmètre de cet audit est 336 fiches.**
- **Effort** : **S** (1 ligne dans `audit_mesures.py`, lecture seule aujourd'hui — à corriger
  hors de cet audit).

### C9. Deux manques de vocabulaire, chiffrés — gravité : mineur

- **Constat** : (a) deux pages ne sont pas des logiciels mais des annuaires de liens
  (`public-apis`, `osint4all`) — 0,6 % du vault ; (b) deux pages sont sous dédicace au domaine
  public (`osint4all` en CC0-1.0, `FossFLOW` sous Unlicense) et déclarent toutes deux
  `licence_type: open-source`, l'énumération `VALUE_ENUMS` (`check_brain.py:54`) ne proposant
  rien d'autre.
- **Preuve** :
  ```
  $ grep -rn "CC0" Dev/ | head -1
  Dev/Outils/osint4all.md:6:pitch: "Annuaire de liens OSINT (CC0, …)"
  $ grep -m1 '^licence_type:' Dev/Outils/osint4all.md Dev/Outils/FossFLOW.md
  Dev/Outils/osint4all.md:licence_type: open-source
  Dev/Outils/FossFLOW.md:licence_type: open-source
  ```
- **Portée** : 4 fiches, 2 valeurs d'énumération.
- **Cause** : les deux énumérations ont été fixées sur les cas les plus fréquents et jamais
  rouvertes ; le contrôle dur (bien) a rendu le contournement plus simple que l'ajout.
- **Recommandation** : (a) **ne pas créer de `type: ressource`** pour deux pages — la
  famille `annuaire` d'annexe B suffit et se pose au bon endroit (la nature, pas la galaxie) ;
  (b) ajouter `public-domain` à `VALUE_ENUMS["licence_type"]`.
- **Effort** : **S** (1 ligne d'énumération + 2 fiches à corriger, hors audit).

## Ce qui va bien

- **Le contrôle dur tient.** `uv run AI/scripts/check_brain.py` renvoie « 647 pages actives
  contrôlées / OK — aucune violation dure ». Zéro catégorie hors taxonomie : la fermeture du
  vocabulaire fonctionne, et c'est précisément ce qui a rendu les six notes de rangement (C4)
  visibles au lieu de les laisser se disperser en valeurs inventées. Ne pas relâcher cette règle.
- **Le rangement n'est pas dans les liens.** `categorie:` ne figure dans aucun wikilink, et
  aucune page ne pointe vers `MOC/Categories/*` (0 occurrence). Une migration de taxonomie ne
  peut donc pas casser la navigation par liens — ce qui rend C7 lourd mais non risqué.
- **Les gabarits sont tenus là où ils existent.** Les six types du vault présentent chacun
  « aucun champ à géométrie variable » au socle de mesures : la dérive constatée est
  taxonomique, pas structurelle. Les 297 fiches `service` portent le même jeu de champs.
- **Les domaines fins existent déjà, en tags.** Le vocabulaire de 321 tags est intégralement
  employé (0 tag déclaré non utilisé). Le nouvel axe `domaine:` ne s'invente pas : il reprend
  un découpage que le vault applique déjà, ailleurs.
- **Une bonne part de la taxonomie n'a pas besoin d'être touchée.** 70 fiches gardent la même
  valeur de domaine, et la moitié des sous-domaines `database/*`, `data/*`, `ml/serving`,
  `ml/tracking`, `llm/eval`, `llm/finetuning` se renomment sans se redécouper. Les frontières
  déjà écrites en prose dans `taxonomie.md` (`compute/sandbox`, `tooling/document`,
  `network/*`, `llm/framework-module`) sont réutilisables telles quelles.

## Questions laissées ouvertes

1. **Quatre pages sont hors du périmètre déclaré du brain**, et l'arbre ne peut pas trancher
   cela : `OpenCut`, `SmartTube` (média grand public), `Superwhisper` (dictée généraliste),
   `public-apis` (annuaire multi-domaines). `SmartTube` l'écrit lui-même : « cette page est ici
   par utilité domestique, pas par cohérence ». Trois options : les garder dans `Dev/` avec un
   domaine `media/*` assumé, les déplacer vers `Wiki/Outils/`, ou les sortir. Arbitrage du
   propriétaire, pas de l'auditeur.
2. **`famille:` doit-elle être contrôlée par `check_brain` ou laissée indicative ?** Contrôlée,
   elle impose de trancher les cas frontière (C6, 52 fiches). Indicative, elle dérivera comme
   `domaines:` (C5).
3. **Faut-il générer des `MOC/Familles/` ?** L'axe famille rend possible un hub « tous les
   clients graphiques », « tous les modèles pré-entraînés ». Utile pour l'humain, sans valeur
   pour l'agent, qui filtre l'index.
4. **Le seuil de création d'un domaine.** Le modèle laisse 22 domaines à une seule page.
   Aucun n'est isolé sur les deux axes, donc aucun n'est orphelin — mais faut-il une règle
   « pas de domaine sous N pages » ? Elle ferait renaître les fourre-fout de C1.
5. **La galaxie `Wiki/`** garde ses 12 `concept/<sous-domaine>` inchangés. Faut-il aligner le
   vocabulaire des concepts sur celui des domaines Dev, ou assumer deux vocabulaires ?
   Hors périmètre de cet axe.

---

## Annexe A — L'arbre de décision et son test à blanc

### A.1 Principe

Deux passes indépendantes, chacune une **suite ordonnée de questions fermées, premier oui
gagne**. Aucune question n'appelle un jugement de valeur ; toutes portent sur un fait
vérifiable dans le dépôt amont.

### A.2 Passe 1 — `famille:` (9 valeurs, ordre strict)

| # | Question fermée | Si oui |
|---|-----------------|--------|
| F1 | La page décrit-elle une liste de ressources externes plutôt qu'un logiciel ? | `annuaire` |
| F2 | Est-ce une norme, un format ou un protocole, sans implémentation de référence unique ? | `specification` |
| F3 | Le livrable téléchargé est-il un jeu de poids entraînés ? | `modele` |
| F4 | Faut-il un logiciel hôte tiers (IDE, navigateur, agent, SGBD) pour l'exécuter ? | `extension` |
| F5 | L'auto-hébergement est-il impossible (compte chez un tiers obligatoire) ? | `saas` |
| F6 | Un autre **programme**, et pas seulement un humain, en est-il le consommateur nominal (port, API réseau) ? | `plateforme` |
| F7 | Le point d'entrée nominal est-il une interface graphique ? | `application` |
| F8 | S'invoque-t-il en commande shell sans être importé dans du code ? | `cli` |
| F9 | Aucun des précédents | `paquet` |

### A.3 Passe 2 — `domaine:` (branche de tête, ordre strict)

| # | Question fermée | Si oui |
|---|-----------------|--------|
| D1 | L'objet a-t-il besoin d'un **grand modèle de langage** pour fonctionner ? | `llm/*` |
| D2 | Entraîne-t-il, sert-il, suit-il ou explique-t-il un **modèle d'apprentissage** ? | `ml/*` |
| D3 | **Stocke et interroge**-t-il des données de façon persistante ? | `database/*` |
| D4 | **Déplace ou transforme**-t-il des données destinées à une **machine** ? | `data/*` |
| D5 | Calcule-t-il des statistiques, du signal ou de l'optimisation mathématique ? | `stats/*`, `signal/*`, `math/*` |
| D6 | Fournit-il de la **capacité de calcul** ? | `compute/*` ou `storage/*` |
| D7 | Sert-il à **exposer une application** à des utilisateurs ? | `web/*`, `ui/*` |
| D8 | Porte-t-il sur **ce qui circule entre machines** ? | `network/*` |
| D9 | Porte-t-il sur la **sécurité** ou le renseignement ? | `security/*` |
| D10 | Sert-il à **déployer ou surveiller** du logiciel en production ? | `devops/*`, `observability/*` |
| D11 | Sert-il à **fabriquer** du logiciel (écrire, tester, configurer, packager) ? | `devtools/*` |
| D12 | Produit-il un document, un média ou un dessin pour un **humain** ? | `docs/*`, `media/*`, `design/*` |
| D13 | Connecte-t-il des applications **sans code** ? | `automation/*` |
| D14 | Aucun des précédents | **arrêt — demander avant d'inventer** |

Le sous-domaine se lit ensuite dans la table d'annexe B, à l'intérieur de la branche retenue.

### A.4 Six règles de départage (à inscrire dans la taxonomie)

Sans elles, l'arbre laisse 35 fiches en suspens. Avec elles, 10.

| # | Règle | Résout |
|---|-------|--------|
| R1 | Si le code est publié et déployable, la famille est `plateforme`, jamais `saas`, même si l'éditeur pousse son offre managée. | Comet, Neptune, Weights & Biases, LangSmith, E2B |
| R2 | Un moteur exécutable en embarqué **et** en serveur est `paquet` si l'installation par défaut ne lance aucun processus. | DuckDB, SQLite, Chroma, LanceDB |
| R3 | La famille suit le **point d'entrée documenté en premier** dans le README amont. | Uvicorn (`cli`), Ray (`paquet`), pi (`cli`), Mermaid (`extension`), LM Studio (`application`), TensorRT (`paquet`), Web-Check (`application`) |
| R4 | `specification` seulement si la page ne documente **aucune** implémentation de référence. | Gymnasium → `paquet` ; ADBC, Parquet, Avro, Iceberg → `specification` |
| R5 | Le tri D1/D2 se fait sur ce dont l'objet **a besoin pour tourner**, pas sur ce à quoi il ressemble. | TransformerLens, SAELens, nnsight, interpreto, sentence-transformers → `ml/*` |
| R6 | `data/*` = sortie destinée à une **machine** ; `docs/*` = sortie destinée à un **humain**. | Stirling PDF → `docs/pdf` ; docTR, PyMuPDF → `data/parsing` |

### A.5 Résultat du test à blanc sur les 336 fiches Dev

```
fiches Dev                : 336
rangees par l'arbre       : 326  (97.0 %)
litigieuses (residu)      :  10  ( 3.0 %)
hors arbre (aucun chemin) :   0

domaine : 94 valeurs, plus gros bucket 13 pages (avant : 74 valeurs cote Dev, 64 pages)
famille :  9 valeurs, aucun singleton
concentration top3 domaines : 34 = 10.1 %  (avant : 110 = 32.7 %)
domaines a 1 page : 22        pages isolees sur LES DEUX axes : 0
```

Le seuil de 95 % est franchi. Les 10 fiches litigieuses et leur motif :

| Fiche | Arbitrage manquant |
|-------|--------------------|
| `public-apis` | annuaire multi-domaines : aucun domaine unique ne s'applique |
| `OpenCut`, `SmartTube` | hors des cinq domaines de prédilection déclarés |
| `Superwhisper` | `media/ingestion` ou hors périmètre |
| `Marqo` | `database/recherche` ou `database/vecteur` |
| `txtai` | `database/recherche` ou `llm/rag` |
| `Ray Tune` | `ml/hyperopt` ou `compute/distribue` |
| `connectorx` | `data/ingestion` ou `database/driver` |
| `bm25s`, `rank-bm25` | `database/recherche` ou `ml/nlp` (classement lexical) |

Quatre relèvent du périmètre (question ouverte 1), six d'une frontière à écrire en une phrase
dans la taxonomie. Aucun n'est un défaut de structure du modèle.

### A.6 Test sur 10 fiches récentes

Les 10 fiches du lot du 2026-09-02 nommées dans l'entrée 3 de `AI/ameliorations-devbrain.md`.

| Fiche | `categorie:` actuelle | Chemin dans l'arbre | Résultat |
|-------|----------------------|---------------------|----------|
| OpenRouter | `llm/framework` | D1 oui → passerelle ; F5 oui | `llm/passerelle` × `saas` |
| LiteLLM | `llm/framework` | D1 oui ; F5 non, F6 oui | `llm/passerelle` × `plateforme` |
| OmniRoute | `llm/framework` | D1 oui ; F6 oui | `llm/passerelle` × `plateforme` |
| CrewAI | `llm/framework` | D1 oui → agents ; F9 | `llm/agents` × `paquet` |
| AutoGen | `llm/framework` | D1 oui → agents ; F9 | `llm/agents` × `paquet` |
| Sniffnet | `network/analysis` | D8 oui ; F7 oui | `network/analyse` × `application` |
| croc | `network/transfer` | D8 oui ; F8 oui | `network/transfert` × `cli` |
| osint4all | `security/osint` | D9 oui ; **F1 oui** | `security/recon` × `annuaire` |
| OpenCut | `tooling/video` | D12 oui ; F7 oui | `media/video` × `application` — **litigieux (périmètre)** |
| SmartTube | `tooling/video` | D12 oui ; F7 oui | `media/video` × `application` — **litigieux (périmètre)** |

8 sur 10 sans arbitrage. Les deux litigieux le sont pour une raison que la taxonomie ne peut
pas résoudre : ces pages sont hors sujet, pas mal rangées. Le `llm/gateway` que l'entrée 3
disait « manifestement manquant » apparaît ici sans décision ad hoc, par le seul jeu de D1.

### A.7 Test sur 3 cas pénibles

**Cas 1 — un annuaire : `public-apis`.**
F1 : « la page décrit-elle une liste de ressources externes plutôt qu'un logiciel ? » → oui →
`famille: annuaire`. La nature est tranchée dès la première question, sans inventer de
`type: ressource`. Le domaine, lui, n'est pas tranché : un annuaire de 1 400 API publiques
n'a pas de domaine. **Verdict : l'arbre range la nature, pas le sujet. Reste litigieux.**
Enseignement : `famille: annuaire` doit dispenser du domaine, ou imposer un
`domaine: <celui du sujet listé>` explicite. À écrire dans la taxonomie.

**Cas 2 — un outil hors data : `SmartTube` (client YouTube pour téléviseur).**
D1 non, D2 non, D3 non, D4 non, D5 non, D6 non, D7 non, D8 non, D9 non, D10 non, D11 non,
D12 oui (média pour un humain) → `media/video`. F1-F6 non, F7 oui → `application`.
**L'arbre le range en 13 questions sans jugement.** Il ne dit pas si la page a sa place dans
`Dev/` — ce n'est pas son rôle. C'est exactement ce que la fiche demande aujourd'hui à un
paragraphe d'avertissement en corps de page.

**Cas 3 — une brique à la frontière de deux domaines : `WrenAI` (text-to-SQL gouverné).**
Le candidat classique au litige : c'est autant du LLM que de la base de données. D1 : « a-t-il
besoin d'un grand modèle de langage pour fonctionner ? » → oui, sans LLM WrenAI ne produit
aucun SQL → `llm/*`, branche close. Sous-domaine `llm/text-to-sql`. F5 non (auto-hébergeable,
R1), F6 oui (une application appelle son API) → `plateforme`.
**Tranché par l'ordre des questions, pas par un arbitrage.** L'ordre D1 avant D3 est la seule
décision de conception ; elle est prise une fois, écrite, et vaut pour toutes les fiches.
Le même mécanisme range `Vanna` (`paquet`), `DB-GPT` (`plateforme`) et les deux ex-
`llm/framework-module`, qui perdent au passage une catégorie inventée pour une nature.

---

## Annexe B — Vocabulaire proposé

### B.1 Axe `famille:` — 9 valeurs fermées

| Famille | Définition | Frontière | Pages |
|---------|-----------|-----------|-------|
| `paquet` | S'installe dans un projet et s'importe dans du code. | Distinct de `cli` : le point d'entrée est un `import`, pas une commande. | 181 |
| `plateforme` | Se déploie et tourne en processus qu'un autre **programme** appelle. | Distinct de `application` : le consommateur nominal n'est pas un humain. Distinct de `saas` : auto-hébergeable (R1). | 80 |
| `application` | S'utilise par une interface faite pour un humain. | Distinct de `plateforme` : aucune API n'est le point d'entrée. | 27 |
| `cli` | S'invoque en commande shell sans être importé. | Distinct de `paquet` par le point d'entrée documenté en premier (R3). | 14 |
| `saas` | Compte chez un tiers obligatoire, aucun auto-hébergement. | Distinct de `plateforme` : le code n'est pas déployable (R1). | 13 |
| `extension` | Ne s'exécute qu'à l'intérieur d'un hôte tiers. | Distinct de `paquet` : l'hôte est un logiciel, pas un projet (IDE, navigateur, agent, SGBD). | 11 |
| `specification` | Norme, format ou protocole sans implémentation de référence. | Distinct de `paquet` : plusieurs implémentations, aucune canonique (R4). | 4 |
| `modele` | Le livrable est un jeu de poids entraînés. | Distinct de `paquet` : on charge des poids, on n'écrit pas d'algorithme. | 4 |
| `annuaire` | Liste de ressources externes, pas un logiciel. | Distinct de tout le reste : rien ne s'installe, rien ne se déploie, pas de version. | 2 |

Aucune famille n'est à une seule page. `type:` reste, mais cesse de porter la nature (C6).

### B.2 Axe `domaine:` — 94 valeurs, 20 préfixes de tête

| Préfixe | Pages | Sous-domaines |
|---------|-------|---------------|
| `ml/*` | 85 | `apprentissage-profond`(8) `vision`(9) `interpretabilite`(7) `series-temporelles`(7) `tracking`(7) `rl`(6) `tabulaire`(6) `nlp`(6) `serving`(9) `non-supervise`(4) `hyperopt`(3) `orchestration`(3) `socle`(2) `eval`(2) `hub`(2) `embeddings`(1) `feature-store`(1) `graphe`(1) `monitoring`(1) |
| `llm/*` | 74 | `agent-de-code`(13) `agents`(9) `runtime`(9) `text-to-sql`(5) `assistant`(5) `finetuning`(5) `eval`(4) `observabilite`(4) `passerelle`(3) `rag`(3) `sortie-structuree`(3) `low-code`(3) `memoire`(3) `mcp`(2) `socle`(2) `outillage`(1) |
| `database/*` | 47 | `vecteur`(11) `admin`(7) `recherche`(6) `relationnel`(6) `orm`(3) `migration`(3) `analytique`(2) `cle-valeur`(2) `driver`(2) `graphe`(2) `series-temporelles`(2) `document`(1) |
| `data/*` | 46 | `scraping`(10) `parsing`(9) `orchestration`(6) `tableau`(5) `viz`(5) `eda`(3) `format`(3) `synthetique`(3) `ingestion`(1) `streaming`(1) |
| `devtools/*` | 19 | `notebook`(5) `config`(4) `cli`(2) `client-api`(2) `paquet`(2) `test`(2) `qualite`(1) `validation`(1) |
| `stats/*` | 10 | `inference`(4) `bayesien`(3) `exploratoire`(2) `causal`(1) |
| `compute/*` | 7 | `a-la-demande`(3) `distribue`(3) `gpu`(1) |
| `design/*` | 7 | `diagramme`(5) `ui`(2) |
| `storage/*` | 6 | `objet`(6) |
| `web/*` | 6 | `backend`(3) `frontend`(2) `api`(1) |
| `automation/*` | 5 | `no-code`(5) |
| `media/*` | 4 | `ingestion`(2) `video`(2) |
| `ui/*` | 4 | `data-app`(4) |
| `observability/*` | 3 | `supervision`(3) |
| `security/*` | 3 | `recon`(2) `auth`(1) |
| `signal/*` | 3 | `traitement`(2) `audio`(1) |
| `devops/*` | 2 | `ci`(1) `conteneur`(1) |
| `docs/*` | 2 | `capture`(1) `pdf`(1) |
| `math/*` | 1 | `optimisation`(1) |

Frontières les plus disputées, à écrire dans la taxonomie :
- `ml/socle` (généraliste, toutes tâches) **distinct de** `ml/tabulaire` (spécialisé données
  en colonnes) parce que scikit-learn ne suppose rien du type de données, XGBoost si.
- `llm/socle` (LangChain, DSPy : on assemble) **distinct de** `llm/agents` (on orchestre une
  boucle d'outils) et de `llm/rag` (on indexe et on récupère).
- `llm/runtime` (servir le modèle) **distinct de** `llm/passerelle` (router vers des
  fournisseurs) et de `llm/outillage` (décider quel modèle, sans le servir).
- `data/*` (sortie machine) **distinct de** `docs/*` (sortie humaine) — règle R6.
- `devtools/*` (fabriquer du logiciel) **distinct de** `devops/*` (le déployer) et de
  `observability/*` (le surveiller une fois déployé).
- `design/diagramme` (schémas techniques) **distinct de** `design/ui` (interfaces produit) et
  de `data/viz` (graphiques de données) — frontière déjà écrite aujourd'hui, conservée.

---

## Annexe C — Correspondance `ancienne categorie → nouveau couple`

Les **74** catégories effectivement portées par une fiche de `Dev/`. Les 12 restantes des 86
du socle sont portées par `Wiki/` (11 `concept/*` + `skill/knowledge`) et ne sont pas touchées
par cette migration ; l'intersection Dev/Wiki est vide. Ordre alphabétique. Une ligne à
plusieurs entrées signale une catégorie qui éclate.

```
$ python3 -c "…categories distinctes par galaxie…"
categories distinctes portees par Dev/  : 74
categories distinctes portees par Wiki/ : 12
union : 86     intersection : []
```

| Ancienne `categorie:` | Pages | Nouveaux couples `domaine` × `famille` |
|---|---|---|
| `auth` | 1 | `security/auth` × `paquet` (1) |
| `automation/ai-agent` | 1 | `automation/no-code` × `saas` (1) |
| `automation/ipaas` | 1 | `automation/no-code` × `saas` (1) |
| `automation/workflow` | 3 | `automation/no-code` × `plateforme` (3) |
| `compute/distributed` | 4 | `compute/distribue` × `paquet` (2), `compute/distribue` × `plateforme` (1), `compute/gpu` × `paquet` (1) |
| `compute/sandbox` | 2 | `compute/a-la-demande` × `saas` (1), `compute/a-la-demande` × `plateforme` (1) |
| `compute/serverless` | 1 | `compute/a-la-demande` × `saas` (1) |
| `data/format` | 2 | `data/format` × `specification` (2) |
| `data/lakehouse` | 1 | `data/format` × `specification` (1) |
| `data/orchestration` | 6 | `data/orchestration` × `plateforme` (6) |
| `data/parsing` | 8 | `data/parsing` × `paquet` (7), `data/parsing` × `saas` (1) |
| `data/scraping` | 10 | `data/scraping` × `paquet` (8), `data/scraping` × `plateforme` (1), `data/scraping` × `application` (1) |
| `data/streaming` | 1 | `data/streaming` × `plateforme` (1) |
| `database/columnar` | 2 | `database/analytique` × `paquet` (1), `database/analytique` × `plateforme` (1) |
| `database/document` | 1 | `database/document` × `plateforme` (1) |
| `database/driver` | 2 | `database/driver` × `paquet` (1), `database/driver` × `specification` (1) |
| `database/graph` | 2 | `database/graphe` × `plateforme` (2) |
| `database/keyvalue` | 1 | `database/cle-valeur` × `plateforme` (1) |
| `database/relational` | 6 | `database/relationnel` × `plateforme` (5), `database/relationnel` × `paquet` (1) |
| `database/search` | 4 | `database/recherche` × `plateforme` (3), `database/recherche` × `paquet` (1) |
| `database/timeseries` | 2 | `database/series-temporelles` × `plateforme` (2) |
| `database/vector` | 11 | `database/vecteur` × `paquet` (6), `database/vecteur` × `plateforme` (3), `database/vecteur` × `saas` (1), `database/vecteur` × `extension` (1) |
| `database/wide-column` | 1 | `database/cle-valeur` × `plateforme` (1) |
| `devops/ci` | 1 | `devops/ci` × `saas` (1) |
| `devops/container` | 1 | `devops/conteneur` × `plateforme` (1) |
| `framework/backend` | 3 | `web/backend` × `paquet` (2), `web/backend` × `cli` (1) |
| `framework/frontend` | 2 | `web/frontend` × `paquet` (2) |
| `framework/orm` | 3 | `database/orm` × `paquet` (3) |
| `llm/app` | 1 | `llm/assistant` × `plateforme` (1) |
| `llm/context` | 1 | `llm/memoire` × `paquet` (1) |
| `llm/eval` | 4 | `llm/eval` × `paquet` (4) |
| `llm/finetuning` | 5 | `llm/finetuning` × `paquet` (5) |
| `llm/framework` | 33 | `llm/agents` × `paquet` (9), `llm/sortie-structuree` × `paquet` (3), `llm/rag` × `paquet` (3), `llm/low-code` × `plateforme` (3), `llm/assistant` × `plateforme` (3), `llm/memoire` × `plateforme` (2), `llm/socle` × `paquet` (2), `llm/text-to-sql` × `plateforme` (2), `llm/passerelle` × `plateforme` (2), `llm/text-to-sql` × `paquet` (1), `llm/mcp` × `paquet` (1), `llm/assistant` × `application` (1), `llm/passerelle` × `saas` (1) |
| `llm/framework-module` | 2 | `llm/text-to-sql` × `paquet` (2) |
| `llm/local` | 9 | `llm/runtime` × `plateforme` (6), `llm/runtime` × `application` (2), `llm/runtime` × `paquet` (1) |
| `llm/observability` | 4 | `llm/observabilite` × `plateforme` (4) |
| `ml/eval` | 2 | `ml/eval` × `paquet` (2) |
| `ml/feature-store` | 1 | `ml/feature-store` × `plateforme` (1) |
| `ml/framework` | 64 | `ml/vision` × `paquet` (7), `ml/interpretabilite` × `paquet` (7), `ml/apprentissage-profond` × `paquet` (7), `ml/series-temporelles` × `paquet` (6), `ml/rl` × `paquet` (6), `ml/tabulaire` × `paquet` (6), `ml/nlp` × `paquet` (5), `ml/non-supervise` × `paquet` (4), `ml/socle` × `paquet` (2), `database/recherche` × `paquet` (2), `ml/vision` × `modele` (2), `stats/inference` × `paquet` (1), `signal/audio` × `paquet` (1), `data/parsing` × `paquet` (1), `ml/series-temporelles` × `modele` (1), `data/synthetique` × `paquet` (1), `ml/hub` × `saas` (1), `ml/graphe` × `paquet` (1), `ml/nlp` × `modele` (1), `ml/embeddings` × `paquet` (1), `ml/hub` × `paquet` (1) |
| `ml/hyperopt` | 3 | `ml/hyperopt` × `paquet` (3) |
| `ml/monitoring` | 1 | `ml/monitoring` × `paquet` (1) |
| `ml/orchestration` | 3 | `ml/orchestration` × `plateforme` (3) |
| `ml/serving` | 9 | `ml/serving` × `plateforme` (7), `ml/serving` × `paquet` (2) |
| `ml/tracking` | 7 | `ml/tracking` × `plateforme` (6), `ml/tracking` × `application` (1) |
| `ml/training` | 1 | `ml/apprentissage-profond` × `paquet` (1) |
| `network/analysis` | 1 | `network/analyse` × `application` (1) |
| `network/transfer` | 1 | `network/transfert` × `cli` (1) |
| `observability/infra` | 1 | `observability/supervision` × `plateforme` (1) |
| `observability/log` | 1 | `observability/supervision` × `plateforme` (1) |
| `observability/metric` | 1 | `observability/supervision` × `application` (1) |
| `security/osint` | 1 | `security/recon` × `annuaire` (1) |
| `security/recon` | 1 | `security/recon` × `application` (1) |
| `storage` | 6 | `storage/objet` × `plateforme` (4), `storage/objet` × `saas` (2) |
| `tooling/api` | 3 | `devtools/client-api` × `application` (1), `devtools/client-api` × `saas` (1), `web/api` × `annuaire` (1) |
| `tooling/capture` | 1 | `docs/capture` × `extension` (1) |
| `tooling/code-assistant` | 13 | `llm/agent-de-code` × `extension` (6), `llm/agent-de-code` × `cli` (5), `llm/agent-de-code` × `application` (2) |
| `tooling/data` | 10 | `data/tableau` × `paquet` (5), `data/synthetique` × `paquet` (2), `signal/traitement` × `paquet` (2), `data/ingestion` × `paquet` (1) |
| `tooling/db-admin` | 7 | `database/admin` × `application` (7) |
| `tooling/design` | 2 | `design/ui` × `application` (1), `design/ui` × `saas` (1) |
| `tooling/diagram` | 5 | `design/diagramme` × `application` (3), `design/diagramme` × `extension` (2) |
| `tooling/document` | 1 | `docs/pdf` × `plateforme` (1) |
| `tooling/lint` | 1 | `devtools/qualite` × `cli` (1) |
| `tooling/llm` | 1 | `llm/outillage` × `cli` (1) |
| `tooling/media` | 2 | `media/ingestion` × `application` (1), `media/ingestion` × `extension` (1) |
| `tooling/migration` | 3 | `database/migration` × `cli` (2), `database/migration` × `paquet` (1) |
| `tooling/notebook` | 5 | `devtools/notebook` × `paquet` (3), `devtools/notebook` × `cli` (1), `devtools/notebook` × `application` (1) |
| `tooling/optim` | 1 | `math/optimisation` × `paquet` (1) |
| `tooling/package` | 9 | `devtools/config` × `paquet` (4), `devtools/cli` × `paquet` (2), `devtools/paquet` × `cli` (2), `devtools/validation` × `paquet` (1) |
| `tooling/stats` | 9 | `stats/inference` × `paquet` (3), `stats/bayesien` × `paquet` (3), `stats/exploratoire` × `paquet` (2), `stats/causal` × `paquet` (1) |
| `tooling/test` | 3 | `devtools/test` × `paquet` (2), `llm/mcp` × `application` (1) |
| `tooling/video` | 2 | `media/video` × `application` (2) |
| `tooling/viz` | 8 | `data/viz` × `paquet` (5), `data/eda` × `paquet` (3) |
| `ui/data-app` | 3 | `ui/data-app` × `paquet` (3) |
| `ui/ml-demo` | 1 | `ui/data-app` × `paquet` (1) |

Les 26 catégories déclarées et jamais portées (socle §1) disparaissent sans reprise. Neuf
d'entre elles réapparaissent sous un autre nom dans le vocabulaire proposé (`data/ingestion`,
`data/quality`, `data/transformation`, `data/versioning`, `llm/embeddings`, `ml/annotation`,
`observability/trace`, `tooling/build`, `tooling/format`) ; les 17 autres sont à ne pas
recréer tant qu'aucune fiche ne les demande.
