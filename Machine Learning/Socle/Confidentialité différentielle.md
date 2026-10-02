---
role: notion
nom: Confidentialité différentielle
alias: [Differential privacy, DP, ε-DP, (ε,δ)-DP, budget de confidentialité, privacy budget, mécanisme de Laplace, mécanisme gaussien, sensibilité, composition, DP-SGD, moments accountant, écrêtage des gradients, Opacus, JAX Privacy, TensorFlow Privacy, VaultGemma, unité de confidentialité]
categorie: ml/socle
domaines: [data-sci, ml-eng]
tags: [privacy, ai-security, deep-learning]
---

# Confidentialité différentielle

## Aperçu

- Une garantie **sur une procédure**, pas sur une donnée : le résultat d'un calcul change **très peu, en probabilité**, que l'on ajoute ou retire un individu du jeu de données. On l'obtient en ajoutant du **bruit calibré** ; $\varepsilon$ mesure la perte de confidentialité, $\delta$ une probabilité d'échec.
- Elle protège la **participation** : un observateur de la sortie ne peut pas dire, avec confiance, si une personne précise figurait dans les données. Elle ne protège **pas** contre une conclusion de population (Dwork et Roth, 2014, §1.1 : une étude qui établit un lien entre le tabac et le cancer le révèle sur un fumeur que celui-ci ait participé ou non) et ne promet pas l'absence de tout préjudice (§2.3.2).
- En apprentissage, la méthode de référence est **DP-SGD** (Abadi et al., CCS 2016) : écrêter le gradient de chaque exemple, ajouter un bruit gaussien, comptabiliser le budget consommé.
- Le sujet est partagé entre une théorie propre et une pratique contestée : le choix de $\varepsilon$ n'a pas de règle consensuelle, les garanties dépendent de l'**unité de confidentialité** retenue, et les chiffres d'utilité restent loin de l'entraînement non privé sur les tâches difficiles (sections *Choisir ε* et *Critiques*).
- Cette page ne répète ni l'[[Apprentissage fédéré]] (qui ne donne aucune garantie formelle seul) ni [[AI security]] (la surface d'attaque des systèmes IA) : elle porte la **définition**, les **mécanismes** et les limites.

## Concepts clés

### Définition $(\varepsilon, \delta)$
- Un mécanisme aléatoire $M$ est $(\varepsilon,\delta)$-différentiellement privé si, pour tout ensemble de sorties $S$ et pour toutes bases $x, y$ **voisines** (qui diffèrent d'un enregistrement, $\lVert x - y\rVert_1 \le 1$) : $\Pr[M(x)\in S] \le e^{\varepsilon}\,\Pr[M(y)\in S] + \delta$ (Dwork et Roth, Déf. 2.4). Avec $\delta = 0$, on dit $\varepsilon$-DP.
- **Origine** : Dwork, McSherry, Nissim et Smith (2006) définissent l'$\varepsilon$-indistinguishabilité et la **sensibilité** $S(f)$ ; le bruit est de Laplace d'échelle $S(f)/\varepsilon$ ; le papier n'a pas encore de $\delta$ (lu dans la version de l'auteur ; la venue TCC 2006 n'est pas dans ce texte).
- **Lire $\varepsilon$** : $e^{\varepsilon}$ borne le rapport de probabilité d'une sortie avec et sans un individu. $\varepsilon = 0{,}1$ donne un rapport d'au plus 1,11 ; $\varepsilon = 1$, 2,72 ; $\varepsilon = 8$, environ 2 981 ; $\varepsilon = 20$, environ $4{,}8\times 10^{8}$. Plus $\varepsilon$ est grand, plus la garantie est faible.
- **Voisins** : le mot « voisin » fixe l'**unité de confidentialité** (un utilisateur, un exemple, une séquence). La garantie ne vaut que pour cette unité (voir *Ce que la garantie dit*).

### Sensibilité et mécanismes
- **Sensibilité** $L_1$ d'une requête $f$ : $\Delta f = \max \lVert f(x) - f(y)\rVert_1$ sur les bases voisines (Déf. 3.1).
- **Laplace** : $M_L(x) = f(x) + (Y_1,\dots,Y_k)$ avec $Y_i$ indépendantes de loi $\mathrm{Lap}(\Delta f/\varepsilon)$ ; $(\varepsilon, 0)$-DP (Th. 3.6).
- **Gaussien** : pour $\varepsilon \in (0,1)$ et $c^2 > 2\ln(1{,}25/\delta)$, un bruit d'écart-type $\sigma \ge c\,\Delta_2 f/\varepsilon$ donne $(\varepsilon, \delta)$-DP (Th. A.1, annexe A, présenté comme un résultat « folklorique »). Il utilise la sensibilité $L_2$, toujours inférieure ou égale à la sensibilité $L_1$ : c'est celui de DP-SGD.

### Propriétés qui rendent la garantie composable
- **Post-traitement** (Prop. 2.1) : toute fonction aléatoire appliquée à la sortie d'un mécanisme $(\varepsilon,\delta)$-DP garde la garantie. Publier ou réutiliser le modèle appris, sans retoucher aux données, ne consomme pas de budget de plus.
- **Groupes** (Th. 2.2) : $\varepsilon$-DP devient $(k\varepsilon, 0)$-DP pour des groupes de $k$ individus.
- **Composition de base** (Th. 3.14, 3.16) : $\varepsilon_1 + \varepsilon_2$ ; ou $(\sum \varepsilon_i, \sum \delta_i)$.
- **Composition avancée** (Th. 3.20) : pour $k$ mécanismes $(\varepsilon,\delta)$-DP composés de façon adaptative, $(\varepsilon', k\delta + \delta')$-DP avec $\varepsilon' = \sqrt{2k\ln(1/\delta')}\,\varepsilon + k\varepsilon(e^{\varepsilon}-1)$. Le budget croît comme $\sqrt{k}$ et non comme $k$. Le **budget de confidentialité** est ce qu'on dépense à chaque requête ou chaque pas d'entraînement.

### DP-SGD : entraîner un réseau avec la garantie
- **Procédé** (Abadi et al., 2016, Alg. 1) : à chaque pas, tirer un lot avec probabilité $q = L/N$ ; **écrêter** la norme $L_2$ du gradient de chaque exemple à $C$ ; moyenner ; ajouter un bruit gaussien $\mathcal{N}(0, \sigma^2 C^2 I)$ ; faire le pas.
- **Garantie** (Th. 1) : pour $\varepsilon < c_1 q^2 T$, l'algorithme est $(\varepsilon,\delta)$-DP si $\sigma \ge c_2\,q\sqrt{T\log(1/\delta)}/\varepsilon$, $T$ étant le nombre de pas.
- **Comptabilité des moments** (*moments accountant*) : pour $q = 0{,}01$, $\sigma = 4$, $\delta = 10^{-5}$, 100 époques donnent $\varepsilon = 1{,}26$ (contre 9,34 avec la composition forte) ; 400 époques, 2,55 (contre 24,22) (§5.1). Une comptabilité plus fine vaut des ordres de grandeur d'$\varepsilon$.
- **Résultats annoncés** : sur MNIST (baseline non privée 98,30 %), 90 %, 95 % et 97 % pour $\varepsilon = 0{,}5$, 2 et 8 ($\delta = 10^{-5}$) ; sur CIFAR-10, 67 %, 70 % et 73 % pour $\varepsilon = 2$, 4 et 8, contre environ 80 % sans confidentialité. **Réserve du papier** : les couches convolutives de CIFAR-10 sont pré-entraînées sur CIFAR-100, **traité comme donnée publique** ; seules les couches denses sont entraînées avec DP. L'écart avec le non privé est d'environ 7 points sur CIFAR-10, de 1,3 sur MNIST.

### L'utilité qu'on perd, et ce qu'on a regagné
- **De, Berrada, Hayes, Smith, Balle (DeepMind, arXiv 2204.13650, 2022)** : avec un réglage soigné et une propagation du signal maîtrisée, un Wide-ResNet-40 atteint **81,4 %** sur CIFAR-10 à $(8, 10^{-5})$-DP **sans donnée supplémentaire**, contre 71,7 % pour l'état de l'art d'alors. Sur ImageNet, en affinant un NFNet-F3 pré-entraîné : 83,8 % en top-1 à $(0{,}5, 8\cdot 10^{-7})$ et 86,7 % à $(8, 8\cdot 10^{-7})$, soit 4,3 points sous l'état de l'art non privé.
- **Tramèr et Boneh (ICLR 2021)** : des modèles linéaires sur des caractéristiques de type ScatterNet battent des CNN privés de bout en bout pour un budget modéré. Pour passer au-dessus, il faut environ dix fois plus de données privées, ou des caractéristiques apprises sur **données publiques**.
- **Désaccord laissé tel quel** : les résultats sur CIFAR-10 ne se comparent pas. Abadi (73 % à $\varepsilon = 8$) pré-entraîne ses convolutions sur des données publiques ; De et al. (81,4 %) n'en utilisent pas. Les deux lectures — passer par des caractéristiques publiques, ou monter en échelle — coexistent.
- **Coût inégal** : Bagdasaryan, Poursaeed, Shmatikov (arXiv 1905.12101, 2019) montrent que la perte de précision touche davantage les **classes et sous-groupes sous-représentés** : l'écrêtage et le bruit favorisent la distribution dominante. Voir [[Équité et biais algorithmique]].

## Choisir ε : un chiffre sans règle

- **NIST SP 800-226** (Near et al., mars 2025) : les lignes directrices **ne donnent aucune règle** de choix. Une étude citée (Wood et al.) suggère $\varepsilon = 0{,}1$ comme protection forte et $\varepsilon < 1$ comme raisonnable ; beaucoup de déploiements utilisent $1 < \varepsilon \le 20$, et de grandes valeurs ne donnent pas toujours de confidentialité réelle (« Privacy Hazard »). L'unité de confidentialité pèse autant que $\varepsilon$ ; l'audit empirique trouve des bugs mais ne prouve pas la garantie.
- **Dwork, Kohli, Mulligan (2019, *J. Privacy and Confidentiality* 9(2))** : pas de consensus des praticiens ; ils proposent un **registre des epsilons**. Lu par la page de l'éditeur seulement.
- **Cummings et al. (arXiv 2304.06929, *Harvard Data Science Review* 6.1, 2024)** : il n'existe « aucune orientation juridique ou numérique concrète » pour traduire un contexte en valeur d'$\varepsilon$ ; ils reprennent l'idée de registre.
- **Domingo-Ferrer, Sánchez, Blanco-Justicia (arXiv 2011.02352, 2020, quatre pages)** : citent des déploiements à $\varepsilon$ élevé (Apple, de 6 sur macOS à 14 sur iOS 10 et jusqu'à 43 en bêta ; RAPPOR jusqu'à 9 ; Facebook avec un bruit calibré à $\varepsilon = 200$), d'après un article de presse. Ils rappellent aussi que la définition suppose les enregistrements **indépendants**.
- **Recensement américain de 2020** : budget total $\varepsilon = 19{,}61$, dont 17,14 pour le fichier des personnes et 2,47 pour les logements (communiqué du Census Bureau du 9 juin 2021, lu par résumé seulement). Ruggles, Fitch, Magnuson, Schroeder (2019, *AEA Papers and Proceedings* 109) y voient « une rupture radicale » avec les lois de confidentialité du Bureau, et jugent la DP pure incompatible avec une diffusion utile de microdonnées.
- **Désaccord laissé tel quel** : le NIST juge $\varepsilon < 1$ raisonnable, mais constate des déploiements jusqu'à 20 ; le recensement est à 19,61. Aucune source lue ne tranche le seuil à partir duquel $\varepsilon$ cesse de protéger.

## Critiques : ce que la garantie dit et ne dit pas

- **Population contre individu** : Dwork et Roth (§1.1, §2.3.2) le disent eux-mêmes : une conclusion de population est apprise que l'individu soit présent ou non. La DP protège la participation, pas la valeur d'un attribut inférable par ailleurs.
- **Corrélations** : Kifer et Machanavajjhala (« No Free Lunch in Data Privacy », SIGMOD 2011) montrent qu'on ne peut garantir en même temps utilité et confidentialité sans hypothèse sur la distribution des données et la connaissance de l'adversaire. Lu par des diapositives de cours et par *Pufferfish* (ACM TODS) : la variation des cotes d'un attaquant n'est bornée par $e^{\varepsilon}$ **que si** les enregistrements sont indépendants ; des enregistrements corrélés fuient davantage (Th. 6.2). L'article de 2011 n'a pas pu être ouvert.
- **L'unité compte** : VaultGemma (Google, arXiv 2510.15001, voir plus bas) offre une garantie **au niveau de la séquence** de 1 024 jetons. Deux séquences identiques issues de documents répétés sont deux unités distinctes pour la garantie : pour une personne dont les données apparaissent dans plusieurs séquences, la garantie est plus faible (effet de groupe, Th. 2.2).
- **La garantie théorique n'est pas la fuite mesurée** : Jagielski, Ullman, Oprea (arXiv 2006.07709, 2020) auditent DP-SGD par empoisonnement et trouvent des bornes inférieures d'$\varepsilon$ environ **dix fois** meilleures que les audits précédents, et encore environ dix fois sous la borne analytique pire cas. Jayaraman et Evans (USENIX Security 2019) mesurent un grand écart entre les bornes garanties et la fuite constatée par attaque d'inférence d'appartenance, et jugent « vides de sens » les garanties des réglages qui gardent l'utilité.
- **À l'inverse** : Nasr et al. (arXiv 2302.07956, 2023) obtiennent un audit **serré** avec seulement deux entraînements, sous l'hypothèse que l'adversaire voit toutes les mises à jour ; sur CIFAR-10 (WRN-16, 79 % de précision, $\varepsilon = 8$, $\delta = 10^{-5}$), l'audit rejoint la borne théorique en boîte blanche, et il détecte des bugs d'implémentation (borne revendiquée $\varepsilon = 1{,}27$) que les audits précédents manquaient. **Les deux conclusions diffèrent selon le modèle de menace** ; désaccord laissé tel quel.

## Depuis 2025 : DP et grands modèles de langage

- **VaultGemma** (Google, arXiv 2510.15001, v2 du 22 octobre 2025) : 1 milliard de paramètres, entièrement pré-entraîné avec DP-SGD, sur le même mélange de données que Gemma 2. Garantie $(\varepsilon \le 2{,}0,\ \delta \le 1{,}1\cdot 10^{-10})$ au niveau séquence de 1 024 jetons ; 100 000 itérations, taille de lot attendue 517 989, multiplicateur de bruit 0,6143481, 2 048 puces TPUv6e ; écrêtage et bruit par JAX Privacy.
- **Coût en utilité** (VaultGemma 1B / Gemma 3 1B / GPT-2 1,5 Md, Table 2) : ARC-C 26,45 / 38,31 / 39,78 ; HellaSwag 39,09 / 61,04 / 47,91 ; TriviaQA (5 coups) 11,24 / 39,75 / 6,00. Aucune mémorisation détectée sur environ un million d'échantillons (préfixe de 50 jetons, suffixe de 50).
- **Ramesh, Pillutla, Pruthi, Field (arXiv 2609.00492, 2026, Findings d'EMNLP 2026)** : les modèles de langage pré-entraînés ou affinés avec DP **hallucinent plus**, d'autant plus que le budget est strict. Résumé seulement.
- **Outils** : Opacus 1.6.0 (5 mai 2026, d'après PyPI, lu par résumé) ajoute FSDP, la précision mixte et un mode sans enveloppe du modèle (`wrap_model=False`) ; TensorFlow Privacy, dernière version vue 0.9.0 (14 février 2024) ; JAX Privacy, version non confirmée. Fine-tuning privé de grands modèles : DP-SFT (Zheng et al., arXiv 2601.11113, 2026) et DP-SelFT (Sha et al., arXiv 2605.17432, 2026), résumés seulement.

## Les maths, simplement

- Définition : $\Pr[M(x)\in S] \le e^{\varepsilon}\Pr[M(y)\in S] + \delta$ pour toutes bases voisines $x, y$ et tout $S$.
- Laplace : $M(x) = f(x) + \mathrm{Lap}(\Delta f/\varepsilon)^k$ ; gaussien : $M(x) = f(x) + \mathcal{N}(0, \sigma^2 I)$ avec $\sigma \ge c\,\Delta_2 f/\varepsilon$.
- Composition de base : $(\varepsilon_1,\delta_1)$ puis $(\varepsilon_2,\delta_2)$ donne $(\varepsilon_1+\varepsilon_2,\ \delta_1+\delta_2)$ ; composition avancée sur $k$ pas : $\varepsilon' = \sqrt{2k\ln(1/\delta')}\,\varepsilon + k\varepsilon(e^{\varepsilon}-1)$.
- Pas de DP-SGD :
  $$\tilde g_t = \frac{1}{L}\Big(\sum_{i \in B_t} \mathrm{clip}\big(\nabla \ell(w_t; x_i),\, C\big) + \mathcal{N}(0, \sigma^2 C^2 I)\Big), \qquad w_{t+1} = w_t - \eta\,\tilde g_t,$$
  avec $\mathrm{clip}(g, C) = g \cdot \min(1, C/\lVert g\rVert_2)$ et $B_t$ un lot tiré avec probabilité $q$ par exemple.
- Le bruit relatif diminue avec la **taille du lot** (le bruit est fixe, la somme des gradients grandit) ; VaultGemma travaille avec des lots attendus de plus de 500 000 séquences.

## En pratique

- **Fixer l'unité de confidentialité d'abord** : l'utilisateur (tous ses exemples), l'exemple, la séquence. Une garantie « par exemple » ne protège pas une personne qui en fournit des centaines.
- **Rapporter le triplet complet** : $(\varepsilon, \delta)$, l'unité, et le procédé de comptabilité (taux d'échantillonnage, nombre de pas, multiplicateur de bruit). Un $\varepsilon$ sans unité ni comptabilité ne se compare à rien. L'idée de registre (Dwork et al., Cummings et al.) va dans ce sens.
- **Entraînement privé** : écrêtage $C$, multiplicateur de bruit $\sigma$, **grand lot**, nombre de pas, tout interagit avec le budget ; des **caractéristiques publiques** pré-entraînées (Abadi, Tramèr et Boneh, De et al.) font gagner beaucoup d'utilité, au prix d'une hypothèse : les données publiques ne sont pas sensibles.
- **Auditer empiriquement** (Nasr et al.) pour détecter un bug d'écrêtage ou de bruit ; ce n'est pas une preuve, c'est un test.
- **Mesurer l'utilité par sous-groupe**, pas seulement en moyenne (Bagdasaryan et al.).
- **Ne pas confondre avec l'anonymisation** : [[Presidio]] détecte et masque des données personnelles dans du texte, des images et des tables ; sa FAQ, référencée dans sa fiche, signale l'absence de garantie. Rien d'équivalent à $(\varepsilon, \delta)$-DP. Voir aussi [[Données personnelles et anonymisation pour LLM]] pour le cas des modèles de langage.
- **Combiner avec le fédéré** : DP côté client pour la fuite par les gradients, agrégation sécurisée pour la confidentialité des mises à jour ; coût d'utilité cumulé ([[Apprentissage fédéré]]).
- **Outils** : Opacus se branche sur [[PyTorch]], JAX Privacy sur [[JAX]] ; l'écrêtage par exemple oblige à calculer des gradients par exemple (voir [[Rétropropagation et différentiation automatique]]).

## Approches voisines & alternatives

- [[Apprentissage fédéré]] — garder les données chez leur propriétaire ; seul, il n'apporte pas de garantie formelle, la DP la fournit.
- [[AI security]] — la surface d'attaque des systèmes à modèle ; la confidentialité y est vue côté exfiltration de prompts et de données RAG.
- [[Données personnelles et anonymisation pour LLM]] — anonymiser et pseudonymiser ; sans garantie formelle.
- [[Presidio]] — détection et anonymisation de données personnelles ; autre famille de protection.
- [[Guardrails]] — filtrer les entrées et les sorties : agit sur l'usage du modèle, pas sur son entraînement.
- [[Équité et biais algorithmique]] — la DP creuse l'écart de précision entre sous-groupes (Bagdasaryan et al.).
- [[Rétropropagation et différentiation automatique]] — DP-SGD a besoin de gradients par exemple et d'écrêtage.
- [[PyTorch]] et [[JAX]] — les deux frameworks où vivent Opacus et JAX Privacy.

## Pour aller plus loin

- Dwork & Roth (2014) — [*The Algorithmic Foundations of Differential Privacy*](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf), Foundations and Trends in Theoretical Computer Science, vol. 9.
- Dwork, McSherry, Nissim & Smith (2006) — [*Calibrating Noise to Sensitivity in Private Data Analysis*](https://people.csail.mit.edu/asmith/PS/sensitivity-tcc-final.pdf), TCC 2006.
- Abadi, Chu, Goodfellow, McMahan, Mironov, Talwar & Zhang (2016) — [*Deep Learning with Differential Privacy*](https://arxiv.org/abs/1607.00133), CCS 2016.
- NIST (2025) — [*SP 800-226, Guidelines for Evaluating Differential Privacy Guarantees*](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.pdf) ; Cummings et al. (2024) — [*Advancing Differential Privacy*](https://arxiv.org/abs/2304.06929) ; Domingo-Ferrer et al. (2020) — [*The Limits of Differential Privacy*](https://arxiv.org/abs/2011.02352) ; Ruggles et al. (2019) — *Differential Privacy and Census Data*, AEA Papers and Proceedings 109.
- De et al. (2022) — [*Unlocking High-Accuracy Differentially Private Image Classification through Scale*](https://arxiv.org/abs/2204.13650) ; Tramèr & Boneh (2021) — [*Differentially Private Learning Needs Better Features (or Much More Data)*](https://arxiv.org/abs/2011.11660), ICLR 2021 ; Bagdasaryan et al. (2019) — [*Differential Privacy Has Disparate Impact on Model Accuracy*](https://arxiv.org/abs/1905.12101).
- Audit : Jagielski et al. (2020) — [*Auditing Differentially Private Machine Learning*](https://arxiv.org/abs/2006.07709) ; Nasr et al. (2023) — [*Tight Auditing of Differentially Private Machine Learning*](https://arxiv.org/abs/2302.07956) ; Jayaraman & Evans (2019) — [*Evaluating Differentially Private Machine Learning in Practice*](https://arxiv.org/abs/1902.08874).
- VaultGemma Team (2025) — [*VaultGemma: A Differentially Private Gemma Model*](https://arxiv.org/abs/2510.15001).
- Non ouvert : Kifer & Machanavajjhala (2011), SIGMOD ; texte intégral de Dwork, Kohli & Mulligan (2019).
