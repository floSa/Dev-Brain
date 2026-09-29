---
role: notion
nom: Licences de modèles open weights
alias: [open weights, poids ouverts, licences de modèles, licence d'un modèle de langage, open-weight licensing, Llama Community License, open washing]
categorie: llm/modele
domaines: [ai-eng, ml-eng]
tags: [llm, local-llm, self-hosted]
---

# Licences de modèles open weights

> Notion de vulgarisation, **pas un conseil juridique** : elle dit quoi lire dans un texte de licence, pas ce qu'il autorise dans un cas donné. Les textes cités ont été lus le 2026-09-30 ; une licence se relit avant chaque livraison, et un juriste tranche.

## Aperçu

- **Poids ouverts** (*open weights*) : les paramètres du modèle se téléchargent. Cela ne dit ni que le code d'entraînement est public, ni que les données le sont, ni **ce que la licence permet**.
- Pour une ESN qui installe un modèle chez un client, la question n'est pas « le modèle est-il ouvert ? » mais « que dit le fichier `LICENSE` de **ce** dépôt, pour **cette** génération, sur **cet** usage ? ». Les petits modèles exploitables en local et leurs raisons d'être sont dans [[Small Language Models]], pas ici.

## Concepts clés

### Poids, code, données : trois ouvertures distinctes
- La **Open Source AI Definition 1.0** de l'OSI (publiée en octobre 2024) exige, pour les paramètres, trois éléments sous des termes approuvés par l'OSI : les **paramètres**, le **code** complet d'entraînement et d'exécution, et des **informations sur les données** assez détaillées pour qu'une personne compétente reconstruise un système substantiellement équivalent. Les données elles-mêmes ne sont pas exigées. L'OSI précise que ses listes ne sont pas des certifications.
- Le **Model Openness Framework** (White et al., arXiv 2403.13784, v6 d'octobre 2024) classe la **complétude** en trois niveaux : Class III « Open Model » (architecture, poids, rapport technique, évaluations, fiches du modèle et des données), Class II « Open Tooling » (plus le code d'entraînement, d'inférence et d'évaluation), Class I « Open Science » (plus les jeux de données, les checkpoints intermédiaires, l'article). Sur la licence, il est binaire : un modèle sous licence à restrictions d'usage n'est pas compté comme ouvert.
- Liesenfeld et Dingemanse (FAccT '24) évaluent plus de 45 systèmes génératifs sur 14 dimensions d'ouverture : beaucoup sont « open weight at best », et l'ouverture est composite, pas binaire.

### Licences OSI contre licences d'éditeur
- **Apache-2.0** : usage, modification, redistribution libres ; licence de **brevets** expresse (§3) limitée aux revendications que la contribution enfreint nécessairement, résiliée si le licencié attaque pour contrefaçon de brevet ; obligations : fournir la licence, signaler les fichiers modifiés, conserver les notices. **MIT** : copie de la notice seulement, sans licence de brevets expresse. Aucune des deux ne pose de clause d'usage ni de seuil. Elles ne disent rien des données d'entraînement ni du droit d'auteur sur les sorties (lecture des textes, non citation).
- **Licences d'éditeur** : des textes propres, qui ajoutent des conditions. Rencontrées ici : Llama Community License, Gemma Terms of Use (génération 1 à 3), Qwen Community License 1.0 et Qwen3.8-Max License, « MIT modifié » de Mistral, Mistral Research License, RAIL. L'OSI a écrit dès 2023 que la licence de Llama 2 n'est « pas Open Source » (restriction de champ d'usage et de commercialisation).
- **La licence suit le dépôt, pas la famille.** Qwen3.8 : le 27 B est en Apache-2.0, Flash-Next en Qwen Community License 1.0, le 2,4 T en Qwen3.8-Max License. Mistral : Apache-2.0 pour Small 4 et Ministral 3, MIT modifié pour Medium 3.5. Et la **génération** la change : Gemma 1 à 3 sous Gemma Terms, Gemma 4 sous Apache-2.0.

### Les clauses à lire avant de livrer
- **Seuil** : d'utilisateurs actifs (Llama : 700 millions, au jour de la sortie de la version ; Qwen : 100 millions ou 20 M$ de revenu mensuel pour l'affichage du nom) ou de **revenu** (Mistral, MIT modifié : 20 M$ par mois, pour « votre société ou votre employeur », dérivés d'un tiers compris). Lire **de qui** le seuil s'apprécie : le licencié, ses affiliés, son employeur.
- **Politique d'usage** : incorporée par référence et modifiable par l'éditeur (Llama), ou réduite à une phrase (gpt-oss : respecter les lois applicables). Une politique externe change sans que le dépôt change.
- **Redistribution** : copie de la licence, fichier de notice, mention d'attribution (« Built with Llama »).
- **Dérivés et sorties** : Llama 4 impose le nom « Llama » au début du nom de tout modèle entraîné ou amélioré avec les matériaux **ou leurs sorties** et distribué ; Llama 2 interdisait d'utiliser les sorties pour améliorer un autre modèle de langage, Llama 4 impose le nom à la place. Gemma Terms (génération 1 à 3) répercutent les restrictions d'usage dans tout accord de distribution.
- **Service** : Qwen Community License 1.0 exige une licence séparée pour une activité « Model as a Service » — donner à un tiers accès à l'inférence ou au fine-tuning par API ou endpoint, avec un contrôle réel sur les entrées, paramètres ou données d'entraînement. L'usage interne qui n'expose ni modèle ni sorties à un tiers est exclu.
- **Géographie** : l'AUP de Llama 4 n'accorde pas les droits sur les modèles **multimodaux** à un individu domicilié dans l'UE ni à une société dont l'établissement principal y est ; les utilisateurs finaux d'un produit sont exemptés.
- **Retrait** : Gemma Terms (génération 1 à 3) réservent à Google le droit de restreindre l'usage « à distance ou autrement » ; Llama et Gemma Terms prévoient la résiliation avec suppression des copies.

### Héberger pour soi, pour un client, offrir un service
- **Pour soi** (usage interne) : la situation la plus sûre ; Qwen l'exclut expressément de sa clause de service.
- **Pour un client** : deux gestes distincts dans les textes. **Livrer les poids** au client est de la redistribution (licence jointe, notice, attribution). **Faire tourner un endpoint** que le client appelle est un service, et les Gemma Terms comptaient l'hébergement via API comme une « distribution ». Les questions à poser au texte : qui est le licencié, qui reçoit les poids, qui opère le serveur, et de qui s'apprécie un seuil.
- **Offrir un service à des tiers** : les seuils d'utilisateurs et la clause de service s'appliquent, et les licences RAIL exigent de faire respecter leurs restrictions d'usage à chaque utilisateur.

### Un modèle finetuné
- C'est un **dérivé** : la licence d'origine le suit. Llama : licence, notice, attribution et nom « Llama » s'attachent à tout dérivé distribué. Mistral MIT modifié : la clause de revenu vise les dérivés, « y compris ceux d'un tiers ». Gemma Terms : les « Model Derivatives » englobent les modèles obtenus par distillation. RAIL et Mistral Research License : les restrictions suivent le dérivé.
- **Adaptateur LoRA seul ou poids fusionnés** : aucun des textes lus ne mentionne adaptateur ni LoRA. La distinction se lit dans les textes de chaque licence, elle ne s'affirme pas ; voir [[LoRA et QLoRA]].

### Le cadre européen
- L'article 53(2) du règlement (UE) 2024/1689 dispense les fournisseurs de modèles à usage général publiés sous **licence libre et ouverte** de la documentation technique (53(1)(a)) et de l'information aux intégrateurs (53(1)(b)). Restent dues : la politique de respect du droit d'auteur et le résumé public du contenu d'entraînement. L'exemption ne joue **pas** pour un modèle à **risque systémique** (présomption au-delà de 10^25 FLOP, art. 51(2)). Le chapitre V s'applique depuis le 2025-08-02 ; les modèles déjà sur le marché à cette date ont jusqu'au 2027-08-02.
- Les lignes directrices de la Commission sur les modèles à usage général (2025) écartent de « libre et ouverte » les licences limitées à la recherche ou au non commercial, les seuils d'utilisateurs et les licences commerciales séparées pour certains usages ; elles qualifient de monétisation la double licence, le support obligatoire et l'hébergement exclusif payant. **Lecture de cette page, non tranchée par les sources** : une licence à seuil (Llama, Qwen, Mistral MIT modifié) n'ouvrirait donc pas l'exemption, Apache-2.0 et MIT oui. Un affineur ne devient fournisseur que si son calcul d'affinage dépasse environ un tiers du calcul d'entraînement d'origine, d'après ces lignes directrices.

## En pratique

- **Ouvrir le fichier `LICENSE` du dépôt précis**, pas la page de l'organisation ni un blog. Le champ `license:` des métadonnées et le fichier peuvent ne pas se recouper : Mistral Small 4 n'a aucun fichier `LICENSE`, seulement la mention Apache-2.0 dans sa carte ; les dépôts Gemma 4 n'en ont pas non plus, la licence est un lien vers le texte Apache de Google.
- **Noter trois choses** dans le cahier des charges : l'identifiant de la licence, la **date de lecture**, et le dépôt exact. La licence d'une famille change entre deux générations et entre deux tailles.
- **Décider qui est licencié** avant de livrer : l'ESN qui héberge, ou le client qui reçoit les poids et les opère. Ce choix fait passer un même modèle d'une clause à l'autre.
- **Avant tout finetuning livrable** : relire la clause de dérivé ; pour Llama, prévoir le nom imposé ; pour un MIT modifié à seuil, vérifier le revenu du licencié.
- **Le vault** range les fiches dans [[Comparatif - Modèles de langage open weights]] : Apache-2.0 sans condition pour [[gpt-oss]], Gemma 4 et le 27 B de [[Qwen]] ; conditions par modèle pour [[Mistral]] et le reste de Qwen.

## Approches voisines & alternatives

- [[Qwen]] · [[Mistral]] · [[Gemma]] · [[gpt-oss]] — les quatre familles, avec leur licence lue dépôt par dépôt.
- [[Comparatif - Modèles de langage open weights]] — ce que chaque licence permet à une ESN, famille par famille.
- [[Small Language Models]] — les modèles compacts exploitables en local, sans les répéter ici.
- [[Fine-tuning]] — ce qui produit un dérivé, donc ce qui déclenche la clause de dérivé ; [[LoRA et QLoRA]] pour l'adaptateur.
- [[Unsloth]] · [[TRL]] — finetuning de modèles sous licence d'éditeur ou Apache-2.0.
- [[vLLM]] · [[Ollama]] — les runtimes qui servent les poids, donc l'endroit où « héberger » devient un service.
- [[HuggingFace]] — d'où viennent les poids ; certains dépôts sont à accès sur demande.
- [[LLM benchmarks]] — le critère qui n'est pas ici : la licence se lit avant les classements.
- [[Fusion de modèles]] — un modèle fusionné hérite des licences de ses parents

## Pour aller plus loin

- Open Source Initiative, *The Open Source AI Definition 1.0* — https://opensource.org/ai/open-source-ai-definition
- White et al. (2024), *The Model Openness Framework* — https://arxiv.org/abs/2403.13784
- Liesenfeld et Dingemanse (2024), *Rethinking open source generative AI: open-washing and the EU AI Act*, FAccT '24 — https://facctconference.org/static/papers24/facct24-120.pdf
- Kapoor et al. (2024), *On the Societal Impact of Open Foundation Models* — https://arxiv.org/abs/2403.07918
- Règlement (UE) 2024/1689, article 53 et considérants 102 à 104 — https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Apache License 2.0 — https://www.apache.org/licenses/LICENSE-2.0.txt
- Llama 4 Community License et son AUP — https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE · https://github.com/meta-llama/llama-models/blob/main/models/llama4/USE_POLICY.md
- Gemma Terms of Use — https://ai.google.dev/gemma/terms
- Qwen Community License 1.0 — https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE
- Mistral, MIT modifié de Medium 3.5 — https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE
