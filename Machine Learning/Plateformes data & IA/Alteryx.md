---
role: brique
nom: Alteryx
alias: [alteryx, Alteryx Designer, Alteryx Server, Alteryx Analytics Cloud]
pitch: "Préparation, enrichissement et analyse de données en flux visuels sans code, pour analystes métier : Designer sur poste Windows, Server pour publier et planifier, Analytics Cloud pour la version managée."
categorie: ml/plateforme
famille: application
domaines: [data-eng, data-sci]
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: 
os: "Windows"
alternatives: ["[[Dataiku]]"]
complements: []
tags: [ml-platform, low-code, data-pipeline, data-quality]
url_docs: https://help.alteryx.com/
url_repo: 
---

# Alteryx

<!-- AUTO:BANDEAU:START -->
> Préparation, enrichissement et analyse de données en flux visuels sans code, pour analystes métier : Designer sur poste Windows, Server pour publier et planifier, Analytics Cloud pour la version managée.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application | propriétaire | self-hébergé ou managé | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de préparation et d'analyse de données par **flux visuels** : on relie des blocs —
lire, joindre, filtrer, agréger, enrichir, écrire — sur un canevas, sans écrire de code. Son
public historique est l'analyste métier, pas le développeur, et c'est ce qui explique sa place
dans les directions financières et commerciales. Le produit se lit en trois morceaux :
**Designer**, l'application de conception installée sur un poste Windows ; **Server**, qui
publie, planifie et partage les flux et se déploie sur site ou sur une machine virtuelle ; et
**Analytics Cloud**, l'offre managée. La famille de la fiche suit Designer, point d'entrée
documenté en premier — règle R3 de la taxonomie.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des analystes métier doivent préparer et croiser des données sans passer par l'informatique | Un flux visuel se **relit, se teste et se versionne mal** : la revue par un pair est difficile, et le suivi des changements est pauvre face à du code dans Git |
| Reprendre un existant Alteryx déjà en place, souvent en finance ou en commerce | La conception est **liée à Windows** : pas de poste de conception Linux ni macOS |
| Le besoin s'arrête à la préparation, l'enrichissement et le reporting | La modélisation avancée n'est pas son terrain : entraîner, déployer et surveiller des modèles → [[DataRobot]] ou [[Dataiku]] |
| Il faut publier et planifier des traitements sur un serveur qu'on possède | Les volumes dépassent ce qu'un poste ou un serveur unique absorbe → [[Databricks]] ou [[Snowflake]] |
| L'autonomie des analystes prime sur la reproductibilité stricte | Une équipe qui écrit du Python : le même travail se fait en [[pandas]] ou [[Polars]], versionné |

## Mise en œuvre

- Installation — Designer s'installe sur un poste Windows ; Server se déploie sur site, sur machine virtuelle ou chez un hébergeur ; Analytics Cloud est managé
- Point d'entrée — le canevas de Designer : des blocs reliés, exécutés localement puis publiés
- Prérequis — un poste Windows pour concevoir ; un Server pour partager, planifier et exécuter sans le poste de l'auteur
- Exécution — Designer sur un seul poste ; Server répartit les exécutions sur ses workers
- Coût — licence commerciale par utilisateur pour Designer, licence serveur à part

## Écosystème

### Alternatives

- [[Dataiku]] — Plateforme data et IA de bout en bout, auto-hébergeable : un même projet se construit en interface visuelle ou en Python, R et SQL, avec préparation, entraînement, déploiement et gouvernance sous une seule console et un seul modèle de droits. — le concurrent direct sur le visuel, avec en plus la moitié data science et le code.

## Ressources

- Documentation — https://help.alteryx.com/

## Voir aussi

- [[Plateformes data & IA]] — le hub du dossier
- [[Plateforme data & IA — concept]] — ce qu'une plateforme intègre, et ce qu'elle enferme
- [[Featuretools]] — l'ingénierie de variables automatique, maintenue par Alteryx et publiée en open-source
- [[Comparatif - Plateformes data & IA]] — ce qui départage les huit suites
