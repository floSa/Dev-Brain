---
role: meta
nom: remontees-lot-8-llm-runtimes-assistants-finetuning
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 8 (LLM : Runtimes, Assistants, Fine-tuning)

Périmètre : les **19** briques de « LLM & IA générative/Runtimes/ » (9), « /Assistants/ » (5)
et « /Fine-tuning/ » (5). Compte annoncé par la table du découpage, compte mesuré : **19**, sans
écart. Branche `claude/lot-8-llm-ia-generative-77e163`.

Rien d'autre n'a été touché : aucun hub, aucune notion, aucun comparatif, aucun document
partagé, aucun script. `build_bandeau.py` a été **lancé** borné aux trois dossiers, jamais
édité.

## Écart de validateurs, mesuré sur cette branche

| | Dur | Avertissements |
|---|---|---|
| Avant (`90d46a2`) | 0 | 149 |
| Après | 0 | **145** |

Les quatre avertissements en moins sont des **R15** du périmètre — `LM Studio`, `Ollama`,
`TensorRT-LLM`, `text-generation-webui` n'avaient aucun lien vers une notion ou un hub. La
section `## Voir aussi` du nouveau gabarit en pose un par construction : la notion du dossier
ou son hub. Aucun avertissement n'a été créé. Ce compte ne vaut que pour cette branche, il lui
manque le travail des seize autres.

`check_arbo.py` et `build_bandeau.py --check` sont au vert sur les trois dossiers.

## 1. Les trois règles du 2026-09-06 sont arrivées en cours de lot — état d'application

Elles ont été reçues après la conversion des 19, avant le commit. Bilan honnête :

- **Règle 1 (wikilink nu en cellule)** — *conforme, vérifié, aucune correction nécessaire*.
  Mesure : la recherche des wikilinks à alias en début de ligne de tableau ne remonte rien sur
  les trois dossiers. Les seuls wikilinks à alias du périmètre — `[[mcp-protocol|MCP]]`,
  `[[a2a-protocol|A2A]]` — vivent en puces de `## Voir aussi`, jamais en cellule.
- **Règle 2 (routage selon l'appartenance à une vue)** — *conforme, et vérifiée par mesure et
  non par supposition* : voir §2.
- **Règle 3 (`complements:` n'est pas « tout ce avec quoi ça s'intègre »)** — *un couple a été
  retiré après coup* : voir §4.

## 2. Règle 2 — l'appartenance mesurée départage nettement les trois dossiers

`AI/migration/scripts/mesure_membres_bases.py`, lancé avant d'arbitrer :

| Dossier | Vue `.base` | Membres | Traitement des puces « besoin → concurrent » |
|---|---|---|---|
| `Runtimes/` | `Comparatif - Exécution & serving LLM.base` | **9 / 9** | au comparatif ; `Écarter si` ne porte que des bornes dures |
| `Fine-tuning/` | `Comparatif - Fine-tuning LLM.base` | **5 / 5** | idem |
| `Assistants/` | **aucune** | **0 / 5** | **restent en `Écarter si`, wikilink compris** |

Le cas d'`Assistants/` est celui que la règle 2 décrit : `llm/assistant` n'a aucun comparatif
— `check_brain` le signale déjà en R8a — et la vue `Comparatif - Frameworks LLM.base`
**exclut explicitement** `llm/assistant` par un commentaire de son propre filtre. Écarter ces
puces les aurait supprimées.

> Conséquence à noter pour l'intégration : les cinq fiches d'`Assistants/` portaient toutes une
> puce `[[Comparatif - Frameworks LLM]] — comparatif de la catégorie`. **C'est un pointeur
> faux** : ce comparatif ne les nomme pas et sa vue les exclut. La ligne a été retirée et
> remplacée par `[[Assistants]] — le hub du dossier`, seul agrégat qui les réunit réellement.
> Le vrai correctif est ailleurs et n'est pas du ressort d'un lot de conversion : créer
> `Comparatif - Assistants` (5 membres, au-dessus du seuil de 2), ou assumer que le domaine
> n'en a pas.

### Effet de bord : un `Écarter si` qui redouble `### Alternatives`

Sur **`LM Studio Bionic`** seulement, deux cellules `Écarter si` pointent vers `[[OpenClaw]]`
et `[[Hermes Agent]]`, qui sont aussi ses deux `alternatives:`. La règle 2 (garder la puce) et
le critère d'acceptation du brief (« aucune cible dans deux sections ») se contredisent ici.
La règle 2 a été suivie, parce qu'elle est la plus récente et la plus spécifique, et parce que
l'autre branche supprimait de l'information qui ne vit nulle part ailleurs. **À trancher à
l'intégration.** Les deux autres fiches routantes d'`Assistants/` n'ont pas le problème :
`OpenClaw` route vers `[[OpenHands]]`, `Hermes Agent` vers `[[Letta]]` et `[[smolagents]]` —
aucune de ces cibles n'est une de leurs alternatives.

### Un angle mort de la règle 2 : membre d'une vue, mais routant hors d'elle

Trois cellules de fiches **membres** de leur vue gardent malgré tout un wikilink, parce que la
cible est hors du périmètre de la vue et que le comparatif ne peut donc pas porter la puce :

| Fiche | Cellule conservée | Pourquoi le comparatif ne peut pas la porter |
|---|---|---|
| `needle` | → [[Outlines]], [[Instructor]] (sortie structurée sur un plus gros modèle) | ni l'un ni l'autre n'est `llm/runtime` |
| `needle` | → [[GLiNER]] (NER zero-shot) | hors domaine |
| `TRL` | → [[PyTorch]] (entraîner de zéro, ce n'est pas du post-training) | hors domaine |

La règle 2 raisonne « la brique est-elle membre ? » ; le cas réel est « **la cible** est-elle
membre ? ». Formulation proposée : *une puce se délègue au comparatif quand la brique **et** sa
cible sont membres de la même vue ; sinon elle reste.*

## 3. Ce que le comparatif portait déjà — la mesure du périmètre

Application de la remontée 7 du pilote. Mesure du 2026-09-06 sur les 19 fiches d'origine
(`git show HEAD:`) : `## Quand NE PAS l'utiliser` contenait **65 puces**, dont **51 de la forme
« besoin → [[concurrent]] »** — soit 78 %, nettement au-dessus des 89 % du pilote rapportés à un
volume trois fois moindre. En face, `## Pièges` en portait **74**.

Les 51 se répartissent selon la règle 2, et la répartition est mesurée, pas estimée :

- **36** visaient une cible **membre de la même vue** que la fiche → non recopiées, le
  comparatif du dossier les portait déjà (vérifié ligne à ligne dans la section « Ce qui
  départage » des deux comparatifs) ;
- **12** sont dans `Assistants/`, dossier sans vue → conservées avec leur wikilink ;
- **3** sont l'angle mort du §2 — cible hors vue → conservées avec leur wikilink.

Ce qui reste en `Écarter si` sur les 14 fiches membres est une **borne dure de la brique
seule** : flags de compilation absents (llama.cpp), contexte par défaut à 4 096 tokens et
endpoint `/v1` qui casse le *tool calling* (Ollama), préallocation VRAM (vLLM), gain
proportionnel au partage de préfixes (SGLang), licence HFOIL de mi-2023 à début 2024 (TGI),
recompilation par couple modèle/GPU/précision (TensorRT-LLM), AGPL-3.0 (text-generation-webui),
chat template silencieusement faux (TRL), multi-GPU bridé en OSS (Unsloth), 0.1.x (Tunix).

## 4. Règle 3 — un couple `complements:` posé puis retiré, deux gardés

Trois couples avaient été ouverts avant la règle 3. Elle en invalide un, retiré avant commit :

| Couple | Source dans la fiche | Verdict |
|---|---|---|
| `LM Studio` ↔ `LM Studio Bionic` | « couche agentique posée sur le runtime », « le runtime, les modèles téléchargés et les quantizations sont réutilisés » | **gardé** — appariement recommandé, énoncé des deux côtés |
| `vLLM` ↔ `Tunix` | « les rollouts d'inférence s'appuient nativement sur vLLM ou SGLang-JAX » | **gardé**, mais le « ou SGLang-JAX » affaiblit : c'est un appariement par défaut, pas exclusif |
| `OpenClaw` ↔ `OpenMAIC` | « intégration messagerie **annoncée** avec OpenClaw » | **retiré** — un fait d'intégration annoncé n'est pas une recommandation d'appariement. Le fait subsiste, en clair, dans `## Voir aussi` des deux fiches |

Les deux couples gardés ont leurs **deux extrémités dans le périmètre** : ils sont posés dans
les deux sens, aucune moitié orpheline n'a été laissée.

### Moitiés non posées, dont la cible est hors périmètre — à fermer par leur lot

Sourcées dans mes fiches, **volontairement laissées vides** pour ne pas mettre les cibles en
faute (mécanisme de la remontée 5 du pilote) :

| Fiche | Complément sourcé | Dossier de la cible | Lot qui le portera |
|---|---|---|---|
| `TensorRT-LLM` | [[NVIDIA Triton]] — « backend d'inférence de Triton » | Machine Learning/Serving/ | lot 3 |
| `Hermes Agent` | [[Modal]], [[Daytona]] — bacs à sable d'exécution au choix | Calcul distribué, Outils de développement | lots 15 et 14 |
| `OpenMAIC` | [[LangGraph]] — « orchestre ses agents via LangGraph » | LLM & IA générative/Agents/ | lot 7 |

Trois candidats **écartés au titre de la règle 3**, parce qu'ils relèvent du « s'intègre à » et
non de la recommandation : `Axolotl`, `LLaMA-Factory` et `TRL` → `[[HuggingFace]]` et
`[[DeepSpeed]]` (socle, cité par toutes les fiches du dossier), `Tunix` → `[[JAX]]` (socle),
`Unsloth` → export GGUF (le format est nommé, `llama.cpp` ne l'est pas — pas de source).

## 5. La prose hors `## Définition` était concentrée sur cinq fiches

Les cinq briques de `Fine-tuning/` portaient toutes, **après** `## Alternatives`, un paragraphe
« Nuance : … » de 3 à 5 lignes qui expliquait la place de la brique dans le cluster. Le nouveau
gabarit l'interdit (« aucune prose hors de `## Définition` »).

Destination trouvée sans perte : les cinq paragraphes disent **exactement** ce que la section
« Ce qui départage » du `Comparatif - Fine-tuning LLM` dit déjà, écrite au lot 5 — TRL « le
niveau code, et la brique sur laquelle les autres reposent », Axolotl « la même chose pilotée
par un seul YAML », LLaMA-Factory « la couverture », Unsloth « des kernels Triton sur mesure »,
Tunix « le pendant JAX/TPU ». Ils ont donc été supprimés, pas déplacés.

> Une information n'y survit pas et n'a **pas** été reportée, faute de destination légitime :
> la fiche `Tunix` citait « en dehors du brain : verl, OpenRLHF ». Deux briques absentes du
> vault, donc ni wikilinkables ni comparables. À arbitrer : les créer, ou assumer la perte.

## 6. `OpenMAIC` portait une justification de taxonomie devenue fausse

Son corps consacrait trois paragraphes à expliquer qu'elle porte « la catégorie `llm/app` », et
opposait `llm/framework` à `llm/app`. **Aucune de ces deux valeurs n'existe plus** : son
frontmatter porte `categorie: llm/assistant` depuis l'éclatement de `llm/framework` en treize
domaines. La substance — « c'est un produit qui consomme une bibliothèque d'agents, pas une
bibliothèque » — a été gardée en deux propositions dans `## Définition` ; l'appareil taxonomique
périmé est tombé.

> Cas général à surveiller sur les seize autres lots : **une fiche qui explique sa propre
> `categorie:` dans son corps se périme au premier renommage de la taxonomie.** Le nouveau
> gabarit règle le problème par construction — le rangement est dérivé, il ne se justifie plus
> dans le texte — mais il faut encore aller retirer les justifications déjà écrites.

## 7. `## Retours` n'a été créée nulle part

Conforme au brief. La seule fiche datée du vault est
`LLM & IA générative/Agents de code/t3code.md`, du ressort du **lot 7**. Aucune des 19 ne
portait d'entrée `- YYYY-MM-DD — …`.

## 8. Cellules laissées vides — le compte exact

Le tableau ne s'équilibre pas, et il n'a pas été équilibré : **30 cellules vides sur 13
fiches**. Le détail, mesuré (`Prendre si` / `Écarter si`) :

| Excédent à gauche | | Excédent à droite | |
|---|---|---|---|
| `vLLM`, `SGLang`, `TGI`, `Axolotl` | 4 / 3 — 1 vide chacune | `TRL`, `Unsloth` | 4 / 5 — 1 vide |
| | | `Tunix` | 3 / 4 — 1 vide |
| | | `OpenHands` | 3 / 5 — 2 vides |
| | | `Hermes Agent` | 4 / 7 — 3 vides |
| | | `OpenClaw` | 3 / 7 — 4 vides |
| | | `OpenMAIC` | 4 / 8 — 4 vides |
| | | `needle`, `LM Studio Bionic` | 4 / 9 — 5 vides |

Les six fiches les plus déséquilibrées sont **les cinq d'`Assistants/` plus `needle`**, et ce
n'est pas un hasard de rédaction : ce sont les six briques dont la surface de risque — shell,
messageries ouvertes, skills tiers non audités, ou chiffres annoncés par l'éditeur et non
reproductibles — est documentée en détail, alors que leur intérêt tient en trois ou quatre
phrases. Un tableau à moitié rempli honnêtement vaut mieux qu'un tableau complet inventé, mais
l'écart mérite d'être vu : la fiche d'un produit jeune penche structurellement vers le refus.

## 9. Deux liens décoratifs retirés, sans destination

`LM Studio` et `vLLM` portaient tous deux en `## Liens` : « Endpoint OpenAI-compatible : se
branche comme une API [[FastAPI]] devant les apps ». La phrase n'apprend rien sur la brique —
FastAPI n'est ni une dépendance, ni un complément, ni une alternative — et le fait utile
(« expose un endpoint OpenAI-compatible ») est passé en `Point d'entrée` de `## Mise en œuvre`.
Les deux wikilinks sont donc perdus, volontairement, et signalés ici plutôt que reportés.

## 10. Deux défauts de données constatés, non corrigés (hors périmètre d'un lot de format)

- **R5, `TensorRT-LLM`** : `alias: [TRT-LLM, trt-llm, tensorrt-llm]` — doublon interne à la
  casse près, avertissement présent avant comme après. Et `tensorrt-llm` y est aussi le `nom:`
  de `Machine Learning/Serving/TensorRT.md`, second R5. Le correctif est évident — retirer
  `trt-llm` — mais c'est une décision sur des métadonnées, pas une conversion de corps : laissé
  tel quel, pour que le diff de cette branche ne contienne que du lot 6.
- **`mesure_membres_bases.py`** compte `Machine Learning/Serving/ONNX Runtime.md` comme membre
  du `Comparatif - Exécution & serving LLM.base`, alors que sa `categorie:` vaut `ml/serving`
  et que le filtre de la vue exige `llm/runtime`. Sans effet sur mes arbitrages — mes 19
  concordent toutes par catégorie — mais le script sur lequel la **règle 2** demande désormais
  de s'appuyer sur-compte, et cela mérite vérification avant que seize conversations s'y fient.
