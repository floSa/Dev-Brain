---
role: notion
nom: Hallucinations des LLM
alias: [hallucination, hallucinations, confabulation, confabulations, factualité, fidélité au contexte, faithfulness hallucination, factuality hallucination, SelfCheckGPT, FActScore, entropie sémantique]
categorie: llm/modele
domaines: [ai-eng]
tags: [llm, llm-eval, reliability, calibration]
---

# Hallucinations des LLM

## Aperçu

- Une **hallucination** est une sortie fluide mais fausse ou sans appui : un fait inventé, une contradiction avec le texte fourni, une consigne détournée. Le modèle ne signale pas son doute.
- Le mot recouvre deux problèmes qui ne se règlent pas pareil : dire faux sur le **monde** (factualité) et s'écarter du **contexte donné** (fidélité). Mal les distinguer fait choisir le mauvais remède.
- Les sources lues ne s'accordent pas sur la fatalité du phénomène : voir *Causes* et *Désaccords*. Ce qui se mesure aujourd'hui, c'est un taux par tâche et par modèle, pas une propriété du « LLM en général ».

## Concepts clés

### Typologie : factualité contre fidélité

- **Ji et al. (2023)** distinguent l'hallucination **intrinsèque** (la sortie contredit la source) de l'**extrinsèque** (la sortie ne peut être ni confirmée ni contredite par la source). Pour eux, la *faithfulness* (cohérence avec la source) et la *factuality* (conformité aux faits du monde) sont deux notions : une phrase peut être fidèle à une source fausse.
- **Huang et al. (2023, publié en 2025)** bâtissent une taxonomie plus fine pour les LLM :
  - *factuality hallucination* : contradiction factuelle (erreur d'entité, erreur de relation) ou fabrication (non vérifiable, affirmation excessive) ;
  - *faithfulness hallucination* : incohérence avec la consigne, avec le contexte, ou **logique** (contradiction interne d'un raisonnement).
- Les vocabulaires divergent. Le papier FACTS Grounding (Google DeepMind, 2025) appelle « factualité » ce que Ji et Huang appellent fidélité au contexte. Chez Ji, l'extrinsèque signifie « non vérifiable depuis la source » ; chez Huang, « non vérifiable depuis la source **ni** depuis des bases externes ». Toujours relire la définition d'un benchmark avant d'en comparer les scores.

### Causes

- **Données : les faits vus une seule fois.** Kalai et Vempala (STOC 2024) démontrent qu'un modèle pré-entraîné **calibré** hallucine sur les faits « arbitraires » (dont la vérité ne se déduit pas des autres) à un taux au moins proche de la fraction de faits apparus **exactement une fois** dans les données d'entraînement (estimation de Good-Turing). La borne vaut même avec des données sans erreur et ne dépend pas de l'architecture. Les auteurs écrivent qu'il n'y a aucune raison statistique d'halluciner sur des faits répétés ni sur des faits systématiques comme l'arithmétique.
- **Entraînement et évaluation : deviner est récompensé.** Kalai, Nachum, Vempala et Zhang (OpenAI, 2025) ramènent la génération à une classification binaire « cette sortie est-elle valide ? » et montrent que l'erreur générative est bornée par le taux d'erreur de cette classification. Leur thèse porte surtout sur l'après : sous une notation 0/1, répondre « je ne sais pas » rapporte 0, soit moins qu'un pari ; un modèle qui devine toujours bat un modèle honnête. Les évaluations dominantes qu'ils passent en revue sont binaires. Leur remède : rendre le seuil de confiance explicite dans la consigne et dans la note (voir *Les maths, simplement*).
- **Décodage et architecture.** Ji et al. citent l'échantillonnage top-k et top-p (qui accroît la diversité) et l'*exposure bias* ; Huang et al. ajoutent la sur-confiance, le goulot du softmax et les échecs de raisonnement. Voir [[Decoding strategies]].
- **Corrélations parasites.** Wang et al. (2025) montrent des hallucinations produites avec une forte confiance quand une association apprise (nom de famille et nationalité, par exemple) l'emporte ; elles résistent à l'augmentation d'échelle et échappent aux détecteurs fondés sur la confiance (résumé lu seulement).
- **Raisonnement.** Les modèles de raisonnement ne sont pas exempts : Yin et al. (2025) rapportent que l'apprentissage par renforcement du raisonnement augmente l'hallucination d'**outils** (appeler un outil absent ou inadapté) ; Yao et al. (2025) concluent au contraire que les pipelines complets (SFT puis RL à récompense vérifiable) tendent à la réduire, et que la distillation seule ou le RL sans SFT en introduisent de plus subtiles (résumés lus seulement). Voir [[Reasoning models]].

### Mesure

- **SelfCheckGPT** (Manakul, Liusie, Gales, EMNLP 2023) : tirer N réponses au hasard ; un fait connu du modèle revient d'un tirage à l'autre, un fait inventé diverge. Aucune ressource externe, aucun accès aux probabilités. Sur 1 908 phrases annotées (WikiBio, texte de GPT-3), la variante par prompt atteint une AUC-PR de 93,4 sur les phrases non factuelles contre 73,0 pour un tirage aléatoire. Coût : N appels de plus et un LLM de vérification.
- **FActScore** (Min et al., EMNLP 2023) : découper un texte long en **faits atomiques** et mesurer la fraction soutenue par une source (Wikipédia). Sur des biographies : 42,5 % pour InstructGPT, 58,3 % pour ChatGPT, 71,5 % pour PerplexityAI. Limites écrites par les auteurs : mesure la **précision** et pas le rappel (une réponse courte et prudente n'est pas pénalisée), ne s'applique qu'à des faits non contestés.
- **Benchmarks de factualité** :
  - *TruthfulQA* (Lin et al., 2022) : 817 questions où des croyances humaines courantes induisent en erreur ; meilleur modèle de l'époque à 58 % de réponses vraies contre 94 % pour les humains.
  - *HaluEval* (Li et al., 2023) : 35 000 échantillons, dont des hallucinations générées par ChatGPT (donc plus proches des erreurs de ChatGPT que d'erreurs spontanées).
  - *SimpleQA* (Wei et al., OpenAI, 2024) : 4 326 questions courtes à réponse unique ; trois notes (correct, incorrect, **non tenté**) et un F-score qui récompense l'abstention.
  - *FACTS Grounding* (Jacovi et al., 2025) : fidélité d'une réponse à un document de 32 000 jetons au plus, notée par trois juges LLM dont l'auto-préférence (+3,23 % en moyenne) a été mesurée.
  - *FACTS Leaderboard* (décembre 2025) : factualité paramétrique, avec recherche, multimodale et ancrée ; Gemini 3 Pro y mène avec 68,8 et aucun modèle évalué n'atteint 70 %.
  - *Leaderboard d'hallucinations de Vectara* : taux d'incohérence factuelle de **résumés**, noté par le modèle HHEM ; Vectara précise que ce n'est pas une mesure définitive.
- **Juge LLM.** Utilisé partout, avec des biais : auto-préférence mesurée dans FACTS Grounding ; Janiak et al. (2025) trouvent que sur des questions-réponses un juge LLM s'aligne bien mieux sur l'humain que ROUGE. Voir [[LLM-as-judge]].

### Atténuations

- **Récupération et citations.** Le [[RAG]] réduit les hallucinations factuelles et ouvre la vérification, sans les supprimer : Huang et al. décrivent des défaillances propres (requêtes, sources, génération), Kalai et al. notent qu'une notation binaire récompense encore le pari quand la récupération échoue, et PerplexityAI copie parfois des sources fausses (FActScore).
- **Vérification.** *Chain-of-Verification* (Dhuliawala et al., Meta, 2023) : brouillon, questions de vérification, réponses **indépendantes** du brouillon, réponse finale. Sur des biographies (Llama 65B), le FActScore passe de 55,9 à 71,4 avec la variante *factored + revise*. Coût : plus de jetons, et seulement les erreurs factuelles directes.
- **Décodage.** *DoLa* (Chuang et al., 2023) contraste les couches tardives et précoces : +12 à +17 points absolus sur TruthfulQA pour la famille LLaMA, gains bien plus faibles sur d'autres jeux.
- **Entraînement.** *FactTune* (Tian et al., 2023) applique du DPO sur des préférences de factualité sans annotation humaine ; à 7B, 58 % d'erreurs factuelles en moins sur des biographies par rapport à Llama-2-chat. Plus récent : Chen et al. (octobre 2025) entraînent par RL avec une récompense binaire n'accordant 1 qu'à une sortie entièrement soutenue par la récupération ; ils annoncent 39,3 % d'hallucinations en moins en génération ouverte sur Qwen3 (résumé lu seulement).
- **Calibration et refus.** Kadavath et al. (2022) : les grands modèles sont bien calibrés sur des questions à choix multiples bien formatées et peuvent estimer P(True) sur leur propre réponse, avec une généralisation fragile d'une tâche à l'autre. *R-Tuning* (Zhang et al., NAACL 2024) apprend à s'abstenir sur ce que le modèle ne sait pas. Voir [[Calibration]].
- **Garde-fous.** Vérifier l'ancrage de la sortie avant de la livrer : voir [[Guardrails]].

### Limites des détecteurs

- **Entropie sémantique** (Farquhar et al., *Nature*, 2024) : tirer plusieurs réponses, les regrouper par sens, mesurer l'entropie des groupes. AUROC moyen de 0,790 sur 30 couples tâche-modèle contre 0,691 pour l'entropie naïve. Elle vise les **confabulations** (réponses arbitraires) ; les auteurs écrivent qu'elle ne voit pas les erreurs **systématiques** apprises des données.
- **Évaluer le détecteur sur la bonne règle.** Janiak et al. (EMNLP 2025) : la plupart des détecteurs étaient notés avec ROUGE contre une réponse de référence ; avec un juge aligné sur l'humain, l'AUROC chute jusqu'à 45,9 %, et de simples heuristiques de **longueur de réponse** égalent des détecteurs sophistiqués. Kulkarni et al. (2025) trouvent aussi que les métriques de détection s'alignent mal sur le jugement humain.
- **Généralisation.** Orgad et al. (ICLR 2025) : l'information de véracité se concentre dans des jetons précis, mais les détecteurs d'erreurs ne généralisent pas d'un jeu de données à l'autre, et un modèle peut encoder la bonne réponse tout en en produisant une fausse. Chen et al. (ACL 2026) proposent TRIVIA+ : un simple juge LLM y est compétitif et le bruit d'étiquettes dégrade tous les détecteurs (résumé et introduction lus).

### Désaccords entre sources, laissés tels quels

- **Inévitable ou atténuable.** Xu, Jain, Kankanhalli (2024) soutiennent par un argument de calculabilité que tout LLM utilisé comme résolveur général hallucinera. Kalai et Vempala bornent le phénomène aux faits arbitraires rares. Kalai et al. (2025) écrivent qu'un modèle qui répond toujours « je ne sais pas » n'a aucune erreur : la persistance viendrait des évaluations. Les trois énoncés portent sur des objets différents.
- **Benchmarks nouveaux ou notation réformée.** Kalai et al. plaident pour changer la notation des benchmarks existants plutôt que d'en ajouter. SimpleQA et FACTS Parametric ont déjà une classe « non tenté », mais FACTS note que le F1 et l'exactitude brute classent autrement : GPT-5 s'abstient dans 13,3 % des cas contre 1,9 % pour o3, avec une exactitude brute de 55,7 contre 57,0 mais un F1 de 59,7 contre 57,6.

## Les maths, simplement

- **Borne de Kalai et Vempala** (forme simplifiée) : taux d'hallucination ≳ MF − (erreur de calibration) − (termes en $1/\sqrt{n}$), où MF est la fraction des faits vus **une seule fois** parmi $n$ échantillons. Si 20 % des anniversaires d'un corpus n'apparaissent qu'une fois, un modèle calibré se trompera au moins vers 20 % du temps sur ce type de fait. Les constantes exactes ne sont pas recopiées ici : un doute existait sur 6 ou 7 devant $1/\sqrt{n}$, à relire dans l'article avant toute citation.
- **FActScore** : $\text{FActScore} = \frac{1}{|A|}\sum_{a \in A} \mathbb{1}[a \text{ est soutenu par la source}]$, où $A$ est l'ensemble des faits atomiques de la sortie. Un texte court et vide obtient un score élevé : la mesure ne voit pas le rappel.
- **Seuil de confiance** (Kalai et al. 2025) : si une erreur coûte $\lambda$ points, une bonne réponse en rapporte 1 et l'abstention 0, alors répondre est rentable quand la probabilité de justesse $p$ vérifie $p - (1-p)\lambda > 0$, soit $p > \lambda/(1+\lambda) = t$ avec $\lambda = t/(1-t)$. Les auteurs citent $t = 0{,}5$ (pénalité 1), $t = 0{,}75$ (pénalité 2) et $t = 0{,}9$ (pénalité 9).

## En pratique

- **Dire de quelle hallucination on parle** : fidélité à un contexte fourni (RAG, résumé) ou factualité du monde (question ouverte). Les métriques et les remèdes diffèrent.
- **Mesurer sur sa tâche et sur son modèle.** Un score de benchmark ne se transporte pas : les classements varient selon la métrique (exactitude brute ou F1) et le juge.
- **Autoriser l'abstention** dans ses propres évaluations : trois notes (correct, incorrect, non tenté) et une pénalité d'erreur explicite. Sans cela, l'évaluation pousse le modèle à parier.
- **Caler un détecteur sur un jugement humain** avant de lui confier un seuil de blocage, et le noter avec un juge validé plutôt qu'avec ROUGE. Un détecteur qui échoue hors de son jeu de données n'est pas un garde-fou.
- **Pour un RAG**, mesurer la fidélité à part de la récupération (voir [[RAG eval]]) ; la citation d'une source rend l'erreur vérifiable, pas absente.
- **Plusieurs échantillons coûtent cher** (SelfCheckGPT, entropie sémantique, CoVe) : les réserver à l'audit ou aux réponses à enjeu.

## Approches voisines & alternatives

- [[RAG]] — l'atténuation la plus déployée ; ne supprime pas l'hallucination.
- [[RAG eval]] — mesurer la fidélité d'une réponse à son contexte (faithfulness, groundedness).
- [[LLM eval metrics]] — le panorama des métriques dont celles de factualité.
- [[LLM benchmarks]] — où se placent TruthfulQA, SimpleQA et les suites de factualité.
- [[LLM-as-judge]] — le mécanisme sous-jacent de la plupart des mesures récentes, avec ses biais.
- [[Calibration]] — fiabilité des probabilités ; l'hypothèse de calibration est au cœur de la borne de Kalai et Vempala.
- [[Guardrails]] — vérification d'ancrage et validation en sortie.
- [[Perplexity]] — mesure de probabilité sur un corpus, distincte de la vérité des énoncés.
- [[Decoding strategies]] — le décodage comme cause et comme levier.
- [[Reasoning models]] — le raisonnement explicite ne garantit pas la factualité.
- [[Ragas]], [[DeepEval]], [[RAGChecker]], [[TruLens]], [[ARES]] — l'outillage qui note la fidélité des réponses d'un RAG.

## Pour aller plus loin

- Ji et al. (2023) — *Survey of Hallucination in Natural Language Generation*, ACM Computing Surveys ; arXiv 2202.03629.
- Huang et al. (2023, publié 2025) — *A Survey on Hallucination in Large Language Models*, ACM TOIS ; arXiv 2311.05232.
- Kalai et Vempala (2024) — *Calibrated Language Models Must Hallucinate*, STOC 2024 ; arXiv 2311.14648.
- Kalai, Nachum, Vempala, Zhang (2025) — *Why Language Models Hallucinate* ; arXiv 2509.04664.
- Manakul, Liusie, Gales (2023) — *SelfCheckGPT*, EMNLP ; arXiv 2303.08896.
- Min et al. (2023) — *FActScore*, EMNLP ; arXiv 2305.14251.
- Farquhar et al. (2024) — *Detecting hallucinations in large language models using semantic entropy*, Nature 630 ; DOI 10.1038/s41586-024-07421-0.
- Janiak et al. (2025) — *The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs*, EMNLP ; arXiv 2508.08285.
- Wei et al. (2024) — *Measuring short-form factuality in large language models* (SimpleQA) ; arXiv 2411.04368.
- Jacovi et al. (2025) — *The FACTS Grounding Leaderboard* ; arXiv 2501.03200 ; Cheng et al. (2025) — *The FACTS Leaderboard* ; arXiv 2512.10791.
- Dhuliawala et al. (2023) — *Chain-of-Verification Reduces Hallucination in Large Language Models* ; arXiv 2309.11495.
- Lin, Hilton, Evans (2022) — *TruthfulQA* ; arXiv 2109.07958.
- Kadavath et al. (2022) — *Language Models (Mostly) Know What They Know* ; arXiv 2207.05221.
- Tian et al. (2023) — *Fine-tuning Language Models for Factuality* ; arXiv 2311.08401.
- Xu, Jain, Kankanhalli (2024) — *Hallucination is Inevitable* ; arXiv 2401.11817.
- Vectara — leaderboard d'hallucinations de résumés (HHEM), dépôt GitHub `vectara/hallucination-leaderboard`, README lu le 2026-10-02.
- Lus au niveau du résumé ou de l'introduction seulement : Yin et al. (arXiv 2510.22977), Yao et al. (2505.23646), Wang et al. (2511.07318), Chen T. et al. (2510.17733), Chen W. et al. (2605.11330), Kulkarni et al. (2504.18114), Orgad et al. (2410.02707).
