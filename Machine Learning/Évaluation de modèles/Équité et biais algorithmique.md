---
role: notion
nom: Équité et biais algorithmique
alias: [Fairness, équité algorithmique, fairness in machine learning, biais algorithmique, algorithmic bias, parité démographique, demographic parity, parité statistique, statistical parity, égalité des chances, equal opportunity, equalized odds, odds égalisées, parité prédictive, predictive parity, calibration par groupe, disparate impact, règle des quatre cinquièmes, règle des 80 %, théorème d'impossibilité de l'équité, anti-classification, COMPAS, attribut sensible, reweighing, AI Act et biais]
categorie: ml/eval
domaines: [data-sci, ml-eng]
tags: [model-evaluation, classification, supervised]
---

# Équité et biais algorithmique

## Aperçu

- Un modèle peut être précis **en moyenne** et se tromper bien plus pour un groupe de personnes (défini par le sexe, l'origine, l'âge…). L'**équité algorithmique** cherche à **définir**, **mesurer** puis **réduire** cet écart.
- Il n'existe pas **une** définition. Les trois plus courantes — parité démographique, égalité des chances, calibration par groupe — sont **incompatibles** entre elles sauf cas particuliers (Kleinberg, Mullainathan, Raghavan, 2016 ; Chouldechova, 2017). Choisir l'une, c'est renoncer aux autres : un choix de société avant d'être un réglage.
- Chouldechova le dit en une phrase : l'équité est « un concept social et éthique, pas statistique » (§1). Plusieurs critiques (Corbett-Davies et al. ; Selbst et al. ; Fazelpour et Lipton) vont plus loin : les métriques de groupe seules ne suffisent pas à juger une décision.
- Le biais ne vient pas seulement du modèle : il traverse tout le cycle de vie (données, étiquettes, mesure, déploiement). Cette page porte les **définitions**, leurs **limites**, les **sources**, l'**atténuation** et une section sur le **cadre européen**, **sans conseil juridique**.
- Notions proches non répétées : la [[Calibration]] (dont la version « par groupe » est ici un critère d'équité), l'[[Explicabilité des modèles]] (voir ce qui pèse dans une prédiction), [[Imbalanced classification]] (les classes rares).

## Concepts clés

### Trois critères, trois familles
Barocas, Hardt et Narayanan (*Fairness and Machine Learning*, 2023) regroupent les définitions en trois critères sur la prédiction $R$, l'attribut sensible $A$ et la cible $Y$ :
- **Indépendance** : $R \perp A$. Le score est indépendant du groupe. C'est la **parité démographique** (même taux de décisions positives).
- **Séparation** : $R \perp A \mid Y$. À cible égale, le score ne dépend pas du groupe : mêmes taux de vrais et de faux positifs. C'est l'**égalité des chances** (Hardt, Price, Srebro, 2016).
- **Suffisance** : $Y \perp A \mid R$. À score égal, la cible ne dépend pas du groupe. C'est la **calibration par groupe** et la **parité prédictive**.
- **Exclusions mutuelles** (chapitre « Classification », lu par un résumé seulement) : indépendance et suffisance sont incompatibles si $A$ et $Y$ sont dépendants ; indépendance et séparation, et séparation et suffisance, sous conditions.

### Parité démographique et règle des quatre cinquièmes
- **Définition** : $\Pr(\hat{Y}=1 \mid A=a)$ identique pour tous les groupes.
- **Règle des 80 %** : Feldman et al. (KDD 2015, *Certifying and removing disparate impact*) la décrivent comme une généralisation d'une règle défendue par l'EEOC (*Uniform Guidelines* de 1979 ; *Griggs v. Duke Power*, 401 U.S. 424) : on compare le rapport $\Pr(C{=}\text{oui} \mid X{=}0) / \Pr(C{=}\text{oui} \mid X{=}1)$ à 0,8. Le texte précise que l'impact disproportionné n'est **pas illégal en soi** (défense par « nécessité économique »).
- **Insuffisance** : Dwork et al. (ITCS 2012, *Fairness through awareness*, §3.1) montrent pourquoi la parité statistique ne suffit pas, avec des exemples d'**utilité réduite** et de **prophétie auto-réalisatrice**. Leur propre critère est l'**équité individuelle** : des individus semblables sont traités de même (propriété de Lipschitz sur une distance entre individus).

### Égalité des chances et odds égalisées
- **Odds égalisées** (Hardt et al., Déf. 2.1) : mêmes taux de vrais positifs **et** de faux positifs entre groupes. **Égalité des chances** (Déf. 2.2) : seulement les vrais positifs, pour $Y=1$.
- **Post-traitement par seuils** : on dérive un prédicteur à partir du score et du groupe, avec des seuils propres à chaque groupe. Pour les odds égalisées, c'est un programme linéaire à quatre variables ; la région réalisable est l'intersection des zones sous les courbes ROC conditionnelles, avec éventuellement des seuils randomisés ; l'égalité des chances se fait avec deux seuils déterministes.
- **Coût mesuré sur FICO** (§7 de la première version de l'arXiv, à 82 % de non-défaut, non recoupé avec la version publiée) : seuil aveugle au groupe, 99,3 % du profit maximal ; égalité des chances, 92,8 % ; odds égalisées, 80,2 % ; parité démographique, 69,8 %.

### Théorèmes d'impossibilité
- **Kleinberg, Mullainathan, Raghavan** (ITCS 2017, arXiv 1609.05807) formalisent trois conditions : (A) **calibration à l'intérieur de chaque groupe** ; (B) **équilibre pour la classe négative** (même score moyen pour les négatifs de chaque groupe) ; (C) **équilibre pour la classe positive**. **Théorème 1.1** : si une assignation de risque satisfait les trois, l'instance admet soit la **prédiction parfaite**, soit des **taux de base égaux** ; il n'y a que ces deux cas. **Théorème 1.2** : la version approchée, qui impose d'être proche de l'un d'eux. Le résultat vaut quelle que soit la méthode de calcul du score.
- **Chouldechova** (*Big Data*, 2017, arXiv 1610.07524) : $\text{FPR} = \frac{p}{1-p}\cdot\frac{1-\text{PPV}}{\text{PPV}}\cdot(1-\text{FNR})$ (Éq. 2.4), où $p$ est la prévalence. Si $p$ diffère entre groupes, une valeur prédictive positive égale (un score « équitable au test ») ne peut pas s'accompagner de taux de faux positifs **et** de faux négatifs égaux.
- **Cas COMPAS (Broward)** : prévalence de récidive de 51 % chez les Noirs contre 39 % chez les Blancs ; taux de faux positifs de 45 % contre 23 %, de faux négatifs de 28 % contre 48 %. Kleinberg et al. notent que la critique d'Angwin et al. porte sur la violation de (B) et (C), les défenseurs de l'outil invoquant (A), que COMPAS satisfait.
- **Une discussion plus ancienne que le ML** : Hutchinson et Mitchell (FAT* 2019, *50 years of test (un)fairness*) relèvent que l'équité dans les tests éducatifs, de 1966 à 1976, contenait déjà des critères mathématiques identiques, un constat d'incompatibilité et des critiques ; elle s'est essoufflée à la fin des années 1970.
- **Travaux 2026 (résumés seulement)** : Penn et Patty (arXiv 2604.06378) montrent que l'incompatibilité entre équilibre des erreurs et parité prédictive peut être levée par une conception en deux étapes, **au prix d'un traitement différencié** des conséquences d'une même classification ; Alsayed (arXiv 2604.15038, reconnaissance faciale) propose un indice de désaccord entre métriques d'équité, qui persiste selon les seuils.

## Sources de biais

Suresh et Guttag (EAAMO 2021, arXiv 1901.10002) en distinguent sept le long du cycle de vie, qui recouvrent les quatre étapes courantes — données, étiquettes, mesure, déploiement :
- **Historique** : le monde reflète déjà une inégalité ; il survient **même si** les données sont parfaitement mesurées et échantillonnées.
- **Représentation** : un échantillon qui sous-représente une population.
- **Mesure** : le choix et la fabrication des variables et des **étiquettes** (une étiquette est une mesure, souvent un indicateur indirect de ce qu'on veut prédire).
- **Agrégation** : un modèle unique pour des groupes dont les relations diffèrent.
- **Apprentissage** : les choix d'objectif et d'optimisation.
- **Évaluation** : un jeu de test ou des métriques qui ne représentent pas la population cible.
- **Déploiement** : l'usage réel diffère de l'usage prévu.
- Mehrabi et al. (ACM Computing Surveys 54(6), 2021) organisent la typologie en **boucle** données → algorithme → utilisateur, où la sortie d'un modèle alimente ses futures entrées. Barocas et al. (chapitres « Causality » et « Legitimacy », résumés) traitent la confusion (l'exemple de Berkeley, paradoxe de Simpson) et l'écart entre cible et objectif.

## Atténuation : avant, pendant, après l'entraînement

- **Avant** (sur les données) : repondérer (Kamiran et Calders, 2012, non ouvert) ou **réparer** les données pour retirer l'impact disproportionné (Feldman et al.).
- **Pendant** (dans l'optimisation) : l'**apprentissage adversaire** de Zhang, Lemoine, Mitchell (AIES 2018, arXiv 1801.07593) entraîne un prédicteur contre un adversaire qui tente de retrouver l'attribut sensible depuis la sortie ; sur UCI Adult, le résultat est « très proche de l'égalité des chances ». Autres voies : contraintes d'équité, réductions.
- **Après** (sur les sorties) : seuils par groupe (Hardt et al.). Mehrabi et al. (Table 4) classent les méthodes selon ce à quoi elles exigent l'accès : données, modèle ou sorties seulement.
- **Les compromis** : Wilms et Heitz (FAccT 2026, arXiv 2605.10604, résumé seulement) caractérisent la frontière de Pareto équité-performance : elle est faite de **seuils déterministes propres à chaque groupe**. Corbett-Davies et al. (voir plus bas) montrent que certaines définitions mènent à des politiques **dominées au sens de Pareto**.
- **Outils** : Fairlearn 0.14.0 (PyPI, 7 juin 2026) propose `CorrelationRemover` (avant), `ThresholdOptimizer` (après, d'après Hardt et al.), `ExponentiatedGradient` et `GridSearch` (réductions) et des classifieurs adversaires ; AIF360 0.6.1 (PyPI, 8 avril 2024) couvre le pré-traitement, le traitement pendant l'apprentissage et le post-traitement, sans que la liste des algorithmes ait été relevée. Ni l'un ni l'autre n'a de brique dans le vault.

## Critiques des définitions formelles

- **Corbett-Davies, Gaebler, Nilforoshan, Shroff, Goel** (JMLR 24, 2023, arXiv 1808.00023, *The Measure and Mismeasure of Fairness*) : la **parité de classification** et l'**anti-classification** (ignorer l'attribut sensible) conduisent à des politiques fortement dominées au sens de Pareto ; la conception équitable doit passer par les **conséquences**, comme pour une politique publique. La calibration est traitée à part, avec la notion de miscalibration entre sous-groupes.
- **Selbst, boyd, Friedler, Venkatasubramanian, Vertesi** (FAT* 2019, *Fairness and abstraction in sociotechnical systems*) : cinq pièges d'abstraction : *Framing*, *Portability*, *Formalism*, *Ripple Effect*, *Solutionism*.
- **Fazelpour et Lipton** (AIES 2020, arXiv 2001.09773, *Algorithmic fairness from a non-ideal perspective*) : les métriques de parité relèvent de l'approche « idéale » de la philosophie politique ; elles négligent les mécanismes qui ont produit le monde non idéal, les responsabilités des décideurs et l'impact des politiques ; ils proposent aussi une relecture des résultats d'impossibilité.
- **Désaccord laissé tel quel** : Kleinberg et Chouldechova présentent l'incompatibilité comme un résultat mathématique **intrinsèque** ; Penn et Patty (2026) la lèvent par un changement de modèle ; Corbett-Davies et Fazelpour–Lipton contestent que choisir une métrique de groupe soit la bonne question. Aucune source lue ne tranche.

## Modèles de langage (2026, résumés seulement)

- **Gao, Jiang, Yan** (arXiv 2606.28978) : quatorze modèles sur le tri de CV, 24 024 paires d'offres par modèle. Le seul modèle de 2023 montre un écart favorable aux candidats blancs de +2,12 points ; les modèles de 2024 et après montrent un écart nul ou inversé, jusqu'à −3,01 points.
- **Vohra et Ravikiran** (arXiv 2609.09048) : 40 726 requêtes sur cinq modèles ; ils concluent que les verdicts d'audit reflètent davantage **la construction de l'audit** que le biais démographique. **Les deux travaux se contredisent en partie** : le premier mesure des écarts qui évoluent d'une génération à l'autre, le second doute de ce que mesure l'audit. Désaccord laissé tel quel.

## Cadre réglementaire européen (faits sourcés, pas un conseil juridique)

- **AI Act, règlement (UE) 2024/1689** (texte du Journal officiel relu sur EUR-Lex, version adoptée) :
  - **Art. 10(2)(f) et (g)** : pour les systèmes à haut risque, la gouvernance des données comprend l'**examen des biais** susceptibles d'affecter la santé et la sécurité des personnes, d'avoir un effet négatif sur les droits fondamentaux ou de conduire à une discrimination interdite par le droit de l'Union, en particulier lorsque les sorties influencent les entrées futures, et des **mesures appropriées pour détecter, prévenir et atténuer** ces biais.
  - **Art. 10(3)** : jeux d'entraînement, de validation et de test **pertinents, suffisamment représentatifs**, autant que possible sans erreurs et complets au regard de la finalité, avec des propriétés statistiques appropriées, y compris pour les groupes de personnes concernés.
  - **Art. 10(5)** : exception pour traiter des **catégories particulières de données personnelles**, « dans la mesure strictement nécessaire » à la détection et à la correction des biais, sous six conditions : impossibilité de le faire avec d'autres données, y compris synthétiques ou anonymisées ; limites techniques de réutilisation et mesures de sécurité de pointe ; accès strictement contrôlé et documenté ; pas de transmission à des tiers ; suppression une fois le biais corrigé ; inscription au registre des traitements des raisons de la stricte nécessité.
  - **Annexe III** (haut risque) : emploi (recrutement, sélection, décisions sur la relation de travail) ; services essentiels (la page de la Commission cite l'évaluation de solvabilité comme exemple).
  - **Application** : le texte adopté prévoit une application générale au **2 août 2026**. La page de la Commission (consultée le 2026-10-02) donne le **2 décembre 2027** pour les obligations des systèmes à haut risque, ce qui diffère du texte adopté ; elle mentionne un « AI Omnibus ». Le texte officiel de cet omnibus n'a pas été relu : d'après des reproductions non officielles, il ajouterait une base juridique pour traiter des catégories particulières de données dans la détection de biais ; **non vérifié à la source officielle**.
- **RGPD** (règlement 2016/679, articles relus sur une reproduction non officielle) : l'**article 22** donne le droit de ne pas faire l'objet d'une décision fondée **exclusivement** sur un traitement automatisé, y compris le profilage, produisant des effets juridiques ou affectant la personne de manière significative ; des exceptions (22(2)), des garanties dont l'intervention humaine (22(3)), et l'interdiction de fonder ces décisions sur les catégories de l'**article 9(1)** sauf consentement explicite ou intérêt public important (22(4)). Le **considérant 71** demande de prévenir les effets discriminatoires et d'employer des procédures mathématiques ou statistiques appropriées.
- **Ce qui n'est pas dans les sources lues** : la qualification d'un système donné, les sanctions, les obligations du déployeur. À confier à un juriste.

## Les maths, simplement

- **Parité démographique** : $\Pr(\hat{Y}=1\mid A=a) = \Pr(\hat{Y}=1\mid A=b)$. **Rapport d'impact** : $\mathrm{DI} = \frac{\Pr(\hat{Y}=1\mid A=0)}{\Pr(\hat{Y}=1\mid A=1)}$, comparé à 0,8.
- **Odds égalisées** : $\Pr(\hat{Y}=1\mid Y=y, A=a) = \Pr(\hat{Y}=1\mid Y=y, A=b)$ pour $y \in \{0,1\}$ ; **égalité des chances** : $y=1$ seulement.
- **Calibration par groupe** : $\Pr(Y=1\mid S=s, A=a) = s$ pour tout score $s$ et tout groupe $a$.
- **Impossibilité (Chouldechova)** : $\text{FPR} = \frac{p}{1-p}\cdot\frac{1-\text{PPV}}{\text{PPV}}\cdot(1-\text{FNR})$ : à PPV fixé, si $p_a \ne p_b$, les trois taux ne peuvent pas être égaux entre groupes en même temps.
- **Ce qui rend l'identité vraie** : toutes les quantités se déduisent de la matrice de confusion et de la prévalence ; l'incompatibilité n'est pas un défaut d'algorithme.

## En pratique

- **Choisir la définition d'après la décision, pas d'après la commodité** : qui subit une erreur (un faux positif refuse un crédit, un faux négatif laisse passer une fraude), qui décide ensuite, quelle est la base légale. L'écrire.
- **Mesurer par groupe avant tout** : taux de décisions positives, TPR, FPR, PPV, calibration par groupe ([[Calibration]]), avec les intervalles de confiance sur les petits groupes. Rapporter plusieurs définitions et leur **désaccord** (Alsayed) plutôt qu'une seule métrique.
- **Chercher la source avant le correctif** : étiquettes biaisées (voir [[Annotation de données]] : accord entre annotateurs, biais d'ancrage), échantillon non représentatif, mesure par proxy. Un correctif sur le score ne répare pas une étiquette fausse.
- **Ne pas se contenter de retirer l'attribut sensible** : l'anti-classification est l'une des définitions critiquées par Corbett-Davies et al. Mesurer un écart entre groupes exige de **disposer** de l'attribut pour l'évaluation, ce que l'article 10(5) de l'AI Act encadre pour les données sensibles.
- **Expliquer ne mesure pas l'équité** : [[SHAP]] et [[LIME]] montrent ce qui pèse dans une prédiction ; aucun ne calcule un critère d'équité.
- **Surveiller après le déploiement** : les métriques par groupe dérivent avec la population ([[Monitoring de modèle en production]], [[Data drift]]) ; le déploiement est une source de biais à part entière.
- **Coût en utilité et en confidentialité** : l'atténuation coûte de la performance (FICO, plus haut) ; la [[Confidentialité différentielle]] creuse l'écart entre sous-groupes (Bagdasaryan et al.).
- **Cadre européen** : les exigences de l'article 10 portent sur les **données** et leur gouvernance, avant le modèle.

## Approches voisines & alternatives

- [[Calibration]] — la calibration par groupe est l'un des trois critères ; l'incompatibilité avec les taux d'erreur égaux en est le théorème.
- [[Explicabilité des modèles]] — comprendre ce qui pèse dans une prédiction ; complémentaire, pas un test d'équité.
- [[Imbalanced classification]] — groupes ou classes rares : mêmes précautions sur les petits effectifs et le choix du seuil.
- [[Classification metrics]] et [[ROC-AUC & courbe PR]] — les métriques qu'on décline par groupe (TPR, FPR, PPV).
- [[Annotation de données]] — la source « mesure » : étiquettes et accord entre annotateurs.
- [[Data leakage]] — autre biais d'évaluation, sans lien avec le groupe : un chiffre trop beau, quel que soit le groupe.
- [[Monitoring de modèle en production]] et [[Data drift]] — suivre les métriques par groupe après le déploiement.
- [[Confidentialité différentielle]] — son coût d'utilité est inégal selon les sous-groupes.
- [[Synthetic data generation]] — l'article 10(5) de l'AI Act place les données synthétiques ou anonymisées avant l'usage de données sensibles pour détecter des biais.
- [[SHAP]] et [[LIME]] — outils d'explicabilité ; ils n'ont pas d'équivalent « équité » dans le vault (Fairlearn et AIF360 n'ont pas de brique).

## Pour aller plus loin

- Kleinberg, Mullainathan & Raghavan (2016) — [*Inherent Trade-Offs in the Fair Determination of Risk Scores*](https://arxiv.org/abs/1609.05807), ITCS 2017 ; Chouldechova (2017) — [*Fair prediction with disparate impact*](https://arxiv.org/abs/1610.07524), Big Data ; Hardt, Price & Srebro (2016) — [*Equality of Opportunity in Supervised Learning*](https://arxiv.org/abs/1610.02413), NIPS 2016.
- Barocas, Hardt & Narayanan (2023) — [*Fairness and Machine Learning: Limitations and Opportunities*](https://fairmlbook.org), MIT Press (trois chapitres lus par résumé).
- Feldman et al. (2015) — [*Certifying and removing disparate impact*](https://arxiv.org/abs/1412.3756), KDD 2015 ; Dwork et al. (2012) — [*Fairness Through Awareness*](https://arxiv.org/abs/1104.3913), ITCS 2012.
- Suresh & Guttag (2021) — [*A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle*](https://arxiv.org/abs/1901.10002), EAAMO 2021 ; Mehrabi et al. (2021) — [*A Survey on Bias and Fairness in Machine Learning*](https://arxiv.org/abs/1908.09635), ACM Computing Surveys 54(6) ; Zhang, Lemoine & Mitchell (2018) — [*Mitigating Unwanted Biases with Adversarial Learning*](https://arxiv.org/abs/1801.07593).
- Critiques : Corbett-Davies et al. (2023) — [*The Measure and Mismeasure of Fairness*](https://arxiv.org/abs/1808.00023), JMLR 24 ; Selbst et al. (2019) — *Fairness and Abstraction in Sociotechnical Systems*, FAT* 2019 ; Hutchinson & Mitchell (2019) — [*50 Years of Test (Un)fairness*](https://arxiv.org/abs/1811.10104) ; Fazelpour & Lipton (2020) — [*Algorithmic Fairness from a Non-ideal Perspective*](https://arxiv.org/abs/2001.09773), AIES 2020.
- Règlement (UE) 2024/1689 — [texte sur EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689) ; [page de la Commission sur l'AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).
- Non ouvert : Kamiran & Calders (2012), pondération.
