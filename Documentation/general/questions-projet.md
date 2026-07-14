---
galaxie: meta
nom: questions-projet
type: gouvernance
created: 2026-06-04
modified: 2026-06-04
tags: [meta, gouvernance, planification]
---

# Questions de cadrage projet

Checklist du skill planifier-projet. L'archétype (cf. [[archetypes]]) conditionne les questions à poser : ne poser que les pertinentes.

## Axe transverse critique : on-premise

Profil : data scientist / analyst / AI eng / MLOps, spécialité **on-prem** (industriels, ESN). À trancher tôt :

- Cloud autorisé, ou **on-prem strict / air-gapped** ?
- GPU disponible, ou CPU only ?
- Les données ont-elles le droit de sortir du réseau client ?

## Checklist

### Cadrage
- Archétype ? Perso ou pro-client ? Jetable, outil durable, ou livrable ?

### Exécution
- Tourne où : notebook local, Streamlit local, service on-prem, conteneur client ?
- On-prem strict / air-gapped ? GPU ou CPU only ? One-shot ou continu ?

### Données
- Source & volumétrie ?
- Type : tabulaire / texte / image / audio / série temporelle ?
- Persistance ? Confidentielles / RGPD / réseau client ?

### IA / LLM
- Besoin d'un LLM ? Local (petit modèle, sans GPU) vs API (interdit si air-gapped) ?
- Entraînement, ou inférence seule ?

### Légal
- Livré / commercialisé ? Licences compatibles (éviter le copyleft si produit fermé) ?

### Qualité
- Jetable (notebook propre) vs packagé (uv + tests + CI) ?
- Repris par client / équipe ? Repro exigée (seed, env figé) ?
