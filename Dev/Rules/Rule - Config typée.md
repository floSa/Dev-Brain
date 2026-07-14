---
galaxie: dev
type: rule
domaine: security
applicable: global
strictness: must
created: 2026-06-11
modified: 2026-06-11
tags: [rule, config, data-validation, type-hints]
---

# Rule — Config typée

## Principe

La configuration est typée et validée au démarrage ([[Pydantic Settings]]) ; les secrets ne sont jamais commités.

## MUST

- Config via [[Pydantic Settings]] : un `Settings(BaseSettings)` typé, lu depuis l'environnement.
- `.env` dans `.gitignore` — jamais commité.
- `.env.example` commité, listant toutes les clés (valeurs vides/factices) = contrat de config.

## SHOULD

- Validation fail-fast au boot : une variable manquante ou mal typée plante au démarrage, pas en plein run.
- Pas d'`os.environ[...]` épars dans le code — tout passe par l'objet `Settings`.

## NICE-TO-HAVE

- Config groupée par domaine (nested models) quand elle grossit.

## Exemples

### Bon

```python
class Settings(BaseSettings):
    database_url: PostgresDsn
    api_key: SecretStr

settings = Settings()  # plante au boot si une clé manque
```

### Mauvais

```python
DB = os.environ["DATABASE_URL"]  # KeyError au milieu d'un run
KEY = os.getenv("API_KEY", "")   # défaut silencieux, type perdu
```

## Exceptions

- Aucune pour les secrets : un secret commité = rotation immédiate.

## Voir aussi

- [[Pydantic Settings]], [[Pydantic]]
- [[Rule - Structure de projet]], [[Rule - Qualité stricte]]
