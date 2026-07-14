---
galaxie: wiki
type: concept
nom: tool-use
alias: [function calling, appel d'outils, tool calling, appel de fonctions]
categorie: concept/llm
domaines: [ai-eng]
tags: [tool-use, structured-output, llm]
---

# tool-use

## Aperçu

- Mécanisme par lequel un LLM **appelle une fonction** : on lui déclare des outils (schémas), il émet un appel structuré (nom + arguments JSON), un exécuteur le lance, le résultat revient dans le contexte.
- Brique de base de tout agent. Cette page décrit le **mécanisme** (function calling) ; les stratégies de conception sont dans [[Tool use patterns]].

## Concepts clés

### Déclaration d'outil
- Un outil = **nom + description + schéma de paramètres typé** (JSON Schema). La clarté de la description et des types conditionne directement le taux de bon appel.

### Boucle d'appel
- Tour type : le modèle décide d'appeler, émet `{name, arguments}` → l'exécuteur appelle la vraie fonction → le **résultat** (ou l'erreur) est réinjecté → le modèle poursuit ou répond. C'est l'étape « action » de [[agent-loops]].

### Natif vs prompté
- **Natif** : l'API expose un champ `tools` et garantit un appel bien formé (souvent via [[Structured outputs|décodage contraint]]). **Prompté** : on décrit les outils en texte et on parse la sortie — plus fragile, utile sur modèles sans support natif.

### Appels parallèles
- Un même tour peut émettre plusieurs appels indépendants (*parallel tool calls*) — gain de latence, à réserver aux appels sans dépendance mutuelle.

### Lien aux sorties structurées
- Un appel d'outil **est** une sortie structurée conforme à un schéma : mêmes garanties, mêmes pièges de validation — d'où le tag commun `structured-output` (cf. [[Structured outputs]]).

## Les maths, simplement

- Choix d'outil vu comme un argmax sur le catalogue : $\hat{a} = \arg\max_{a \in \mathcal{A}} p_\theta(a \mid \text{contexte}, \text{schémas})$, où $\mathcal{A}$ est l'ensemble des outils déclarés.
- La probabilité de bon appel décroît quand $|\mathcal{A}|$ grandit ou que les schémas se recouvrent — peu d'outils, bien désambiguïsés, maximise $p_\theta$.

## En pratique

- Déclarer **peu d'outils, aux frontières nettes**, avec des paramètres stricts (types, enums) plutôt qu'une description floue.
- **Valider les arguments** avant exécution et borner les retries ; réinjecter l'erreur pour auto-correction — [[Dev/Services/Instructor|Instructor]], [[Dev/Services/PydanticAI|PydanticAI]] pour le typage + validation.
- Standardiser l'exposition des outils via [[mcp-protocol]] plutôt que recâbler chaque intégration à la main.
- Outillage de la boucle : [[Dev/Services/LangChain|LangChain]], [[Dev/Services/LangGraph|LangGraph]] ; passerelle multi-fournisseurs au format unifié : [[Dev/Services/LiteLLM|LiteLLM]].
- Piège : un outil à **effet de bord** (écriture, paiement) sans garde-fou transforme une hallucination en action réelle — cf. [[Reliability patterns]] et [[Tool use patterns]].

## Approches voisines & alternatives

- [[Tool use patterns]] — les **patrons** de conception bâtis sur ce mécanisme (sélection, robustesse, garde-fous).
- [[Structured outputs]] — sortie typée *sans* exécution ; le function calling en est l'extension agissante.
- [[agent-loops]] — l'appel d'outil est l'action de la boucle.
- [[mcp-protocol]] — standardise la **mise à disposition** des outils (client-serveur), au lieu du câblage ad hoc.
- [[Agent patterns]] — le patron ReAct repose entièrement sur l'appel d'outils.

## Pour aller plus loin

- Schick et al. (2023) — *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Documentation *tool use* / function calling des fournisseurs (Anthropic, OpenAI).
