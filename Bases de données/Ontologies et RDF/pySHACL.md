---
role: brique
nom: pySHACL
alias: [pyshacl, pySHACL validator]
pitch: "Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider."
categorie: database/rdf
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: []
complements: ["[[rdflib]]", "[[LinkML]]", "[[Oxigraph]]"]
tags: [rdf, data-validation]
url_docs: https://github.com/RDFLib/pySHACL
url_repo: https://github.com/RDFLib/pySHACL
---

# pySHACL

<!-- AUTO:BANDEAU:START -->
> Validateur SHACL en Python pur (Apache-2.0), construit sur rdflib — vérifie un graphe RDF contre ses formes, en ligne de commande, en API ou en service HTTP ; peut développer le graphe par RDFS ou OWL-RL avant de valider.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Validateur SHACL écrit en Python pur : il vérifie qu'un graphe RDF respecte les formes (les règles) d'un autre graphe, selon la Recommandation W3C SHACL de 2017, et rend un rapport de conformité. Il s'appuie sur [[rdflib]] pour manipuler le RDF et sur le module OWL-RL pour le profil OWL 2 RL. Il s'utilise en ligne de commande (`pyshacl -s formes.ttl donnees.ttl`), en API Python, en service HTTP (extra `http`) ou en image Docker. Options notables : les fonctionnalités avancées de SHACL (les règles, activées par `-a`), le support de SHACL-JS (extra `js`), une expansion RDFS ou OWL-RL du graphe avant validation (`-i`), un graphe d'ontologie additionnel (`-e`), et la validation d'un graphe distant en lecture seule par SPARQL. Relevé le 2026-10-19 : version **0.40.1** (2026-07-28), Python 3.9 ou plus, licence Apache-2.0, environ 360 étoiles.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vérifier des données RDF contre des formes SHACL dans un pipeline Python ou une CI, avec un code retour (0 conforme, 1 non conforme) | Un graphe de centaines de millions de triplets à valider en continu : une implémentation en Python pur se mesure avant de s'y fier ; voir plutôt la validation intégrée de [[RDF4J]] ou de [[Apache Jena]] |
| Un rapport de validation lisible (`-f human`) ou un graphe de rapport à relire en RDF | Valider à chaque transaction dans la base : c'est le rôle de la couche SHACL de [[RDF4J]], pas d'un outil externe |
| Étendre un graphe par RDFS ou OWL-RL avant de valider, sans raisonneur Java | Un raisonnement OWL DL : le profil visé est OWL 2 RL |
| Valider un graphe stocké dans [[Oxigraph]] (extra `oxigraph`) | Un schéma à maintenir en une seule source : voir [[LinkML]], qui génère les formes SHACL |

## Mise en œuvre

- Installation — `uv add pyshacl` ; extras optionnels `http`, `js`, `oxigraph`
- Point d'entrée — la commande `pyshacl`, ou `pyshacl.validate(...)` en Python
- Prérequis — Python 3.9 ou plus ; rdflib et OWL-RL sont tirés comme dépendances
- Exécution — en bibliothèque ou en commande, rien à héberger ; un service HTTP et une image Docker existent
- Coût — gratuit, Apache-2.0

## Limites à connaître

- **Fidélité à la norme non vérifiée ici.** Le README dit que le module est développé pour respecter la Recommandation SHACL ; le taux de réussite aux tests officiels du W3C n'a pas été relevé. Sur des formes rares (SHACL-SPARQL, règles), tester avec ses propres cas.
- **Monde fermé contre monde ouvert.** Valider après une expansion OWL-RL change ce que les formes « voient » : les faits déduits comptent. Voir la distinction dans [[SHACL]] et [[OWL et raisonnement]].
- **Version 0.x.** Le numéro dit « pré-1.0 » : épingler la version dans `uv.lock` et relire les notes de version à chaque mise à jour.

## Écosystème

### Alternatives

- Aucune alternative déclarée : les autres validateurs SHACL du dossier sont intégrés à un moteur ([[Apache Jena]], [[RDF4J]], [[Fluree]]) et non à un paquet Python.

### Compléments

- [[rdflib]] — Bibliothèque Python pour manipuler du RDF (BSD-3-Clause) — lit et écrit Turtle, JSON-LD et RDF/XML, interroge en SPARQL 1.1 (requêtes et mises à jour), graphe en mémoire ou persistant ; ce n'est pas un serveur. — fournit le graphe RDF que pySHACL valide.
- [[LinkML]] — Langage de modélisation en YAML et sa boîte à outils Python (Apache-2.0) — un schéma unique génère JSON Schema, SHACL, OWL, ShEx, Pydantic ou SQL, et valide des données JSON, RDF ou TSV. — génère des formes SHACL depuis un schéma YAML, que pySHACL applique.
- [[Oxigraph]] — Base RDF et SPARQL en Rust sur RocksDB (Apache-2.0 ou MIT) — serveur en un binaire, bibliothèque Rust et paquet Python ; mono-nœud, sans SHACL ni raisonnement annoncés. — sert de magasin au graphe à valider, par l'extra `oxigraph`.

## Ressources

- Documentation — https://github.com/RDFLib/pySHACL
- Dépôt — https://github.com/RDFLib/pySHACL

## Voir aussi

- [[Ontologies et RDF]] — le hub du sous-domaine
- [[Comparatif - Outils RDF et OWL en Python]] — ce qui départage les outils Python
- [[SHACL]] — la notion : valider un graphe contre ses formes
