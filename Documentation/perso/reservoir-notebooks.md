# Réservoir Notebooks → backlog d'enrichissement DevBrain

> Dérivé de **Notebooks-Cheat-Sheet** (`2_New_Notebooks/md/`, 44 cheat-sheets lus **au contenu**, pas aux titres).
> Ne liste que ce qui est **réellement traité dans les notebooks** ET **absent du DevBrain v2** (croisé avec les 347 pages existantes).
> `source:` = notebook(s) d'origine, pour traçabilité.

**Légende** : ⬜ à créer · ⚠️ sous-domaine à créer / à valider.

Déjà couvert en v2 (donc **exclu** d'ici) : DuckDB, bases vectorielles, Docling, PyTorch/TensorFlow/JAX/HuggingFace, Optuna/Hyperopt/Ray Tune, MLflow, RandomForest/boosting (XGBoost/LightGBM/CatBoost), bagging/boosting, validation croisée, sélection de variables, ARIMA/SARIMA, statsmodels/scipy.stats/prince/fanalysis, FastAPI, Streamlit, SQLAlchemy/psycopg2, MongoDB, RAG/transformers/embeddings/reranking/PEFT-LoRA, RL de base (Q-learning/DQN/PPO/bandits), PCA/CA/MCA/FAMD/GPA, imbalanced classification, mise à l'échelle/encodage/imputation (concept).

---

## 1. Traitement du signal → « Signal & audio » (`signal/traitement`)
*source : TdS_Introduction_Traitement_Signal*
**Notions :**
- ⬜ Transformée de Fourier (DFT / FFT)
- ⬜ Ondelettes (DWT / CWT)
- ⬜ STFT & spectrogramme (dont mel / MFCC)
- ⬜ Filtrage numérique (Butterworth, fenêtrage, Hilbert)

**Libs (Dev) :**
- ⬜ scipy.signal → `tooling/data` (ou `ml/framework`)
- ⬜ PyWavelets → `tooling/data`
- ⬜ librosa → `ml/framework` (audio)

## 2. NLP → « Machine Learning » (`ml/nlp`)
*sources : NLP_Classification_Supervisee, NLP_Classification_Smote, NLP_NER, NLP_NER_BiLSTM_CRF, NLP_Recherche_d_informations*
**Notions :**
- ⬜ TF-IDF
- ⬜ BM25
- ⬜ Recherche d'information (dense / lexicale / hybride RRF, re-ranking)
- ⬜ NER & étiquetage de séquence (IOB/BILOU, CRF, Viterbi)
- ⬜ Classification de texte supervisée (baseline → embeddings → LLM)

**Briques (`ml/framework`) :**
- ⬜ spaCy
- ⬜ sentence-transformers
- ⬜ GLiNER (NER zero-shot)
- ⬜ rank-bm25
- ⬜ pytorch-crf
- ⬜ SetFit

## 3. Détection d'outliers & anomalies → « Machine Learning »
*sources : Detection_Outliers, TS_Maintenance_Predictive*
**Notions :**
- ⬜ Détection d'outliers — univarié (Z-score, IQR, MAD)
- ⬜ Détection d'outliers — multivarié (LOF, Isolation Forest, Elliptic Envelope, ECOD/COPOD)
- ⬜ Détection d'anomalies en séries temporelles (matrix profile)

**Briques (`ml/framework`) :**
- ⬜ PyOD
- ⬜ STUMPY

## 4. Explicabilité / interprétabilité → « Machine Learning » (`ml/interpretabilite`)
*source : ML_Explication_Feature_Importance_Selection (+ SHAP dans DL_TensorFlow, ML_Bagging_Boosting)*
**Notion :**
- ⬜ Explicabilité des modèles (SHAP, LIME, permutation importance, MDI, drop-column, Boruta)

**Briques (`ml/framework`) :**
- ⬜ SHAP
- ⬜ LIME

## 5. Frameworks & libs ML manquants → `ml/framework` (+ `ml/apprentissage-profond`)
*sources : DL_Keras, DL_KAN, ML_Apprentissage_par_Renforcement, ML_Optimisation_de_Modeles, TS_ARIMA*
- ⬜ Keras (Keras 3, multi-backend) → `ml/framework`
- ⬜ PyTorch Lightning → `ml/framework`
- ⬜ Stable-Baselines3 → `ml/framework` (RL)
- ⬜ Gymnasium → `ml/framework` (RL, environnements)
- ⬜ imbalanced-learn → `ml/framework`
- ⬜ Boruta → `ml/framework` (sélection de variables)
- ⬜ River → `ml/framework` (ML en ligne / streaming)
- ⬜ pmdarima → `ml/framework` (AutoARIMA)
- ⬜ **KAN — Kolmogorov-Arnold Networks** → notion, `ml/apprentissage-profond`

## 6. Compléments — sous-domaines existants
**`ml/socle`** *(sources : ML_Regression_Classification_Multiple, Test_donnees_manquante_modeles)*
- ⬜ Régression / classification multi-sorties (MultiOutput, RegressorChain)
- ⬜ Mécanismes de données manquantes (MCAR / MAR / MNAR) + imputation avancée (KNNImputer, IterativeImputer/MICE) — complète *Imputation des valeurs manquantes*

**`stats/exploratoire`** *(source : EDA_Analyse_Multivarie)*
- ⬜ MANOVA / tests multivariés
- ⬜ Manifold learning (Isomap, LLE, Kernel PCA) — complète *Réduction de dimension*

**`ml/series-temporelles`** *(sources : TS_Maintenance_Predictive, TS_Time_Series_Overview)*
- ⬜ Maintenance prédictive / RUL (remaining useful life)
- ⬜ Foundation models pour séries temporelles (panorama)

**`framework/backend`** *(source : Flask_API)*
- ⬜ Flask *(à confirmer : peut déjà être cité en alternative de FastAPI)*

---

## Récap
- **~35 nouvelles pages**. Les deux sous-domaines qui étaient « à créer » existent depuis :
  `signal/traitement` et `ml/nlp` portent chacun un dossier de l'arbre. La question de les
  rabattre sur les mathématiques ou sur le LLM est donc close.
- Décision à trancher avant de lancer les rounds : élaguer d'éventuels clusters non voulus.
- Ensuite : mêmes prompts / même boucle que pour le réservoir v1 (plan → GO → drainer → check_brain → commit/push/merge).
