---
role: brique
nom: Pydantic
alias: [pydantic]
pitch: "Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires."
categorie: devtools/validation
famille: paquet
licence_type: open-source
maturite: production
langage: Python / Rust
alternatives: []
complements: ["[[Pydantic Settings]]"]
tags: [data-validation, type-hints]
url_docs: https://pydantic.dev/docs/validation/
url_repo: https://github.com/pydantic/pydantic
---

# Pydantic

<!-- AUTO:BANDEAU:START -->
> Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python / Rust | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Validation de données pilotée par les **annotations de type**. On déclare un `BaseModel` aux
champs typés ; Pydantic valide, **coerce** et structure les données entrantes à l'exécution,
avec des erreurs qui désignent le champ fautif et la règle enfreinte. Depuis la **v2**, le
cœur `pydantic-core` est écrit en Rust via PyO3 — d'où un gain de performance majeur, et une
API changée : `@validator` devient `@field_validator`, `.dict()` devient `.model_dump()`.
C'est le socle de validation d'un écosystème entier : FastAPI, SQLModel et LangChain
s'appuient dessus pour leurs schémas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Valider et parser des données externes — payloads d'API, JSON, formulaires — vers des objets Python typés | Objets internes purs, sans validation ni entrées-sorties → `@dataclass` de la bibliothèque standard, plus léger |
| Définir des schémas auto-documentés : `.model_dump()`, génération de JSON Schema | (Dé)sérialisation déclarative sans modèle riche → attrs et cattrs, ou marshmallow |
| Garantir la forme des données aux frontières de modules, ou en sortie structurée de LLM | La coercition surprend (`"1"` devient `1`) : activer le mode strict quand la tolérance n'est pas voulue |
| | Valider à chaque instanciation a un coût : ne pas revalider dans une boucle chaude des objets déjà sûrs |

## Mise en œuvre

- Installation — `uv add pydantic` ; la roue embarque le binaire Rust précompilé
- Point d'entrée — import Python : une classe qui hérite de `BaseModel`
- Prérequis — Python ; vérifier la version ciblée, l'API v1 et l'API v2 ne sont pas la même
- Exécution — dans le process appelant, en mémoire ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Compléments

- [[Pydantic Settings]] — Configuration typée chargée depuis l'environnement, les fichiers .env et les secrets, bâtie sur Pydantic. — la configuration d'application bâtie sur ce socle

## Ressources

- Documentation — https://pydantic.dev/docs/validation/
- Dépôt — https://github.com/pydantic/pydantic

## Voir aussi

- [[Outils de développement]] — le hub du domaine
