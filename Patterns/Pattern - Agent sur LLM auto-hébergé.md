---
role: pattern
contexte: Piloter un agent prêt à l'emploi avec un modèle servi sur sa propre machine ou son propre réseau, sans dépendre d'une API cloud — le harnais d'un côté, le serveur d'inférence de l'autre.
services_cles: [LM Studio, Ollama, vLLM, llama.cpp, OpenClaw, Hermes Agent, LM Studio Bionic]
projets_appliques: []
tags: [pattern, agents, llm, local-llm, tool-use]
---

# Pattern — Agent sur LLM auto-hébergé

## Contexte

Faire tourner un agent complet — celui qui lit des fichiers, exécute des commandes, appelle des outils — en gardant l'inférence **chez soi**. Motivations habituelles : confidentialité, coût nul à l'usage, absence de dépendance à un fournisseur, ou simple envie de comprendre la mécanique.

Le montage se lit dans le vocabulaire de la triade (cf. [[Harnais d'agent]]) : on choisit un **harnais**, on lui sert un **modèle**, l'**agent** est le résultat. Les deux couches sont indépendantes, reliées par un contrat étroit — et c'est précisément ce contrat qui casse en pratique.

## Stack

**Couche serving** (le modèle) :
- [[LM Studio]] — GUI, gestion des modèles, endpoint OpenAI-compatible ; la plus simple sur poste de travail
- [[Ollama]] — démon léger, une commande par modèle ; le plus répandu côté serveur
- [[vLLM]] / [[SGLang]] — débit GPU, endpoint partagé pour plusieurs agents ou utilisateurs
- [[llama.cpp]] — contrôle bas niveau, matériel modeste

**Couche harnais** (l'agent) :
- [[OpenClaw]] — accès par messageries, résident sur serveur
- [[Hermes Agent]] — mémoire persistante et skills auto-créés, résident sur serveur
- [[LM Studio Bionic]] — application de bureau, **couplée à son propre runtime**

**Contrat entre les deux** : un endpoint HTTP, du tool calling fonctionnel, une fenêtre de contexte suffisante.

## Décisions clés

### 1. Toutes les combinaisons ne sont pas possibles

| Serving | → OpenClaw | → Hermes Agent | → Bionic |
|---|---|---|---|
| LM Studio | oui, stack recommandée | oui | oui, natif |
| Ollama | oui, **via l'API native** | oui | non |
| vLLM / SGLang | oui | oui | non |
| llama.cpp | oui | oui | non |

[[LM Studio Bionic]] n'accepte pas d'endpoint arbitraire : il consomme le runtime LM Studio, une machine du réseau via LM Link, ou le cloud de l'éditeur. Vouloir le nourrir avec Ollama est une impasse — c'est le seul harnais fermé des trois.

### 2. « OpenAI-compatible » ne suffit pas à garantir le tool calling

Le piège le plus coûteux du montage. La documentation OpenClaw est explicite : **ne pas utiliser l'endpoint `/v1` d'Ollama**, qui casse le tool calling — le modèle recrache alors le JSON d'appel d'outil en texte brut au lieu de déclencher l'outil. Il faut viser l'API **native** :

```
baseUrl: "http://host:11434"   # sans /v1
api: "ollama"
apiKey: "ollama-local"          # marqueur local accepté
```

Pour les autres backends locaux (vLLM, SGLang, llama.cpp, LocalAI, text-generation-webui), l'endpoint OpenAI-compatible convient — avec `api: "openai-responses"` quand le serveur le gère, `openai-completions` sinon.

### 3. La fenêtre de contexte est le vrai plancher

C'est ici que le montage échoue le plus silencieusement. [[Hermes Agent]] **exige 64 000 tokens** et refuse de démarrer en dessous : prompt système et schémas d'outils consomment déjà 4 à 8 k avant le moindre travail utile.

Or [[Ollama]] sert **4 096 tokens par défaut**. Il faut donc forcer :

```bash
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```

et faire correspondre le `context_length` côté harnais. Sans cela : refus au démarrage, ou pire, troncature silencieuse de l'historique en cours de tâche.

### 4. Le tool calling s'active explicitement selon le moteur

| Moteur | Ce qu'il faut poser |
|---|---|
| llama.cpp | `--jinja` |
| vLLM | `--enable-auto-tool-choice --tool-call-parser hermes` |
| SGLang | `--tool-call-parser qwen` |
| Ollama | actif par défaut sur les modèles compatibles |
| LM Studio | version 0.3.6+, modèle à support natif |

Le parser dépend de la **famille du modèle**, pas du serveur : un mauvais parser produit des appels d'outils muets.

### 5. Le modèle doit être capable d'agir, pas seulement de discuter

Un modèle qui converse bien peut être inutilisable en agent : les appels d'outils en chaîne demandent de la rigueur de format sur des dizaines de tours. Compter **32 Go de RAM ou de VRAM** pour un modèle réellement capable, et privilégier les familles entraînées au tool use. En dessous, l'agent tourne, mais échoue une étape sur trois — et la fiabilité par étape se compose de façon multiplicative (cf. [[Harnais d'agent]]).

### 6. Savoir quand renoncer au local

Le tout-local n'est pas une fin en soi. Une tâche longue et complexe sur un petit modèle coûte plus cher en temps humain qu'un appel cloud. Les harnais prévoient d'ailleurs la bascule : LM Studio Secure Cloud pour Bionic, [[OpenRouter]] ou tout endpoint distant pour OpenClaw et Hermes. Le montage local garde son sens pour la **confidentialité** et le **volume**, moins pour la performance brute.

## Pièges

- **Endpoint `/v1` d'Ollama avec OpenClaw** : tool calling cassé, aucune erreur explicite. Le symptôme est un agent qui « répond » au lieu d'agir.
- **Contexte par défaut à 4 096** : l'erreur la plus fréquente, et la plus déroutante quand elle se manifeste par une troncature en cours de route.
- **Attribuer au modèle un échec du montage** : outil mal déclaré, parser inadapté, historique tronqué — changer de modèle ne corrige rien. Diagnostiquer la couche avant de la remplacer.
- **Sous-dimensionner le matériel** : un modèle qui déborde de la VRAM bascule en RAM et rend l'agent inutilisable en pratique.
- **Croire le local plus sûr par nature** : l'inférence ne quitte pas la machine, mais l'agent garde shell et fichiers. L'isolation reste à faire — cf. [[Sandboxing de code généré]].
- **Configuration datée** : ces options bougent vite (OpenClaw publie plusieurs fois par semaine). Les invariants — contrat d'endpoint, plancher de contexte, activation du tool calling — tiennent ; les noms de clés, non. État vérifié en **août 2026**.

## Voir aussi

- [[Harnais d'agent]] — la décomposition modèle / harnais / agent qui structure ce montage
- [[agent-loops]], [[Tool use patterns]], [[Context engineering]] — la mécanique interne du harnais
- [[Sandboxing de code généré]] — isoler l'exécution, indépendamment du lieu d'inférence
- [[Comparatif - Exécution & serving LLM]] — choisir la couche serving
- [[Comparatif - Frameworks LLM]] — choisir la couche harnais
