---
name: planifier-projet
description: |
  Cadre un nouveau projet par une série de questions, une à la fois, puis choisit
  les technologies avec le DevBrain et initialise le projet avec ses règles écrites.
  À utiliser dès que l'utilisateur démarre ou décrit un projet : « je veux une
  appli qui fait X », « nouveau projet », « quel stack », « aide-moi à cadrer »,
  « initialise le projet », ou l'appel direct du skill. Générique : fonctionne avec
  tout agent qui sait lire des fichiers et lancer une commande.
---

# planifier-projet

Cadrer, choisir, initialiser. Dans cet ordre. Rien n'est écrit avant la validation.

## Comment parler à l'utilisateur

- Court, direct, impersonnel. Phrases courtes. Pas de formule de politesse, pas de blabla.
- Une seule question par message. Toujours avec la réponse proposée et sa raison en une ligne.
- Réfléchir longuement en interne. Ne montrer que la conclusion.
- Nommer les choses : jamais d'option réduite à une lettre.
- Si un outil de questions à choix existe, l'utiliser, mais toujours **une** question par appel. Sinon, poser la question en texte simple. Ça doit marcher dans tous les cas.

## Règles de conduite

- **Rien de bloquant.** À tout moment l'utilisateur peut dire « passe » (saute la question), « propose maintenant » (va à l'étape 3 avec ce qu'on a, hypothèses signalées) ou « stop ».
- **Ne pas redemander ce qui est dit.** Lire le premier message avant toute question. Une question dont la réponse y figure se saute. Une question dont la réponse ne change aucun choix se saute aussi.
- **Arrêt des questions** : quand la réponse suivante est prévisible, ou après 10 questions.
- **Challenger une fois.** Si l'utilisateur choisit autre chose que ce que le DevBrain indique : une phrase (« Le brain donne Y pour ce cas : <raison>. Raison de X ? »), noter la réponse, puis suivre son choix. Jamais de débat en boucle.

Fichiers de ce skill, à côté de ce fichier :
`questions.json` (la banque de questions), `scripts/sonde.py`, `scripts/candidats.py`,
`scripts/garde_fous.sh`, `modeles/`. Le DevBrain se trouve par `DEVBRAIN_PATH`, sinon
`~/Projets/DevBrain`. Sans DevBrain accessible, le dire et continuer en « hors DevBrain ».

## Étape 0 — Lire

Lire le message de l'utilisateur. Relever en silence : le type de projet (voir `par_type.reconnaitre` dans `questions.json`), les réponses déjà données, les technologies déjà citées. Ne rien dire encore.

## Étape 1 — Questions génériques

Parcourir `generiques` dans l'ordre. Pour chaque question : la sauter si son `saute_si` apparaît dans le message, ou si son `si` n'est pas vrai. La question `git` ne se saute jamais.

À la question `machine_finale`, lancer d'abord :

```bash
python3 scripts/sonde.py
```

Montrer le résumé en trois ou quatre lignes, puis poser la question. Si la machine n'est pas la machine finale, poser les questions de la machine cible : GPU, mémoire, accès réseau. Sous WSL sans GPU détecté, demander si un GPU existe côté Windows.

Les services déjà en place (vLLM, Postgres, Docker, Redis…) sont des contraintes : ne pas proposer leur doublon.

## Étape 2 — Questions du projet

Prendre les questions de `par_type` pour le type reconnu. Si le type est ambigu, le demander en une question. Si aucune banque ne convient, inventer des questions logiques sur l'application : ce qui entre, ce qui sort, le volume, la fréquence, qui s'en sert, ce qui doit être mesuré. La banque est un socle, pas un plafond. Même règles : une à la fois, réponse proposée, sauter l'inutile.

## Étape 3 — Choisir les technologies

C'est ici, et seulement ici, qu'on interroge le DevBrain. Procéder besoin par besoin (base de données, modèle, interface, orchestration, tests, documentation…) :

1. Si le domaine est incertain, lire `AI/index/carte.md` (9 Ko) et le hub du domaine.
2. Lire le comparatif du domaine, s'il existe :
   `python3 scripts/candidats.py comparatif --categorie <domaine>`
3. Lister les candidats, filtrés par les réponses :
   `python3 scripts/candidats.py besoin --categorie <domaine> --commercial <oui|non> --sur-site`
   Ajouter `--langage`, `--famille`, `--exclure <déjà en place>` si utile.
4. Retenir 2 ou 3 candidats. N'ouvrir que leurs pages, et seulement les sections « Prendre si / Écarter si », « Pièges » et « Retours ».
5. Vérifier la fraîcheur des deux finalistes : activité récente du dépôt, pas archivé. Si le réseau manque, le dire.
6. Écarter ce qui est déjà en place, ce que la licence interdit, ce qui est déprécié. Dire pourquoi.
7. Si le DevBrain ne couvre pas le besoin, proposer quand même, en le marquant **hors DevBrain**.

À égalité, préférer ce que l'agent de développement connaît bien. Si le journal de projets (`candidats.py` affiche `projets N`) montre un choix déjà éprouvé, le dire.

Proposer aussi 2 à 4 notions du DevBrain à relire avant de partir, prises dans le même dossier que les briques retenues. Seulement si elles aident.

Règles et patterns : `python3 scripts/candidats.py regles --mot <langage ou sujet>`. Lire les lignes `MUST` des règles pertinentes.

## Étape 4 — Proposition et débat

Une proposition courte :

```
Besoin : choix retenu — pourquoi (deux lignes). Écarté : X (raison), Y (raison).
```

Une ligne par besoin. Mentionner « hors DevBrain » quand c'est le cas. Puis demander : validé, infirmé, ou à discuter. Si infirmé : ajouter la contrainte et refaire l'étape 3 pour ce besoin seulement.

## Étape 5 — Initialiser (après validation seulement)

Écrire dans le **dossier du projet**, jamais dans le DevBrain. Adapter au poids du projet : jetable = `AGENTS.md` très court et un `docs/cadrage.md` de cinq lignes, rien d'autre. Durable ou livrable = le jeu complet.

Chaque chose va là où elle doit aller (modèles dans `modeles/`) :

| Fichier | Contenu |
|---|---|
| `AGENTS.md` | Ce qui change un geste de l'agent à chaque tâche : commandes, identité git, aucun co-auteur, tests, règles `MUST` (dix au plus), ton, renvois. Quarante lignes au plus. |
| `docs/cadrage.md` | Les réponses, la machine, les contraintes. |
| `docs/decisions/NN-sujet.md` | Un fichier par choix technique : retenu, écartés, raisons, source. |
| `docs/specification.md` | Ce que fait le projet, critères de réussite. |
| `README.md` | Présentation pour qui arrive. |

Un choix technique (« base de données : Postgres ») va dans `docs/decisions/`, pas dans `AGENTS.md`. Si l'agent de développement n'est pas Claude, `AGENTS.md` reste le fichier de consignes ; ajouter le fichier propre à cet agent seulement s'il ne lit pas `AGENTS.md`, avec un simple renvoi.

Puis :

1. Régler l'identité git et installer les contrôles de commit (refus de tout co-auteur, refus de la mauvaise identité), avec l'accord de l'utilisateur :
   `bash scripts/garde_fous.sh <projet> "<nom>" "<adresse>"`
2. Proposer le journal : une page `Projects/<projet>.md` dans le DevBrain (modèle `modeles/journal-projet.md`). **Seulement si l'utilisateur dit oui.** C'est la seule écriture permise dans le DevBrain, et elle se clôt avec `cloturer-brain`.
3. Dire en trois lignes ce qui a été écrit et où.

## Ne jamais

- Écrire un fichier avant la validation de l'étape 4.
- Écrire dans le DevBrain sans accord, hors `Projects/`.
- Proposer une brique absente du DevBrain sans la marquer « hors DevBrain ».
- Proposer une brique `deprecated` sans le dire.
- Mettre dans `AGENTS.md` ce qui est un choix technique ou un compte rendu.
- Poser plusieurs questions dans le même message.
