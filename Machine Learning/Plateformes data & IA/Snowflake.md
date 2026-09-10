---
role: brique
nom: Snowflake
alias: [snowflake, Snowpark, Snowflake Cortex, Snowflake ML]
pitch: "Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement."
categorie: ml/plateforme
famille: saas
domaines: [data-eng, data-sci, ai-eng]
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: distributed
alternatives: ["[[Databricks]]", "[[ClickHouse]]", "[[DuckDB]]"]
complements: ["[[Streamlit]]"]
tags: [ml-platform, olap, columnar, distributed, data-governance, llm]
url_docs: https://docs.snowflake.com/
url_repo: 
---

# Snowflake

<!-- AUTO:BANDEAU:START -->
> Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Entrepôt de données managé dont l'architecture sépare le **stockage** du **calcul** : les
données vivent dans un stockage objet, et des entrepôts virtuels dimensionnés indépendamment
les interrogent, se suspendent et se réveillent à la demande. Ce qui l'a fait sortir du rang
des moteurs est l'exécution qu'il a absorbée : **Snowpark** fait tourner du Python, du Java et
du Scala dans le moteur, **Snowpark Container Services** y déploie des conteneurs sur des
pools de calcul, GPU compris, **Cortex** expose des fonctions LLM appelables en SQL, et
**Snowflake ML** porte l'entraînement distribué et un registre de modèles. Le produit est
entièrement managé : il tourne sur AWS, Azure ou GCP, et **aucune installation sur site
n'existe ni n'est annoncée**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| L'entrepôt SQL est déjà le centre de gravité, et l'IA doit venir à la donnée plutôt que l'inverse | **Aucun auto-hébergement, et rien qui l'annonce** : éliminatoire dès que les données ne peuvent pas sortir du site |
| Le besoin est de gouverner un périmètre unique : catalogue, droits, journal d'audit sur données et modèles | Les fonctions maison — Cortex en SQL, procédures Snowpark — **ne se rejouent nulle part ailleurs** : c'est là que l'enfermement se paie |
| Des équipes SQL doivent accéder à des modèles sans changer d'outil | Le calcul se facture à la seconde d'entrepôt virtuel : un traitement mal dimensionné coûte vite |
| La séparation stockage / calcul doit permettre d'isoler les charges par équipe | Data engineering lourd en code, sur des fichiers plutôt que des tables → [[Databricks]] |
| L'exploitation doit rester nulle : pas de cluster à tenir | Analytique locale sur un poste, ou volumes modestes → [[DuckDB]] |
| | Analytique temps réel à très faible latence sur des événements → [[ClickHouse]] |

## Mise en œuvre

- Installation — rien à installer : un compte Snowflake, sur AWS, Azure ou GCP
- Point d'entrée — SQL, depuis l'interface web ou un pilote ; Snowpark pour le Python dans le moteur
- Prérequis — un compte chez Snowflake ; le dimensionnement des entrepôts virtuels et leur suspension automatique, faute de quoi la facture dérive
- Exécution — managé, distribué ; entrepôts virtuels indépendants, pools de calcul pour les conteneurs et les charges GPU
- Coût — à l'usage : crédits de calcul par seconde d'entrepôt actif, plus le stockage

## Écosystème

### Alternatives

- [[Databricks]] — Plateforme lakehouse bâtie sur Spark et Delta Lake, managée sur AWS, Azure ou GCP : data engineering, SQL analytique et ML dans un même espace, gouvernés par Unity Catalog ; très technique, et sans auto-hébergement. — le concurrent frontal : l'arbitrage se joue sur le point de départ, entrepôt SQL contre lac de fichiers.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — même famille colonnes, mais un moteur qu'on opère soi-même et qui vise la latence, pas la plateforme.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — l'extrême inverse : rien à héberger parce que rien n'est hébergé, et le volume tient sur un poste.

### Compléments

- [[Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS. — racheté par Snowflake, et exécutable dans le compte pour publier une application à côté des données.

## Ressources

- Documentation — https://docs.snowflake.com/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Comparatif - Bases colonnes]] — les moteurs colonnes dont il vient, et dont le rangement l'a séparé
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
