---
role: comparatif
nom: Comparatif - BI auto-hébergée
categorie: data/bi
tags: [bi, dashboard, self-hosted]
---

# Comparatif - BI auto-hébergée

> On tranche sur : sans code ou SQL libre, ce que l'édition gratuite permet (SSO, droits par ligne, embedding), le nombre de pièces à exploiter, et la nature de la donnée (table d'entrepôt ou signal d'atelier).

![[Comparatif - BI auto-hébergée.base]]

## Ce qui départage

- [[Metabase]] — mise en route minimale (un conteneur, une base PostgreSQL) et usage sans code pour l'utilisateur métier ; mais c'est de l'open-core : AGPL-3.0, et SAML, JWT, OIDC, droits par ligne et par colonne, audit, SDK d'embedding et marque blanche exigent une édition payante.
- [[Apache Superset]] — Apache-2.0, sans édition payante : droits par ligne, alertes et rapports, embedding par SDK et SQL Lab libre sont dans la distribution ; le prix est l'exploitation (base de métadonnées, Redis, Celery, navigateur headless) et la configuration manuelle de l'authentification.
- [[Grafana]] — **absent de la vue ci-dessus, et c'est voulu** : il est rangé en observabilité, pour les métriques et les séries techniques branchées sur Prometheus, Loki ou une base temporelle. Il dépanne pour un tableau de bord d'exploitation d'atelier, pas pour l'exploration libre d'un entrepôt.
- [[Streamlit]] et [[Dash]] — **absents de la vue aussi** : ce sont des applications qu'un développeur écrit en Python, pas des outils servis à des utilisateurs qui ne programment pas. Le choix se fait quand l'écran est sur mesure ; la BI sert quand des équipes veulent poser leurs propres questions.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
