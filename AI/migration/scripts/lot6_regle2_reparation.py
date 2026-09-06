# /// script
# requires-python = ">=3.10"
# ///
"""lot6_regle2_reparation.py — remettre en `Écarter si` les renvois que la
première formulation de la règle 2 avait envoyés au comparatif à tort.

La règle corrigée (2026-09-06) : un renvoi « besoin → [[cible]] » ne part au
comparatif QUE si la brique ET la cible sont membres de la MÊME vue `.base`.
Les renvois listés ici n'ont pas de vue commune : ils reviennent sur la fiche.

Deux gestes seulement, et jamais d'invention : soit la cellule existante dit
déjà la chose sans le lien, et on lui ajoute le lien (ENRICHIR) ; soit la
cellule n'existe pas, et on la pose (REMPLIR une cellule vide, ou AJOUTER une
ligne). Le texte vient de la puce `## Quand NE PAS l'utiliser` d'origine.

Les wikilinks des cellules sont NUS (règle 1). Idempotent : un remplacement
déjà appliqué est signalé « déjà fait », pas rejoué.

Audit associé : `lot6_regle2_audit.py`, à relancer après pour mesurer l'écart.
"""

from __future__ import annotations

import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]

# (fiche, geste, argument)
#   ENRICHIR : (ancien fragment de cellule, nouveau fragment)
#   REMPLIR  : (début de la cellule « Prendre si » de la ligne, texte de la cellule droite)
#   AJOUTER  : texte de la cellule droite, sur une ligne neuve
TRAVAUX = [
    # ---- lot 1 — Bases de données, niveau domaine ----
    ("Bases de données/ADBC.md", "REMPLIR",
     ("Standardiser l'accès à plusieurs bases",
      "Lecture seule la plus rapide possible vers un DataFrame, sans écriture → [[connectorx]]")),
    ("Bases de données/ADBC.md", "AJOUTER",
     ("Application transactionnelle Postgres classique, ligne à ligne → driver DB-API [[psycopg2]]",)),
    ("Bases de données/ADBC.md", "AJOUTER",
     ("Mapping objet, migrations, modèle de domaine → [[SQLAlchemy]]",)),
    ("Bases de données/Alembic.md", "AJOUTER",
     ("Migrations couplées à un ORM TypeScript → [[Prisma]]",)),
    ("Bases de données/Apache Cassandra.md", "ENRICHIR",
     ("Ni jointure ni agrégation libre : `ALLOW FILTERING` est une porte ouverte aux scans",
      "Requêtes ad hoc, jointures, agrégations imprévues → [[Postgres]] ; ici, `ALLOW FILTERING` est une porte ouverte aux scans")),
    ("Bases de données/Apache Cassandra.md", "ENRICHIR",
     ("Petit volume tenant sur un nœud : la complexité opérationnelle du cluster ne se rembourse pas",
      "Petit volume tenant sur un nœud : la complexité opérationnelle du cluster ne se rembourse pas → [[Postgres]]")),
    ("Bases de données/ClickHouse.md", "REMPLIR",
     ("Ingestion à fort débit de logs",
      "OLTP transactionnel, beaucoup de petites écritures et de mises à jour ponctuelles → [[Postgres]]")),
    ("Bases de données/DuckDB.md", "REMPLIR",
     ("Tests et prototypes analytiques jetables",
      "OLTP et écritures concurrentes transactionnelles → [[Postgres]]")),
    ("Bases de données/Flyway.md", "AJOUTER",
     ("Migrations dérivées d'un schéma d'ORM TypeScript → [[Prisma]]",)),
    ("Bases de données/InfluxDB.md", "AJOUTER",
     ("Données relationnelles, jointures et transactions ACID → [[Postgres]]",)),
    ("Bases de données/InfluxDB.md", "AJOUTER",
     ("Analytique colonne à haute cardinalité, non strictement temporelle → [[ClickHouse]]",)),
    ("Bases de données/Liquibase.md", "AJOUTER",
     ("Migrations générées et couplées à un ORM TypeScript → [[Prisma]]",)),
    ("Bases de données/MongoDB.md", "REMPLIR",
     ("Prototypage rapide, tant que le schéma n'est pas figé",
      "Fortes garanties relationnelles, jointures complexes, intégrité référentielle → [[Postgres]], dont le `JSONB` couvre déjà le semi-structuré modéré")),
    ("Bases de données/Nebula Graph.md", "AJOUTER",
     ("Données peu connectées, modèle tabulaire et transactions classiques → [[Postgres]]",)),
    ("Bases de données/Neo4j.md", "AJOUTER",
     ("Données tabulaires peu reliées, transactions classiques → [[Postgres]]",)),
    ("Bases de données/Prisma.md", "REMPLIR",
     ("Déploiement serverless sensible au cold start",
      "Stack Python — data, ML, [[FastAPI]] → un ORM Python ([[SQLAlchemy]]) ou un outil de migration dédié, [[Liquibase]] ou [[Flyway]]")),
    ("Bases de données/Redis.md", "AJOUTER",
     ("Source de vérité durable au-delà de ce qui tient en RAM → une base sur disque, [[Postgres]]",)),
    ("Bases de données/SQLAlchemy.md", "AJOUTER",
     ("Seulement des migrations, sans couche d'accès → outils dédiés, [[Flyway]] ou [[Liquibase]]",)),
    ("Bases de données/psycopg2.md", "AJOUTER",
     ("Vouloir un **mapping objet** et des **migrations** → [[SQLAlchemy]] et [[Alembic]]",)),
    ("Bases de données/TimescaleDB.md", "REMPLIR",
     ("Agrégats continus et compression sur l'historique",
      "Analytique colonne massive, non temporelle → [[ClickHouse]]")),
    # ---- lot 2 — Recherche/ ----
    ("Bases de données/Recherche/Marqo.md", "AJOUTER",
     ("Embedding maîtrisé côté application, plus une base vectorielle dédiée → [[Qdrant]], [[Weaviate]]",)),
    ("Bases de données/Recherche/txtai.md", "AJOUTER",
     ("Base vectorielle managée clé en main → [[Pinecone]] ; fort filtrage sur une base dédiée → [[Qdrant]]",)),
    ("Bases de données/Recherche/Vespa.md", "REMPLIR",
     ("Late-interaction : tenseurs multi-vecteurs",
      "Petit corpus, besoin simple : la complexité opérationnelle est disproportionnée → une base vectorielle dédiée, [[Qdrant]] ou [[Weaviate]]")),
    ("Bases de données/Recherche/Vespa.md", "AJOUTER",
     ("Prototype Python embarqué → un index [[Faiss]] en mémoire",)),
    # ---- lot 3 — Vision/ ----
    ("Machine Learning/Vision/albumentations.md", "AJOUTER",
     ("Augmentation **sur GPU** et **différentiable**, dans le graphe d'autograd → [[Kornia]]",)),
    ("Machine Learning/Vision/OpenCV.md", "REMPLIR",
     ("Détecteurs et trackers classiques",
      "Entraîner ou fine-tuner un réseau de vision → [[PyTorch]], avec [[torchvision]] ou [[timm]]")),
    ("Machine Learning/Vision/OpenCV.md", "REMPLIR",
     ("Capture caméra et pipeline vidéo temps réel",
      "Opérations de vision **différentiables**, dans une boucle d'autograd sur GPU → [[Kornia]]")),
    ("Machine Learning/Vision/segment-anything.md", "AJOUTER",
     ("**Classes fixes**, latence serrée, précision sur un domaine donné → un U-Net, DeepLab ou Mask R-CNN dédié, via [[torchvision]]",)),
    ("Machine Learning/Vision/timm.md", "AJOUTER",
     ("Augmentation seule, sans modèles → [[albumentations]] ou [[Kornia]]",)),
    ("Machine Learning/Vision/Ultralytics YOLO.md", "AJOUTER",
     ("Briques de détection et de segmentation dans l'écosystème PyTorch officiel, sans contrainte de licence → [[torchvision]]",)),
    # ---- lot 5 — Tabulaire/ ----
    ("Machine Learning/Tabulaire/CatBoost.md", "AJOUTER",
     ("Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Scikit-Learn]]",)),
    ("Machine Learning/Tabulaire/category_encoders.md", "ENRICHIR",
     ("Faible cardinalité : les encodeurs natifs de scikit-learn suffisent",
      "Faible cardinalité : les encodeurs natifs de [[Scikit-Learn]] suffisent")),
    ("Machine Learning/Tabulaire/Featuretools.md", "ENRICHIR",
     ("Une seule table plate, sans relations : un `ColumnTransformer` écrit à la main suffit",
      "Une seule table plate, sans relations : un `ColumnTransformer` de [[Scikit-Learn]] écrit à la main suffit")),
    ("Machine Learning/Tabulaire/Featuretools.md", "AJOUTER",
     ("Encodage catégoriel fin — Target, WoE → [[category_encoders]]",)),
    ("Machine Learning/Tabulaire/LightGBM.md", "AJOUTER",
     ("Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Scikit-Learn]], inspiré de LightGBM",)),
    ("Machine Learning/Tabulaire/XGBoost.md", "AJOUTER",
     ("Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Scikit-Learn]]",)),
    # ---- lots 6 à 8 — le résidu des trois lots qui ont trouvé la règle fausse ----
    ("Machine Learning/Apprentissage par renforcement/Stable-Baselines3.md", "ENRICHIR",
     ("→ [[RLax]] pour composer soi-même, ou une implémentation mono-fichier",
      "→ [[RLax]] pour composer soi-même, ou une implémentation mono-fichier type CleanRL, écrite sur [[PyTorch]]")),
    ("Machine Learning/PyTorch Geometric.md", "ENRICHIR",
     ("Données en grille ou séquence régulière — CNN, Transformers — plutôt qu'un graphe",
      "Données en grille ou séquence régulière : un CNN ([[torchvision]]) ou un Transformer, plutôt qu'un GNN")),
    ("LLM & IA générative/Agents/OpenAI Agents SDK.md", "AJOUTER",
     ("**Mémoire persistante** longue durée comme primitive centrale → [[Letta]]",)),
    ("LLM & IA générative/Agents de code/ai-memory.md", "ENRICHIR",
     ("plutôt que d'une CLI de code : ce n'est pas la cible → [[Letta]]",
      "plutôt que d'une CLI de code : ce n'est pas la cible → [[Letta]], [[OpenViking]]")),
    ("LLM & IA générative/Agents de code/swarm-forge.md", "ENRICHIR",
     ("on n'écrit rien avec — on orchestre des CLI tierces déjà installées",
      "on n'écrit rien avec — on orchestre des CLI tierces déjà installées → [[CrewAI]], [[AutoGen]]")),
    ("LLM & IA générative/Assistants/OpenMAIC.md", "ENRICHIR",
     ("c'est une bibliothèque qu'il faut → [[PraisonAI]], [[CrewAI]]",
      "c'est une bibliothèque qu'il faut → [[LangGraph]], [[PraisonAI]], [[CrewAI]]")),
]

TITRE = "\n## Prendre si / Écarter si\n"


def bloc_tableau(txt: str, rel: str):
    m = re.search(re.escape(TITRE) + r"(.*?)(?=\n## )", txt, re.S)
    if not m:
        raise SystemExit(f"tableau introuvable dans {rel}")
    return m.start(1), m.end(1), m.group(1)


def main() -> int:
    faits = deja = 0
    for rel, geste, arg in TRAVAUX:
        p = VAULT / rel
        txt = p.read_text(encoding="utf-8")
        deb, fin, tab = bloc_tableau(txt, rel)
        if geste == "ENRICHIR":
            ancien, neuf = arg
            if neuf in tab:
                deja += 1
                continue
            if ancien not in tab:
                raise SystemExit(f"ENRICHIR : fragment absent dans {rel}\n  {ancien}")
            tab = tab.replace(ancien, neuf, 1)
        elif geste == "REMPLIR":
            debut_gauche, cellule = arg
            if cellule in tab:
                deja += 1
                continue
            lignes = tab.split("\n")
            for i, ligne in enumerate(lignes):
                if ligne.startswith("| " + debut_gauche) and ligne.rstrip().endswith("| |"):
                    lignes[i] = ligne.rstrip()[:-1].rstrip() + " " + cellule + " |"
                    break
            else:
                raise SystemExit(f"REMPLIR : ligne vide introuvable dans {rel}\n  {debut_gauche}")
            tab = "\n".join(lignes)
        else:  # AJOUTER
            cellule = arg[0]
            if cellule in tab:
                deja += 1
                continue
            lignes = tab.rstrip("\n").split("\n")
            lignes.append("| | " + cellule + " |")
            tab = "\n".join(lignes) + "\n"
        p.write_text(txt[:deb] + tab + txt[fin:], encoding="utf-8")
        faits += 1
    print(f"{faits} geste(s) appliqué(s), {deja} déjà fait(s), sur {len(TRAVAUX)} prévus.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
