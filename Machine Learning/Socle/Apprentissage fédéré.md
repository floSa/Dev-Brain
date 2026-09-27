---
role: notion
nom: Apprentissage fédéré
alias: [Federated learning, FL, apprentissage fédéré, entraînement fédéré, FedAvg, Federated Averaging, FedProx, FedSGD, cross-device, cross-silo, inter-appareils, inter-silos, non-IID, hétérogénéité des clients, fuite de gradients, gradient inversion, deep leakage from gradients, agrégation sécurisée, secure aggregation, apprentissage collaboratif sans partage de données]
categorie: ml/socle
domaines: [ml-eng, mlops]
tags: [privacy, distributed, ai-security]
---

# Apprentissage fédéré

## Aperçu

- Entraîner **un seul modèle** à partir de données qui **ne quittent pas** leur propriétaire. Plusieurs clients collaborent sous la coordination d'un serveur ; les données brutes restent locales et seules des **mises à jour ciblées**, destinées à une agrégation immédiate, sont échangées (Kairouz et al., 2021, §1, principe de minimisation).
- Deux régimes qui se ressemblent peu : **inter-appareils** (*cross-device* : des millions de téléphones) et **inter-silos** (*cross-silo* : quelques organisations, chacune avec un serveur et un jeu de données conséquent). Les clients industriels qui ne partagent pas leurs données relèvent du second.
- Ce que l'apprentissage fédéré **ne garantit pas** : la vie privée. Kairouz et al. écrivent que l'apprentissage fédéré de base n'offre « aucune garantie formelle », qu'il faut y ajouter agrégation sécurisée, [[Confidentialité différentielle|confidentialité différentielle]] et vérifiabilité. Zhu et al. (2019) ont montré qu'on peut **reconstruire** les données d'entraînement à partir des gradients partagés.
- Sa valeur est **discutée** : FLamby (2022) trouve, sur cinq de ses sept jeux de santé, qu'aucune stratégie fédérée n'atteint le modèle entraîné sur les données rassemblées (section *Quand la valeur est contestée*).

## Concepts clés

### FedAvg : calcul local, moyenne globale
- **Algorithme** (McMahan et al., AISTATS 2017) : à chaque tour, le serveur tire une fraction $C$ des clients ; chacun fait $E$ passes de descente de gradient sur ses données avec des lots de taille $B$ ; le serveur fait la **moyenne pondérée** des modèles reçus (poids $n_k / n$). **FedSGD** est le cas $E = 1$, $B = \infty$.
- **Hypothèse de coût** : la communication est le goulot, le calcul local presque gratuit. D'où l'idée d'ajouter du calcul local pour économiser des tours.
- **Annoncé** : une réduction du nombre de tours de **10 à 100 fois** par rapport à une SGD synchrone (abstract).
- **Chiffres du corps du texte** : MNIST réparti de façon IID, 35 fois (CNN) et 46 fois (2NN) ; MNIST réparti de façon pathologique, 2,8 à 3,7 fois ; Shakespeare, répartition par rôle (non IID et déséquilibrée), 95 fois contre 13 fois en version IID équilibrée ; LSTM sur 10 millions de messages et plus de 500 000 clients, 35 tours contre 820 pour FedSGD. Sur CIFAR-10, la SGD atteint 86 % après 197 500 mises à jour, FedAvg 85 % après 2 000 tours. $C = 0{,}1$ est retenu comme bon compromis.
- **Limites écrites dans le papier** : un $E$ trop grand fait stagner ou diverger FedAvg (Shakespeare). Les clients qui répondent mal ou envoient des mises à jour corrompues sont hors périmètre, comme la confidentialité différentielle et le calcul multipartite, renvoyés à des travaux futurs.
- **Nuance sur le non-IID** : la partition « pathologique » de MNIST (deux chiffres par client) laisse FedAvg gagner 2,8 à 3,7 fois ; la répartition de Shakespeare, plus réaliste, lui donne 95 fois parce que quelques rôles portent beaucoup de données locales. Les chiffres ne se comparent pas d'un jeu à l'autre.

### Inter-appareils contre inter-silos
Table 1 de Kairouz et al. (2021) :

| Critère | Inter-silos | Inter-appareils |
|---|---|---|
| Clients | organisations ou centres de données répartis | téléphones, objets connectés |
| Échelle | 2 à 100 | jusqu'à $10^{10}$ |
| Disponibilité | presque permanente | une fraction, variations diurnes |
| État du client | conserve un état | sans état |
| Fiabilité | peu de pannes | au moins 5 % d'abandons attendus |
| Adressabilité | clients identifiés | non indexables |
| Goulot | calcul ou communication | communication |
| Partition des données | horizontale ou verticale | horizontale |

- **Propre à l'inter-silos** (§2.2, §7.5) : les **incitations** (un concurrent peut profiter du modèle sans contribuer) et la partition par **variables** (chaque silo détient d'autres colonnes des mêmes individus), avec calcul multipartite ou chiffrement homomorphe ; FATE est cité. Les silos sont plus fiables et authentifiables, mais les coûts de coordination et d'harmonisation des données sont élevés.
- **Définitions du nombre de clients** : FLamby (2022) retient 2 à 50 clients fiables pour l'inter-silos ; Kairouz et al. 2 à 100. Les bornes ne sont pas fixées.

### Hétérogénéité : le non-IID
- Kairouz et al. (§3.1) distinguent cinq formes : décalage de **variables** (*feature skew*), d'**étiquettes** (*label skew*), dérive de concept, changement de concept et décalage de quantité. La plupart des travaux empiriques ne couvrent que le décalage d'étiquettes.
- **§3.3.4** : sur des données pathologiquement non IID, un modèle **local** peut faire mieux que le modèle fédéré.
- **FedProx** (Li et al., MLSys 2020) : chaque client minimise sa perte **plus** un terme proximal $\frac{\mu}{2}\lVert w - w^t\rVert^2$ qui le retient près du modèle global ; FedAvg est le cas $\mu = 0$. Les clients lents peuvent livrer un **travail partiel** (notion de $\gamma$-inexactitude) au lieu d'être écartés. Garanties de convergence en fonction de la **B-dissimilarité** locale. Annoncé : 22 % de précision absolue en plus en moyenne en environnement très hétérogène (jusqu'à 90 % de clients lents dans la simulation).
- **Aucun algorithme ne gagne partout** : Li, Diao, Chen, He (2021, arXiv 2102.02079) comparent FedAvg, FedProx, SCAFFOLD et FedNova sur des silos non IID ; aucun ne domine, et le non-IID dégrade nettement la précision.

### Ce que les gradients révèlent
- **Deep Leakage from Gradients** (Zhu, Liu, Han, NeurIPS 2019) : on part de données et d'étiquettes factices, et on les ajuste jusqu'à ce que leur gradient égale celui reçu. La reconstruction est exacte au pixel pour les images et au mot pour le texte. Conditions : modèle deux fois dérivable (ReLU remplacée par sigmoïde, convolutions sans *stride*), et la reconstruction n'est montrée que jusqu'à des lots de 8 images de 64×64 pixels.
- **Défenses testées** (même papier) : un bruit de variance $10^{-4}$ ou $10^{-3}$ n'empêche pas la fuite ; au-delà de $10^{-2}$ l'attaque échoue mais la précision chute ; l'élagage de gradients tolère environ 20 % ; fp16 et bfloat16 ne protègent pas ; int8 protège mais dégrade fortement le modèle. L'agrégation sécurisée est jugée la plus sûre mais « pas assez générale ».
- **Prolongements** : **iDLG** (Zhao, Mopuri, Bilen, 2020) déduit l'étiquette analytiquement du signe du gradient de la dernière couche (entropie croisée) ; **Geiping et al.** (NeurIPS 2020) reconstruisent des images ImageNet d'un ResNet entraîné, jusqu'à 100 images moyennées, avec un serveur honnête mais curieux.
- **Le réalisme est contesté** : Huang et al. (NeurIPS 2021) relèvent que l'attaque de Geiping suppose de connaître les statistiques de normalisation par lots et les étiquettes ; relâchées, elle s'affaiblit nettement, et bruit, élagage et InstaHide combinés la rendent presque inefficace sur des lots de 32. Hatamizadeh et al. (2022) concluent de même que les attaques deviennent peu pratiques si le client met à jour ses statistiques de normalisation. **À l'inverse**, Wen et al. (2022) et Fowl et al. (ICLR 2022) montrent qu'un **serveur malveillant**, qui modifie les paramètres ou l'architecture envoyés, contourne ces limites jusqu'à copier les données. Désaccord laissé tel quel : tout dépend du modèle de menace.
- **Défenses cadrées par les hypothèses** : Huang et al. excluent explicitement agrégation sécurisée et chiffrement homomorphe de leur évaluation.

### Empoisonnement et agrégation sécurisée
- **Porte dérobée** (Bagdasaryan et al., AISTATS 2020) : un client malveillant envoie un modèle qui **remplace** le modèle global, en échappant à la détection d'anomalies. Une attaque en un seul tour fait atteindre 100 % de précision sur la tâche de porte dérobée (abstract) ; un attaquant qui contrôle moins de 1 % des participants peut empêcher le modèle de l'oublier. Kairouz et al. (§5) citent Bhagoji et al. : 10 % de clients compromis suffisent malgré un détecteur d'anomalies.
- **Agrégation sécurisée** (Bonawitz et al., CCS 2017) : le serveur ne voit que la **somme** des mises à jour, pas chaque mise à jour. Protocole en quatre tours, tolérant les abandons par partage de secret à seuil ; sécurité contre un serveur honnête mais curieux et contre des adversaires actifs. Coût : $O(n^2 + mn)$ en calcul client, $O(n + m)$ en communication par client, pour $n$ clients et des vecteurs de dimension $m$. Daly et al. (2025) indiquent qu'elle est utilisée en pratique pour Gboard.
- **Tension** (Bagdasaryan et al.) : l'agrégation sécurisée **masque** les mises à jour individuelles, donc rend les anomalies indétectables et facilite l'attaque. La protection de la vie privée gêne la défense contre l'empoisonnement.

## Quand la valeur est contestée

- **FLamby** (Ogier du Terrail et al., 2022, NeurIPS Datasets and Benchmarks) : sept jeux de santé aux partitions naturelles. Sauf Fed-TCGA-BRCA et Fed-Heart-Disease, **aucune stratégie fédérée n'atteint** le modèle entraîné sur les données rassemblées. Sur Fed-Camelyon16, Fed-LIDC-IDRI et Fed-IXI, aucun bénéfice de la collaboration n'est observé ; sur Fed-KITS2019 et Fed-ISIC2019, le fédéré dépasse l'entraînement local. FedAvg n'est pas le meilleur, sauf sur deux jeux où il reste compétitif ; les variantes d'optimiseurs fédérés sont les meilleures quand le fédéré dépasse le modèle rassemblé.
- **À l'opposé**, Pati et al. (2022, arXiv 2204.10836) : 71 sites, 6 314 patients (25 256 IRM), détection de limites de tumeur rare ; +33 % sur la zone opérable et +23 % sur la tumeur entière par rapport à un modèle public ; serveur d'agrégation derrière un pare-feu, avec OpenFL.
- **Ce qui concilie les deux, en partie** : les études fédérées positives comparent à un modèle **local** ou **public** ; FLamby compare au modèle entraîné sur **toutes** les données rassemblées, qui est la borne haute. Aucune source lue ne les réconcilie davantage.
- **Daly et al. (Google, arXiv 2410.08892, v2 de mars 2025)** : le fédéré actuel n'entraîne de façon fiable, en inter-appareils, que des modèles de quelques millions de paramètres ; la vérifiabilité côté serveur est un point faible, les environnements d'exécution de confiance sont proposés comme piste.

## Pertinence pour des clients industriels on-prem

- **Inter-silos** : quelques organisations, chacune avec son serveur et son jeu de données ; c'est le cas de plusieurs industriels qui refusent de partager leurs données avec un intégrateur ou entre eux. Le serveur d'agrégation peut être hébergé par l'un d'eux ou par un tiers ; c'est lui qu'il faut croire honnête, ou protéger (agrégation sécurisée).
- **Cadres existants** : Flower (Beutel et al., arXiv 2007.14390), NVIDIA FLARE (Roth et al., arXiv 2210.13291, SDK Python, mode simulation et production), OpenFL (Reina et al., arXiv 2105.06413, d'Intel, pour TensorFlow et PyTorch), FATE (Liu et al., JMLR 22, 2021). Lus par leur résumé ou leur introduction ; aucun benchmark de performance n'a été vérifié, et aucun n'a de brique dans le vault.
- **Retours de terrain** : Kotevska et al. (arXiv 2609.39803, 30 septembre 2026) décrivent des déploiements multi-sites en production : NVFLARE entre laboratoires du ministère américain de l'énergie, et l'ajustement d'un LLaMA-2 de 7 milliards de paramètres sur quatre supercalculateurs (plus de 1 700 GPU). Leur constat : la question passe de « peut-on entraîner » à « peut-on **opérer, auditer, modifier** ». Non validé à l'échelle : l'audit de fuite résiduelle et la traçabilité d'une fuite jusqu'à un participant ; la confidentialité différentielle dégrade l'utilité. Rittig et Kortmann (arXiv 2506.18525, 2025) simulent plusieurs entreprises chimiques : le modèle fédéré est plus précis que les modèles locaux et proche du modèle rassemblé, **en simulation** et non en déploiement.
- **Lacune** : aucune source ouverte n'a chiffré le **coût réel d'infrastructure** d'un fédéré on-prem entre industriels (réseau, exploitation, gouvernance). Il ne s'écrit pas ici.

## Depuis 2025 : fédéré et grands modèles

- **LoRA fédéré** : Liu et al. (ICLR 2026, arXiv 2602.19926, *LA-LoRA*) : avec $\varepsilon = 1$ sur Swin-B et TinyImageNet, +16,83 % de précision face à RoLoRA (lu en partie). Wu et al. (TMLR, février 2026, arXiv 2503.12016) : revue du fine-tuning fédéré de grands modèles de langage, lue par son résumé seulement.
- **Attaques récentes (résumés seulement)** : ARES (Gong et al., arXiv 2603.17623) reconstruit activement sur de gros lots sans modifier l'architecture ; Diana et al. (arXiv 2604.15063) proposent une reconstruction **vérifiable** de données tabulaires, avec un certificat de justesse.

## Les maths, simplement

- Objectif : minimiser la perte moyenne pondérée des $K$ clients, chacun avec $n_k$ exemples :
  $$\min_w F(w) = \sum_{k=1}^{K} \frac{n_k}{n}\, F_k(w), \qquad F_k(w) = \frac{1}{n_k}\sum_{i \in \mathcal{P}_k} \ell(w; x_i, y_i)$$
- **FedAvg**, tour $t$ : chaque client sélectionné part de $w_t$ et rend $w_{t+1}^k$ après $E$ passes ; $w_{t+1} = \sum_{k \in S_t} \frac{n_k}{n_{S_t}}\, w_{t+1}^k$.
- **FedProx**, problème local : $\min_w F_k(w) + \frac{\mu}{2}\lVert w - w^t\rVert^2$.
- **Fuite de gradient** : $(x^*, y^*) = \arg\min_{x', y'} \big\lVert \nabla_W \ell\big(F(x', W), y'\big) - \nabla_W \big\rVert^2$, où $\nabla_W$ est le gradient reçu.
- **Agrégation sécurisée**, idée : chaque paire de clients partage un masque $m_{kj}$ que l'un ajoute et l'autre retranche ; la somme des masques s'annule, le serveur ne voit que $\sum_k x_k$.

## En pratique

- **Vérifier d'abord que le fédéré est nécessaire** : si les données peuvent être rassemblées, l'entraînement centralisé est la borne haute (FLamby). Si elles ne le peuvent pas, comparer au modèle **local** de chaque silo.
- **Mesurer le non-IID avant de choisir l'algorithme** : FedAvg suffit parfois, FedProx ou une variante d'optimiseur fédéré aident sur des silos hétérogènes, et aucun ne gagne partout.
- **Ne pas confondre fédéré et confidentialité** : les gradients fuient. Il faut au minimum l'**agrégation sécurisée** ; pour une garantie formelle, la [[Confidentialité différentielle|confidentialité différentielle]], avec sa perte d'utilité.
- **Modèle de menace explicite** : serveur honnête mais curieux, ou serveur malveillant ; clients tous honnêtes, ou un fraudeur. La même défense couvre l'un et pas l'autre.
- **Prévoir l'exploitation** : versionner le modèle agrégé à chaque tour ([[Model registry & versioning]]), tracer qui a contribué, surveiller la dérive par silo ([[Monitoring de modèle en production]], [[Data drift]]).
- **Valider chez chacun** : un modèle fédéré moyen peut être mauvais pour un silo particulier. L'évaluer sur les données de chaque client.

## Approches voisines & alternatives

- [[Confidentialité différentielle]] — la garantie formelle qui complète le fédéré ; coût en utilité.
- [[AI security]] — le cadre de sécurité des systèmes IA ; l'empoisonnement et la fuite de gradients y relèvent.
- [[Entraînement distribué]] — le parallélisme d'un centre de données (données, modèle, pipeline) ; mêmes mots, hypothèses opposées : données rassemblées, réseau rapide et fiable, clients de confiance.
- [[Model registry & versioning]] — où ranger le modèle agrégé et ses versions par tour.
- [[Monitoring de modèle en production]] et [[Data drift]] — surveiller le modèle déployé chez chaque client.
- [[Synthetic data generation]] — autre voie pour ne pas partager de données brutes.
- [[Apprentissage supervisé]] — le régime d'entraînement local de chaque client.
- [[Données personnelles et anonymisation pour LLM]] — pseudonymiser ou anonymiser avant tout échange ; ne remplace pas une garantie formelle.
- [[PyTorch]] — OpenFL accepte PyTorch (d'après son résumé), qui sert alors de moteur d'entraînement local ; aucun cadre fédéré n'a de brique dans le vault.

## Pour aller plus loin

- McMahan, Moore, Ramage, Hampson & Agüera y Arcas (2017) — [*Communication-Efficient Learning of Deep Networks from Decentralized Data*](https://arxiv.org/abs/1602.05629), AISTATS 2017.
- Kairouz et al. (2021) — [*Advances and Open Problems in Federated Learning*](https://arxiv.org/abs/1912.04977), Foundations and Trends in Machine Learning, vol. 14 (n° 1-2).
- Li, Sahu, Zaheer, Sanjabi, Talwalkar & Smith (2020) — [*Federated Optimization in Heterogeneous Networks*](https://arxiv.org/abs/1812.06127), MLSys 2020.
- Zhu, Liu & Han (2019) — [*Deep Leakage from Gradients*](https://arxiv.org/abs/1906.08935), NeurIPS 2019 ; Zhao, Mopuri & Bilen (2020) — [*iDLG*](https://arxiv.org/abs/2001.02610) ; Geiping et al. (2020) — [*Inverting Gradients*](https://arxiv.org/abs/2003.14053), NeurIPS 2020 ; Huang et al. (2021) — [*Evaluating Gradient Inversion Attacks and Defenses in Federated Learning*](https://arxiv.org/abs/2112.00059), NeurIPS 2021 ; Hatamizadeh et al. (2022) — [*Do Gradient Inversion Attacks Make Federated Learning Unsafe?*](https://arxiv.org/abs/2202.06924).
- Bagdasaryan et al. (2020) — [*How To Backdoor Federated Learning*](https://arxiv.org/abs/1807.00459), AISTATS 2020 ; Bonawitz et al. (2017) — [*Practical Secure Aggregation for Privacy-Preserving Machine Learning*](https://eprint.iacr.org/2017/281), CCS 2017.
- Ogier du Terrail et al. (2022) — [*FLamby*](https://arxiv.org/abs/2210.04620) ; Pati et al. (2022) — [*Federated Learning Enables Big Data for Rare Cancer Boundary Detection*](https://arxiv.org/abs/2204.10836) ; Li, Diao, Chen & He (2021) — [*Federated Learning on Non-IID Data Silos: An Experimental Study*](https://arxiv.org/abs/2102.02079).
- Daly et al. (2025) — [*Federated Learning in Practice*](https://arxiv.org/abs/2410.08892) ; Kotevska et al. (2026) — [*From Pilots to Production*](https://arxiv.org/abs/2609.39803).
- Cadres : [Flower](https://arxiv.org/abs/2007.14390), [NVIDIA FLARE](https://arxiv.org/abs/2210.13291), [OpenFL](https://arxiv.org/abs/2105.06413).
