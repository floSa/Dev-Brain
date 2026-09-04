---
role: brique
nom: Weights & Biases
alias: [wandb, W&B]
pitch: "Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning."
categorie: ml/tracking
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[MLflow]]", "[[Neptune]]", "[[Comet]]", "[[ClearML]]", "[[Aim]]", "[[TensorBoard]]"]
complements: []
tags: [experiment-tracking, model-registry]
url_docs: https://docs.wandb.ai/
url_repo: https://github.com/wandb/wandb
---

# Weights & Biases

<!-- AUTO:BANDEAU:START -->
> Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | propriétaire | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de suivi d'expériences devenue un standard de fait en recherche deep learning.
Deux appels — `wandb.init`, `wandb.log` — suffisent à diffuser métriques, courbes, gradients,
images et tables vers des tableaux de bord interactifs et partageables. Autour du suivi :
**Sweeps**, une recherche d'hyperparamètres distribuée intégrée au tracking ; **Artifacts**,
le versionnage de jeux de données et de modèles ; un registre de modèles ; et **Reports**,
des rapports collaboratifs. Le SDK `wandb` est ouvert ; la plateforme qui le reçoit ne l'est pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualisations riches, partage et collaboration soignés | Données envoyées au cloud par défaut : vérifier la conformité avant d'y mettre du sensible |
| R&D deep learning : suivi fin des gradients, des médias, des métriques système GPU | Le mode *online* bloque ou retarde si le réseau tombe : prévoir `offline`, puis synchroniser |
| Campagnes d'hyperparamètres via les Sweeps, intégrés au tracking | Facturation qui croît avec le volume journalisé — médias et métriques système en tête |
| Équipe qui accepte un service hébergé, ou dispose d'une licence self-host entreprise | Le self-host n'est pas gratuit : W&B Server est sous licence commerciale |

## Mise en œuvre

- Installation — `uv add wandb`, puis `wandb login`
- Point d'entrée — API Python `wandb.init` / `wandb.log`, UI web, et agents pour les Sweeps
- Prérequis — un compte côté éditeur ; pour le self-host, une licence commerciale W&B Server
- Exécution — service managé, ou W&B Server auto-hébergé en architecture horizontalement scalable
- Coût — gratuit en usage personnel et recherche, payant par siège en équipe ; SDK ouvert, plateforme et serveur propriétaires

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Neptune]] — Tracker d'expériences SaaS spécialisé entraînements longue durée et foundation models — racheté par OpenAI, service hébergé arrêté en mars 2026.
- [[Comet]] — Plateforme SaaS de suivi d'expériences ML couplée à l'observabilité LLM (Opik, open-source) — du tracking classique au monitoring d'applications génératives.
- [[ClearML]] — Plateforme MLOps open-source tout-en-un — tracking automatique sans code, plus gestion de données, pipelines, orchestration d'agents et serving.
- [[Aim]] — Tracker d'expériences open-source léger et auto-hébergé — UI de comparaison rapide sur des centaines de milliers de runs, sans dépendance à un SaaS.
- [[TensorBoard]] — Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.

## Ressources

- Documentation — https://docs.wandb.ai/
- Dépôt — https://github.com/wandb/wandb

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[PyTorch]] · [[TensorFlow]] · [[HuggingFace]] · [[Optuna]] — les frameworks qu'il instrumente
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
