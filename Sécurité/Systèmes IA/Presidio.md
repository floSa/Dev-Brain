---
role: brique
nom: Presidio
alias: [presidio, microsoft presidio, presidio analyzer, presidio anonymizer, data privacy stack presidio]
pitch: "Détection et anonymisation de données personnelles dans du texte, des images et des tables (MIT, projet communautaire Data Privacy Stack, ex-Microsoft) — reconnaisseurs par regex et NER (spaCy, Transformers, Stanza), opérateurs de masquage dont un chiffrement réversible, tout en local ; mais anglais seul par défaut et aucun reconnaisseur propre à la France."
categorie: security/ia
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[spaCy]]", "[[GLiNER]]", "[[LiteLLM]]", "[[NeMo Guardrails]]"]
tags: [privacy, ner, ai-security]
url_docs: https://presidio.dataprivacystack.org/
url_repo: https://github.com/data-privacy-stack/presidio
---

# Presidio

<!-- AUTO:BANDEAU:START -->
> Détection et anonymisation de données personnelles dans du texte, des images et des tables (MIT, projet communautaire Data Privacy Stack, ex-Microsoft) — reconnaisseurs par regex et NER (spaCy, Transformers, Stanza), opérateurs de masquage dont un chiffrement réversible, tout en local ; mais anglais seul par défaut et aucun reconnaisseur propre à la France.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils de **détection et d'anonymisation de données personnelles** (PII) dans du texte, des images, des tables et des fichiers structurés. Deux pièces principales : l'**analyseur** (`presidio-analyzer`) repère les entités — personne, adresse e-mail, téléphone, carte bancaire, IBAN, adresse IP, lieu — par des **reconnaisseurs** à base d'expressions régulières validées (somme de contrôle, contexte) et par un moteur de **reconnaissance d'entités nommées** (spaCy par défaut) ; l'**anonymiseur** (`presidio-anonymizer`) applique ensuite un **opérateur** à chaque entité trouvée. S'y ajoutent un outil de caviardage d'images (avec Tesseract), un module pour les données structurées et une interface en ligne de commande. Chaque brique tourne en bibliothèque Python ou en service REST (images Docker).

Relevé le 2026-10-01 : **v2.2.364** (2026-07-22), 11 120 étoiles, dernier commit le 2026-09-29. Le projet a **changé de propriétaire** : le dépôt `microsoft/presidio` est devenu `data-privacy-stack/presidio`, sous une gouvernance communautaire qui n'appartient à aucune entreprise ; la licence MIT est déclarée inchangée par le document de transition du dépôt (sans date). Sert de moteur « données personnelles » à plusieurs outils voisins : le garde-fou PII de [[LiteLLM]], le rail PII de [[NeMo Guardrails]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Masquer des noms, e-mails, téléphones et numéros de carte **avant** d'envoyer un texte à un modèle hébergé par un tiers, sur du texte anglais | Des documents **en français** à passer sans écrire de reconnaisseurs : la configuration livrée ne couvre que l'anglais, l'allemand et l'espagnol, et aucun reconnaisseur propre à la France n'existe |
| Tout garder en local : analyse et anonymisation tournent dans le processus ou dans deux conteneurs internes, sans appel à un service tiers | Une garantie de détection : la documentation écrit qu'il n'y en a aucune |
| Une pseudonymisation **réversible** : l'opérateur de chiffrement AES s'inverse avec la même clé | Une anonymisation au sens du RGPD : masquer des champs détectés ne la prouve pas, voir [[Données personnelles et anonymisation pour LLM]] |
| Brancher la détection sur une passerelle ([[LiteLLM]]) ou un framework de garde-fous ([[NeMo Guardrails]]) qui l'appelle déjà | Une couverture que la documentation reconnaît meilleure dans les services en SaaS ; Presidio vaut par sa personnalisation |
| Étendre la détection avec ses propres règles, listes de refus ou un modèle de NER ([[GLiNER]], Transformers) | Un site qui ne veut ni écrire de règles ni maintenir des modèles de NER |

## Mise en œuvre

- Installation — `pip install presidio_analyzer presidio_anonymizer` puis `python -m spacy download <modèle>` ; Python 3.10 à 3.13 (PyPI : jusqu'à moins de 3.15) ; images Docker `presidio-analyzer` (port 5002), `presidio-anonymizer` (5001) et `presidio-image-redactor` (5003), à prendre sur `ghcr.io/data-privacy-stack/` — les images du registre Microsoft ne sont plus mises à jour
- Point d'entrée — `AnalyzerEngine().analyze(text, language="en")` rend des entités avec un score ; `AnonymizerEngine().anonymize(text, results, operators)` les remplace. Opérateurs : `replace` (défaut, `<TYPE_ENTITÉ>`), `redact`, `mask`, `hash`, `encrypt`, `custom` (fonction), `keep`
- Prérequis — **hors ligne** : les modèles de NER ne viennent pas avec le paquet ; un modèle spaCy se télécharge à l'installation, un modèle Transformers par `huggingface_hub.snapshot_download()`, puis l'ensemble se sert depuis un répertoire local. La page d'installation ne traite pas explicitement le cas du site coupé d'internet : préparer les modèles et les images en amont. **Licence des modèles** : celle du modèle choisi, pas celle de Presidio — `en_core_web_lg` est en MIT, `fr_core_news_md` en LGPL-LR (métadonnées du dépôt `spacy-models`), à relire à chaque livraison
- Exécution — bibliothèque embarquée ou deux services REST ; le caviardage d'images demande Tesseract
- Coût — gratuit sous MIT ; le coût réel est l'écriture des reconnaisseurs et des jeux de test de la langue visée, plus la mémoire du modèle de NER

## Limites à connaître

- **Le français n'est pas livré.** Par défaut seul l'anglais est configuré ; le fichier `spacy_multilingual.yaml` du dépôt déclare l'anglais, l'allemand et l'espagnol. Le répertoire des reconnaisseurs par pays (relevé le 2026-10-01) compte 18 pays — Australie, Canada, Finlande, Allemagne, Inde, Italie, Corée, Nigeria, Philippines, Pologne, Singapour, Afrique du Sud, Espagne, Suède, Thaïlande, Turquie, Royaume-Uni, États-Unis — **sans la France**. Numéro de sécurité sociale, SIREN et SIRET, plaque d'immatriculation, IBAN français (hors la somme de contrôle générique de l'IBAN) : à écrire soi-même, en `PatternRecognizer` (expression régulière plus validation). Le reconnaisseur de téléphone sait lire les numéros français (bibliothèque `phonenumbers`) mais sa langue par défaut est l'anglais : à instancier avec `supported_language="fr"` et à tester. Les mots de contexte ne sont pas indépendants de la langue, dit la documentation : les écrire en français aussi.
- **Aucune garantie de détection.** La FAQ du dépôt : parce que la détection est automatique, rien n'assure que Presidio trouve toute l'information sensible, et d'« autres systèmes et protections devraient être employés ». Les faux négatifs sont la règle d'usage, pas l'exception : un nom propre rare, une référence interne, une adresse sans mot-clé passent.
- **Un seul opérateur est réversible.** `encrypt` (AES en mode CBC, clé de 128, 192 ou 256 bits) se défait par l'opérateur de déchiffrement avec la même clé ; `replace`, `redact`, `mask` et `hash` ne reviennent pas en arrière. Depuis la 2.2.361, `hash` prend un sel aléatoire par défaut : sans sel constant de 128 bits au moins, deux occurrences d'un même nom ne donnent plus la même empreinte. Le texte chiffré, long et illisible, brouille le modèle qui le lit : la documentation ne présente pas ce cas d'usage dans un flux LLM, l'équivalence est à tester. La restauration des valeurs d'origine dans la réponse (`output_parse_pii`) est une fonction du garde-fou de [[LiteLLM]], pas de Presidio.
- **Transition de gouvernance.** Le dépôt, le domaine de la documentation (`presidio.dataprivacystack.org`, l'ancien `microsoft.github.io/presidio` redirige) et le registre d'images ont changé ; le document de transition prévoit que « des dépôts, des liens et des références de paquets peuvent changer progressivement ». Le dernier tag a plus de deux mois, alors que `main` avance chaque semaine : trois versions entre mars et juillet 2026. Épingler la version et les images par empreinte.
- **Coût en mémoire et latence** : la documentation lue ne donne aucun chiffre. Un modèle de NER de type Transformers est autrement plus lourd que `en_core_web_lg` ; mesurer sur le matériel cible.
- **Adoption** : repris par [[LiteLLM]] (garde-fou avec modes `pre_call`, `post_call` et `logging_only`, qui ne masque que ce qui part vers l'outil de traçage), par le rail PII de [[NeMo Guardrails]] et par des validateurs et scanners d'outils voisins (Guardrails AI, LLM Guard). Aucun chiffre d'efficacité de l'éditeur n'est repris ici.

## Écosystème

### Alternatives

- *Aucune alternative déclarée : le brain ne contient pas d'autre détecteur de données personnelles. Les services en SaaS (Azure AI Language, Google Cloud DLP, AWS Comprehend) exigent d'envoyer le texte chez un tiers, ce qui défait l'objet ; [[GLiNER]] est un modèle de NER qu'on branche **dans** Presidio, pas un concurrent.*

### Compléments

- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs. — le moteur de NER par défaut de l'analyseur ; les modèles français (`fr_core_news_*`) sont à déclarer à la main.
- [[GLiNER]] — Modèle de NER généraliste zero-shot — extrait n'importe quel type d'entité décrit en langage naturel, sans réentraînement, à partir d'un seul modèle léger. — se branche comme reconnaisseur personnalisé (la documentation de Presidio cite GLiNER parmi les moteurs possibles) ; utile pour des types d'entités qu'aucune règle ne décrit.
- [[LiteLLM]] — Passerelle LLM unifiée (SDK + proxy) de BerriAI — appelle 100+ fournisseurs (OpenAI, Anthropic, Bedrock, Azure…) au format OpenAI, avec routage, suivi des coûts, load-balancing et garde-fous. — son garde-fou `presidio` appelle les deux services REST (analyseur et anonymiseur) avant et après l'appel au modèle, en masquant ou en bloquant.
- [[NeMo Guardrails]] — Framework de garde-fous programmables de NVIDIA (Apache-2.0) — cinq types de rails autour d'un LLM (entrée, dialogue, récupération, exécution, sortie) décrits en YAML et en Colang, avec des rails prêts à l'emploi (sûreté du contenu, jailbreak, thème, PII) ; chaque contrôle sémantique rappelle un LLM, d'où une latence ajoutée. — son rail de données personnelles s'appuie sur Presidio (et sur un modèle GLiNER dédié).

## Ressources

- Documentation — https://presidio.dataprivacystack.org/
- Dépôt — https://github.com/data-privacy-stack/presidio
- Documentation — langues et configuration multilingue : https://presidio.dataprivacystack.org/analyzer/languages/
- Documentation — entités et reconnaisseurs supportés : https://presidio.dataprivacystack.org/supported_entities/
- Documentation — anonymiseur et opérateurs : https://presidio.dataprivacystack.org/anonymizer/
- Documentation — FAQ (absence de garantie) : https://presidio.dataprivacystack.org/faq/
- Dépôt — document de transition : https://github.com/data-privacy-stack/presidio/blob/main/docs/project_transition.md
- Documentation — garde-fou Presidio de LiteLLM : https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2

## Voir aussi

- [[Données personnelles et anonymisation pour LLM]] — la notion : ce qui compte comme donnée personnelle, pseudonymiser contre anonymiser, les limites de la détection
- [[Systèmes IA]] — le hub du dossier
- [[Guardrails]] — la notion : la couche de contrôle autour des appels LLM, dont le filtrage des données personnelles
- [[Comparatif - Garde-fous pour LLM]] — les outils qui filtrent entrées et sorties
