---
galaxie: wiki
type: concept
nom: Prompt engineering
alias: [conception de prompts, prompt design, few-shot prompting, in-context learning]
categorie: concept/llm
domaines: [ai-eng]
tags: [prompting, llm]
---

# Prompt engineering

## Aperçu

- Art de **formuler l'entrée** d'un LLM — instructions, exemples, format, rôle — pour obtenir la sortie voulue, sans toucher aux poids du modèle.
- Premier levier à essayer : rapide, sans entraînement, réversible. On ne paie qu'en tokens et en itérations, pas en GPU.

## Concepts clés

### In-context learning
- Le modèle apprend la tâche **à partir des exemples du prompt**, à l'inférence, sans mise à jour de poids. **Zero-shot** (consigne seule), **few-shot** (quelques démonstrations) : ajouter des exemples bien choisis améliore souvent nettement la fiabilité.

### Anatomie d'un prompt
- **Rôle / système** : qui parle, ton, contraintes globales.
- **Instruction** : la tâche, explicite et non ambiguë.
- **Contexte** : données utiles injectées ([[RAG]], documents).
- **Exemples** : démonstrations entrée→sortie (few-shot).
- **Format de sortie** : ce qu'on attend, idéalement contraint ([[Structured outputs]]).

### Techniques courantes
- **Décomposer** la tâche, demander un **raisonnement explicite** ([[Chain-of-Thought]]), donner un **format** strict, fixer un **persona**, fournir des **garde-fous** (« si tu ne sais pas, dis-le »).
- **Sensibilité** : la sortie dépend de la formulation, de l'ordre des exemples, voire de la ponctuation. D'où l'itération empirique.

### Prompting manuel vs optimisation
- À la main, on itère au jugé. Quand le besoin se systématise, on passe à l'**optimisation automatique** ([[Dev/Services/DSPy|DSPy]]) qui compile des prompts à partir d'exemples et d'une métrique.

## Les maths, simplement

- Pas de formule : le prompt $x$ conditionne la distribution $p(y \mid x)$ apprise au pré-entraînement. Le few-shot exploite cette conditionnelle — les démonstrations déplacent la masse de probabilité vers la forme de réponse attendue, sans rien réapprendre.

## En pratique

- Commencer **simple et explicite**, puis ajouter des exemples seulement si nécessaire.
- **Mesurer** : un petit jeu de cas de test vaut mieux que l'impression « ça a l'air mieux » ([[Dev/Services/DSPy|DSPy]], eval).
- Contraindre la sortie ([[Structured outputs]]) plutôt que parser du texte libre fragile.
- Distinguer trois leviers, du moins au plus coûteux : **prompting** → récupération de contexte ([[RAG]]) → entraînement ([[SFT]]). Essayer dans cet ordre.
- Ne pas confondre avec le [[Context engineering]] : le prompting travaille la **formulation**, l'ingénierie de contexte le **quoi** et le **combien** dans la fenêtre.

## Approches voisines & alternatives

- [[Chain-of-Thought]] — technique de prompting qui fait expliciter le raisonnement avant la réponse.
- [[Context engineering]] — gère ce qui entre dans la fenêtre ; complémentaire de la formulation.
- [[Structured outputs]] — contraindre le format de sortie, prolongement naturel du prompt.
- [[SFT]] — quand le prompting plafonne, entraîner le modèle sur des exemples ; plus coûteux, plus durable.
- [[Dev/Services/DSPy|DSPy]] — Programmation et optimisation de prompts — déclare des signatures et compile les prompts (ou un fine-tune) à partir d'exemples et d'une métrique, plutôt que de bricoler des chaînes de caractères.

## Pour aller plus loin

- Brown et al. (2020) — *Language Models are Few-Shot Learners* (GPT-3, in-context learning).
- Guides de prompting des fournisseurs (Anthropic, OpenAI) — bonnes pratiques et exemples.
