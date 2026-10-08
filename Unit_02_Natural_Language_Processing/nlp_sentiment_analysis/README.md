# Exercise 03: Spanish Sentiment Corpus Audit and Text Classification

**Course:** INF-8239 Data Science II  
**Unit:** 02 · Natural Language Processing, Networks, and Vision  
**Student:** Francisco Pascual  
**Integrated laboratories:** U02.LAB04 and U02.LAB05  
**Project version:** 1.7.0  

**Repository:**  
https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II

**Project directory:**

```text
Unit_02_Natural_Language_Processing/nlp_sentiment_analysis/
```

---

## 1. Project Overview

Exercise 03 integrates the evidence produced in U02.LAB04 and U02.LAB05 into an executable, reproducible, and explainable text-classification project.

U02.LAB04 covered:

- Public corpus selection.
- License and provenance verification.
- Dataset download and SHA-256 verification.
- Text reconstruction from an encoded representation.
- Dataset auditing.
- Data-contract testing.
- Creation of a processed three-class dataset.

U02.LAB05 continued with:

- TF-IDF feature extraction.
- A `DummyClassifier` baseline.
- Complement Naive Bayes.
- Logistic Regression.
- Model comparison using macro F1-score.
- Per-class evaluation.
- Confusion-matrix interpretation.
- Classification error analysis.
- Model persistence with Joblib.
- Automated model tests.
- A local Streamlit application.
- Cloud-portability verification.

---

## 2. Research Question

> Can a Natural Language Processing model classify Spanish-language Twitter texts as negative, neutral, or positive?

The conclusions are limited to the language, period, source, and population represented by the selected corpus.

The results do not demonstrate equivalent performance for:

- Every type of Spanish-language text.
- Every Spanish-speaking region.
- Current social-media language.
- Formal documents.
- Technical or medical text.
- Domains not represented by the training corpus.

---

## 3. Repository Structure

```text
nlp_sentiment_analysis/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── sample/
│       └── demo_text.csv
├── docs/
│   ├── DATASET_CARD.md
│   ├── dataset_candidates.csv
│   └── data_dictionary.md
├── models/
│   └── text_model.joblib
├── notebooks/
│   └── [EXECUTED_NOTEBOOK_NAME].ipynb
├── reports/
│   ├── confusion_text.png
│   ├── error_analysis.csv
│   └── text_metrics.csv
├── scripts/
│   ├── audit_data.py
│   ├── download_data.py
│   ├── embeddings_network.py
│   └── train_text.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data.py
│   └── modeling.py
├── test/
│   ├── test_data_contract.py
│   ├── test_embeddings_network.py
│   └── test_text_model.py
├── .env.example
├── pyproject.toml
├── requirements-cloud.txt
└── uv.lock
```

Large downloaded and generated datasets are not stored in Git. The `data/raw/` and `data/processed/` directory structures are preserved through `.gitkeep` files.

---

## 4. Dataset Selection and Provenance

### 4.1 Approved Corpus

The selected corpus was:

**Spanish Tweet Datasets Encoded for Sentiment Analysis Based on Context of Words**

The dataset was published through the Universidad de Alcalá institutional repository.

- **Version:** 1.0
- **DOI:** `10.21950/XEV9IC`
- **License:** Creative Commons Attribution 4.0 (`CC BY 4.0`)
- **Language:** Spanish
- **Source:** Twitter
- **Downloaded archive:** `Data.zip`
- **SHA-256:**

```text
42709113f5b10ef421ad0b900f6b836f28fa02073ca3d0869edb689bc9c825d2
```

### 4.2 Selection Criteria

| Criterion | Evaluation |
|---|---|
| Relevance | Contains Spanish-language texts and sentiment labels compatible with the research question. |
| License | CC BY 4.0 permits analysis and the publication of derived results with attribution. |
| Representativeness | Primarily represents historical Twitter language, not the complete Spanish-speaking population. |
| Quality | Contains class imbalance, duplicated texts, no-opinion records, and evaluation records without disclosed labels. |
| Reproducibility | Provides a DOI, version, institutional source, and a downloadable archive that can be identified through SHA-256. |
| Risk | May include mentions, informal language, sensitive opinions, offensive language, or potentially identifiable references. |

### 4.3 Rejected Candidate

`TwitterSentimentDataset` was also evaluated.

This candidate was rejected because its `unclassified` group could not be reliably interpreted as neutral sentiment. The absence of emoticons does not prove that a text expresses neutral sentiment.

### 4.4 Approval Decision

> **Approved with conditions.**

The `NONE` category was excluded because absence of opinion is not equivalent to neutral sentiment.

Evaluation records without disclosed labels were also excluded from supervised model training.

---

## 5. Corpus Reconstruction

The original corpus was not distributed as a conventional CSV file containing `text` and `label` columns.

The information was stored across multiple encoded files:

- `words_cod.txt`: relationship between words and numerical identifiers.
- `reviews_cod.txt`: encoded word sequences and contextual features.
- `reviews_tw_definitivo.txt`: review identifiers, dataset partitions, and label codes.
- `readme.txt`: documentation of the internal format.

Each text was reconstructed by:

1. Reading the first field of each encoded word row, called `id_Dict`.
2. Mapping the identifier to its corresponding word.
3. Preserving the original word order.
4. Joining tokens until the `%%` review separator was found.

### 5.1 Label Mapping

| Code | Interpreted label |
|---:|---|
| 1 | `negative` |
| 2 | `neutral` |
| 3 | `positive` |
| 4 | `none` |
| 5 | `unlabeled` |

Code `5` was not interpreted as a fifth sentiment class.

All 1,899 records with label code `5` belonged to the evaluation partition, indicating that their true sentiment labels were not disclosed.

### 5.2 Reconstruction Result

```text
Metadata records:      63,238
Reconstructed texts:   63,238
```

One identifier was not included in the supplied dictionary:

```text
Reserved identifier:   0
Occurrences:            203,114
```

Identifier `0` was interpreted as a reserved or padding value and was omitted during reconstruction.

This result does not represent 203,114 different unknown words. It represents one reserved identifier repeated 203,114 times.

---

## 6. Dataset Audit

### 6.1 Complete Reconstructed Corpus

| Audit result | Value |
|---|---:|
| Reconstructed records | 63,238 |
| Missing values | 0 |
| Empty texts | 114 |
| Additional duplicated-text occurrences | 1,599 |
| Duplicated text-label pairs | 1,565 |
| Positive texts | 22,356 |
| Negative texts | 16,219 |
| Neutral texts | 1,486 |
| No-opinion texts | 21,278 |
| Records without disclosed labels | 1,899 |

Empty texts were excluded because they cannot produce useful TF-IDF features.

### 6.2 Processed Three-Class Dataset

After excluding empty texts, `none`, and `unlabeled` observations, the modeling dataset contained:

| Class | Observations | Percentage |
|---|---:|---:|
| Positive | 22,340 | 55.79% |
| Negative | 16,219 | 40.50% |
| Neutral | 1,486 | 3.71% |
| **Total** | **40,045** | **100%** |

The processed dataset contained:

```text
Columns: text, label
Missing values: 0
Empty texts: 0
Additional duplicated-text occurrences: 357
```

### 6.3 Duplicate and Leakage Risk

Duplicated texts create a potential information-leakage risk.

If the same text appears in both the training and test partitions, the model may be evaluated using an observation already seen during training. This can artificially improve the reported metrics.

Before a definitive experiment, duplicated texts should be controlled before creating the training and test partitions, or grouped so that identical texts cannot appear in different partitions.

---

## 7. Compared Classification Pipelines

A single stratified split with random seed `42` was used to compare the models.

The TF-IDF vectorizer remained inside every pipeline to prevent the vocabulary and term weights from being learned using test data.

### 7.1 Baseline

```text
TF-IDF → DummyClassifier
```

The `DummyClassifier` establishes the minimum reference performance that a useful model should exceed.

### 7.2 Complement Naive Bayes

```text
TF-IDF → Complement Naive Bayes
```

Complement Naive Bayes was included as a probabilistic text classifier suitable for sparse feature matrices and imbalanced data.

### 7.3 Logistic Regression

```text
TF-IDF → Logistic Regression
```

Logistic Regression learns weights for the TF-IDF features and predicts one of the three sentiment classes.

### 7.4 Selected Model

Logistic Regression obtained the best macro F1-score among the evaluated pipelines and was selected as the final model.

The complete model-comparison results are stored in:

```text
reports/text_metrics.csv
```

The selected pipeline was saved in:

```text
models/text_model.joblib
```

The saved object preserves both:

- The fitted TF-IDF vectorizer.
- The trained classifier.

This allows new texts to be transformed and classified through one reusable pipeline.

---

## 8. Model Evaluation

### 8.1 Confusion Matrix

The confusion matrix is available at:

```text
reports/confusion_text.png
```

reports/confusion_text.png

The rows represent the true classes, while the columns represent the predicted classes.

| True class | Predicted negative | Predicted neutral | Predicted positive |
|---|---:|---:|---:|
| Negative | 3,511 | 196 | 342 |
| Neutral | 197 | 87 | 88 |
| Positive | 722 | 185 | 4,594 |

### 8.2 Correct Predictions

The main diagonal represents correct classifications:

```text
Negative → Negative: 3,511
Neutral  → Neutral:      87
Positive → Positive:  4,594
```

The model generated:

```text
8,192 correct predictions from 9,922 test observations
```

The approximate accuracy was:

```text
82.56%
```

Accuracy was not interpreted independently because the classes were severely imbalanced.

### 8.3 Largest Confusion

The largest off-diagonal cell was:

```text
True positive → Predicted negative: 722
```

In a public-opinion or customer-feedback monitoring system, this error could:

- Overestimate negative sentiment.
- Underestimate satisfaction or approval.
- Present a more negative interpretation of the population.
- Incorrectly prioritize positive comments as potential complaints.

### 8.4 Most Difficult Class

| Class | Approximate recall |
|---|---:|
| Negative | 86.71% |
| Neutral | 23.39% |
| Positive | 83.51% |

Only 87 of the 372 truly neutral texts were classified correctly.

The neutral class also had an approximate precision of:

```text
18.59%
```

When the model predicts `neutral`, the prediction is correct in approximately 19 out of every 100 cases.

This result is consistent with neutral sentiment representing only 3.71% of the processed dataset.

---

## 9. Error Analysis

Classification errors are stored in:

```text
reports/error_analysis.csv
```

At least 20 errors were reviewed using the following categories:

- Negation.
- Irony.
- Ambiguity.
- Dialect.
- Insufficient text.
- Questionable label.
- Out-of-domain topic.
- Mixed sentiment.

The true labels and model predictions were not manually modified.

### 9.1 Manual Review Summary

| Error category | Count |
|---|---:|
| Negation | [COMPLETE] |
| Irony | [COMPLETE] |
| Ambiguity | [COMPLETE] |
| Dialect | [COMPLETE] |
| Insufficient text | [COMPLETE] |
| Questionable label | [COMPLETE] |
| Out of domain | [COMPLETE] |
| Mixed sentiment | [COMPLETE] |

The most frequent error category was:

```text
[COMPLETE WITH THE MOST FREQUENT CATEGORY]
```

The proposed hypothesis for the next experiment is:

> [COMPLETE WITH A TESTABLE HYPOTHESIS BASED ON THE DOMINANT ERROR CATEGORY]

For example, if negation errors predominate, the next experiment can compare a unigram TF-IDF representation against a unigram-and-bigram representation.

---

## 10. Automated Tests and Model Persistence

The automated tests verify that:

- The data contract accepts structurally valid data.
- The data contract rejects missing required columns.
- The data contract rejects empty texts.
- The model pipelines can be created.
- The selected pipeline produces predictions.
- Predictions belong to the expected class vocabulary.
- The saved model preserves its required components.
- The Joblib file can be loaded successfully.

### Run all tests

```bash
uv run pytest -q
```

In Google Colab:

```bash
python -m pytest test -q
```

### Inspect the saved model

```bash
uv run python -c "import joblib; m=joblib.load('models/text_model.joblib'); print(m.predict(['Excelente servicio']))"
```

Automated tests confirm programmed behavior. They do not replace statistical evaluation, confusion-matrix interpretation, or manual error analysis.

---

## 11. Streamlit Application

The local application is located at:

```text
app/streamlit_app.py
```

The interface allows the user to:

- Enter a Spanish-language text.
- Generate a sentiment prediction.
- Display class probabilities when supported.
- Calculate a prediction-uncertainty indicator.
- Warn about low-confidence outputs.
- Explain that the output depends on the training corpus.

The interface presents the label as a **model prediction**, not as an objective fact.

### Run the application

```bash
uv run streamlit run app/streamlit_app.py
```

Alternatively:

```bash
python -m streamlit run app/streamlit_app.py
```

### Functional Test Examples

**Clearly positive**

```text
Excelente servicio, estoy muy satisfecho.
```

**Clearly negative**

```text
El servicio fue terrible y no lo recomiendo.
```

**Ambiguous**

```text
Bueno, pudo haber sido peor.
```

**Potentially neutral**

```text
La reunión comienza mañana a las diez.
```

**Out of domain**

```text
La válvula neumática opera a una presión de seis bares.
```

Ambiguous, potentially neutral, and out-of-domain examples were not assigned mandatory expected classes during functional testing. Their predictions were preserved to document the model limitations honestly.

---

## 12. Installation and Execution

### 12.1 Requirements

- Git.
- Python 3.12 or a compatible version.
- `uv` for local dependency management.

### 12.2 Clone the Repository

```bash
git clone https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git
```

Enter the project directory:

```bash
cd INF-8239-Ciencia-de-Datos-II/Unit_02_Natural_Language_Processing/nlp_sentiment_analysis
```

### 12.3 Synchronize the Environment

```bash
uv sync
```

This installs the dependencies registered in:

```text
pyproject.toml
uv.lock
```

### 12.4 Create the Local Configuration

Copy the environment template:

```bash
cp .env.example .env
```

Example configuration:

```dotenv
DATA_SOURCE=local
DATASET_PATH=data/processed/spanish_tweets_three_class.csv
DATASET_URL=
TEXT_COLUMN=text
TARGET_COLUMN=label
RANDOM_STATE=42
```

The `.env` file contains local configuration and must not be committed to Git.

### 12.5 Download and Prepare the Dataset

Run the download script:

```bash
uv run python scripts/download_data.py
```

Then execute the Exercise 03 notebook to:

1. Verify the downloaded archive.
2. Extract the corpus.
3. Reconstruct the encoded texts.
4. Map the labels.
5. Remove unusable observations.
6. Generate the processed three-class CSV.

Large raw and processed datasets are not stored in Git. They must be downloaded or regenerated by following the repository instructions.

### 12.6 Audit the Processed Dataset

```bash
uv run python scripts/audit_data.py
```

The audit reports:

- File path and SHA-256.
- Rows and columns.
- Missing values.
- Empty texts.
- Duplicated texts.
- Class distribution.
- Text-length statistics.

### 12.7 Run the Tests

```bash
uv run pytest -q
```

### 12.8 Train the Models

```bash
uv run python scripts/train_text.py
```

The training script creates:

```text
reports/text_metrics.csv
reports/confusion_text.png
reports/error_analysis.csv
models/text_model.joblib
```

### 12.9 Run the Application

```bash
uv run streamlit run app/streamlit_app.py
```

Open the local address displayed by Streamlit in a web browser.

---

## 13. Cloud Portability

Cloud-compatible dependencies were exported with:

```bash
uv export --format requirements.txt --output-file requirements-cloud.txt
```

The following conditions were verified:

| Verification | Result |
|---|---|
| Reusable code uses project-relative paths | Passed |
| Saved model exists | Passed |
| Model size is reasonable | 10.43 MB |
| No credentials are embedded in the code | Passed |
| Application does not depend on Google Drive | Passed |
| Application does not depend on a personal directory | Passed |
| Cloud dependency file exists | Passed |
| Streamlit starts in a clean environment | Passed |

### Clean-Environment Verification

A new isolated environment was created outside the repository.

Only the dependencies listed in:

```text
requirements-cloud.txt
```

were installed.

The application was started using the equivalent of:

```text
streamlit run app/streamlit_app.py
```

The Streamlit health endpoint returned:

```text
ok
```

Final result:

```text
PASSED: streamlit run app/streamlit_app.py works in a clean environment.
```

---

## 14. Responsible Use of Artificial Intelligence

Microsoft Copilot was used as a support tool during project development.

### Uses

Microsoft Copilot assisted with:

- Explaining TF-IDF and n-gram concepts.
- Explaining the encoded corpus structure.
- Reviewing import errors and file paths.
- Proposing automated tests.
- Reviewing the dataset audit.
- Interpreting model metrics.
- Interpreting the confusion matrix.
- Reviewing portability procedures.
- Improving project documentation.

### Relevant Prompts

Examples of prompts used include:

- “How is one sentence decoded from the corpus?”
- “Explain the data contract line by line.”
- “Correct the imports to use the `src` package.”
- “Interpret the confusion matrix.”
- “Verify that Streamlit works in a clean environment.”
- “Review the `.gitignore` rules for large files.”

### Verified Components

AI-assisted suggestions were validated through actual execution of:

- Dataset auditing.
- SHA-256 verification.
- Pytest.
- Model training.
- Joblib loading.
- Predictions on new texts.
- Confusion-matrix inspection.
- Streamlit startup.
- Clean-environment dependency installation.
- Git status and ignore-rule inspection.

### Corrections Made

The verified corrections included:

- Replacing `inf8239_u02` imports with `src`.
- Correcting the source-directory name from `scr` to `src`.
- Installing and documenting `gensim`.
- Correcting project paths.
- Excluding large datasets and local secrets with `.gitignore`.
- Interpreting label code `5` as `unlabeled`.
- Interpreting identifier `0` as a reserved value.
- Adjusting the uncertainty-warning threshold.
- Removing temporary Streamlit logs.

The student remains responsible for the data, code, references, metrics, and conclusions.

No predictions, labels, or evaluation results were manually changed to make the model appear more accurate.

---

## 15. Final Decision

The project is executable, reproducible, and portable.

However, the selected model should be presented as an experimental classifier rather than an authoritative sentiment evaluator.

Before public deployment, the following actions are recommended:

1. Control duplicated texts across training and test partitions.
2. Improve neutral-class recall and precision.
3. Complete and document the manual categorization of at least 20 errors.
4. Evaluate bigrams and hyperparameter adjustments.
5. Continue using macro F1-score and per-class recall as primary metrics.
6. Present class probabilities as estimates rather than facts.
7. Preserve clear warnings about the corpus scope and model limitations.

---

## 16. Exercise 03 Evidence

The repository includes:

- Executed notebook.
- Dataset candidate comparison.
- Dataset card.
- Data dictionary.
- Dataset audit.
- SHA-256 verification.
- Reproducible processing workflow.
- Baseline and two comparable classifiers.
- Per-class metrics.
- Confusion matrix.
- Error-analysis file.
- Automated tests.
- Saved model.
- Streamlit application.
- `requirements-cloud.txt`.
- `pyproject.toml`.
- `uv.lock`.
- Git commit history.
- Responsible-AI disclosure.

---

## 17. Rubric Alignment

| Criterion | Repository evidence |
|---|---|
| Dataset selection, license, traceability, and question | Candidate comparison, DOI, license, SHA-256, research question, and approval decision |
| Audit, duplicates, and leakage prevention | Reconstruction, nulls, empty texts, duplicates, class distribution, and partition risk |
| Baseline and two comparable pipelines | DummyClassifier, Complement Naive Bayes, and Logistic Regression with TF-IDF |
| Evaluation and analysis of 20 errors | Macro F1, per-class metrics, confusion matrix, contextual cost, and manual categories |
| Tests, README, Git, and reproducibility | Pytest, reusable code, saved model, Streamlit, clean environment, dependencies, and commit history |
