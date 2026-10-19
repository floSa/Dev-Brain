---
role: brique
nom: MiMo-V2.6
alias: [MiMo-V2.6-Pro, MiMo-V2.6-Flash, MiMo-V2.6-Pro-RL, MiMo-V2.6-Flash-RL, Xiaomi MiMo, MiMo V2.6]
pitch: "Modèles omnimodaux à poids ouverts de Xiaomi (MIT selon les cartes) — Pro de 1,02 T dont 42 B actifs, Flash de 309 B dont 15 B actifs, entrée texte, image, audio et vidéo, sortie texte seule, 1 M de tokens ; 573 Go et 178 Go de poids, donc des nœuds multi-GPU."
categorie: llm/modele
famille: modele
licence_type: open-source
maturite: production
alternatives: ["[[DeepSeek-V4.1-Flash]]", "[[Qwen]]"]
tags: [llm, local-llm, reasoning, tool-use, vision-language]
url_docs: https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL
url_repo: 
---

# MiMo-V2.6

<!-- AUTO:BANDEAU:START -->
> Modèles omnimodaux à poids ouverts de Xiaomi (MIT selon les cartes) — Pro de 1,02 T dont 42 B actifs, Flash de 309 B dont 15 B actifs, entrée texte, image, audio et vidéo, sortie texte seule, 1 M de tokens ; 573 Go et 178 Go de poids, donc des nœuds multi-GPU.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Deux modèles à poids ouverts de l'équipe MiMo de Xiaomi, dépôts Hugging Face `XiaomiMiMo/MiMo-V2.6-Pro-RL` et `XiaomiMiMo/MiMo-V2.6-Flash-RL` créés le 2026-09-21, modifiés le 2026-10-09 (lecture du 2026-10-20). **Pro** : Mixture of Experts de 1,02 T paramètres dont 42 Md actifs, 70 couches (60 à attention locale sur 128 tokens, 10 globales), 384 experts routés dont 8 par token. **Flash** : 309 Md dont 15 Md actifs, 48 couches (39 locales, 9 globales), 256 experts dont 8 par token. Contexte de **1 M de tokens**. Entrée texte, image, audio et vidéo par le même modèle ; **sortie texte seule** : les démos de musique ou de vidéo sont un agent qui pilote des outils. Un rapport technique est publié en PDF dans le dépôt du Pro. Un troisième mode, Pro-UltraSpeed, est un mode de service payant, pas un modèle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un modèle **omnimodal** (audio, vidéo, image en entrée) à poids ouverts et licence MIT déclarée | Un **poste ou un seul GPU** : 573 Go (Pro) et 178 Go (Flash) de poids, même avec 42 et 15 Md actifs → [[gpt-oss]] |
| Un **rapport qualité-prix** sur un indice généraliste (46, 0,13 $ par tâche sous v4.3.2 au 2026-09-22) | Un **agent autonome en terminal** : Terminal Bench 4.0 à 34,9 contre 59,6 au meilleur, chiffres d'éditeur |
| Le **Flash** sur 4 GPU (`--tensor-parallel-size 4` dans la carte) comme palier de coût | Un **contexte long servi à beaucoup de sessions** : 25 600 octets de cache par token, 29 fois [[DeepSeek-V4.1-Flash]] |
| Les cartes donnent des **commandes de serving** vLLM et SGLang | Un **fichier `LICENSE`** : aucun dans les dépôts, la licence tient au champ de la carte |

## Mise en œuvre

- Installation — poids sur Hugging Face ; moteurs vLLM et SGLang, d'après les cartes
- Point d'entrée — Pro : `vllm serve XiaomiMiMo/MiMo-V2.6-Pro-RL --tensor-parallel-size 8` ou, pour la recette SGLang de l'éditeur, `--tp 16 --nnodes 2` ; Flash : `vllm serve XiaomiMiMo/MiMo-V2.6-Flash-RL --tensor-parallel-size 4`, ou SGLang `--tp 8 --dp 2`. Échantillonnage recommandé du Flash : `temperature=1.0`, `top_p=0.95`
- Prérequis — Pro : 573 Go de poids, soit au moins un nœud de huit GPU de 141 Go ; Flash : 178 Go, au moins deux cartes (poids relevés par un tiers sur les dépôts le 2026-09-22 ; calcul de nœud estimé)
- Exécution — hors d'un centre de données, seul le Flash est à portée ; l'API de Xiaomi est un service payant, citée ici en texte simple et sans page
- Coût — gratuit, MIT selon le champ `license: mit` des deux cartes

## Limites à connaître

- **Pas de fichier `LICENSE`** dans les dépôts du Pro et du Flash au 2026-10-20 (listage des fichiers) : la licence MIT est celle du champ `license` des deux cartes, que reprend Artificial Analysis en « Open Weights » sans restriction d'usage commercial. Précédent du brain : Gemma 4 et Mistral Small 4 sont dans le même cas. À relire avant toute livraison.
- **Les 42 Md actifs ne réduisent pas la mémoire**, seulement le calcul : tous les experts restent chargés. Le total annoncé et le décompte du dépôt ne se réconcilient pas publiquement (le compteur de Hugging Face donne environ la moitié).
- **Terminal Bench 4.0 à 34,9 contre 59,6 au meilleur** : un indice composite à dix épreuves absorbe l'écart, car ce banc n'en pèse qu'un dixième. Les bancs d'agents sont exécutés par l'éditeur ; aucun tiers n'a rejoué une colonne au 2026-09-22.
- **Le 2,62 M$ de Xiaomi couvre la seule phase d'apprentissage par renforcement** (30 étapes, moins de six jours) du Pro ; le pré-entraînement n'est chiffré nulle part. Le code de RL annoncé n'était pas publié le 2026-09-22.
- **Aucune mesure à un million de tokens** et aucune mesure indépendante du Flash.

## Écosystème

### Alternatives

- [[DeepSeek-V4.1-Flash]] — Modèle de langage à poids ouverts de DeepSeek-AI (MIT, MoE de 552 B dont 8 B actifs au prefill et 16 B au décodage) — contexte de 1 M de tokens, cache KV de 890 octets par token, effort de raisonnement réglable de 1 à 100 ; checkpoint de 510 Go, donc un nœud multi-GPU. — le même million de tokens avec 29 fois moins de cache par token, mais texte et image seuls, sans audio ni vidéo en entrée.
- [[Qwen]] — Famille de modèles de langage d'Alibaba (Qwen3.8 : 27 B dense en Apache-2.0 ; Flash-Next et 2,4 T sous licences propres à clause « Model as a Service ») — 262 144 tokens, mode pensée réglable, appel d'outils, image et vidéo. — un 27 B dense en Apache-2.0 qui tient sur un GPU, avec image et vidéo en entrée mais sans audio cité par la fiche.

## Ressources

- Documentation — carte du Pro : https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL
- Carte du Flash : https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL
- Rapport technique : https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf

## Voir aussi

- [[Licences de modèles open weights]] — la notion : lire le dépôt, ici un champ de carte sans fichier
- [[Comparatif - Modèles de langage open weights]] — ce qui départage les familles du dossier
- [[Mixture of Experts]] — pourquoi les paramètres actifs décident du calcul, jamais de la mémoire
- [[Contexte long]] — le coût du cache KV : 25,6 Go pour une session d'un million de tokens
- [[Lire un score publié]] — 46,32 sous v4.3, 46 sous v4.3.2, et une diapositive « là où il gagne » qui contient deux défaites
- [[Tarif catalogue contre coût par tâche]] — même tarif entre V2.5 et V2.6, coût par tâche multiplié par 2,6
- [[Vision Language Models]] — l'encodeur visuel de 681 M de paramètres du Pro et du Flash
