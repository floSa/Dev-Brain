---
role: meta
nom: remontees-lot-10-llm-domaine
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 10 : « LLM & IA générative », niveau domaine

Périmètre : les **11** fiches `role: brique` posées directement dans
« LLM & IA générative/ », sans sous-dossier — DSPy, Dify, Flowise, Headroom, LangChain,
Langflow, Letta, OpenViking, fastmcp, llmfit, mcpjam. Branche
`claude/lot-10-llm-domaine-f58fec`.

Compte annoncé par la table du pilote : 11. Compte trouvé : 11. Aucune fiche voisine
touchée, aucun hub, aucune notion, aucun comparatif, aucun fichier partagé.

## 1. `build_bandeau.py` ne se lance PAS sur le dossier, ici — il se lance fichier par fichier

C'est le piège propre aux trois lots « niveau domaine » (1, 10 et 13), et il n'est écrit
nulle part. Le scope du script est un **chemin**, et un chemin de dossier est traité en
`rglob("*.md")` : passer `"LLM & IA générative"` aurait réécrit les 132 pages des douze
sous-dossiers — celles des lots 7, 8 et 9, en train de tourner en parallèle. C'est
exactement le conflit que la règle 1 interdit, et le script ne peut pas le voir : le dossier
donné est bien dans le vault, il existe, il n'est pas de l'outillage. Rien ne refuse.

Ce lot a donc passé les **onze chemins de fichier**, jamais le dossier :

```bash
uv run AI/scripts/build_bandeau.py "LLM & IA générative/DSPy.md" "LLM & IA générative/Dify.md" ...
```

> À faire tenir aux lots 1 et 13, qui ont la même topologie : un lot « niveau domaine »
> énumère ses fichiers. Un lot « sous-dossier » peut passer son dossier sans risque.

## 2. Deux fiches sur onze sont membres d'un comparatif — et cinq en citaient un à tort

Relevé par `mesure_membres_bases.py`, recoupé à la main sur le bloc `filters:` de
`Comparatif - Frameworks LLM.base` et confirmé une troisième fois par les `R8a` de
`check_brain` :

| Catégorie | Fiches du périmètre | Comparatif d'accueil |
|---|---|---|
| `llm/socle` | DSPy, LangChain | **`Comparatif - Frameworks LLM`** — membres |
| `llm/low-code` | Dify, Flowise, Langflow | aucun (`R8a` le signale) |
| `llm/memoire` | Headroom, Letta, OpenViking | aucun (`R8a` le signale) |
| `llm/protocole` | fastmcp, mcpjam | aucun |
| `llm/outillage` | llmfit | aucun |

Le filtre de la vue est `role == "brique"` **et** `categorie ∈ {llm/socle, llm/agents,
llm/rag, llm/sortie-structuree}`. Neuf fiches sur onze en sont dehors par construction.

**Cinq d'entre elles portaient pourtant la puce
`[[Comparatif - Frameworks LLM]] — comparatif de la catégorie`** : Dify, Flowise, Langflow,
Letta, OpenViking. C'est faux au sens strict — aucune n'apparaît dans la vue, un lecteur qui
suit le lien ne les y trouve pas. **La puce est retirée des cinq.** C'est le seul lien
supprimé du lot ; tous les autres wikilinks des onze fiches sont conservés (mesuré par diff
des `[[…]]` contre `d8f81d6` : zéro perte ailleurs, et onze gains — le hub du domaine, plus
`[[Prompt engineering]]` sur DSPy).

> Hypothèse sur l'origine : la formule « comparatif de la catégorie » date d'avant
> l'éclatement de `llm/framework` en treize domaines (lot 4). Les fiches ont changé de
> catégorie, la puce est restée. **À vérifier ailleurs dans le vault** — le motif est
> mécanique, `grep -l "comparatif de la catégorie"` croisé au relevé des membres.

## 3. Application de la règle 2 : 48 lignes `Écarter si`, 7 redirections parties au comparatif

Le crible est celui du 2026-09-06 : la puce part au comparatif **seulement si la brique ET
la cible** sont membres de la même vue.

- **DSPy** et **LangChain** sont membres. Leurs sept redirections visent LangChain,
  LlamaIndex, Haystack, DSPy et LangGraph — **toutes membres**. Elles partent donc au
  comparatif, qui les porte déjà, mot pour mot, dans sa section « Ce qui départage ».
  Vérifié en lisant la page, pas supposé. Ne restent en `Écarter si` que des bornes dures :
  métrique absente et budget de compilation (DSPy), surface d'API mouvante et abstractions
  opaques (LangChain).
- **Les neuf autres** tombent dans le cas 1 de la règle — leur catégorie n'a aucun
  comparatif. Leurs **23** redirections restent en `Écarter si` avec leur wikilink :
  aucun comparatif ne peut les porter, les écarter les supprimerait.

## 4. Le recouvrement « une cible dans deux sections » est STRUCTUREL, pas accidentel

Le critère cède sur **cinq fiches**, et il faut voir pourquoi : quand une catégorie n'a pas
de comparatif, les cibles de `alternatives:` **sont** les cibles des redirections. La règle 2
les maintient en `Écarter si` ; R11 — violation **dure** — exige qu'elles figurent en
`### Alternatives`. Les deux sections doivent donc les porter toutes les deux.

| Fiche | Cible présente dans les deux sections |
|---|---|
| Dify | [[Flowise]], [[Langflow]] |
| Flowise | [[Dify]], [[Langflow]] |
| Langflow | [[Dify]] |
| Letta | [[Agno]], [[CrewAI]], [[smolagents]] |
| OpenViking | [[Letta]] |

Ce n'est pas un défaut de conversion qu'un lot ultérieur pourrait nettoyer : c'est la forme
que prend une fiche dont la catégorie n'a pas de comparatif. **Le lot 8, qui doit réécrire ce
critère, a besoin de le savoir** — la réécriture ne peut pas se contenter d'ajouter « sauf
exception », il faut dire que le recouvrement est la règle dans ces catégories-là.

## 5. Cellules laissées vides : 11, jamais comblées

Sur 48 lignes de tableau : **8 cellules `Prendre si` vides** (Dify, Flowise, Letta,
OpenViking — 1 chacune ; Headroom, llmfit — 2 chacune, leurs bornes dures étant plus
nombreuses que leurs cas d'usage) et **3 cellules `Écarter si` vides** (DSPy 1,
LangChain 2). Aucune n'a été inventée.

Par ailleurs, **25 des 48 cellules `Écarter si` ne portent pas de wikilink** : ce sont des
bornes dures de la brique seule — budget de compilation, cache KV ignoré, licence AGPL,
pré-1.0, dépendance à LangChain.js. Elles n'ont pas de cible parce qu'elles ne redirigent
vers rien. Même constat que le pilote (remontée 7).

## 6. `complements:` — un seul couple posé, et cinq appariements refusés

**Posé, des deux côtés, parce que les deux fiches sont dans le périmètre :**

| Couple | Ce qui l'autorise |
|---|---|
| [[fastmcp]] ↔ [[mcpjam]] | fastmcp : « se teste / se débogue avec mcpjam ». mcpjam : « déboguer un serveur MCP, p. ex. bâti avec fastmcp ». L'appariement est énoncé **dans les deux fiches**, comme une recommandation d'usage conjoint |

**Refusés**, en application de la règle 3 — « s'intègre à » et « et la couche X » sont du
positionnement, pas un appariement :

| Candidat | Ce que dit la fiche | Pourquoi non |
|---|---|---|
| Headroom → [[LiteLLM]] | « Intégration LiteLLM par callback » | Une intégration technique documentée, pas une recommandation d'usage conjoint. Headroom nomme d'ailleurs LiteLLM en **redirection** (routage ≠ volume) |
| DSPy → [[LiteLLM]] | « s'appuie sur LiteLLM en interne » | Dépendance d'implémentation, invisible à l'usage |
| LangChain → [[LangGraph]] | « la couche dédiée du même écosystème » | Les deux fiches se renvoient l'une vers l'autre en **exclusion** selon la complexité de l'agent. C'est une substitution, pas un couple |
| Flowise, Langflow → [[LangChain]] | « bâti sur LangChain.js », « s'appuie sur l'écosystème » | Filiation d'implémentation |
| llmfit → [[Ollama]], [[llama.cpp]] | « détectés comme environnements cibles » | Positionnement fonctionnel, et la réciprocité côté runtime n'existe pas — un runtime ne recommande pas llmfit |

Aucune moitié de couple n'a donc été laissée ouverte vers l'extérieur du périmètre. Contraste
net avec le pilote (cinq moitiés remontées) : c'est un domaine où les briques se
**substituent** plutôt qu'elles ne s'apparient.

## 7. Une huitième fiche sans `maturite:` — et la conjecture du pilote tombe

`llmfit` n'a pas de `maturite:` : la colonne **Maturité** de son bandeau affiche un tiret
cadratin, et `build_bandeau.py` le nomme à chaque passage. Champ facultatif au gabarit, donc
pas une faute de validateur — un trou de donnée, dont le comblement est une décision
éditoriale de floSa.

La remontée 6 du pilote conjecturait que le trou pourrait être propre à `famille:
application` (ses sept fiches d'Administration l'étaient toutes). **`llmfit` est
`famille: cli`.** La conjecture ne tient pas : le trou n'est pas corrélé à la famille. Les
lots suivants n'ont donc pas de raison de ne le chercher que sur les applications.

## 8. Deux catégories fantômes, citées en prose dans le corps de deux fiches

| Fiche | Ce qu'elle affirmait | Réalité |
|---|---|---|
| Headroom | « la catégorie `llm/context` est neuve et Headroom y est seul » | `llm/context` **n'existe pas** dans `taxonomie.md`. Headroom est en `llm/memoire`, où vivent aussi Letta et OpenViking |
| llmfit | « `tooling/llm` est ici la bonne famille, et non `llm/local` » | Aucun préfixe `tooling/` n'existe. llmfit est en `llm/outillage` |

Les deux formulations datent d'avant le lot 4, qui a arrêté le vocabulaire des catégories.
Elles sont **fausses depuis**, et rien ne les signalait : une prose qui survit à ce qui
l'invalide — le défaut de la remontée 9 du lot 5, encore lui.

Corrigé **sans nommer aucune catégorie** : « la compression réversible de contexte n'y a pas
d'autre représentant », « llmfit y est seul sur ce créneau — décider quel modèle une machine
peut tenir, sans le servir ». Une prose qui ne cite pas la taxonomie ne peut pas se périmer
avec elle.

> Motif à chercher ailleurs : `grep -rn "la catégorie \`" --include=*.md` sur l'arbre. Toute
> fiche qui **nomme sa propre catégorie en prose** est une bombe à retardement du même type.

## 9. Deux constats non traités, hors mandat de conversion

- **`R5` sur `mcpjam`** : `alias en doublon interne ['mcpjam inspector']` — la liste porte
  `MCPJam Inspector` et `mcpjam inspector`, identiques à la casse près. Correction dans
  `alias:`, donc dans le frontmatter, que ce lot ne touche que pour `complements:`.
  Avertissement souple, présent avant comme après.
- **`Flowise`** porte `licence_type: open-source` alors que son corps décrit un
  **open-core** de fait (SSO, RBAC et espaces de travail réservés à l'édition Enterprise),
  et le dit explicitement. Le bandeau affiche donc « open-source » au-dessus d'un texte qui
  le nuance. Contradiction **préexistante**, conservée telle quelle : trancher est une
  décision de taxonomie, pas de conversion. À rapprocher de `DBeaver`, classé `open-core`
  pour exactement le même modèle.

## 10. Le critère « la Définition ne redit pas la maturité » ne se vérifie pas par `grep`

Vérification par script des sept critères d'acceptation : **11 fiches sur 11 conformes** —
aucune section morte, les sept sections neuves présentes, les cinq étiquettes de
`Mise en œuvre`, les étiquettes de `Ressources` dans le vocabulaire fermé, aucun wikilink à
alias dans une cellule.

Mais le test « la `Définition` ne recontient pas `maturite:` » a d'abord signalé **deux faux
positifs**, Dify et Langflow, sur le mot **production** : « du prototype à la production »,
« une app de production ». C'est le nom commun français, pas la valeur du frontmatter, et
aucune expression régulière ne les distingue.

> Aux seize autres : ce critère se vérifie mécaniquement pour `beta`, `experimental` et
> `deprecated`, **jamais pour `production`**. Sur cette valeur-là, c'est une relecture, pas
> un script. Tordre le texte pour faire taire le test aurait dégradé deux définitions
> justes.

## 11. Ce que le lot n'a pas eu à faire

- **Aucune section `## Retours`** : aucune entrée datée dans les onze fiches. La seule du
  vault reste `Agents de code/t3code.md`, du ressort du lot 7.
- **Aucune fiche sans `## Alternatives`** dans le périmètre. Headroom et llmfit ont
  `alternatives: []` mais portaient bien la section, avec une phrase à la place d'une liste ;
  elles ne sont donc pas parmi les trois fiches sans section que le pilote a comptées.
- **Aucune puce de `Pièges` supprimée sans destination** : 39 puces au total, réparties entre
  `Écarter si` (les limites qui orientent un choix), `Définition` (celles qui n'orientent
  rien mais qu'il faut savoir — les gains auto-déclarés de Headroom, la fracture FastMCP
  1.0 / 4.x, l'illisibilité des flux visuels) et `Mise en œuvre` (le cache d'originaux de
  Headroom, la matrice d'assistants mouvante).

## 12. Écart de validateurs mesuré sur la branche

| | Avant (`d8f81d6`) | Après |
|---|---|---|
| `check_brain.py` | 0 violation dure, **149** avertissements | 0 violation dure, **148** avertissements |
| `check_arbo.py` | vert | vert |

L'unique avertissement fermé est le `R15` de `DSPy` — « aucun lien vers une notion ou un
hub ». Le nouveau gabarit le ferme mécaniquement : `## Voir aussi` porte le hub du domaine
sur les onze fiches, et DSPy était la seule des onze à ne citer aucune notion. **C'est la
baisse attendue** que décrit la règle 5 du protocole : le compte de cette branche ne vaut
que pour elle.
