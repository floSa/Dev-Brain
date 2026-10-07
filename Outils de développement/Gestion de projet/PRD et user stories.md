---
role: notion
nom: PRD et user stories
alias: [PRD, product requirements document, document d'exigences produit, user story, user stories, histoires utilisateur, job stories, critères d'acceptation, INVEST]
categorie: devtools/projet
domaines: [ai-eng, data-eng]
tags: [project-management, spec-driven, agents]
---

# PRD et user stories

## Aperçu

- Le **PRD** (*product requirements document*) dit **quoi** construire et **pourquoi** : le problème, pour qui, jusqu'où, comment savoir que c'est réussi. Il ne dit pas comment.
- Les **user stories**, les **job stories** et les **critères d'acceptation** découpent ce quoi en unités qu'on peut estimer, livrer et vérifier.
- Pour un agent de code, c'est l'entrée de la chaîne décrite dans [[Développement piloté par la spécification]]. La forme compte moins que la précision des critères.

## Concepts clés

### Contenu minimal d'un PRD

Les guides s'accordent sur un noyau, à peu près toujours le même :

| Section | Contenu | Piège courant |
|---|---|---|
| Problème | ce qui ne va pas, pour qui, avec quelle preuve | décrire la solution à la place |
| Utilisateurs | qui est concerné, dans quelle situation | « tout le monde » |
| Objectifs et non-objectifs | ce qui compte, et ce qui est écarté explicitement | oublier les non-objectifs, qui bornent le périmètre |
| Périmètre | première version, ce qui attend | périmètre qui grossit sans le dire |
| Exigences | ce que le produit doit faire, vérifiable | mélanger exigence et solution technique |
| Métriques | comment mesurer le succès, avec une valeur cible | métrique de vanité, sans seuil |
| Questions ouvertes | décisions en attente, avec un responsable | les laisser en suspens dans le texte |

### User stories

Format courant : **En tant que** <type d'utilisateur>, **je veux** <action>, **afin de** <bénéfice>. La carte est un rappel d'avoir la conversation, pas la spécification complète. Ron Jeffries les résume par trois C : *Card* (la carte), *Conversation* (la discussion), *Confirmation* (les critères d'acceptation).

Origine : Kent Beck, dans Extreme Programming, pour une collecte d'exigences plus conversationnelle que de longues spécifications écrites (Fowler, 2013).

**INVEST** (Bill Wake, 2003) : une bonne story est **I**ndépendante, **N**égociable, **V**aluable, **E**stimable, **S**mall (petite), **T**estable. Les deux qui comptent le plus avec un agent : *petite* (tient dans une session) et *testable* (l'agent sait quand s'arrêter).

### Job stories

Format Intercom : **Quand** <situation>, **je veux** <motivation>, **pour** <résultat>. Paul Adams (2016) les oppose aux user stories : le « en tant que » installe un persona sans preuve empirique et décrit une fonction plutôt qu'une motivation. La situation passe en premier. Utile quand le contexte d'usage détermine la solution ; sinon, un gain modeste.

### Critères d'acceptation

Deux formes, selon la nature de l'exigence :

- **Given / When / Then** (Dan North et Chris Matts, issu du BDD) : *Given* l'état initial, *When* l'événement, *Then* le résultat observable. Se traduit presque mécaniquement en test, par exemple avec Gherkin.
- **Liste vérifiable** : chaque ligne se tranche par oui ou non. « Le temps de réponse est inférieur à 2 s sur 100 requêtes » est vérifiable ; « l'interface est rapide » ne l'est pas.

### Exemple court

> **Story** : en tant que responsable qualité, je veux exporter le rapport de lots non conformes au format CSV, afin de le transmettre au client.
>
> **Critères**
> - Given un rapport de 500 lots dont 12 non conformes, when l'export est lancé, then le fichier contient exactement 12 lignes plus l'en-tête.
> - Given un rapport sans lot non conforme, when l'export est lancé, then le fichier contient l'en-tête seul.
> - Le fichier est encodé en UTF-8 et séparé par des points-virgules.
>
> **Hors périmètre** : export Excel, envoi par courriel.

## En pratique

- **Critique du PRD fleuve.** Un document de vingt pages que personne ne relit ne sert à rien : il se périme avant la fin de la lecture. Cagan (2006) remarquait déjà que des semaines de rédaction pour une spécification que peu lisent et qui ne se teste pas sont mal investies. Les PRD actuels tiennent plutôt en deux à six pages (guides de gestion de produit).
- **Version minimale pour un agent** : une page. Problème en deux phrases, non-objectifs, trois à cinq exigences numérotées, critères d'acceptation vérifiables, questions ouvertes. L'agent n'a besoin ni de contexte commercial ni de persona : il a besoin de limites nettes et de critères qu'il peut exécuter.
- **Transformer les critères en tests** avant le code : le test échoue d'abord, l'agent code jusqu'au vert. C'est la forme la plus fiable de spécification exécutable.
- **En solo**, une story par fichier ou par ligne de backlog suffit ; le PRD d'un projet de quelques semaines tient dans le `README` ou un `PRD.md` à la racine.
- **Sur un projet industriel ou en ESN**, le PRD est souvent imposé par le client ou le contrat : le garder court dans le dépôt et renvoyer au document contractuel plutôt que le recopier.
- Pièges : stories trop grosses (épopées déguisées) ; critères qui décrivent l'implémentation ; métriques sans seuil ; PRD jamais mis à jour après la première version ; confondre critères d'acceptation d'une story et définition de terminé de l'équipe.

## Approches voisines & alternatives

- [[Développement piloté par la spécification]] — le PRD ou la story est le point d'entrée de la chaîne spécification, plan, tâches.
- [[Backlog, Kanban, Scrum et Shape Up]] — où vivent les stories et comment on les ordonne.
- [[ADR et design docs]] — la partie « comment », volontairement absente du PRD.
- [[Revue, tests et définition de terminé avec un agent]] — critères d'acceptation et définition de terminé : deux niveaux à ne pas confondre.
- [[Fichiers de contexte pour agents]] — les règles permanentes du projet, distinctes de l'exigence d'une fonctionnalité.
- [[Spec Kit]] — outil dont l'étape de spécification transforme les besoins en spécification formelle avant le plan.
- [[BMAD]] — méthode à base d'agents qui prévoit un travail de cadrage produit en amont du code.
- [[pytest]] — support naturel pour traduire des critères Given/When/Then en tests.
- Alternative : **prototype** au lieu de texte, défendu par Cagan (2006) pour l'expérience utilisateur ; pour un pipeline de données ou un service sans interface, un schéma d'entrée et de sortie plus des cas d'exemple jouent ce rôle.

## Pour aller plus loin

- Cagan, M. (2006) — *Revisiting the Product Spec*, SVPG, 12 octobre 2006. Plaidoyer pour des prototypes plutôt que de longues spécifications écrites.
- Fowler, M. (2013) — *UserStory*, martinfowler.com, 22 avril 2013. Origine dans XP, rôle de la carte et de la conversation.
- Cohn, M. — *User Stories*, Mountain Goat Software : format « en tant que, je veux, afin de », trois C attribués à Ron Jeffries.
- Wake, B. (2003) — *INVEST in Good Stories, and SMART Tasks*, xp123.com, 17 août 2003.
- Adams, P. (2016) — *How we accidentally invented Job Stories*, blog Intercom, 28 juin 2016.
- Fowler, M. (2013) — *GivenWhenThen*, martinfowler.com, 21 août 2013 ; Cucumber, *Gherkin reference* pour la syntaxe.
- Contenu d'un PRD : synthèse de guides de gestion de produit en ligne (problème, utilisateurs, objectifs et non-objectifs, métriques, questions ouvertes) ; pas de source normative unique, la liste est une convention.
