---
galaxie: dev
type: outil
nom: osint4all
alias: [osint4all, osint4all.github.io]
pitch: "Annuaire de liens OSINT (CC0, portage GitHub d'une page start.me) : de l'ordre de 78 rubriques et 1 400 liens — générateurs, récupération de hash, confidentialité, recherche de personnes, guides. Ni logiciel, ni service, et sans commit depuis juillet 2022."
categorie: security/osint
domaines: [infra-ops]
licence_type: open-source
os: 
langage: 
status: abandonne
alternatives: []
tags: [osint]
url_docs: https://github.com/osint4all/osint4all.github.io
url_repo: https://github.com/osint4all/osint4all.github.io
---

# osint4all

## Pourquoi

**Avertissement de rangement, à lire en premier** : ce n'est ni un logiciel, ni un service, ni un outil exécutable. C'est un **annuaire de liens** — un unique `README.md` de quelque 3 000 lignes, servi en page GitHub Pages via Jekyll. Il est classé en `security/osint` faute de type `ressource` dans la taxonomie. Il ne faut pas le lire comme une brique choisissable : rien ne s'installe, rien ne se déploie, il n'y a pas de version à suivre. Le vault a un précédent exact pour ce cas — [[Dev/Outils/public-apis|public-apis]], autre annuaire rangé par défaut dans une famille d'outils.

Cela posé, ce que c'est : le portage GitHub d'une page `start.me` (celle nommée « osint4all » dans la description du dépôt), sous licence CC0-1.0 — domaine public. De l'ordre de **78 rubriques** et **1 400 liens** : contacts jetables, générateurs d'identité, bacs à sable, récupération de hash, services de confidentialité et communication sécurisée, renseignement sur les menaces, résolution d'identité, recherche par personne / pseudonyme / courriel / téléphone, plateforme par plateforme pour les réseaux sociaux, moteurs et *dorking*, images et médias, plaques et véhicules, suivi aérien et maritime, WHOIS et DNS, malware, IoT, radio, immobilier, jeux de données, guides.

Il faut être franc sur la taille du projet : de l'ordre de **95 étoiles**, huit commits, et **aucune mise à jour depuis le 9 juillet 2022**. Ce n'est pas une référence de premier plan, c'est une liste correcte et modeste. La page `start.me` d'origine n'a pas pu être consultée pour vérifier si la source, elle, vit encore.

## Quand l'utiliser

- Chercher le nom d'un service spécialisé pour une tâche de reconnaissance précise, avant de savoir lequel existe.
- Se faire une carte du domaine OSINT en une lecture, par rubrique.
- Trouver des utilitaires périphériques et durables : adresse jetable, bac à sable, dépôt de fichier temporaire, générateur de données de test.

## Quand NE PAS l'utiliser

- Comme outil : il n'y en a pas un seul ici, seulement des adresses vers des outils tiers.
- Comme source à jour : quatre ans sans commit sur un domaine où les services ferment vite, une part significative des liens est morte ou a changé de mains.
- Comme garantie de qualité : aucune curation vérifiable, aucune note sur les services listés — plusieurs rubriques pointent vers des services commerciaux de recherche de personnes, à traiter avec la prudence qui s'impose.
- Comme référence dans un livrable client : ni citable, ni pérenne.

## Installation & plateformes

Aucune installation : une page GitHub, lisible en ligne ou clonée. Pas de langage applicatif, pas de plateforme, pas de dépendance.

## Pièges

- **Le cadre légal est à la charge de l'utilisateur.** Une bonne partie des liens portent sur des données personnelles ; leur consultation et leur conservation relèvent du RGPD et du droit national, quelle que soit la disponibilité publique de la donnée.
- Liens vers des services tiers non audités : y déposer un fichier, une adresse ou une empreinte de mot de passe revient à la confier à un inconnu.
- La rubrique de récupération de hash n'est pas un outil d'administration : usage sur ses propres empreintes uniquement, et avec autorisation.
- Aucune indication de fraîcheur par entrée : impossible de savoir quel lien a été vérifié et quand.
- **Un seul tag du vocabulaire fermé s'applique honnêtement** (`osint`) ; il désigne le sujet, pas la nature de la page. Aucun tag ne dit « annuaire de ressources ».
- `status: abandonne` porte sur le dépôt, pas sur la valeur résiduelle de la liste — la nuance ne se lit pas dans le champ.

## Alternatives

Aucune. Un annuaire de liens n'a pas d'équivalent fiché dans le brain, et les outils de reconnaissance n'en sont pas des substituts. Hors brain, la référence vivante du domaine est l'OSINT Framework, et les listes `awesome-osint`.

## Liens

- [[Dev/Outils/public-apis|public-apis]] — l'autre annuaire du vault, même problème de rangement, même avertissement
- [[Dev/Services/Web-Check|Web-Check]] — un outil de reconnaissance réel, à opposer à cette page : l'un s'exécute, l'autre se lit
- Repo : https://github.com/osint4all/osint4all.github.io
