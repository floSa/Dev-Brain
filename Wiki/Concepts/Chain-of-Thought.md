---
galaxie: wiki
type: concept
nom: Chain-of-Thought
alias: [CoT, chaîne de pensée, raisonnement pas à pas, self-consistency, zero-shot CoT]
categorie: concept/llm
domaines: [ai-eng]
tags: [prompting, reasoning, llm]
---

# Chain-of-Thought

## Aperçu

- Technique de prompting qui demande au modèle d'**expliciter les étapes intermédiaires** avant de donner la réponse finale, au lieu de répondre d'un coup.
- Gain net sur les tâches à plusieurs étapes (arithmétique, logique, raisonnement symbolique) : dérouler le raisonnement « pas à pas » améliore la justesse, surtout sur les grands modèles.

## Concepts clés

### Few-shot CoT vs zero-shot CoT
- **Few-shot CoT** : fournir des exemples où la réponse est accompagnée de son raisonnement détaillé.
- **Zero-shot CoT** : ajouter une simple amorce comme « *réfléchissons étape par étape* » suffit souvent à déclencher le déroulé, sans exemple.

### Self-consistency
- Échantillonner **plusieurs** chaînes de raisonnement (température > 0, cf. [[Decoding strategies]]) puis garder la réponse **majoritaire**. Marginaliser sur les chemins corrige les dérapages d'une chaîne unique — au prix de N générations.

### Extensions
- **Tree / Graph of Thoughts** : explorer plusieurs branches de raisonnement avec retour arrière, au-delà de la chaîne linéaire.
- Lien avec les **modèles de raisonnement** (à créer) : ceux-ci internalisent le CoT par entraînement (RL), produisant une longue réflexion avant la réponse, sans qu'on ait à la demander.

### Limites
- Le raisonnement affiché n'est pas toujours le raisonnement **réel** (rationalisation a posteriori) — utile pour la perf, pas comme preuve d'explicabilité.
- Coûteux en tokens ; inutile sur les tâches simples où il peut même nuire.

## Les maths, simplement

- Au lieu d'estimer $p(y \mid x)$ directement, on factorise via une trace de raisonnement $z$ : $p(y \mid x) = \sum_z p(y \mid z, x)\,p(z \mid x)$. Générer $z$ avant $y$ conditionne la réponse sur des étapes intermédiaires.
- **Self-consistency** approxime cette somme : tirer $z_1,\dots,z_N$ et voter sur les $y$ obtenus — une marginalisation par Monte-Carlo sur les chemins de raisonnement.

## En pratique

- Activer le CoT sur les tâches à **plusieurs étapes** ; l'éviter sur les tâches triviales (coût, latence).
- **Zero-shot CoT** d'abord (« étape par étape ») ; passer au **few-shot CoT** si la forme du raisonnement compte.
- Pour la fiabilité critique : **self-consistency** (plusieurs tirages + vote), en acceptant le surcoût.
- Séparer le **raisonnement** de la **réponse finale** dans le format de sortie (ex. balise / champ dédié) pour parser proprement ([[Structured outputs]]).
- Sur un modèle de raisonnement natif, ne pas re-imposer un CoT manuel : il le fait déjà en interne.

## Approches voisines & alternatives

- [[Prompt engineering]] — le CoT en est une technique phare ; tout le reste du prompt s'applique aussi.
- [[Decoding strategies]] — la self-consistency repose sur l'échantillonnage à température.
- [[Structured outputs]] — pour isoler proprement raisonnement et réponse.
- *Reasoning models* (à créer) — internalisent le CoT par entraînement plutôt que par prompt.

## Pour aller plus loin

- Wei et al. (2022) — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- Kojima et al. (2022) — *Large Language Models are Zero-Shot Reasoners* (« let's think step by step »).
- Wang et al. (2022) — *Self-Consistency Improves Chain of Thought Reasoning*.
