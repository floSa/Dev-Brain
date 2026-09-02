---
role: hub
nom: Relationnel
pitch: Tables à schéma fixe, SQL et transactions ACID — le défaut solide de la majorité des applications.
domaines: [data-eng, data-sci]
---

# Relationnel

> Tables à schéma fixe, SQL et transactions ACID — le défaut solide de la majorité des applications.

## Ce qu'il faut comprendre

- Le modèle relationnel range la donnée en tables reliées par clés, impose un schéma, et garantit l'**ACID** : une transaction passe entièrement ou pas du tout. C'est ce qui le rend ennuyeux, et c'est exactement pourquoi on le prend par défaut.
- Ces moteurs sont taillés pour l'**OLTP** — beaucoup de petites transactions concurrentes. Les grosses agrégations analytiques relèvent du colonnaire ([[ClickHouse]], [[DuckDB]]), au niveau du domaine.
- Le distribué (« NewSQL ») n'est pas une version plus grosse du mono-instance : [[CockroachDB]] paie la cohérence multi-région en latence d'écriture.

## Choisir

- Aucune contrainte particulière → [[Postgres]]. C'est le standard de fait, le plus extensible, et l'écosystème le plus fourni.
- Une base = un fichier, zéro administration, embarqué → [[SQLite]].
- Écosystème web historique, hébergement mutualisé → [[MySQL]] ou son fork communautaire [[MariaDB]].
- Contrainte d'entreprise .NET / Azure → [[Microsoft SQL Server]].
- Scale horizontal et forte cohérence multi-région, en gardant SQL → [[CockroachDB]].

<!-- AUTO:START -->
### Briques
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.

### Comparatifs
- [[Comparatif - Bases relationnelles]]
<!-- AUTO:END -->
