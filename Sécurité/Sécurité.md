---
role: hub
nom: Sécurité
alias: [securite, security, appsec]
pitch: Prouver qui appelle, voir ce qu'un système expose de lui-même vu de l'extérieur, et tenir un modèle qui obéit à ce qu'on lui donne à lire.
domaines: [ai-eng, infra-ops]
tags: [authentication, recon, osint, cryptography, ai-security, prompt-injection, jailbreak, guardrails]
---

# Sécurité

> Prouver qui appelle, voir ce qu'un système expose de lui-même vu de l'extérieur, et tenir un modèle qui obéit à ce qu'on lui donne à lire.

## Ce qu'il faut comprendre

- **Trois** activités sans recouvrement partagent ce domaine. **Authentifier** ([[PyJWT]]) est du code qu'on écrit dans son propre service. **Reconnaître** ([[Web-Check]], [[osint4all]]) est une inspection depuis l'extérieur, sans accès privilégié. **Tenir un système qui embarque un modèle** est une discipline entière, arrivée ici au lot 4 et assez fournie depuis pour tenir son propre dossier — [[Systèmes IA]] : ce n'est pas un sous-sujet de l'IA générative, c'est une pratique de sécurité qui traverse les modèles.
- Sur les JWT, la faute classique n'est pas cryptographique mais logique : **un token décodé n'est pas un token vérifié**. Lire les revendications sans valider la signature, l'algorithme attendu, l'émetteur et l'expiration revient à faire confiance à l'appelant. [[PyJWT]] rend la vérification explicite ; c'est au code de la demander.
- Un JWT est **porteur** (*bearer*) : quiconque l'a l'utilise, et il reste valide jusqu'à son expiration. Il n'y a pas de révocation sans état côté serveur. D'où des durées de vie courtes, et un jeton de rafraîchissement séparé.
- La reconnaissance passive ([[Web-Check]]) est aussi un outil **défensif** : elle dit ce qu'un tiers voit de votre propre infrastructure — en-têtes manquants, certificats, sous-domaines oubliés, technologies annoncées.
- **La faille fondatrice des systèmes à modèle n'est pas cryptographique non plus** : instructions et données arrivent dans le même canal de tokens, donc rien ne distingue structurellement une consigne d'un contenu. [[AI security]] est le panorama ; [[Prompt injection]] est le risque n° 1 et détourne les instructions du développeur ; [[Jailbreaking and defenses]] vise autre chose — la politique de refus du modèle — et la frontière entre les deux mérite d'être tenue nette ; [[Guardrails]] est la couche de contrôle déterministe qu'on pose autour, en entrée et en sortie ; [[Sandboxing de code généré]] traite le cas où le modèle ne produit plus du texte mais du code à exécuter, et part du principe que ce code est non fiable par construction.
- **Ce qui rend l'injection grave, c'est l'agence, pas le texte.** Un modèle sans outils ni données sensibles produit une réponse fausse ; le même modèle branché sur des outils à effet de bord exécute. Le moindre privilège et la validation humaine des actions irréversibles font donc partie de la sécurité au même titre que les filtres — cf. [[Reliability patterns]].

## Choisir

- Émettre ou vérifier des JWT en Python → [[PyJWT]].
- Auditer un site depuis sa seule URL, en défense comme en reconnaissance → [[Web-Check]].
- Chercher par où commencer une recherche en source ouverte → [[osint4all]].
- Tout ce qui touche à la sécurité d'un système qui embarque un modèle → [[Systèmes IA]] : le panorama ([[AI security]]), l'entrée non fiable qui détourne les instructions ([[Prompt injection]]), le contournement de l'alignement ([[Jailbreaking and defenses]]), le filtrage d'entrée et de sortie ([[Guardrails]]) et l'isolation du code généré ([[Sandboxing de code généré]]).
- Les briques qui appliquent tout ça (passerelles, observabilité, sortie structurée) → [[LLM & IA générative]], qui garde les outils là où ce domaine garde la discipline.

<!-- AUTO:START -->
### Sous-domaines
- [[Systèmes IA]]

### Briques
- [[osint4all]] — Annuaire de liens OSINT (CC0, portage GitHub d'une page start.me) : de l'ordre de 78 rubriques et 1 400 liens — générateurs, récupération de hash, confidentialité, recherche de personnes, guides. Ni logiciel, ni service, et sans commit depuis juillet 2022.
- [[PyJWT]] — Implémentation Python de référence des JSON Web Tokens (RFC 7519) — encode, décode et vérifie des tokens signés (HMAC, RSA, ECDSA, EdDSA) avec validation des claims (exp, aud, iss) ; brique d'auth stateless pour API.
- [[Web-Check]] — Audit d'un site depuis sa seule URL, sans accès privilégié : DNS, TLS, en-têtes de sécurité, technologies détectées, redirections, ports, traceroute, listes de blocage et archives — auto-hébergeable en Docker.
<!-- AUTO:END -->
