---
role: rule
domaine: security
applicable: global
strictness: must
tags: [rule, secrets-management, secret-scanning, config]
---

# Rule — Secrets hors du dépôt

## Principe

Aucun secret (mot de passe, clé d'API, jeton, clé privée) n'entre dans le dépôt, dans une image ou dans un journal : un détecteur le cherche avant chaque commit et en CI, et un secret qui a fuité est considéré comme compromis.

Cette règle complète [[Rule - Config typée]], qui couvre le `.env` ignoré par git, le `.env.example` et la validation au démarrage. Elle ajoute ce qui y manque : la détection, la fuite, la séparation des environnements et le chiffrement.

## MUST

- Ne jamais commiter un secret, dans aucun fichier : code, notebook, test, `README.md`, `AGENTS.md`.
- Faire scanner les secrets par un détecteur à chaque commit et en CI.
- Traiter tout secret commité comme compromis : le révoquer et le remplacer, puis seulement nettoyer l'historique.
- Utiliser un secret distinct par environnement : jamais le secret de production sur un poste de développement.
- Fournir les secrets à l'exécution, par un fichier monté ou une variable donnée au lancement, jamais dans le code ni dans l'image.
- Ne jamais écrire un secret dans un journal, un message d'erreur ou une invite donnée à un agent.

## SHOULD

- Détecter avec [[Gitleaks]], en hook de commit et en CI. Sur un poste sans réseau, [[Lefthook]] avec un binaire local évite de miroiter les dépôts de hooks que demande [[pre-commit]].
- Chiffrer un fichier de secrets qui doit rester versionné avec [[SOPS]] : les clés restent lisibles, les valeurs sont chiffrées, la clé de déchiffrement est ailleurs. SOPS n'apporte ni audit, ni révocation, ni rotation automatique.
- Passer à un serveur de secrets auto-hébergé ([[OpenBao]]) quand plusieurs services, une rotation ou un audit de lecture s'imposent.
- Donner à chaque service le secret dont il a besoin, et lui seul, avec les droits minimaux.
- Planifier la rotation et noter qui la fait : un secret sans échéance reste actif des années.
- Nommer le premier secret, celui qu'aucun outil ne fournit (clé de déchiffrement, jeton du coffre) : où il est, qui le détient, comment on le remplace.
- Scanner aussi l'image avant livraison ([[Rule - Image Docker minimale]]).

## NICE-TO-HAVE

- Une base de référence (baseline) du détecteur pour un dépôt hérité, afin que seuls les nouveaux secrets bloquent un commit.
- Un type dédié (`SecretStr`) dans la configuration, pour qu'un secret ne s'affiche pas quand on imprime l'objet.
- Un exercice de rotation par an, pour vérifier que la procédure fonctionne.

## Pour AGENTS.md

- Aucun secret dans le dépôt ni dans `AGENTS.md`. Les secrets viennent de l'environnement ou d'un fichier monté.
- Un détecteur de secrets passe avant chaque commit.
- Un secret commité est compromis : le dire, ne pas se contenter de le retirer.
- Ne jamais afficher un secret dans un journal ni dans une réponse.

## Exemples

### Bon

```yaml
# .pre-commit-config.yaml : détecteur de secrets avant chaque commit
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.24.2          # version de la page du projet, à mettre à jour
    hooks:
      - id: gitleaks
```

```bash
# secret chiffré versionné avec SOPS, clé age hors du dépôt
sops --encrypt --age "$CLE_PUBLIQUE" secrets.yaml > secrets.enc.yaml
```

### Mauvais

```python
API_KEY = "sk-live-0123456789"      # dans le code, donc dans l'historique
print(f"connexion avec {API_KEY}")  # et dans les journaux
```

```text
git rm .env && git commit -m "retire le .env"   # le secret reste dans l'historique : il est compromis
```

## Exceptions

- Valeur factice d'un fichier d'exemple (`.env.example`) ou d'un test : permise tant qu'elle ne marche nulle part. Un détecteur peut l'exclure par une règle écrite, pas par un `--no-verify`.
- Clé publique, certificat ou empreinte : ce ne sont pas des secrets.
- Projet de démonstration sans service réel : un secret de démo se génère au lancement, il ne se commite pas.

## Voir aussi

- [[Gestion des secrets]] — la notion : stocker, livrer, lire, renouveler, et le premier secret
- [[Rule - Config typée]] — `.env`, `.env.example`, validation au démarrage
- [[Rule - Image Docker minimale]] — aucun secret dans l'image
- [[Rule - Git et identité]] — le même mécanisme de hooks
- [[Gitleaks]] — le détecteur ; [[SOPS]] — le chiffrement de fichiers ; [[OpenBao]] — le serveur de secrets
- [[Supply chain logicielle et SBOM]] — le versant dépendances
