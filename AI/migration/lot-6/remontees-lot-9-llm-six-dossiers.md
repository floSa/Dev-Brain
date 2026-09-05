---
role: meta
nom: remontees-lot-9-llm-six-dossiers
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 9 (LLM, six sous-dossiers)

Périmètre : « LLM & IA générative/ » — `Observabilité des LLM/` (4), `Passerelles/` (3),
`RAG & retrieval/` (3), `Sortie typée/` (3), `Text-to-SQL/` (5), `Évaluation/` (4).
**22 fiches `role: brique`**, exactement le compte annoncé par la table du brief.
Branche `claude/lot-9-llm-six-dossiers-dd3c2b`, partie de `d8f81d6`.

Aucun fichier partagé touché : ni le brief, ni `CLAUDE*.md`, ni la taxonomie, ni un script.
`build_bandeau.py` a été **lancé** six fois, borné à un dossier à chaque fois.

## 1. Trois briques annonçaient un comparatif qui ne les contient pas

Les trois passerelles — [[LiteLLM]], [[OpenRouter]], [[OmniRoute]] — portaient en `## Liens`
la ligne « [[Comparatif - Frameworks LLM]] — comparatif de la catégorie ». C'est **faux, et le
`.base` le dit lui-même** : son filtre énumère `llm/socle`, `llm/agents`, `llm/rag`,
`llm/sortie-structuree`, et son commentaire nomme explicitement `llm/passerelle` parmi les
catégories sorties. `check_brain` le confirme par ailleurs :
`[WARN] R8a — categorie llm/passerelle : 3 briques, aucun comparatif .base ne les réunit`.

La ligne n'a pas été supprimée — une puce ne se supprime pas sans destination — mais
**reformulée** : « le comparatif du domaine LLM, dont les passerelles sont hors périmètre par
construction ». Elle garde la navigation et cesse de mentir.

> À trancher hors de ce lot : soit `llm/passerelle` gagne son comparatif (3 membres, c'est le
> minimum viable), soit ces trois fiches n'ont pas de comparatif et la ligne disparaît. Une
> conversation de conversion ne peut pas créer un `.base` (règle 1).

Symétriquement, [[Guidance]] **est** membre de `Comparatif - Frameworks LLM.base` mais ne le
citait nulle part : le lien a été ajouté. Deux erreurs opposées dans le même domaine.

## 2. La règle 2 tranche dans les deux sens, et le lot le montre en miroir

Les 22 fiches se répartissent proprement selon la règle du 2026-09-06 :

| Cas | Dossiers | Conséquence |
|---|---|---|
| **La brique ET la cible sont membres de la même vue** | Observabilité, Text-to-SQL et Évaluation entre elles ; RAG et Sortie typée via `Comparatif - Frameworks LLM` | la puce part au comparatif, où elle est **déjà écrite** |
| **Le dossier n'a aucun comparatif** | `Passerelles/` | toutes les puces **restent** en `Écarter si` |
| **La brique est membre, la cible ne l'est pas** | Observabilité → [[Ragas]], [[DeepEval]] ; Évaluation → [[Langfuse]], [[LangSmith]], [[Phoenix Arize]] | la puce **reste**, avec son wikilink |

Le troisième cas est ici parfaitement **symétrique**, et c'est ce qui le rend démonstratif :
les quatre plateformes d'observabilité renvoient vers les outils d'éval, les quatre outils
d'éval renvoient vers les plateformes d'observabilité, et **aucun comparatif ne réunit les
deux familles**. Huit fiches, huit renvois croisés, zéro comparatif d'accueil. Sous la
première formulation de la règle — « la brique est membre, donc la puce part » — les huit
renvois auraient disparu du vault.

Vérification faite avec `AI/migration/scripts/mesure_membres_bases.py`, **recoupée à la main**
sur un cas avant usage en masse ([[Guidance]] : `role: brique` + `categorie:
llm/sortie-structuree`, donc bien pris par le filtre de `Comparatif - Frameworks LLM.base`).
Aucun sur-comptage constaté sur ce périmètre.

## 3. Le critère « un wikilink dans chaque cellule Écarter si » : le chiffre

Mesuré sur les 22 fiches : **79 cellules `Écarter si` remplies, dont 17 portent un wikilink
(22 %) et 62 n'en portent pas (78 %)**. Ce n'est pas un oubli, c'est la conséquence directe de
la règle 2 : quand le renvoi vers un concurrent est déjà au comparatif, ce qui reste sur la
fiche est une **borne dure de la brique seule**, qui n'a personne vers qui pointer.

Le chiffre est cohérent avec le pilote, qui avait **zéro** wikilink sur 18 fiches. L'écart
s'explique : le pilote n'avait que des dossiers à comparatif interne, ce lot a en plus les
passerelles (sans comparatif) et les renvois croisés observabilité ↔ éval.

## 4. Comment j'ai lu « aucune cible dans deux sections », et pourquoi

Le critère est **inapplicable au pied de la lettre** depuis la règle 2 : une cible gardée en
`Écarter si` est presque toujours aussi une `alternatives:`, donc présente en
`### Alternatives`. Les deux critères entreraient en collision frontale.

Lecture retenue, et tenue sur les 22 : le critère porte sur les **sections de liste de
liens** — `### Alternatives`, `### Compléments`, `## Voir aussi`. Aucune cible n'apparaît dans
deux d'entre elles (vérifié par script, zéro écart). La prose de `## Définition` et les
cellules du tableau de décision ne sont pas des listes de liens et peuvent citer librement.

C'est aussi la lecture qui restitue le défaut d'origine que le critère visait : sur la page
Faker, Mimesis apparaissait en `Alternatives` **et** en `Liens` — deux listes, pas une prose.

> À réécrire au lot 8 avec la règle 2, comme le brief l'annonce déjà.

## 5. `complements:` — deux couples posés, un demi-couple à refermer

Trois fiches sur 22 remplissent le champ. Le critère appliqué est celui de la règle 3 :
l'appariement doit être **énoncé comme une recommandation**, pas comme une intégration.

| Fiche | Complément | Statut |
|---|---|---|
| [[LlamaIndex NLSQLTableQueryEngine]] | [[LlamaIndex]] | **couple fermé** — les deux fiches sont dans mon périmètre |
| [[LlamaIndex]] | [[LlamaIndex NLSQLTableQueryEngine]] | **couple fermé** |
| [[LangChain SQL agent]] | [[LangChain]] | **demi-couple** — [[LangChain]] est au niveau domaine, du ressort du **lot 10** |

> **À faire par le lot 10** : ajouter `complements: ["[[LangChain SQL agent]]"]` au frontmatter
> de `LLM & IA générative/LangChain.md`, et la puce correspondante sous `### Compléments`.

Le motif retenu est celui du pilote : `pgvector` ↔ `Postgres`, `MongoDB Compass` ↔ `MongoDB`.
Un **module et le framework qu'il étend** ont la même forme — le module ne s'utilise pas sans
son hôte, et les deux fiches se nomment mutuellement. C'est le seul motif que j'ai considéré
comme franchissant la barre.

Ce que j'ai **écarté**, et pourquoi — tous des cas de « s'intègre à », que la règle 3 exclut
nommément :

- `Langfuse` ↔ `LiteLLM` : « ingestion via LiteLLM » est une intégration, et la fiche LiteLLM ne mentionne même pas Langfuse. Unidirectionnel.
- `Haystack` et `LlamaIndex` ↔ `LiteLLM` : « peut router ses appels via LiteLLM » — du positionnement.
- `Instructor`, `Outlines`, `Guidance` ↔ `Pydantic` : dépendance technique énoncée d'un seul côté ; Pydantic ne les recommande pas en retour.
- `Instructor` ↔ `PydanticAI` : la fiche emploie le mot « couple », mais PydanticAI est déjà en `alternatives:` d'Instructor. Une cible ne peut pas être les deux.
- `Vanna` ↔ un magasin de vecteurs : trois candidats listés ([[Chroma]], [[Qdrant]], [[pgvector]]), donc une dépendance à choisir, pas un appariement.
- `Phoenix Arize` ↔ `TruLens` : la fiche Phoenix écrit « complément de TruLens », mais TruLens ne le lui rend pas — elle cite Phoenix comme concurrente. Le lien reste en `## Voir aussi`, non promu en couple.

**Sur 22 fiches, 19 gardent `complements: []`.** Le champ reste massivement vide, et c'est le
signe que la règle 3 fonctionne : elle refuse le bruit.

## 6. Une propriété de domaine, écrite quatre fois — rangée en `Mise en œuvre`

Les quatre fiches d'observabilité portaient en `## Pièges` la même puce : « le volume de
traces, de logs ou de spans fait exploser le stockage — régler échantillonnage et rétention ».
Ce n'est ni une borne qui oriente un choix (les quatre l'ont), ni un retour d'expérience.

Le pilote, face au cas identique de [[Chroma]] et [[LanceDB]], avait **consigné sans
reporter**, la destination naturelle étant la notion. J'ai tranché autrement : la puce est un
fait **opérationnel**, elle est donc allée sous l'étiquette `Prérequis` de `## Mise en œuvre`,
sur chaque fiche. Trois raisons :

1. elle reste sur la fiche, donc aucune information n'est perdue ni déplacée vers une page que la règle 1 m'interdit de toucher ;
2. `## Mise en œuvre` a des étiquettes fixes, dont une — `Prérequis` — dit exactement cela ;
3. la répéter en `## Définition` l'aurait diluée dans de la prose, ce que le gabarit refuse.

Cas particulier : [[LangSmith]] écrivait « le volume de traces **facturé** peut surprendre ».
Là ce n'est pas du stockage, c'est la facture — la puce est allée sous `Coût`.

> À arbitrer pour le vault : deux conversations ont traité le même motif de deux façons.
> Aucune n'est fausse ; l'intégration devrait en retenir une.

## 7. Recouvrement fiche ↔ comparatif : seize faits sur seize fiches

Application de la règle « un fait à la fois discriminant du comparatif et borne dure de la
brique reste **sur la fiche** ». Le recouvrement est donc assumé, mais il se mesure :

| Fiche | Fait présent des deux côtés |
|---|---|
| [[Helicone]] | maintenance mode depuis le rachat Mintlify ; proxy sur le chemin critique |
| [[LangSmith]] | self-host réservé à l'offre entreprise |
| [[Langfuse]] | frontière cœur MIT / `ee/` ; self-host de prod lourd |
| [[Phoenix Arize]] | ELv2 *source-available*, pas OSI |
| [[Haystack]] | rupture d'API 1.x → 2.x |
| [[LlamaIndex]] | réglages par défaut décisifs ; index avancés coûteux en tokens |
| [[RAGatouille]] | maintenance arrêtée en mai 2025 ; index multi-vecteur volumineux |
| [[Outlines]] | contraindre biaise la distribution |
| [[Guidance]] | le DSL est à apprendre ; ce qui est contraint dépend du backend |
| [[Instructor]] | les retries gonflent facture et latence |
| [[Vanna]] | dépôt OSS archivé le 29 mars 2026 |
| [[DB-GPT]] | coût conceptuel élevé (AWEL, agents, pipeline) |
| [[WrenAI]] | le MDL est le cœur de la valeur **et** le coût d'entrée |
| [[promptfoo]] | rachat OpenAI, mars 2026 |
| [[Ragas]] | API 0.x remaniée, épingler la version |
| [[LlamaIndex NLSQLTableQueryEngine]] | query engine, pas boucle d'agent |

Les formulations diffèrent — la fiche dit **ce qui va mordre**, le comparatif dit **ce qui
fait choisir** — mais ce sont bien seize paires à tenir d'accord. Le pilote en signalait trois
sur dix-huit et posait la question ; à ce volume-là, elle mérite une réponse au lot 8.

## 8. Cellules laissées vides — le compte exact

**17 cellules vides sur 13 fiches**, jamais comblées :

`OmniRoute` 3 ; `Helicone` et `Phoenix Arize` 2 chacune ; `LangSmith`, `Langfuse`,
`OpenRouter`, `Haystack`, `LlamaIndex`, `Guidance`, `Outlines`,
`LlamaIndex NLSQLTableQueryEngine`, `Vanna`, `TruLens` 1 chacune.

Les neuf autres — `LiteLLM`, `RAGatouille`, `Instructor`, `DB-GPT`, `LangChain SQL agent`,
`WrenAI`, `DeepEval`, `Ragas`, `promptfoo` — ont un tableau équilibré.

[[OmniRoute]] est le cas remarquable, et **dans l'autre sens** : 4 raisons de la prendre pour
**7 de l'écarter**, les trois cellules vides étant côté `Prendre si`. C'est fidèle à la fiche
d'origine, qui est une fiche d'avertissement : détournement de CGU documenté par le wiki
amont, six mois d'existence, chiffres de compression auto-déclarés, clés API dans un SQLite
non chiffré, dépôt de 475 Mo. Rien n'a été adouci pour équilibrer un tableau.

## 9. Le `## Écosystème` d'une fiche sans `alternatives:`

[[RAGatouille]] est l'une des trois fiches du vault dont le frontmatter `alternatives:` est
vide. Son ancienne section `## Alternatives` était de la **prose** : « pas de substitut direct
dans le brain pour la late-interaction clé en main ». Le brief dit que ces fiches « n'auront
pas de `### Alternatives` à écrire » — mais supprimer la section aurait supprimé
l'information, et supprimer `## Écosystème` aurait créé un trou de gabarit.

Choix retenu : `## Écosystème` → `### Alternatives` **en prose**, qui dit l'absence de
substitut et renvoie aux deux voisinages réels ([[sentence-transformers]] pour le reranking
par cross-encoder, [[Vespa]] pour la late-interaction à l'échelle). R11 n'a rien à contrôler,
le frontmatter étant vide ; le validateur reste vert et la page garde son gabarit.

Cas connexe, mesuré : [[RAGatouille]] est membre de **deux** vues, `Comparatif - Frameworks
LLM.base` et `Comparatif - NLP.base`. Son renvoi « reranking simple → sentence-transformers »
part bien au comparatif — mais au **second**, `Comparatif - NLP`, seul à contenir les deux
briques, et qui porte effectivement l'arbitrage. Son renvoi vers [[Vespa]], lui, reste sur la
fiche : Vespa n'est membre que de `Comparatif - Moteurs de recherche.base`.

## 10. Une puce de `## Ressources` sans URL n'est pas une ressource

La fiche [[Ragas]] mentionne un papier EACL 2024, **sans lien**. Une puce
« `- Papier — EACL 2024` » a d'abord été écrite, puis retirée : `## Ressources` est une
section de liens externes, et une étiquette sans URL n'y sert à rien. Le fait est resté en
`## Définition`, où il dit ce qu'il doit dire — que le framework est adossé à un papier publié.

Confirmation de la réserve du brief, mesurée : sur les 22 fiches, `## Ressources` compte **42
puces, 22 « Documentation » et 20 « Dépôt »**. Zéro tutoriel, zéro article, zéro papier. Deux
fiches n'ont qu'une seule puce — [[LangSmith]] et [[OpenRouter]], dont le `url_repo:` est
vide, ce qui est correct pour du propriétaire.

## 11. `## Retours` — aucune, conforme

Aucune entrée datée dans les 22 fiches, donc aucune section `## Retours` créée. La seule du
vault reste `LLM & IA générative/Agents de code/t3code.md`, du ressort du lot 7.

## 12. Aucun trou de `maturite:` dans ce périmètre

Le pilote signalait sept fiches sans `maturite:`, toutes de `famille: application`, et se
demandait si le champ manquait pour cette famille. **Élément de réponse : ce n'est pas la
famille en général.** Les 22 fiches d'ici couvrent `paquet` (12), `plateforme` (8), `saas` (1)
et `cli` (1) — aucune `application` — et les 22 portent une maturité. La colonne du bandeau
est remplie partout, `deprecated` pour [[Vanna]] compris, `beta` pour [[OmniRoute]] et
[[RAGatouille]]. L'hypothèse « le champ n'a jamais été rempli pour `famille: application` »
reste donc ouverte, et c'est à un lot qui en porte de la trancher.

## 13. Vérification

- `check_brain.py` : **aucune violation dure**, 149 avertissements — **identique à la base `d8f81d6`** avant conversion. Aucun R15 fermé, parce qu'aucune des 22 fiches n'en portait : toutes citaient déjà une notion ou un hub en v2.
- `check_arbo.py` : chemin et catégorie concordent partout.
- `build_bandeau.py --check` sur les six dossiers : tous les bandeaux concordent avec leur frontmatter.
- Critères d'acceptation vérifiés **par script**, pas affirmés : zéro section morte (`## Pourquoi`, `## Quand l'utiliser`, `## Quand NE PAS l'utiliser`, les **trois** noms de la section déploiement, `## Pièges`, `## Liens`, `## Alternatives` en `##`), les cinq étiquettes de `## Mise en œuvre` présentes sur les 22, vocabulaire de `## Ressources` respecté, zéro wikilink à alias dans une cellule de tableau, zéro cible en double entre deux sections de liste de liens.
- Le frontmatter n'a été touché que pour `complements:`, sur trois fiches. Le premier `diff` de chaque commit commence après la ligne `# <Titre>` — vérifié.
