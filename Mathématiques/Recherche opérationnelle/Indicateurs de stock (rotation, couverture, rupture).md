---
role: notion
nom: Indicateurs de stock (rotation, couverture, rupture)
alias: [inventory turnover, rotation des stocks, days of supply, couverture de stock, stockout, taux de rupture, DIO, days inventory outstanding, inventory turns, stock turns, inventory record accuracy, précision de stock, DSI, days sales of inventory, stock dormant]
categorie: math/recherche-operationnelle
domaines: [data-sci]
tags: [inventory, probability]
---

# Indicateurs de stock (rotation, couverture, rupture)

## Aperçu

- Référentiel des **indicateurs** qui résument l'état d'un stock : rotation, couverture, rupture, valeur, stock dormant, précision des enregistrements. Chacun est un rapport de deux grandeurs ; chaque grandeur admet plusieurs lectures.
- **Les définitions varient d'une entreprise à l'autre.** Les sources ouvertes pour cette page le disent elles-mêmes : un cours du MIT note que les définitions du niveau de service « en pratique sont floues » (*fuzzy*), et la page Wikipedia sur la rotation donne plusieurs formules concurrentes et conclut qu'une organisation doit seulement rester **cohérente** avec la sienne. Un indicateur n'est comparable qu'avec sa définition écrite à côté.
- Ces indicateurs **décrivent le passé**. Les politiques qui les produisent (quantité de commande, stock de sécurité) sont dans [[Politiques de réapprovisionnement (s,S) et (R,Q)]] et [[Stock de sécurité et taux de service]]. Cette page ne fixe aucune cible.

## Concepts clés

### Rotation des stocks et DIO

- Notations : $C$ = coût des ventes (ou consommation) de la période, **au coût** ; $\bar S$ = stock moyen de la même période, **au coût** ; $T$ = nombre de jours de la période.
- **Rotation** (*inventory turnover*, *stock turns*) : $R = C / \bar S$. Sans unité, lue en « tours par période » (ou par an).
- **DIO** (*days inventory outstanding*, *days in inventory*) : $\mathrm{DIO} = T\,\bar S / C = T / R$, en **jours**. C'est l'inverse de la rotation, exprimé en durée. Wikipedia l'écrit $\mathrm{average\ inventory} / (\mathrm{COGS}/\mathrm{jours})$ avec 365 jours « en général ».
- Variante en unités physiques : unités vendues / unités moyennes en stock. La même page la signale comme celle de certains logiciels.

### Couverture

- **Couverture** (*days of supply*) : $K = S_{\text{dispo}} / \bar d$, en **jours**, avec $S_{\text{dispo}}$ le stock à l'instant considéré et $\bar d$ la consommation moyenne par jour.
- La couverture est une **photographie à une date** ; la rotation est une **moyenne sur une période**. Les deux se calculent sur le même stock mais ne répondent pas à la même question.
- **Couverture projetée** : stock disponible **plus** les commandes en cours, rapporté à la consommation, ou, plus finement, date à laquelle le solde projeté (stock + réceptions attendues − besoins prévus) atteint zéro. Formule de travail : aucune source ouverte ici ne fixe la variante.
- Deux choix changent le résultat : le stock au numérateur (physique, ou disponible net des réservations) et la consommation au dénominateur (historique récent, ou prévision).

### Taux de rupture : trois dénominateurs

Le « taux de rupture » désigne au moins trois quantités différentes. Le cours MIT classe d'ailleurs les ruptures par événement, par unités manquantes, par durée et par lignes manquantes.

- **Sur périodes** : $\tau_p = \#\{t : S_t = 0\} / T$, part des jours (ou des cycles) en rupture. Proche, en lecture, de $1-\alpha$ pour le niveau de service de type α (*ready rate* par période, selon Wikipedia).
- **Sur lignes de commande** : $\tau_l$ = lignes non servies complètement / lignes demandées. Se lit comme $1 -$ taux de remplissage par ligne.
- **Sur quantités** : $\tau_q = 1 - \text{vendu} / \text{demandé}$. Se lit comme $1 -$ taux de remplissage (β, ou « P2 » dans le cours MIT).
- Le même historique donne trois nombres différents (exemple plus bas). Les définitions précises du niveau de service et du taux de remplissage sont dans [[Stock de sécurité et taux de service]] ; elles ne sont pas répétées ici.
- La demande **non servie** n'apparaît pas dans les ventes. Un taux sur quantités exige un journal de **demande** (commandes, lignes), pas seulement de sorties de stock.

### Valeur, dormant, obsolète, précision

- **Valeur du stock** : somme $\sum_i q_i\, c_i$ des quantités par coût unitaire. La norme IAS 2 (IFRS) mesure les stocks au **plus bas du coût et de la valeur nette de réalisation**, et affecte le coût par identification spécifique, ou par la formule *first-in first-out* ou au **coût moyen pondéré** pour les articles interchangeables. Deux entreprises conformes peuvent donc valoriser le même stock différemment.
- **Stock dormant** : stock sans sortie depuis une durée seuil. Le seuil est une convention interne ; aucune valeur de référence n'a été trouvée dans une source ouverte. **Stock obsolète** : stock dont la valeur de réalisation est inférieure au coût, d'où la dépréciation prévue par IAS 2.
- **Précision de stock** (*inventory record accuracy*) : part des articles dont la quantité **enregistrée** correspond à la quantité **comptée**, au seuil de tolérance près (tolérance, périmètre et période à écrire avec le chiffre). Raman, DeHoratius et Ton (2001) l'ont mesurée chez un grand distributeur : plus de 65 % des enregistrements étaient inexacts (compte rendu de Chicago Booth Review, qui cite « près de 240 000 articles » dans 37 magasins sans préciser si ce nombre est le dénominateur ou les seuls articles inexacts).

## Les maths, simplement

- **Rotation et DIO sont inverses** : $\mathrm{DIO} = T / R$. Une rotation annuelle de 12 donne environ 30 jours.
- **Lien avec la loi de Little.** Pour un système où des unités entrent, séjournent et sortent : $L = \lambda W$, avec $L$ le nombre moyen d'unités présentes, $\lambda$ le débit moyen et $W$ le temps de séjour moyen. Appliqué au stock : $\bar S = \bar d \times W$, donc $W = \bar S / \bar d$, soit **le DIO en unités** ; la rotation vaut $1/W$ par jour.
- **Hypothèses de Little (1961)** : les trois moyennes sont finies, les processus sont strictement stationnaires, le processus d'arrivée est métriquement transitif de moyenne non nulle ; la loi ne suppose ni distribution des arrivées, ni discipline de file. Une unité qui ne rejoint pas le système doit être exclue de $\lambda$. Little (2011) montre que sur une fenêtre finie $[0,T]$ l'identité est **exacte et sans hypothèse de stationnarité**, indépendante de la discipline (FIFO, LIFO, aléatoire) ; elle s'écrit alors $L = A/T$, $\lambda = S(T)/T$, $W = A/S(T)$ avec $A$ l'aire sous la courbe de stock et $S(T)$ les unités arrivées **plus** celles déjà présentes en $0$.
- **Déduction propre à cette page (non issue des articles)** : le DIO calculé comme $T\bar S / \text{sorties}$ est le $W$ de Little seulement si le stock est proche au début et à la fin de la fenêtre, puisque Little compte les arrivées et les unités initiales, non les sorties. En valeur, $\sum c_i W_i / \sum c_i$ : un temps de séjour **pondéré par le coût**.
- **Agrégation** : pour des classes d'articles $k$, Little (2011) donne $L=\sum_k L_k$, $\lambda=\sum_k\lambda_k$ et $W=\sum_k(\lambda_k/\lambda)\,W_k$. Le temps moyen global est la moyenne des temps par classe **pondérée par le débit**.
- **Ordre de grandeur d'une politique** : sous demande constante et continue, le stock moyen d'un dent de scie de lot $Q$ avec stock de sécurité $SS$ vaut $\bar S \approx Q/2 + SS$, d'où $R \approx D/(Q/2+SS)$ pour une demande annuelle $D$. Re-dérivé et vérifié par simulation en pas fin (74,95 simulé pour 75 attendu) ; il casse dès que la demande est aléatoire ou intermittente, cf. [[Intermittent demand]].

## En pratique

### Pièges de lecture

- **Une moyenne cache la distribution.** Un stock moyen correct peut coexister avec des ruptures fréquentes : trois semaines de surstock et une semaine à zéro donnent le même $\bar S$ qu'un stock stable. Rotation et couverture ne disent rien de la fréquence des ruptures.
- **Des indicateurs qui tirent en sens opposé.** Une rotation haute (stock bas) accompagne en général plus de ruptures ; une couverture longue protège et immobilise de la valeur. Le compromis est formalisé dans [[Stock de sécurité et taux de service]].
- **Stock moyen : quelle moyenne ?** (début + fin) / 2, moyenne de fins de jour ou moyenne de moyennes mensuelles. Wikipedia indique que la moyenne de plusieurs points, par exemple les moyennes mensuelles, donne un chiffre « bien plus représentatif ». Le résultat diffère (exemple ci-dessous).
- **Coût d'achat ou prix de vente ?** Wikipedia donne deux formules, ventes nettes / stock moyen **au prix de vente**, ou coût des ventes / stock moyen **au coût**, et note que certains compilateurs d'industrie (Dun & Bradstreet) emploient les ventes en numérateur. Mêler un numérateur au prix de vente et un stock au coût multiplie la rotation par le rapport prix/coût.
- **Saisonnalité.** Une rotation annuelle moyenne efface le pic d'avant-saison ; une fenêtre qui commence ou finit à un creux saisonnier biaise (début + fin) / 2. Wikipedia (*days in inventory*) rappelle que la valeur reflète aussi la saisonnalité et le modèle d'affaires, et préconise de comparer dans un même secteur et dans le temps.
- **Agréger des unités différentes.** Additionner des pièces, des litres et des palettes n'a pas de sens ; une rotation globale se calcule **en valeur**, et le résultat est dominé par les références chères (voir la classification ci-dessous).
- **Ventes ≠ demande.** Pendant une rupture, les ventes baissent : la rotation observée sous-estime la demande, et la prévision apprise sur ces ventes en hérite. Le compte rendu de Chicago Booth Review décrit le cas voisin : un article en rupture, non enregistré comme tel, n'enregistre aucune vente, et la nouvelle prévision peut être trop basse.
- **Précision de stock.** Un enregistrement faux fausse $\bar S$, la couverture et la rupture (un article absent du rayon mais présent dans le système n'est compté en rupture nulle part : conséquence directe de la définition).

### Exemple exécuté

Journal de 10 jours d'une référence : stock initial 40, une réception de 70 au jour 6.

```python
import pandas as pd
j = pd.DataFrame({"demande": [10, 12, 13, 9, 7, 12, 12, 15, 13, 12],
                  "vendu":   [10, 12, 13, 5, 0, 12, 12, 15, 13, 12],
                  "recu":    [0, 0, 0, 0, 0, 70, 0, 0, 0, 0]})
j["stock"] = 40 + (j["recu"] - j["vendu"]).cumsum()          # fin de jour
moy, moy2 = j["stock"].mean(), (40 + j["stock"].iloc[-1]) / 2   # moyenne des jours | (début+fin)/2
print(moy, moy2, j["vendu"].sum() / moy, j["vendu"].sum() / moy2)
print(j["stock"].iloc[-1] / j["vendu"].mean(), (j["stock"] == 0).mean(), 1 - j["vendu"].sum() / j["demande"].sum())
```

- Sorties : stock moyen 21,2 (moyenne des jours) contre 23,0 ((début + fin)/2) ; rotation 4,91 contre 4,52 tours sur 10 jours, soit un DIO de 2,04 jours (celui de la moyenne des jours).
- Couverture au dernier jour : 0,58 jour. Taux de rupture **sur périodes** 20 % (2 jours à zéro), **sur quantités** 9,6 % (11 unités sur 115 non servies) : le même historique donne deux taux.

### Usage

- **Tableau de bord par classe** : calculer chaque indicateur par classe de [[Classification ABC-XYZ]] plutôt que globalement. Le cours MIT rappelle que les classes A/B/C sont des classifications « arbitraires » et suggère un contrôle plus serré des articles A.
- **Comparer à une cible** issue des politiques ([[Politiques de réapprovisionnement (s,S) et (R,Q)]]) : la politique implique un stock moyen, donc une rotation et une couverture attendues, auxquelles l'observé se mesure.
- **Écrire la définition avec le chiffre** : numérateur, dénominateur, valorisation, fenêtre, jours calendaires ou ouvrés, périmètre, tolérance pour la précision.

## Approches voisines & alternatives

- [[Stock de sécurité et taux de service]] — définit niveau de service et taux de remplissage, dont les taux de rupture ci-dessus sont les compléments.
- [[Classification ABC-XYZ]] — segmente les références pour lire les indicateurs par classe.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — les règles qui fixent le stock moyen que les indicateurs mesurent.
- [[Quantité économique de commande et tailles de lot]] — le lot $Q$ qui entre dans $\bar S \approx Q/2 + SS$.
- [[Intermittent demand]] — références à rotation faible et demande sporadique, où les moyennes décrivent mal.
- [[Forecasting metrics]] — mesurent la qualité d'une prévision, non l'état d'un stock ; à ne pas confondre avec les indicateurs ci-dessus.
- [[Probabilités]] — espérances et moyennes temporelles, vocabulaire de la loi de Little.

## Pour aller plus loin

- Little (1961), *A proof for the queuing formula: L = λW*, Operations Research 9(3), 383-387 : <https://doi.org/10.1287/opre.9.3.383> — lu en entier.
- Little (2011), *OR Forum — Little's Law as Viewed on Its 50th Anniversary*, Operations Research 59(3), 536-549 : <https://doi.org/10.1287/opre.1110.0940> — lu sur la réimpression de Project Production Institute (<https://projectproduction.org/journal/reprint-littles-law-as-viewed-on-its-50th-anniversary/>), sections sur l'horizon fini et les classes.
- Raman, DeHoratius, Ton (2001), *Execution: The Missing Link in Retail Operations*, California Management Review 43(3) : <https://cmr.berkeley.edu/2001/05/43-3-execution-the-missing-link-in-retail-operations/> — résumé lu ; les chiffres de 37 magasins viennent du compte rendu de Chicago Booth Review (<https://www.chicagobooth.edu/review/first-measure-then-manage>), lu.
- DeHoratius & Raman (2008), *Inventory Record Inaccuracy: An Empirical Analysis*, Management Science 54(4), 627-641 : <https://doi.org/10.1287/mnsc.1070.0789> — seules les métadonnées ont été vues.
- Caplice (2006), *Inventory Management: Probabilistic Demand*, MIT ESD.260 Logistics Systems, cours 11 : <https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf> — lu.
- IFRS Foundation, *IAS 2 Inventories* : <https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/> — page de synthèse lue.
- Wikipedia, *Inventory turnover* (<https://en.wikipedia.org/wiki/Inventory_turnover>), *Days in inventory* (<https://en.wikipedia.org/wiki/Days_in_inventory>), *Service level* (<https://en.wikipedia.org/wiki/Service_level>) — sources secondaires, lues ; leurs références (Weygandt, Ross, Bowersox et al.) n'ont pas été ouvertes.
- Non consultés : ASCM (APICS) *Dictionary*, Silver–Pyke–Thomas, Chopra–Meindl, Bowersox–Closs. Aucune définition de ces ouvrages n'est reprise ici.
- Connexions brain : [[Stock de sécurité et taux de service]], [[Classification ABC-XYZ]], [[Politiques de réapprovisionnement (s,S) et (R,Q)]], [[Intermittent demand]].
