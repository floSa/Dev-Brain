---
role: hub
nom: Sortie typée
pitch: Obtenir du modèle un objet conforme à un schéma plutôt que du texte à parser.
domaines: [ai-eng]
tags: [structured-output, decoding, data-validation]
---

# Sortie typée

> Obtenir du modèle un objet conforme à un schéma plutôt que du texte à parser.

## Ce qu'il faut comprendre

- Ce dossier garantit une **forme**, il ne déclenche aucun **effet**. C'est la confusion la plus fréquente du domaine : la sortie structurée contraint la génération, le tool use fait exécuter une fonction. La première ne fait rien arriver, le second n'assure aucune forme — cf. [[tool-use]], dans [[Agents]].
- **Trois mécanismes de force croissante**, et ils ne se valent pas. Le *JSON mode* d'un fournisseur promet du JSON valide, pas votre schéma. Le *prompt + validation + retry* rattrape après coup et se paie en appels. Le [[Constrained decoding]] masque à chaque pas les tokens qui violeraient la grammaire : la validité est **garantie par construction**, sans parsing fragile. [[Structured outputs]] pose le cadre des trois.
- La contrainte se paie : un schéma trop rigide **dégrade le contenu** avant de dégrader la forme. Le modèle remplit les champs qu'on lui impose, y compris quand il n'a rien à y mettre.
- **Un quatrième mécanisme ne génère rien.** Un [[Modèle de décision]] reçoit un état et des questions typées (`noul`, `choice`, `score`) et rend une probabilité par option, en une passe, sans un token de sortie : la garantie de type vient de la lecture sur un ensemble fermé de jetons, pas d'un masque. Elle ne garantit **que le type** : la réponse peut être fausse, et il n'existe aucune option « je ne sais pas ». Les modèles de décision à poids ouverts n'ont pas de fiche : la notion les cite en texte simple.
- **Avant de prendre un modèle de décision, regarder le `if`.** Sur un banc public, une règle de deux lignes fait 91,8 % là où la question large posée à Jev fait 62,6 % ; [[Choisir entre règle, classifieur, modèle de décision et LLM]] donne les cinq conditions, [[Décomposer une question en signaux étroits]] la façon de lui poser la question, et [[Entraîner pour la calibration]] pourquoi un seuil de confiance ne se reprend pas d'un autre modèle.
- Les trois briques attaquent par trois bouts, et se choisissent sur le mécanisme, pas sur la syntaxe : [[Instructor]] valide et réessaie autour d'un modèle Pydantic, [[Outlines]] contraint le décodage par grammaire ou regex, [[Guidance]] entrelace contrôle de flux et génération dans un même programme.

## Choisir

- Un objet Pydantic en sortie, sur l'API d'un fournisseur → [[Instructor]].
- Une grammaire, une regex ou un JSON Schema strictement respectés, sur un modèle qu'on sert soi-même → [[Outlines]].
- Alterner texte libre, appels et champs contraints dans un même programme → [[Guidance]].
- Une décision (router, noter, filtrer, approuver) avec sa probabilité, sans générer de texte → [[Modèle de décision]] ; savoir d'abord si une règle suffit → [[Choisir entre règle, classifieur, modèle de décision et LLM]].
- Faire agir le modèle sur le monde plutôt que lui imposer une forme → [[Agents]].

<!-- AUTO:START -->
### Notions
- [[Choisir entre règle, classifieur, modèle de décision et LLM]] — domaines : ai-eng, ml-eng
- [[Constrained decoding]] — domaines : ai-eng
- [[Décomposer une question en signaux étroits]] — domaines : ai-eng, ml-eng
- [[Entraîner pour la calibration]] — domaines : ai-eng, ml-eng
- [[Modèle de décision]] — domaines : ai-eng, ml-eng
- [[Structured outputs]] — domaines : ai-eng

### Briques
- [[Clef]] — Famille de modèles de décision de Cloudflare à poids ouverts (Apache-2.0) — Clef 27 Md, Clef-flash 9 Md et Clef-omni 30 Md MoE : un état et des questions typées donnent une probabilité par option en une passe, sans texte ; entrée texte, image et vidéo (audio pour Clef-omni) ; 54,7, 18,8 et 70,5 Go en BF16, donc un GPU de serveur.
- [[d1-3B]] — Modèle de décision à poids ouverts de Liquid AI (3,1 Md, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel, à lire avant de livrer chez un client) — un état en texte ou en image et des questions typées donnent une probabilité par option en une passe, sans texte ; 6,25 Go en BF16, 8 ms sur RTX 4090 et 30 ms sur Apple M5 Pro selon Liquid.
- [[d1-omni-600M]] — Modèle de décision expérimental à poids ouverts de Liquid AI (587 M, LFM Open License : gratuit sous 10 M$ de chiffre d'affaires annuel) — un état en texte avec une image ou un clip audio de 30 s en anglais donne des probabilités typées en une passe ; 2,35 Go en FP32 ; aucune latence publiée par l'éditeur ; 2 documents sur 8 triés dans l'essai d'un tiers.
- [[Guidance]] — Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing.
- [[Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[Laya]] — Modèle de décision à poids ouverts de Convai Innovations (Apache-2.0), à ajuster avant usage — encodeur ModernBERT de 421 M (mmBERT de 322 M en multilingue) dont les poids de base font 0,362 sur son banc, sous la classe majoritaire (0,461), contre 0,766 pour le checkpoint ajusté ; texte seul, 512 à 1 024 tokens de contexte ; 0,84 Go en FP16, 33 ms sur Tesla T4 en multilingue.
- [[Outlines]] — Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas.

<!-- AUTO:END -->
