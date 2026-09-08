---
role: brique
nom: osint4all
alias: [osint4all, osint4all.github.io]
pitch: "Annuaire de liens OSINT (CC0, portage GitHub d'une page start.me) : de l'ordre de 78 rubriques et 1 400 liens — générateurs, récupération de hash, confidentialité, recherche de personnes, guides. Ni logiciel, ni service, et sans commit depuis juillet 2022."
categorie: security/recon
famille: annuaire
domaines: [infra-ops]
licence_type: open-source
os: 
langage: 
maturite: deprecated
alternatives: []
complements: []
tags: [osint]
url_docs: https://github.com/osint4all/osint4all.github.io
url_repo: https://github.com/osint4all/osint4all.github.io
---

# osint4all

<!-- AUTO:BANDEAU:START -->
> Annuaire de liens OSINT (CC0, portage GitHub d'une page start.me) : de l'ordre de 78 rubriques et 1 400 liens — générateurs, récupération de hash, confidentialité, recherche de personnes, guides. Ni logiciel, ni service, et sans commit depuis juillet 2022.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Annuaire | open-source | rien à exécuter | deprecated | amont ancien · 2022-07-09 |
<!-- AUTO:BANDEAU:END -->

## Définition

Ni un logiciel, ni un service, ni un outil exécutable : un **annuaire de liens**, un
unique `README.md` d'environ 3 000 lignes servi en page GitHub Pages via Jekyll. Rien ne
s'installe, rien ne se déploie, il n'y a pas de version à suivre. C'est le portage d'une
page `start.me` sous CC0-1.0 — domaine public — rassemblant de l'ordre de **78 rubriques**
et **1 400 liens** : contacts jetables, générateurs d'identité, bacs à sable, récupération
de hash, confidentialité et communication sécurisée, renseignement sur les menaces,
résolution d'identité, recherche par personne, pseudonyme, courriel ou téléphone, réseaux
sociaux plateforme par plateforme, moteurs et *dorking*, images et médias, plaques et
véhicules, suivi aérien et maritime, WHOIS et DNS, malware, IoT, radio, immobilier, jeux
de données, guides. Sa `categorie:` porte le **sujet listé**, pas la nature de la page.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Chercher le nom d'un service spécialisé pour une tâche de reconnaissance précise, avant même de savoir lequel existe | Comme outil : il n'y en a pas un seul ici, uniquement des adresses vers des outils tiers → [[Web-Check]], qui s'exécute |
| Se faire une carte du domaine OSINT en une lecture, rubrique par rubrique | Comme source à jour : huit commits, rien depuis le 9 juillet 2022, sur un terrain où les services ferment vite — une part des liens est morte ou a changé de mains, et rien n'indique la fraîcheur entrée par entrée |
| Trouver des utilitaires périphériques et durables : adresse jetable, bac à sable, dépôt de fichier temporaire, générateur de données de test | Comme garantie de qualité : aucune curation vérifiable, aucune note ; plusieurs rubriques pointent vers des services commerciaux de recherche de personnes, et vers des services tiers non audités auxquels on confierait un fichier ou une empreinte |
| | Comme référence dans un livrable client : ni citable, ni pérenne |
| | Sans avoir qualifié le cadre légal : une bonne part des liens porte sur des données personnelles, dont la consultation et la conservation relèvent du RGPD et du droit national quelle que soit la disponibilité publique de la donnée — la rubrique de récupération de hash ne s'utilise que sur ses propres empreintes, et avec autorisation |

## Mise en œuvre

- Installation — aucune : une page GitHub, lisible en ligne ou clonée
- Point d'entrée — le `README.md` du dépôt, rendu sur `osint4all.github.io` par Jekyll
- Prérequis — un navigateur ; ni langage applicatif, ni plateforme, ni dépendance
- Exécution — rien ne s'exécute ici : la page se lit, et tout ce qu'elle liste tourne chez des tiers
- Coût — gratuit, CC0-1.0, domaine public ; les services listés ont chacun leur propre modèle

## Écosystème

### Alternatives

- *Aucune : un annuaire de liens n'a pas d'équivalent fiché au brain, et les outils de reconnaissance n'en sont pas des substituts. Hors brain, les références vivantes du domaine sont l'OSINT Framework et les listes `awesome-osint`.*

## Ressources

- Dépôt — https://github.com/osint4all/osint4all.github.io

## Voir aussi

- [[Sécurité]] — le hub du domaine
- [[public-apis]] — l'autre annuaire du vault : même problème de rangement, même avertissement
