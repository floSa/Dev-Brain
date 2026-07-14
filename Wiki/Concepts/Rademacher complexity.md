---
galaxie: wiki
type: concept
nom: Rademacher complexity
alias: [Complexité de Rademacher, Rademacher, complexité de Rademacher empirique, Rademacher averages]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [learning-theory, rademacher-complexity]
---

# Rademacher complexity

## Aperçu

- Mesure la **capacité** d'une classe de fonctions par sa faculté à **corréler avec du bruit aléatoire** : une classe qui sait s'aligner sur n'importe quel étiquetage aléatoire est trop riche pour généraliser.
- Contrairement à la [[VC dimension]] (binaire, pire cas), elle est **dépendante des données** et s'applique aux fonctions à valeurs réelles → bornes de généralisation plus serrées.

## Concepts clés

### Variables de Rademacher
- Les $\sigma_i \in \{-1,+1\}$ tirées à pile ou face indépendamment ($\mathbb P=\tfrac12$ chacune) sont du **pur bruit**. La complexité mesure à quel point la classe $\mathcal F$ peut s'aligner dessus en moyenne.

### Empirique vs espérée
- **Empirique** $\hat{\mathfrak R}_S(\mathcal F)$ : calculée sur l'échantillon observé $S$ — quantifiable depuis les données.
- **Espérée** $\mathfrak R_n(\mathcal F)=\mathbb E_S[\hat{\mathfrak R}_S]$ : moyenne sur les échantillons. C'est elle qui entre dans les bornes théoriques.

### Pourquoi c'est plus fin que la VC
- La Rademacher s'adapte à la **distribution réelle** des données, pas au pire cas. Pour une classe de VC dimension $d$, on a $\mathfrak R_n(\mathcal F)=O(\sqrt{d/n})$ — elle retrouve la borne VC mais peut être bien plus petite sur des données « faciles ». Elle se contrôle aussi pour les marges (SVM, boosting).

## Les maths, simplement

- $\hat{\mathfrak R}_S(\mathcal F) = \mathbb E_{\sigma}\Big[\sup_{f\in\mathcal F}\dfrac{1}{n}\sum_{i=1}^{n}\sigma_i\,f(x_i)\Big]$ — le $\sup$ cherche la fonction qui colle le mieux au bruit ; l'espérance sur $\sigma$ moyenne sur les tirages.
- **Borne de généralisation** : avec probabilité $1-\delta$, uniformément sur $\mathcal F$,
- $\mathbb E[f] \le \hat{\mathbb E}[f] + 2\,\hat{\mathfrak R}_S(\mathcal F) + 3\sqrt{\dfrac{\ln(2/\delta)}{2n}}$ — le dernier terme vient de [[Inégalités de concentration|McDiarmid]].
- **Lemme de contraction** (Talagrand) : composer par une fonction $L$-lipschitzienne (une perte) ne gonfle la complexité que d'un facteur $L$ — d'où son usage pour borner le risque via la marge.

## En pratique

- Sert à dériver les bornes à **marge** : SVM et [[Gradient Boosting (GBDT)|boosting]] généralisent bien parce qu'une grande marge réduit la Rademacher effective, même à VC dimension élevée.
- Donne un cadre pour analyser des classes où la VC est infinie ou non informative (réseaux de neurones via normes des poids).
- Reste un outil d'**analyse** : rarement calculée en production, mais elle justifie pourquoi la [[Régularisation]] (contrôle de norme) améliore la généralisation.

## Approches voisines & alternatives

- [[VC dimension]] — mesure de capacité binaire et pire-cas ; la Rademacher la raffine et la rend data-dependent.
- [[Generalization bounds]] — la Rademacher fournit l'un des termes de complexité les plus serrés.
- [[Inégalités de concentration]] — McDiarmid/Hoeffding relient la quantité empirique à son espérance.
- [[PAC learning]] — cadre général dont la Rademacher instancie la complexité d'échantillon.
- [[Compromis biais-variance]] — une Rademacher élevée = classe à forte variance.

## Pour aller plus loin

- Bartlett & Mendelson (2002) — *Rademacher and Gaussian Complexities: Risk Bounds and Structural Results*.
- Mohri, Rostamizadeh & Talwalkar — *Foundations of Machine Learning*, ch. 3.
