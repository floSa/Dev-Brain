---
role: brique
nom: Zapier
alias: [zapier]
pitch: "Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host."
categorie: automation/no-code
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[n8n]]", "[[Activepieces]]", "[[Windmill]]", "[[gumloop]]"]
complements: []
tags: [low-code, orchestration, agents]
url_docs: https://help.zapier.com/
url_repo: 
---

# Zapier

<!-- AUTO:BANDEAU:START -->
> Plateforme SaaS d'automatisation no-code / iPaaS (propriétaire) — connecte 8000+ applications via des « Zaps » (déclencheur → actions), plus Tables, Interfaces et agents IA ; entièrement managé, sans self-host.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

La référence historique de l'iPaaS no-code : on connecte plus de **8 000 applications** par des
« **Zaps** » — un déclencheur, puis une ou plusieurs actions. C'est le plus large catalogue
d'intégrations du marché, et le plus immédiat à prendre en main pour un profil métier : rien à
opérer, rien à installer, un compte suffit. L'offre a débordé du seul iPaaS avec **Tables**
(base de données d'automatisation), **Interfaces** (apps et formulaires), **Functions**
(Python), **Canvas** et des agents IA. Ce confort a une contrepartie structurelle, et elle
n'est pas technique mais économique — voir la colonne de droite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Connecter rapidement des SaaS grand public sans rien opérer ni coder | La facturation est **à la tâche** : le coût explose sur de gros volumes, et c'est le modèle économique, pas un palier à négocier |
| Vouloir le plus large catalogue d'intégrations du marché, prêt à l'emploi | Lock-in propriétaire : ni self-host, ni export du moteur — ce qui est construit ici y reste |
| Utilisateurs métier ou non développeurs : la prise en main est immédiate | Logique avancée — boucles, branches complexes — moins souple que chez les outils code-first |

## Mise en œuvre

- Installation — aucune : un compte suffit
- Point d'entrée — l'éditeur de Zaps ; Tables, Interfaces, Functions et Canvas complètent l'offre
- Prérequis — aucun ; c'est le point du produit
- Exécution — 100 % managé, sans self-host possible
- Coût — plan gratuit à 100 tâches/mois, puis Professional (~20 $/mois) et Team (~69 $/mois), Enterprise sur devis. Le coût suit le **volume de tâches** et le palier de fonctions, jamais l'infra

## Écosystème

### Alternatives

- [[n8n]] — Plateforme d'automatisation de workflows fair-code (source-available, Sustainable Use License) — éditeur visuel de nœuds avec code custom et nœuds IA natifs, 400+ intégrations ; self-host ou n8n Cloud.
- [[Activepieces]] — Automatisation de workflows open source (cœur MIT, éditeur Activepieces) — éditeur visuel TypeScript, 200+ pièces, agents IA et serveurs MCP ; self-host Docker ou Activepieces Cloud, alternative à Zapier.
- [[Windmill]] — Plateforme développeur open source (AGPLv3, Windmill Labs) — transforme des scripts (Python, TS, Go, Bash…) en workflows, UIs et apps internes ; moteur d'exécution distribué très rapide, self-host ou Windmill Cloud, alternative à Temporal/Retool.
- [[gumloop]] — Plateforme SaaS d'automatisation no-code pilotée par l'IA (propriétaire, YC W24) — canvas drag-and-drop où chaque nœud peut porter de la logique IA pour bâtir agents et workflows ; entièrement managé, sans self-host.

## Ressources

- Documentation — https://help.zapier.com/

## Voir aussi

- [[Automatisation no-code]] — le hub du domaine
- [[Comparatif - Automatisation no-code]] — ce qui départage les cinq plateformes du dossier
