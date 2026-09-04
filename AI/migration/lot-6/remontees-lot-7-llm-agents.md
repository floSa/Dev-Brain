---
role: meta
nom: remontees-lot-7-llm-agents
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 / lot 7 — remontées de la conversion « LLM : Agents de code/, Agents/ »

Périmètre : les **22** `role: brique` des dossiers « LLM & IA générative/Agents de code/ » (13)
et « LLM & IA générative/Agents/ » (9). Compte annoncé par la table du découpage : 22. **Compte
mesuré : 22.** Aucun débordement.
Branche `claude/lot-7-llm-ia-agents-cd531c`, basée sur `90d46a2`.

Rien d'autre n'a été touché : ni hub, ni notion, ni comparatif, ni `.base`, ni script, ni
document partagé. `build_bandeau.py` a été **lancé** borné aux deux dossiers, jamais édité.
Aucune régénération d'index, aucun appel à `cloturer-brain`.

## 0. Les trois règles de `98f4112` sont arrivées en cours de conversion — appliquées

Elles ont été lues par `git show`, sans rebase ni merge : la règle 6 du protocole parallèle
interdit les deux, et le commit ne touche que `lot-6-gabarit.md`, que cette branche ne modifie
pas — l'intégration n'y verra aucun conflit. Effet réel de chacune, plus bas : §1 pour la nue,
§2 pour le routage, §3 pour `complements:`.

## 1. Règle « wikilink nu en cellule » — vérifiée, zéro écart

Contrôle passé sur les 22 fiches converties : **aucune cellule de tableau ne porte de wikilink
à alias**. Les seuls liens qui vivent en cellule sont `[[E2B]]`, `[[Daytona]]`, `[[Letta]]`,
`[[OpenRouter]]`, `[[Langflow]]`, `[[Dify]]` — tous nus.

> Les formes à alias trouvées dans ces deux dossiers (`[[Guardrails|garde-fous]]`,
> `[[Structured outputs|décodage contraint]]`, `[[Human-in-the-loop|human-in-the-loop]]`) vivent
> dans des **hubs, des notions et les comparatifs**, hors du périmètre d'une conversation de
> conversion. Elles sont signalées ici, pas corrigées. À vérifier : sont-elles en cellule de
> tableau ou en prose ? En prose l'alias est légitime, et la règle ne les vise pas.

## 2. Règle de routage — les 22 sont membres d'une vue, mais trois renvois ne le sont pas

Appartenance vérifiée sur les deux `.base`, pas supposée :

| Vue | Filtre | Membres du périmètre |
|---|---|---|
| `Comparatif - Assistants de code IA.base` | `role == brique` ∧ `categorie == llm/agent-de-code` | **13 / 13** |
| `Comparatif - Frameworks LLM.base` | `role == brique` ∧ `categorie ∈ {llm/socle, llm/agents, llm/rag, llm/sortie-structuree}` | **9 / 9** |

C'est donc uniformément la **première branche** de la règle : la puce « besoin → concurrent »
reste au comparatif, et `Écarter si` ne porte que des bornes dures. Mesure de ce que ça donne :

| | Prendre si | Écarter si |
|---|---|---|
| cellules remplies | 68 | **79** |
| cellules vides | 14 | **3** |

**L'inversion par rapport au pilote est le fait marquant.** Le pilote comptait 17 cellules
`Écarter si` vides sur 18 fiches ; ici il en reste 3 sur 22, et c'est `Prendre si` qui se vide.
La raison est dans le matériau : ces 22 fiches portent des bornes dures nombreuses et non
substituables — licence absente (swarm-forge), clause de marque (BMAD), plateforme non supportée
(Maka sous Linux, ai-memory sous Windows natif), absence de système de permissions (pi),
exécuteur qui n'est pas une frontière de sécurité (smolagents), tracing sortant par défaut
(OpenAI Agents SDK), dépôt en maintenance (AutoGen), successeur annoncé (Semantic Kernel),
modèle économique par la publicité (freebuff). Retirer les redirections ne vide pas la colonne
quand la brique a de vraies bornes ; elle ne se vidait au pilote que parce que les bases
vectorielles se départagent surtout **les unes par rapport aux autres**.

### Les trois exceptions, et pourquoi elles sont assumées

Trois puces « besoin → concurrent » ont été **gardées en `Écarter si`** alors que la fiche est
membre d'une vue. La règle 2 les fait tomber dans sa première branche, mais son propre
argument — « l'écarter la supprimerait » — joue ici : **la cible du renvoi n'est membre
d'aucune des deux vues**, donc aucun comparatif ne peut la porter.

| Fiche | Puce gardée | Cible | Pourquoi le comparatif ne la porte pas |
|---|---|---|---|
| `Maka` | isoler du code non fiable | [[E2B]], [[Daytona]] | `compute/a-la-demande` — hors des deux vues |
| `ai-memory` | mémoire d'un agent applicatif, pas d'une CLI | [[Letta]] | `llm/memoire` — sortie du comparatif Frameworks LLM au lot 5 |
| `PraisonAI` | canvas visuel plutôt que YAML | [[Langflow]], [[Dify]] | `llm/low-code` — sortie du même comparatif au lot 5 |

**Proposition pour la règle 2** : le critère n'est pas l'appartenance de la **fiche** à une vue,
c'est celle de la **cible du renvoi**. Une fiche membre dont le renvoi sort de la vue est
exactement le cas que la seconde branche protège. Formulé ainsi, les trois cas ci-dessus cessent
d'être des exceptions. Le cas se reproduira mécaniquement aux lots 8, 9 et 10 : l'éclatement de
`llm/framework` en 13 domaines au lot 5 a laissé le comparatif Frameworks LLM avec quatre
catégories sur treize, et les fiches continuent de renvoyer vers les neuf autres.

Ces trois cellules sont aussi les **seules** des 79 à porter un wikilink. La règle dure nº 5 du
lot 8 en voudrait 79 ; la remontée 20 du lot 5 explique pourquoi 76 n'en ont pas et n'en veulent
pas. Rien de nouveau, mais le rapport est ici de 3 contre 76, plus net qu'au pilote.

## 3. Règle `complements:` — six couples retirés, six posés

**Retirés après lecture de la règle.** Six couples `LangGraph ↔ {CrewAI, AutoGen, OpenAI Agents
SDK, Agno, smolagents, PraisonAI}` avaient été écrits avant qu'elle n'arrive. Ils tombent : ce
que les fiches énoncent est « même famille de frameworks d'agents que X, Y **et la couche
d'orchestration LangGraph** » — une phrase de **positionnement**, pas une recommandation
d'appariement, exactement la forme que l'exemple MLflow de la règle rejette. Et le fait que
LangGraph soit « complémentaire plutôt que substitut » vise **[[LangChain]]**, hors périmètre,
pas CrewAI. `complements:` et le bloc `### Compléments` ont été retirés des six.

> Conséquence à connaître : `LangGraph` a désormais `alternatives: []` **et** `complements: []`.
> C'est la règle 4 du validateur (voisinage déclaré, souple) qui le signalera, et c'est le
> signal juste — sa fiche dit elle-même n'avoir aucun substitut direct.

**Posés, six couples, dans les deux sens.** `Spec Kit ↔ {Aider, Cline, Continue}` et
`BMAD ↔ {Aider, Cline, Continue}`. Ils passent le test de la règle 3 : la fiche **énonce
l'appariement comme une nécessité**, pas comme une intégration parmi d'autres —

- BMAD, verbatim : « BMAD ne **remplace pas** l'agent qui code — il le pilote. L'exécution reste
  chez [[Aider]], [[Cline]] ou [[Continue]]. »
- Spec Kit, verbatim : « c'est un **cadre méthodologique**, pas un assistant de code. Les agents
  qu'il pilote sont fichés à part : [[Aider]], [[Cline]], [[Continue]]. »

C'est la forme pgvector ↔ Postgres : la brique est inopérante seule. À arbitrer si l'intégration
juge qu'un couple « un pour trois » reste du bruit — mais alors l'information disparaît des deux
côtés, car ces deux fiches n'ont pas d'autre endroit où dire de quoi elles ont besoin.

**Moitiés de couple hors périmètre — à fermer par les lots qui portent la cible.** Aucune n'a été
posée, la réciprocité étant obligatoire :

| Fiche du lot 7 | Complément sourcé | Domaine de la cible | Lot qui le portera |
|---|---|---|---|
| `Agno`, `CrewAI`, `OpenAI Agents SDK`, `smolagents`, `PraisonAI`, `LangGraph`, `Semantic Kernel`, `PydanticAI` | [[LiteLLM]] — « peut router ses appels via » | `llm/passerelle` | lot 9 |
| `PydanticAI` | [[Pydantic]] — « bâti sur » | hors LLM | lot 14 ou 16 |
| `LangGraph` | [[LangChain]] — « au-dessus de », même équipe | `llm/socle` | lot 10 |

> Les huit lignes `LiteLLM` sont à relire à l'aune de la règle 3 avant d'être posées : « peut
> router ses appels via LiteLLM » ressemble beaucoup à « MLflow s'intègre à PyTorch ». La ligne
> `LangGraph ↔ LangChain`, elle, est un couple franc — même équipe, position déclarée dans le
> stack, et les deux fiches l'énoncent.

## 4. `maturite:` manque sur les 13 fiches d'« Agents de code/ », et sur aucune d'« Agents/ »

`build_bandeau` le nomme à chaque passage : **13 bandeaux sur 22 affichent un tiret cadratin en
Maturité**, et ce sont exactement les 13 du dossier « Agents de code/ ». Les 9 d'« Agents/ »
portent toutes le champ (8 `production`, 1 `deprecated`).

La coupure est **par dossier**, pas par famille — contrairement à ce que le pilote observait, ses
sept trous étant ses sept `famille: application`. Ici le dossier mélange `cli`, `extension`,
`application` et `plateforme`, et les treize manquent. L'hypothèse la plus simple est que ce
dossier a été peuplé après l'ouverture du champ, ou par une passe qui ne le remplissait pas. Non
comblé : c'est une décision éditoriale de floSa, pas une déduction de conversion.

## 5. Deux autres cellules vides, de nature différente

- `swarm-forge` — **Licence vide, et c'est le contenu de la fiche**. `licence_type:` est laissé
  vide volontairement : le dépôt ne déclare aucune licence, le remplir `open-source` serait faux.
  Le tiret cadratin du bandeau dit ici quelque chose de vrai. À ne pas « réparer ».
- `ai-memory` — **Exécution vide**, et celle-là est un vrai trou : `famille: plateforme` sans
  `hosted:`. La fiche est sans ambiguïté self-hébergée (binaires, images Docker, paquets AUR,
  build `cargo`), donc `hosted: [self]` la remplirait — mais poser un champ de frontmatter
  déborde de la conversion et modifie la vue `.base`. Signalé, pas posé.

## 6. Le vocabulaire fermé de `Ressources` n'a pas d'étiquette pour un site de projet

`{Documentation, Dépôt, Tutoriel, Article, Papier, Cours, Vidéo}`. Deux fiches portaient un lien
de **site** distinct de la doc et du dépôt : `freebuff` (https://freebuff.com) et `t3code`
(https://t3.codes). Les deux ont été rangées sous `Documentation` avec la précision entre
parenthèses — `- Documentation — https://t3.codes (site du projet)`. C'est l'option qui respecte
le vocabulaire ; elle produit deux lignes `Documentation` sur `t3code`.

À trancher au lot 8 : ajouter `Site` au vocabulaire, ou acter la convention parenthétique.

> Effet de bord heureux, contre la « réserve connue » du brief : `url_repo` étant renseigné sur
> les 22, chaque `## Ressources` porte au minimum **deux** puces — `Documentation` et `Dépôt` —
> là où l'ancienne section `## Liens` n'en portait souvent qu'une. La section n'est donc pas
> réduite à une ligne, même si tutoriels, articles et papiers manquent toujours.

## 7. La « seule entrée datée du vault » n'en est pas une — `## Retours` n'existe nulle part

Le brief et la spec annoncent une fiche du vault portant une entrée datée dans `Pièges`, et la
nomment : `LLM & IA générative/Agents de code/t3code.md`, du ressort de ce lot. Vérification
faite, la puce est :

> `- Créé le 2026-02-08 : peu de recul terrain, périmètre susceptible de bouger vite.`

Ce n'est pas un retour d'expérience — c'est la **date de création du dépôt**, un fait sur le
projet, écrit `- <texte> le YYYY-MM-DD` et non `- YYYY-MM-DD — <symptôme> : <correctif>.`, la
convention que `CLAUDE.md` définit. La mesure qui l'a désignée cherchait une date dans la
section, pas la convention. Sa destination est la cellule `Écarter si` sur la précocité du
projet, où elle rejoint l'avertissement du README.

**Conséquence pour tout le lot 6 : le vault ne contient aucune entrée REX datée, et `## Retours`
n'a vocation à être créée dans aucun des dix-sept lots.** La section reste au gabarit pour les
entrées futures. Le grep de contrôle est `^- [0-9]{4}-[0-9]{2}-[0-9]{2} —` : il ne remonte rien
sur l'arbre entier.

## 8. Deux fiches citaient en dur un champ supprimé au lot 2

`Maka` et `t3code` écrivaient dans leur corps « d'où le `status: en-eval` retenu ici plutôt
qu'`actif` ». Le champ `status:` a été retiré du frontmatter au lot 2 — R6 du validateur est
tombée avec lui — et aucune des deux fiches ne le porte : ces phrases désignaient un champ qui
n'existe plus. La substance (dépôt très jeune, rien de publié, périmètre mouvant) est conservée
en `Écarter si` ; la référence au champ est tombée.

À vérifier ailleurs par l'intégration : un `grep -rn 'status: '` sur l'arbre, hors frontmatter,
pour voir si d'autres corps de fiches gardent la trace du champ.

## 9. `t3code` déclare en `alternatives:` ce que son propre texte dit ne pas en être

Le frontmatter porte `alternatives: [Cline, Aider, Continue, Maka]`, et la section commence par
« **Aucune** des pages ci-dessous n'est un équivalent : t3code se place **au-dessus** de ces
outils, pas à côté d'eux. » La phrase a été conservée telle quelle — elle est juste, et c'est le
frontmatter qui est en tort.

Non corrigé, et délibérément : basculer ces quatre cibles vers `complements:` casse quatre
réciprocités d'`alternatives:` dans quatre fiches, ce qui est un ré-arbitrage éditorial, pas une
conversion de format. Même remarque, en plus léger, pour `Graphify` et `i-have-adhd`, dont les
sections `Alternatives` s'ouvrent en disant qu'il n'y a pas d'alternative.

> C'est le cas général que la règle 3 gagnerait peut-être à couvrir dans l'autre sens : **une
> brique qui se place au-dessus d'une autre n'en est pas une alternative**. Le brain en compte au
> moins trois dans ce seul lot — t3code, Spec Kit, BMAD — et le lot 5 avait déjà dû l'écrire à la
> main dans le comparatif (« il pilote, il ne code pas »).

## 10. Un avertissement souple non corrigé, dans le périmètre

`R5 — Agents de code/BMAD.md : alias en doublon interne ['bmad-method']`. Le frontmatter porte
`BMAD-METHOD` **et** `bmad-method`, que la comparaison insensible à la casse voit comme un
doublon. Non touché : `alias:` sert la résolution de liens et la recherche, sa modification est
éditoriale. C'est le seul avertissement qui subsiste sur les 22 fiches.

## 11. Écart d'avertissements mesuré sur cette branche

Avant : **149**. Après : **144**. Les cinq qui tombent sont des `R15` — « aucun lien vers une
notion ou un hub » — sur `Aider`, `Cline`, `Continue`, `Spec Kit` et `Semantic Kernel` : le
`## Voir aussi` du nouveau gabarit ouvre systématiquement sur le hub du dossier, ce que
l'ancienne section `## Liens` ne faisait pas.

`check_brain.py` : **aucune violation dure**. `check_arbo.py` : **chemin et catégorie concordent
partout**. `build_bandeau.py --check` sur le périmètre : **tous les bandeaux concordent**.

> Le gabarit fait donc tomber R15 mécaniquement. Si les seize autres lots ouvrent aussi leur
> `## Voir aussi` sur le hub du dossier, les R15 restants du vault devraient s'éteindre au fil du
> lot 6, sans qu'aucune conversation ait à les traiter comme un chantier.

## 12. Recouvrement fiche / comparatif — nettement moindre qu'au pilote

Le pilote comptait trois faits présents des deux côtés sur 18 fiches et demandait un arbitrage.
Sur ces 22, le recouvrement est faible : les comparatifs de ces deux dossiers ont été écrits au
lot 5 sur un axe **fonctionnel** (« ce que la brique fait dans la chaîne », « la couche qu'on
importe »), là où les `Écarter si` d'ici sont des bornes d'**exploitation** — plateforme, licence,
permissions, quota, cycle de vie. Les deux ne parlent pas de la même chose et se lisent bien l'un
après l'autre.

Deux faits font exception, et ce sont les deux plus lourds du lot : la **licence absente** de
swarm-forge et le **modèle publicitaire** de freebuff apparaissent des deux côtés. Là le
recouvrement paraît souhaitable — ce sont des bornes qu'on ne veut pas rater, où qu'on entre.
