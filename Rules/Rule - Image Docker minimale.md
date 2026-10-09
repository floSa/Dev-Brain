---
role: rule
domaine: containers
applicable: docker
strictness: must
tags: [rule, container, secrets-management, reproducibility]
---

# Rule — Image Docker minimale

## Principe

Une image Docker est petite, tourne sans droits root, se vérifie elle-même et ne contient aucun secret : ce qu'elle n'embarque pas ne peut pas être attaqué ni fuir.

La règle vaut pour tout projet qui livre une image, y compris sur un serveur du client sans accès Internet, où l'image est souvent la seule chose qui arrive.

## MUST

- Partir d'une image de base minimale (`-slim`) à version épinglée, jamais `latest`.
- Construire en plusieurs étapes : l'image finale ne contient ni compilateur, ni cache, ni sources inutiles.
- Lancer le processus sous un utilisateur non root, avec `USER` et un UID explicite.
- Ajouter un `.dockerignore` qui écarte `.git`, `.env`, `.venv`, les caches et les données.
- Déclarer un `HEALTHCHECK` dans l'image, ou une `healthcheck` du service dans le fichier Compose.
- Ne mettre aucun secret dans l'image : ni `ENV`, ni `ARG`, ni fichier copié.

## SHOULD

- Épingler l'image de base par empreinte (`tag@sha256:…`) et mettre à jour l'empreinte par un outil de mise à jour des dépendances : la construction redonne la même image, et chaque changement de base passe en revue.
- Faire `apt-get update` et `apt-get install` dans le même `RUN`, puis supprimer `/var/lib/apt/lists/*` dans ce même `RUN`.
- Passer un secret de construction par `RUN --mount=type=secret`, un secret d'exécution par un fichier monté ou une variable fournie au lancement. Les valeurs d'`ARG` se lisent dans `docker history`, celles d'`ENV` restent dans l'image.
- Copier d'abord les fichiers de dépendances, puis le code : le cache des couches évite de tout réinstaller à chaque modification.
- Scanner l'image avant livraison avec [[Grype]] ou [[Trivy]]. Lire la fiche de Trivy : sa release a été compromise en mars 2026.
- Servir les images depuis un registre interne ([[Harbor]], [[Zot]]) quand le site client n'a pas Internet.
- Un seul processus par conteneur, des volumes nommés pour les données.

## NICE-TO-HAVE

- Système de fichiers en lecture seule à l'exécution (`read_only: true` sous Compose), avec un volume pour ce qui doit s'écrire.
- [[Podman]] à la place de Docker quand le poste ou le site interdit un démon qui tourne en root.
- Une commande `make check-image` qui construit, lance le scan et vérifie que l'utilisateur n'est pas root.

## Pour AGENTS.md

- Image Docker : base `-slim` à version épinglée, build en plusieurs étapes, `USER` non root.
- Un `.dockerignore` écarte `.git`, `.env` et les caches.
- Aucun secret dans l'image : ni `ENV`, ni `ARG`, ni fichier copié.
- Un `HEALTHCHECK` dans l'image ou dans le Compose.

## Exemples

### Bon

```dockerfile
FROM python:3.12-slim AS build
WORKDIR /src
COPY pyproject.toml ./
COPY src ./src
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir .

FROM python:3.12-slim
RUN useradd --uid 10001 --no-create-home app
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
USER 10001
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request as u; u.urlopen('http://127.0.0.1:8000/health')"
CMD ["mon-projet", "serve"]
```

```text
# .dockerignore
.git
.env
.venv
__pycache__
data/
```

### Mauvais

```dockerfile
FROM python:latest
COPY . .
ENV API_KEY=sk-live-0123456789
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
# root, tout le dépôt copié dont .env, secret dans une couche, aucune vérification de santé
```

## Exceptions

- Un programme qui exige root (port inférieur à 1024, accès à un périphérique) : le dire dans le `README.md`, et réduire les droits plutôt que les garder tous.
- Image de CI ou de développement jetable : l'image minimale n'est pas nécessaire, l'interdiction de secrets reste.
- Démo locale lancée par `docker compose up` : voir [[Rule - Packaging démo]], qui fixe sa propre barre.

## Voir aussi

- [[Docker]], [[Podman]] — les moteurs de conteneurs
- [[Rule - Packaging démo]] — la démo qui monte d'un `docker compose up`
- [[Rule - Secrets hors du dépôt]] — les secrets, au-delà de l'image
- [[Rule - Config typée]] — la configuration lue à l'exécution
- [[Grype]], [[Trivy]] — les scanners d'image
- [[Harbor]], [[Zot]] — les registres d'images auto-hébergés
- [[Supply chain logicielle et SBOM]] — pourquoi épingler et scanner
