---
role: hub
nom: Sécurité
alias: [securite, security, appsec]
pitch: Prouver qui appelle, et voir ce qu'un système expose de lui-même vu de l'extérieur.
domaines: [ai-eng, infra-ops]
tags: [authentication, recon, osint, cryptography]
---

# Sécurité

> Prouver qui appelle, et voir ce qu'un système expose de lui-même vu de l'extérieur.

## Ce qu'il faut comprendre

- Deux activités sans recouvrement partagent ce domaine. **Authentifier** ([[PyJWT]]) est du code qu'on écrit dans son propre service. **Reconnaître** ([[Web-Check]], [[osint4all]]) est une inspection depuis l'extérieur, sans accès privilégié.
- Sur les JWT, la faute classique n'est pas cryptographique mais logique : **un token décodé n'est pas un token vérifié**. Lire les revendications sans valider la signature, l'algorithme attendu, l'émetteur et l'expiration revient à faire confiance à l'appelant. [[PyJWT]] rend la vérification explicite ; c'est au code de la demander.
- Un JWT est **porteur** (*bearer*) : quiconque l'a l'utilise, et il reste valide jusqu'à son expiration. Il n'y a pas de révocation sans état côté serveur. D'où des durées de vie courtes, et un jeton de rafraîchissement séparé.
- La reconnaissance passive ([[Web-Check]]) est aussi un outil **défensif** : elle dit ce qu'un tiers voit de votre propre infrastructure — en-têtes manquants, certificats, sous-domaines oubliés, technologies annoncées.
- Les questions de sécurité **propres aux LLM** — [[Prompt injection]], [[Jailbreaking and defenses]], [[Guardrails]], [[AI security]] — portent encore `concept/ai` et ne sont pas descendues ici : elles figurent dans la liste « Hors arbre » et relèvent du lot 4.

## Choisir

- Émettre ou vérifier des JWT en Python → [[PyJWT]].
- Auditer un site depuis sa seule URL, en défense comme en reconnaissance → [[Web-Check]].
- Chercher par où commencer une recherche en source ouverte → [[osint4all]].

<!-- AUTO:START -->
### Briques
- [[osint4all]] — Annuaire de liens OSINT (CC0, portage GitHub d'une page start.me) : de l'ordre de 78 rubriques et 1 400 liens — générateurs, récupération de hash, confidentialité, recherche de personnes, guides. Ni logiciel, ni service, et sans commit depuis juillet 2022.
- [[PyJWT]] — Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.
- [[Web-Check]] — Audit d'un site depuis sa seule URL, sans accès privilégié : DNS, TLS, en-têtes de sécurité, technologies détectées, redirections, ports, traceroute, listes de blocage et archives — auto-hébergeable en Docker.
<!-- AUTO:END -->
