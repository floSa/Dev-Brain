---
galaxie: dev
type: service
nom: Pydantic
alias: [pydantic]
pitch: "Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires."
categorie: tooling/package
licence_type: open-source
hosted: self
maturite: production
langage: Python / Rust
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [data-validation, type-hints]
url_docs: https://docs.pydantic.dev/
url_repo: https://github.com/pydantic/pydantic
---

# Pydantic

## Pourquoi

Bibliothèque de **validation de données** pilotée par les **annotations de type** Python. On déclare un `BaseModel` avec des champs typés ; Pydantic valide, **coerce** et structure les données entrantes à l'exécution, avec des messages d'erreur précis. Depuis la **v2**, le cœur de validation (`pydantic-core`) est **écrit en Rust** (via PyO3), d'où un gain de performance majeur sur la v1. C'est le socle de validation de tout un écosystème : FastAPI, SQLModel, LangChain et de nombreux outils l'utilisent pour leurs schémas.

## Quand l'utiliser

- Valider et parser des données externes (payloads API, JSON, formulaires) vers des objets Python typés.
- Définir des schémas clairs et auto-documentés (`.model_dump()`, génération de JSON Schema).
- Sorties structurées de LLM, frontières de modules — partout où l'on veut garantir la forme des données.

## Quand NE PAS l'utiliser

- Objets internes purs sans validation ni I/O → `@dataclass` de la stdlib (plus léger).
- (Dé)sérialisation déclarative sans modèle riche → attrs + cattrs, marshmallow.

## Déploiement & coût

- Bibliothèque Python (`uv add pydantic`) ; roue avec binaire Rust précompilé. MIT, gratuit.
- Single-node, en mémoire ; rien à héberger.

## Pièges

- Migration **v1 → v2** : API changée (`@validator` → `@field_validator`, `.dict()` → `.model_dump()`) ; vérifier la version ciblée.
- La coercition est puissante mais peut surprendre (`"1"` → `1`) ; activer le mode strict si besoin.
- Valider à chaque instanciation a un coût : éviter de revalider des objets déjà sûrs dans les boucles chaudes.

## Alternatives

- dataclasses (stdlib), attrs, marshmallow — autres approches de modélisation / validation ; Pydantic se distingue par la validation à l'exécution pilotée par les types et son cœur Rust. *(Pages dédiées non créées.)*

## Liens

- Configuration typée bâtie sur Pydantic : [[Dev/Services/Pydantic Settings|Pydantic Settings]].
- Doc : https://docs.pydantic.dev/
