---
galaxie: wiki
type: concept
nom: Shannon entropy
alias: [Entropie de Shannon, entropie, information entropy, entropy, entropie de l'information]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [information-theory, entropy]
---

# Shannon entropy

## Aperçu

- Mesure l'**incertitude moyenne** d'une distribution de probabilité : combien d'information, en moyenne, apporte la réalisation d'une variable aléatoire. Maximale quand tout est équiprobable, nulle quand l'issue est certaine.
- Brique fondatrice de la théorie de l'information : l'[[Cross-entropy|entropie croisée]], la [[KL divergence|divergence KL]] et l'[[Mutual information|information mutuelle]] s'expriment toutes à partir d'elle.

## Concepts clés

### Surprise et espérance
- L'**information** d'un événement de probabilité $p$ est $-\log p$ : un événement rare surprend beaucoup, un événement certain n'apporte rien. L'entropie est l'**espérance de cette surprise**.
- Unité selon la base du log : **bits** (base 2), **nats** (base $e$), **dits** (base 10).

### Bornes
- $H \ge 0$, nulle ssi la distribution est déterministe (une issue certaine).
- Maximale pour la **loi uniforme** sur $K$ issues : $H = \log K$. Toute concentration de la masse fait baisser l'entropie.

### Entropie conjointe et conditionnelle
- $H(X,Y)$ : incertitude du couple. $H(Y\mid X)$ : incertitude restante sur $Y$ une fois $X$ connu.
- Chaîne : $H(X,Y) = H(X) + H(Y\mid X)$. La réduction $H(Y) - H(Y\mid X)$ est l'[[Mutual information|information mutuelle]].

## Les maths, simplement

- Cas discret : $H(X) = -\sum_{i} p_i \log p_i$ — somme pondérée des surprises $-\log p_i$.
- Cas continu (entropie différentielle) : $h(X) = -\int p(x)\log p(x)\,dx$ ; à la loi normale d'écart-type $\sigma$, $h = \tfrac12\log(2\pi e\,\sigma^2)$.
- Lien aux autres mesures : $H(p,q) = H(p) + D_{KL}(p\,\|\,q)$ — l'[[Cross-entropy|entropie croisée]] est l'entropie plus le « surcoût » d'utiliser $q$ au lieu de $p$.

## En pratique

- **Arbres de décision** : le gain d'information (réduction d'entropie) sert de critère de découpe — c'est l'alternative à l'indice de Gini dans [[Arbres de décision]] et [[Random Forest]].
- **Quantité d'information** d'une variable catégorielle, mesure de diversité (indice de Shannon en écologie), critère de sélection de features (cf. [[Sélection de variables]]).
- Une entropie élevée signale une distribution plate (peu prédictible) ; surveiller sa chute pour détecter une concentration ou un effondrement de diversité.
- Outils : `scipy.stats.entropy` ([[Dev/Services/scipy.stats|scipy.stats]]) calcule $H$ (et la KL si on passe une seconde distribution).

## Approches voisines & alternatives

- [[Cross-entropy]] — incertitude quand on encode la vraie loi $p$ avec une loi estimée $q$ ; entropie + divergence.
- [[KL divergence]] — l'écart $H(p,q) - H(p)$, le surcoût net de se tromper de distribution.
- [[Mutual information]] — entropie partagée : ce que connaître une variable retire d'incertitude sur l'autre.
- [[Perplexity]] — l'exponentielle de l'entropie, lue comme un facteur de branchement effectif.

## Pour aller plus loin

- Shannon (1948) — *A Mathematical Theory of Communication*, l'article fondateur.
- Cover & Thomas — *Elements of Information Theory* (référence du domaine).
