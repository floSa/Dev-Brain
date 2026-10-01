---
role: notion
nom: Données personnelles et anonymisation pour LLM
alias: [données personnelles et LLM, RGPD et LLM, PII masking, masquage de données personnelles, pseudonymisation, anonymisation de données personnelles, PII]
categorie: security/ia
domaines: [ai-eng, infra-ops]
tags: [privacy, ai-security, ner]
---

# Données personnelles et anonymisation pour LLM

> Notion de vulgarisation, **pas un conseil juridique** : elle dit quoi chercher dans un document et ce que les textes officiels établissent, pas ce qu'un traitement donné a le droit de faire. Les textes ont été lus le 2026-10-01 ; le délégué à la protection des données du client et un juriste tranchent. Les recommandations de la CNIL et de l'EDPB changent : relire la source avant de livrer.

## Aperçu

- Un assistant interne qui lit des contrats, des courriels, des tickets ou des dossiers RH **lit des données personnelles**, que personne ne les ait cherchées. Les envoyer à un modèle, c'est les **traiter** au sens du RGPD ; le choix de l'endroit où tourne le modèle devient un choix de conformité autant que de coût.
- Trois leviers, qui se superposent et ne se remplacent pas : **ne pas envoyer** (héberger le modèle sur le site), **masquer avant d'envoyer** (détection puis remplacement), **limiter ce qui reste** (journaux, traces, durées de conservation). La détection automatique est le levier le moins sûr des trois : elle se trompe, et ses erreurs sont silencieuses.
- Cette page traite de la donnée personnelle *dans les entrées et les traces* d'une application LLM. L'attaque qui la fait sortir est dans [[Prompt injection]] ; le panorama des risques dans [[AI security]] ; la couche de filtrage dans [[Guardrails]]. Rien n'y est répété ici.

## Concepts clés

### Ce qui compte comme donnée personnelle
- Le RGPD (art. 4(1), texte officiel, version française lue) : « toute information se rapportant à une personne physique identifiée ou identifiable » ; est identifiable celle qui peut l'être « directement ou indirectement », notamment par un nom, un numéro d'identification, des données de localisation ou un identifiant en ligne.
- La CNIL donne en exemples : nom et prénom (identification directe) ; numéro de téléphone, plaque d'immatriculation, numéro de sécurité sociale, adresse postale ou courriel, voix, image (identification indirecte). L'identification peut venir d'une seule donnée ou du **croisement** de plusieurs : « une femme vivant à telle adresse, née tel jour et membre de telle association ».
- Dans des documents d'entreprise, cela donne : noms et signatures des signataires, adresses courriel nominatives (`prenom.nom@`), téléphones directs, adresses IP, identifiants d'employés, données RH et de paie. Les coordonnées d'entreprise génériques (standard, adresse de service) ne le sont « en principe » pas, dit la CNIL. Un **numéro de contrat** ou un identifiant de dossier n'est pas listé comme tel par les textes lus : il le devient quand un autre jeu de données permet de remonter à une personne, au cas par cas.
- **Catégories particulières** (art. 9) : origine, opinions, santé, biométrie… leur traitement est interdit sauf exceptions de l'art. 9(2). Un compte rendu médical dans un dossier de l'assistant change la nature de l'exercice.

### Pseudonymisation contre anonymisation
- **Pseudonymisation** (art. 4(5)) : rendre les données non attribuables à une personne sans informations supplémentaires, ces dernières étant **conservées séparément** et protégées. La donnée reste personnelle (considérant 26) : le RGPD continue de s'appliquer. Les lignes directrices 01/2025 de l'EDPB (adoptées le 2025-01-16, version soumise à consultation publique ; statut final à revérifier) le répètent, y compris quand les informations supplémentaires ne sont pas entre les mêmes mains.
- **Anonymisation** : les données ne se rapportent plus à une personne identifiable. Le test (considérant 26) porte sur « l'ensemble des moyens raisonnablement susceptibles d'être utilisés », par le responsable du traitement **ou par toute autre personne**, en tenant compte du coût, du temps et des technologies. Une donnée anonyme sort du champ du règlement.
- L'avis 05/2014 du groupe de l'article 29 sur les techniques d'anonymisation (WP216) retient trois risques à écarter : la **singularisation** (isoler une personne), la **corrélation** (relier deux jeux de données à une même personne) et l'**inférence** (déduire une information sur elle). Il écrit que la pseudonymisation n'est pas une méthode d'anonymisation. La CNIL en donne l'illustration : une base de CV dont le nom est remplacé par un numéro est « pseudonymisée et non anonymisée ».
- Conséquence pour un masquage automatique : remplacer les noms détectés par `<PERSONNE_1>` produit au mieux un texte **pseudonymisé** ; l'anonymisation exigerait de prouver qu'aucune combinaison (poste, date, lieu, fait rare) ne permet de remonter à quelqu'un, preuve qu'un détecteur d'entités ne fournit pas.

### Détection : règles, modèle, dictionnaire
- **Règles** (expressions régulières avec validation : somme de contrôle d'un IBAN ou d'une carte, format d'un numéro de sécurité sociale) : précises sur les formats rigides, aveugles à tout le reste.
- **Modèle de reconnaissance d'entités nommées** (spaCy, Transformers, [[GLiNER]]) : repère les noms de personnes, de lieux, d'organisations par le contexte ; plus de rappel, plus de faux positifs, et une dépendance à la langue du modèle.
- **Dictionnaire ou liste de refus** : les noms de clients, de projets, de produits de l'entreprise, que ni règle ni modèle ne reconnaissent comme sensibles ; efficace, à maintenir.
- Aucune ne suffit seule ; [[Presidio]] assemble les trois dans un même moteur, en local.

### Masquer : quatre opérateurs, une seule réversibilité
- **Remplacer** par un jeton de type (`<PERSONNE>`), **caviarder**, **masquer** partiellement, **hacher**, **chiffrer**. Seul le chiffrement se défait avec la clé ; remplacer et caviarder perdent l'information ; hacher la perd aussi, sauf à tenir une table de correspondance (donc une donnée de plus à protéger).
- La **réversibilité** sert à remettre les vrais noms dans la réponse du modèle, côté serveur : le mapping reste sur le site, le modèle ne voit que des jetons. Un jeton lisible et stable (`<PERSONNE_1>` toujours pour la même personne dans la conversation) se laisse mieux manipuler par un modèle qu'un texte chiffré, long et illisible ; l'équivalence entre les deux est à tester sur le cas réel.
- Le mapping est la donnée **additionnelle** de l'art. 4(5) : le garder séparé du flux, protégé, et à durée de vie courte.

### Envoyer à un modèle hébergé par un tiers
- La FAQ de la CNIL sur les systèmes d'IA générative (2024-07-18) distingue les usages non confidentiels, où un service grand public est envisageable « avec des garanties appropriées » (par exemple en désactivant la réutilisation des données d'usage par le fournisseur), des usages qui impliquent des données personnelles ou de la documentation sensible, **« par exemple pour le RAG »** : l'hébergement sur site y est « généralement plus opportun et plus sécurisé ».
- En mode API, la maîtrise est « quasi exclusivement dans les mains du fournisseur » : éviter autant que possible d'y saisir des données personnelles et surveiller les conditions contractuelles, dont les transferts hors de l'Union. Un hébergeur distant est un sous-traitant : contrat (art. 28), garanties suffisantes, et encadrement des transferts (chapitre V).
- Le rapport « AI Privacy Risks & Mitigations – LLMs » (2025-04-10, rédigé pour l'EDPB par un expert indépendant ; **l'EDPB précise qu'il n'engage pas sa position**) liste les risques propres aux LLM : journalisation non voulue des requêtes et réponses chez le fournisseur, accès non autorisé aux journaux, agrégation dans le temps, absence de politique de conservation, exposition à des tiers par l'infrastructure.

### L'hébergement local comme réponse, et ses limites
- Servir le modèle sur le site ([[vLLM]], [[Ollama]]) supprime le tiers et le transfert : la donnée ne quitte pas le périmètre du client. Cela **ne supprime pas** le traitement : l'assistant reste un traitement de données personnelles, avec sa base légale, son registre, ses droits des personnes, et la sécurité de ses journaux.
- L'avis 28/2024 de l'EDPB sur les modèles d'IA (2024-12-17) dit qu'un modèle entraîné sur des données personnelles n'est pas anonyme dans tous les cas, au cas par cas, selon la probabilité d'en extraire les données. Le sujet touche l'entraînement ou le réentraînement sur les documents du client, pas l'inférence simple, mais il pèse sur tout projet de réglage fin : la CNIL (fiche du 2025-07-22) demande, dans la plupart des cas, des tests d'attaques par réidentification dans la documentation.

### Journaux et traces
- Un prompt contenant un nom se retrouve dans le journal de l'application, la trace de l'outil d'observabilité ([[Langfuse]], [[Phoenix Arize]]), les caches et les sauvegardes. Masquer **avant** l'appel n'aide que si les traces enregistrent le texte masqué : la passerelle [[LiteLLM]] a un mode du garde-fou Presidio qui ne masque que ce qui part vers l'outil de traçage (documentation de LiteLLM), et pas la requête envoyée au modèle.
- La CNIL, dans sa recommandation sur la journalisation (délibération 2021-122), demande de limiter les données personnelles incluses dans les traces et de ne pas les conserver au-delà du traitement principal ; elle fixe une conservation de six mois à un an pour les traces de sécurité. Cette recommandation vise la journalisation de sécurité, pas l'observabilité LLM : l'appliquer au prompt est une **extrapolation** de cette page, à valider avec le client.

## Les maths, simplement

- Une détection automatique est un classifieur : rappel `r` (la part des vraies entités trouvées) et précision (la part des trouvailles justes). Le danger ici est le **rappel**, car une entité ratée part en clair.
- Illustration (hypothèse, pas une mesure) : un document contient 40 entités sensibles, le détecteur en trouve 95 % de façon indépendante. La probabilité de **toutes** les masquer est `0,95^40 ≈ 0,13` : dans près de neuf documents sur dix, au moins une fuit. Plus le texte est long, plus le « presque parfait » devient « presque toujours une fuite ». D'où l'utilité de ne pas dépendre d'un seul masquage.
- Les mesures publiques sont peu rassurantes hors anglais et hors corpus d'origine : un préprint de septembre 2026 (Zafar et Nowaczyk, arXiv 2609.03464) rapporte que les trois détecteurs testés — spaCy, Presidio et Qwen2.5-3B — se dégradent sur des entrées bruitées ou non standard ; un autre préprint (Jha, arXiv 2604.15776, avril 2026) mesure un F1 inférieur à 0,14 pour huit systèmes sur un corpus fusionné de dix jeux de données aux étiquettes hétérogènes, Presidio en tête avec 0,1385 — chiffre qui dit surtout que le jeu est hétérogène, pas que l'outil échoue sur vos documents. Aucune mesure sur des documents d'entreprise en français n'a été trouvée : **la mesurer soi-même** sur un échantillon annoté du client.

## En pratique

- **Cartographier avant de masquer** : lister les types de données présents dans les sources de l'assistant (RH, contrats, tickets, courriels) ; c'est ce qui décide entre « ne pas indexer ce corpus », « masquer » et « héberger seulement ».
- **Héberger le modèle sur le site** d'abord (la réponse à la majorité du risque lié au tiers) ; le masquage vient en seconde couche, pas à la place.
- **Mesurer le rappel** sur 100 à 200 documents du client annotés à la main ; ne pas se fier à un taux publié. En français, prévoir des reconnaisseurs maison (numéro de sécurité sociale, SIREN, SIRET, plaque) : [[Presidio]] n'en livre aucun pour la France.
- **Masquer côté serveur, restaurer côté serveur** : le mapping reste sur le site ; le modèle ne voit jamais le jeton réversible.
- **Brancher le masquage là où tout passe** : sur la passerelle ([[LiteLLM]]) ou dans le framework de garde-fous ([[NeMo Guardrails]]), pour qu'aucune application ne l'oublie.
- **Réduire les traces** : décider ce que l'observabilité enregistre (texte masqué, hash, longueurs), la durée de conservation, et qui y accède.
- **Piège : la sortie** : le modèle peut reconstituer une donnée à partir du contexte ou la citer depuis un passage non masqué ; filtrer aussi la sortie ([[Guardrails]]).
- **Piège : l'indexation** : masquer la requête n'efface pas le document déjà indexé en clair dans la base vectorielle ; le masquage se décide à l'ingestion.

## Approches voisines & alternatives

- [[Presidio]] — la brique de détection et de masquage, locale, avec chiffrement réversible.
- [[NeMo Guardrails]] — son rail de données personnelles s'appuie sur Presidio ; un moyen d'imposer le masquage à toute l'application.
- [[LiteLLM]] — le garde-fou Presidio de la passerelle : masquer ou bloquer avant l'appel, et restaurer dans la réponse.
- [[GLiNER]] — un modèle de reconnaissance d'entités sans réentraînement, pour des types que les règles ne décrivent pas.
- [[Guardrails]] et [[AI security]] — le cadre : où se place le filtrage, et quelles menaces il adresse.
- **Alternatives** : chiffrer le corpus et ne le déchiffrer qu'à l'intérieur du périmètre ; exclure les sources trop sensibles de l'assistant ; données synthétiques pour les essais (la documentation de Presidio en donne un exemple de génération) ; les services de détection en SaaS, qui supposent d'envoyer le texte à un tiers et défont l'objet.

## Pour aller plus loin

- Règlement (UE) 2016/679 (RGPD), articles 4, 5, 9, 28, 35, chapitre V et considérant 26 — EUR-Lex.
- EDPB — *Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models* (2024-12-17) : https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
- EDPB — *Guidelines 01/2025 on Pseudonymisation* (adoptées le 2025-01-16, version pour consultation publique) : https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf
- Groupe de l'article 29 — *Opinion 05/2014 on Anonymisation Techniques* (WP216, 2014-04-10).
- CNIL — questions-réponses sur l'utilisation d'un système d'IA générative (2024-07-18) : https://www.cnil.fr/fr/les-questions-reponses-de-la-cnil-sur-lutilisation-dun-systeme-dia-generative
- CNIL — analyser le statut d'un modèle d'IA au regard du RGPD (2025-07-22) : https://www.cnil.fr/fr/ia-analyser-le-statut-dun-modele-dia-au-regard-du-rgpd
- CNIL — la donnée personnelle : https://www.cnil.fr/fr/definition/donnee-personnelle
- CNIL — recommandation relative à la journalisation (délibération n° 2021-122 du 14 octobre 2021).
- Isabel Barberá, *AI Privacy Risks & Mitigations – Large Language Models* (EDPB Support Pool of Experts, 2025-04-10) : https://www.edpb.europa.eu/documents/support-pool-of-experts/ai-privacy-risks-mitigations-large-language-models-llms_en
- Pilán, Lison, Øvrelid, Papadopoulou, Sánchez, Batet, *The Text Anonymization Benchmark (TAB)*, arXiv 2202.00443 (2022) : corpus de 1 268 décisions de la Cour européenne des droits de l'homme annotées, en anglais.
- Zafar, Nowaczyk, *Mind the Gap: Robustness Risks in PII Detection Systems*, arXiv 2609.03464 (2026-09-03, préprint).
- Jha, *PIIBench*, arXiv 2604.15776 (2026-04-17, préprint).
