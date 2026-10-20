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
- **Un quatrième mécanisme ne génère rien.** Un [[Modèle de décision]] reçoit un état et des questions typées (`noul`, `choice`, `score`) et rend une probabilité par option, en une passe, sans un token de sortie : la garantie de type vient de la lecture sur un ensemble fermé de jetons, pas d'un masque. Elle ne garantit **que le type** : la réponse peut être fausse, et il n'existe aucune option « je ne sais pas ». Quatre fiches à poids ouverts ([[Clef]], [[d1-3B]], [[d1-omni-600M]], [[Laya]]) sont départagées dans [[Comparatif - Modèles de décision]].
- **Avant de prendre un modèle de décision, regarder le `if`.** Sur un banc public, une règle de deux lignes fait 91,8 % là où la question large posée à Jev fait 62,6 % ; [[Choisir entre règle, classifieur, modèle de décision et LLM]] donne les cinq conditions, [[Décomposer une question en signaux étroits]] la façon de lui poser la question, et [[Entraîner pour la calibration]] pourquoi un seuil de confiance ne se reprend pas d'un autre modèle.
- Les trois briques attaquent par trois bouts, et se choisissent sur le mécanisme, pas sur la syntaxe : [[Instructor]] valide et réessaie autour d'un modèle Pydantic, [[Outlines]] contraint le décodage par grammaire ou regex, [[Guidance]] entrelace contrôle de flux et génération dans un même programme.

## Choisir

- Un objet Pydantic en sortie, sur l'API d'un fournisseur → [[Instructor]].
- Une grammaire, une regex ou un JSON Schema strictement respectés, sur un modèle qu'on sert soi-même → [[Outlines]].
- Alterner texte libre, appels et champs contraints dans un même programme → [[Guidance]].
- Une décision (router, noter, filtrer, approuver) avec sa probabilité, sans générer de texte → [[Modèle de décision]] ; savoir d'abord si une règle suffit → [[Choisir entre règle, classifieur, modèle de décision et LLM]].
- Un modèle de décision à poids ouverts : sur un poste → [[d1-3B]] ou [[Laya]] ajusté ; sur un GPU de serveur, avec image, vidéo et Apache-2.0 → [[Clef]] ; avec de l'audio, à titre d'essai → [[d1-omni-600M]] ; la licence, la mémoire et les scores datés dans [[Comparatif - Modèles de décision]].
- Faire agir le modèle sur le monde plutôt que lui imposer une forme → [[Agents]].

<!-- AUTO:START -->
### Notions
- [[Constrained decoding]] — domaines : ai-eng
- [[Structured outputs]] — domaines : ai-eng

### Briques
- [[Guidance]] — Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing.
- [[Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[Outlines]] — Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas.
<!-- AUTO:END -->
