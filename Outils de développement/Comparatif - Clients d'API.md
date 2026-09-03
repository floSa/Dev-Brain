---
role: comparatif
nom: Comparatif - Clients d'API
categorie: devtools/client-api
tags: [api-client, version-control]
---

# Comparatif - Clients d'API

> On tranche sur : où vivent les collections — dans le dépôt git ou dans un cloud — et le prix d'une équipe.

![[Comparatif - Clients d'API.base]]

## Ce qui départage

- [[Bruno]] — les collections sont des fichiers texte `.bru` posés dans le dépôt : diff lisible, branche, revue de code, et **aucun compte ni cloud**. Le format lui est propre, il n'est pas interopérable, et il n'y a ni mocks ni monitoring.
- [[Postman]] — la plateforme entière : mocks, monitors, doc publiée, catalogue, espaces partagés. Les collections vivent **dans son cloud** par défaut, l'export est un JSON illisible en diff, et depuis mars 2026 le plan gratuit est limité à **un seul utilisateur**.
