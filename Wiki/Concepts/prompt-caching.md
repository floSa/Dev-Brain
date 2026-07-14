---
galaxie: wiki
type: concept
nom: prompt-caching
alias: [prompt caching, cache de préfixes de prompt, prefix caching, cache de prompt, context caching]
categorie: concept/llm
domaines: [ai-eng]
tags: [caching, inference-optimization, llm, context-engineering]
---

# prompt-caching

## Aperçu

- Mettre en cache le **préfixe** d'un prompt côté serveur pour ne pas le recalculer à chaque requête. Quand un long préfixe stable (system prompt, few-shot, documents, définitions d'outils) est réutilisé, le fournisseur réutilise l'état d'attention déjà calculé.
- Gain : **latence** (time-to-first-token) et **coût** (les tokens d'entrée mis en cache sont facturés bien moins cher). La génération, elle, a toujours lieu.

## Concepts clés

### Mécanisme : le KV-cache réutilisé
- S'appuie directement sur le **KV-cache** et le **prefix caching** du serving (→ [[Inference optimization]]). Un préfixe identique ⇒ on saute son recalcul d'attention.

### Contrainte d'ordre
- Seul un préfixe **exactement identique** (mêmes tokens, même ordre) est réutilisable : un seul caractère qui change en tête invalide tout ce qui suit.
- Conséquence de conception : mettre le **stable en tête** (instructions, contexte, outils) et le **variable en queue** (la question). C'est un point d'[[Context engineering]].

### TTL et trafic
- Le cache **expire** (de quelques minutes à plus, selon le fournisseur) ; il faut un trafic régulier pour le garder chaud, sinon on repaie le préfixe.

### Côté API
- Anthropic (`cache_control` explicite, breakpoints), OpenAI (automatique sur les longs préfixes), Gemini (context caching explicite). Facturation distincte écriture vs lecture du cache selon le fournisseur.

### À ne pas confondre avec le cache de réponses
- Ici on réutilise le **calcul du préfixe** ; l'appel et la génération ont lieu. Le [[LLM caching|cache de réponses]] court-circuite l'appel **entier** sur une requête déjà vue.

## Les maths, simplement

- Coût d'entrée $\approx n_{\text{cache}} \cdot r + n_{\text{frais}}$, où $n_{\text{cache}}$ = tokens servis depuis le cache, $r$ = ratio de prix d'un token caché (souvent ~0,1) et $n_{\text{frais}}$ = tokens non cachés.
- Plus le préfixe stable est **long et réutilisé**, plus l'économie est forte. Un préfixe court ou rarement réutilisé ne franchit pas le seuil et n'apporte rien.

## En pratique

- Structurer le prompt en couches **stable → variable** ; regrouper documents et instructions en tête.
- Viser un préfixe assez long pour franchir le seuil minimal de mise en cache du fournisseur ; surveiller le **taux de hit**.
- Couplage RAG : le contexte récupéré change à chaque requête (peu cachable), mais le system prompt + les définitions d'outils, eux, le sont — d'où l'intérêt de les isoler en tête.

## Approches voisines & alternatives

- [[Inference optimization]] — le socle technique (KV-cache, prefix / RadixAttention) sur lequel ceci repose.
- [[LLM caching]] — le cran au-dessus : cache de la réponse entière, au niveau applicatif.
- [[Context engineering]] — l'organisation du contexte conditionne directement ce qui est cachable.

## Pour aller plus loin

- Documentation Anthropic — *Prompt caching*.
- Documentation OpenAI — *Prompt caching*.
- Kwon et al. (2023) — *PagedAttention* / Zheng et al. (2024) — *SGLang RadixAttention* (prefix caching côté serveur).
