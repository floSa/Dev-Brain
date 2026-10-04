---
role: notion
nom: Plannings de personnel (rostering)
alias: [rostering, nurse rostering, nurse scheduling, staff scheduling, personnel scheduling, planning de personnel, planning du personnel, planning d'équipes, roulement, shift scheduling, tour scheduling, days-off scheduling, planification des équipes, INRC]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [scheduling, constraint-programming, combinatorial-optimization]
---

# Plannings de personnel (rostering)

## Aperçu

- Décider **qui travaille quand** : pour chaque personne et chaque jour, un poste (matin, soir, nuit, repos), de sorte que chaque poste soit tenu par assez de monde, que les règles de travail soient respectées et que la charge soit répartie équitablement.
- Le problème est ancien (Dantzig en 1954 le traite en programmation linéaire pour des postes de péage) et reste actif : le rostering des infirmières fait l'objet d'un concours international à plusieurs éditions. La difficulté tient moins au calcul qu'à la **quantité de règles** : repos minimum, jours consécutifs maximum, compétences, souhaits, équité.
- Il se distingue de [[Ordonnancement d'atelier (job-shop, flow-shop)]] par les ressources (des personnes avec des droits, pas des machines) et par la question centrale : **couvrir une demande** de présence en respectant des règles, plutôt qu'enchaîner des tâches.

## Concepts clés

### Trois questions emboîtées

- **Combien de personnes par poste et par jour** : le dimensionnement. La demande de présence se déduit de la charge prévue (voir [[Forecasting framing]] pour la prévision d'un volume d'activité). Dantzig (1954) pose le problème de couverture avec une formulation de **recouvrement** : choisir, parmi des **motifs de travail** (par exemple cinq jours d'affilée puis deux de repos), combien de personnes suivent chacun, pour couvrir chaque jour au moins la demande en minimisant l'effectif.
- **Quels jours de repos** : Baker (1974, *Management Science* 20(12), 1561-1568) traite le cas d'une demande hebdomadaire cyclique où chaque personne a **deux jours de repos consécutifs** : un algorithme simple, calculable à la main, qui trouve l'**effectif minimal**.
- **Qui prend quel poste** : le rostering proprement dit, avec règles individuelles, préférences et équité. C'est ce que couvre la revue de Burke, De Causmaecker, Vanden Berghe et Van Landeghem (2004, *Journal of Scheduling* 7(6), 441-449) pour les infirmières : de l'équilibre de la charge au respect des préférences, des techniques de recherche opérationnelle aux méthodes d'intelligence artificielle. La revue d'Ernst, Jiang, Krishnamoorthy et Sier (2004, *European Journal of Operational Research* 153(1), 3-27) élargit à d'autres secteurs (transport, centres d'appel, santé) ; l'article n'a pas été lu (résumé indisponible dans la source consultée).

### Contraintes dures, contraintes souples

- Les **contraintes dures** font l'**admissibilité** : un poste n'a qu'une personne, une personne n'a qu'un poste par jour, repos minimum entre deux postes, limites légales ou conventionnelles. Un planning qui les viole est inutilisable.
- Les **contraintes souples** font la **qualité** : souhaits de jours de repos, équité de la charge de nuit et de week-end, succession agréable de postes. On les compte, avec un poids, dans une fonction objectif.
- La documentation d'OR-Tools sépare les deux dans ses exemples : le premier ne comporte que des contraintes dures (recherche d'un planning admissible), le second ajoute un objectif qui maximise le nombre de **souhaits satisfaits** (13 sur 20 dans l'exemple donné). Le **poids** donné à chaque contrainte souple est un choix de gestion, pas un résultat mathématique.

### Planning stable ou planning réactif

- Un planning publié se **défait** : absences, congés, pics d'activité. La seconde compétition internationale (INRC-II ; Ceschia, Dang, De Causmaecker, Haspeslagh, Schaerf, *Annals of Operations Research* 274, 171-186) formule un problème **à étapes** : on construit le planning semaine après semaine, avec une connaissance partielle du futur et un historique qui contraint la semaine suivante.
- Corollaire : un bon planning n'est pas seulement un planning de faible coût, c'est un planning **modifiable sans tout casser**. Les modèles de base l'ignorent.

## Les maths, simplement

- Recouvrement de motifs : $x_s$ le nombre de personnes qui **commencent** leur série de cinq jours le jour $s$ ; $a_{d,s} = 1$ si le jour $d$ est travaillé dans ce motif ; $r_d$ la demande du jour $d$ :
  $$\min \sum_s x_s \quad \text{sous} \quad \sum_s a_{d,s}\, x_s \ge r_d \;\;(d = 1,\dots,7), \qquad x_s \in \mathbb{N}.$$
  C'est un **problème en nombres entiers**, voir [[Programmation linéaire en nombres entiers (MIP)]].
- Exemple calculé ici (`scipy.optimize.milp`) : demande de lundi à dimanche $[17, 13, 15, 19, 14, 16, 11]$, soit 105 présences, motif de cinq jours de travail suivis de deux jours de repos.
  - borne triviale : $\lceil 105/5 \rceil = 21$ personnes, puisqu'une personne apporte cinq présences ;
  - **relaxation linéaire : 22,33** personnes ;
  - **optimum entier : 23** personnes, avec 7, 5, 1, 8, 0, 2 et 0 personnes qui commencent leur série du lundi au dimanche ; la couverture obtenue est $[17, 14, 15, 21, 21, 16, 11]$ ;
  - lecture : la contrainte « deux jours de repos consécutifs » coûte au moins deux personnes de plus que la borne triviale (23 contre 21). Lundi, mercredi, samedi et dimanche sont couverts exactement ; mardi, jeudi et vendredi sont sur-couverts de 1, 2 et 7 (10 présences de trop, soit $23 \times 5 - 105$) : un effectif plus bas ne tient pas, la structure des repos oblige à ce surplus.
- Exemple de rostering à contraintes dures, **reproduit ici** avec CP-SAT (OR-Tools 9.15) à partir de la page de documentation d'OR-Tools : 4 infirmières, 3 postes par jour, 3 jours ; chaque poste a exactement une personne, chacune travaille au plus un poste par jour et entre 2 et 3 postes au total. L'énumération trouve **5 184 plannings admissibles**, le même nombre que la documentation. Le modèle tient en trois familles de contraintes :

```python
x = {(n, d, s): m.NewBoolVar("") for n in range(N) for d in range(D) for s in range(S)}
for d in range(D):
    for s in range(S): m.AddExactlyOne(x[n, d, s] for n in range(N))   # un poste = une personne
    for n in range(N): m.AddAtMostOne(x[n, d, s] for s in range(S))     # un poste par jour au plus
for n in range(N):
    t = sum(x[n, d, s] for d in range(D) for s in range(S)); m.Add(t >= 2); m.Add(t <= 3)  # équité
```

- Lecture : **5 184** admissibles sur 3 jours seulement. Le nombre explose avec l'horizon, et c'est ce qui rend l'énumération inutilisable en pratique. La question devient : parmi les admissibles, lequel est le meilleur selon les contraintes souples.

## En pratique

- **Écrire les règles avant de modéliser.** Quelles sont les limites légales et conventionnelles ? Elles dépendent du pays, de la convention collective et du statut ; elles ne sont pas traitées ici. Chaque règle écrite devient une contrainte, dure ou souple : la liste est la vraie spécification.
- **Une contrainte dure de trop rend le problème infaisable** : le solveur répond « aucun planning » plutôt que « presque ». Passer une règle en souple, avec un poids élevé, donne un planning qui viole le moins possible et dit laquelle des règles pose problème.
- **Les souhaits individuels sont un arbitrage** : 13 souhaits satisfaits sur 20 (exemple d'OR-Tools) n'est pas « 65 % de réussite » mais l'état du compromis entre souhaits et couverture. Équité : mesurer la dispersion (écart entre la personne la plus et la moins chargée en nuits) plutôt que la moyenne.
- **Outils** : le modèle à variables booléennes et contraintes de cardinalité s'écrit directement en [[Programmation par contraintes]] ; la formulation en nombres entiers donne en plus une **borne** (relaxation) qui dit à quelle distance de l'optimum on se trouve. Pour les instances de référence et la comparaison de méthodes : les instances des compétitions internationales d'infirmières (INRC-I, INRC-II) sont publiques. Aucune brique de solveur n'a de page dans ce dossier pour le moment : OR-Tools est cité en texte simple.
- **Données d'entrée** : la demande de présence vient en partie de la prévision d'activité, qui a son erreur. Un planning calé sur la prévision moyenne est insuffisant les jours de pointe ; voir [[De la prévision probabiliste à la quantité commandée]] pour la même idée appliquée à un stock (un quantile plutôt qu'une moyenne).

## Approches voisines & alternatives

- [[Programmation par contraintes]] — la modélisation naturelle : variables booléennes, cardinalités, règles de succession.
- [[Programmation linéaire en nombres entiers (MIP)]] — la formulation par motifs de travail, avec relaxation linéaire comme borne.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — placer des tâches sur des machines plutôt que des personnes sur des postes.
- [[Tournées de véhicules (VRP)]] — les routes des véhicules, un autre problème de construction sous contraintes de capacité et de fenêtres de temps.
- [[Optimisation combinatoire]] — le cadre général (affectation, couverture) dont le rostering est une instance riche.
- [[Forecasting framing]] — comment la demande de présence est prévue.
- [[Optimisation sous contrainte]] — le sens des poids de pénalité des contraintes souples (multiplicateurs).

## Pour aller plus loin

- Dantzig (1954), *A Comment on Edie's « Traffic Delays at Toll Booths »*, Journal of the Operations Research Society of America 2(3), 339-341 : <https://ideas.repec.org/a/inm/oropre/v2y1954i3p339-341.html> (notice lue, article non lu)
- Baker (1974), *Scheduling a Full-Time Workforce to Meet Cyclic Staffing Requirements*, Management Science 20(12), 1561-1568 : <https://ideas.repec.org/a/inm/ormnsc/v20y1974i12p1561-1568.html> (résumé lu)
- Burke, De Causmaecker, Vanden Berghe, Van Landeghem (2004), *The state of the art of nurse rostering*, Journal of Scheduling 7(6), 441-449 : <https://lirias.kuleuven.be/handle/123456789/496913> (résumé lu)
- Ernst, Jiang, Krishnamoorthy, Sier (2004), *Staff scheduling and rostering: A review of applications, methods and models*, European Journal of Operational Research 153(1), 3-27 : <https://ideas.repec.org/a/eee/ejores/v153y2004i1p3-27.html> (notice seule)
- Ceschia, Dang, De Causmaecker, Haspeslagh, Schaerf (2019), *The Second International Nurse Rostering Competition*, Annals of Operations Research 274, 171-186 : <https://research-repository.st-andrews.ac.uk/handle/10023/20910> (résumé lu) ; description du problème : <https://arxiv.org/abs/1501.04177>
- Documentation OR-Tools, *Employee Scheduling* : <https://developers.google.com/optimization/scheduling/employee_scheduling> (page lue ; 5 184 solutions reproduites)
- Connexions brain : [[Programmation par contraintes]], [[Programmation linéaire en nombres entiers (MIP)]], [[Ordonnancement d'atelier (job-shop, flow-shop)]], [[Tournées de véhicules (VRP)]], [[Optimisation combinatoire]].
