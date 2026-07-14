---
galaxie: dev
type: rule
domaine: docs
applicable: global
strictness: nice-to-have
created: 2026-06-11
modified: 2026-06-11
tags: [rule, container, ci-cd, reproducibility]
---

# Rule — Packaging démo

## Principe

Une démo se lance en une commande et se comprend en un coup d'œil : environnement reproductible, commandes triviales, aperçu visuel.

## MUST

- `docker-compose.yml` : la démo monte d'un `docker compose up`, sans install manuelle (cf. [[Docker]]).
- Commandes encapsulées dans un `Makefile` (`make up`, `make demo`, `make test`).

## SHOULD

- Un `demo.gif` (ou court mp4) dans le `README.md` : on voit le résultat sans rien lancer.
- Healthchecks et volumes nommés dans le compose — cf. [[Pattern - Stack démo ML locale multi-services]].

## NICE-TO-HAVE

- Données de seed / fixtures embarquées pour une démo déterministe.

## Exemples

### Bon

```makefile
up:    ; docker compose up -d
demo:  ; uv run python -m mon_projet.demo
test:  ; uv run pytest
```

### Mauvais

```
README : « installer Postgres, créer la base, exporter 6 variables, puis... »
```

## Exceptions

- Lib pure (pas d'app à lancer) → pas de compose ; un exemple exécutable suffit.

## Voir aussi

- [[Docker]], [[Pattern - Stack démo ML locale multi-services]]
- [[Rule - Structure de projet]], [[Rule - Toolchain Python]]
