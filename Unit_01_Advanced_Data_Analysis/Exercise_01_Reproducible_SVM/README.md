# Exercise 01: Reproducible SVM Classification Workflow

## INF-8239 · Data Science II

### Unit 01: Advanced Models, Dimensionality Reduction, and Green AI

---

## Overview

This project integrates the guided workflows developed in **U01.LAB01** and
**U01.LAB02**.

The objective is to demonstrate a reproducible supervised-classification
workflow that includes:

- Dataset selection and documentation
- Reproducible public-data access
- Dataset auditing
- Target and leakage analysis
- Leakage-safe preprocessing
- Baseline comparison
- Support Vector Machine classification
- Hyperparameter experimentation
- Automated testing
- Model-performance interpretation
- Version-controlled documentation

The project begins with the Breast Cancer Wisconsin dataset as the common
LAB01 baseline and then adapts the workflow to the publicly documented
Diabetic Retinopathy Debrecen dataset in LAB02.

---

# 1. Laboratory Components

## U01.LAB01: SVM Pipeline, Search, and Evaluation

LAB01 establishes the common reproducible baseline using:

- Breast Cancer Wisconsin dataset
- `DummyClassifier`
- `StandardScaler`
- RBF Support Vector Machine
- `GridSearchCV`
- Stratified cross-validation
- F1-Macro
- ROC-AUC
- Classification report
- Confusion matrix
- Reusable model-building functions
- Automated model tests

## U01.LAB02: Public Dataset Selection and Audit

LAB02 adapts the LAB01 workflow to a new public dataset through:

- Comparison of two documented dataset candidates
- Dataset acceptance criteria
- Reproducible UCI API access
- Schema recognition
- Missing-value and duplicate auditing
- Target definition
- Leakage-risk analysis
- Mixed-type preprocessing
- Baseline and SVM comparison
- Dataset-contract tests
- Reproducibility documentation

---

# 2. Analytical Question

The principal analytical question is:

> Can a leakage-controlled SVM pipeline identify numerical patterns associated
> with signs of diabetic retinopathy and substantially outperform a
> majority-class baseline?

The experiment also evaluates whether the selected predictors provide useful
information after excluding variables that contain previous screening or
automated-classification results.

---

# 3. Selected Dataset

## Diabetic Retinopathy Debrecen

- **Repository:** UCI Machine Learning Repository
- **UCI Dataset ID:** `329`
- **Documentation:**  
  https://archive.ics.uci.edu/dataset/329/diabetic+retinopathy+debrecen
- **Authors:** Bálint Antal and András Hajdu
- **Donation Date:** November 2014
- **Instances:** 1,151
- **Original Predictors:** 19
- **Target:** `Class`
- **Task:** Supervised Binary Classification
- **Missing Values:** None reported

The dataset contains numerical features extracted from retinal images. The
project does not process the original retinal images directly.

## License Note

A specific dataset license was not explicitly displayed in the reviewed UCI
metadata. The conditions for reuse and redistribution should therefore be
verified before independently publishing the original raw data.

---

# 4. Unit of Analysis

The unit of analysis is:

> An individual retinal image represented through numerical features obtained
> from image-processing and lesion-detection procedures.

Each row corresponds to one observation represented through image-derived
measurements.

---

# 5. Target Definition

The target variable is:

```text
Class
```

The target classes are:

- `0`: No signs of diabetic retinopathy
- `1`: Signs of diabetic retinopathy

The target contains no missing values and has two observable classes.

---

# 6. Error Priority

The most costly error is a **false negative**.

A false negative occurs when an observation containing signs of diabetic
retinopathy is classified as negative.

For this reason, the evaluation considers:

- F1-Macro
- Positive-class recall
- Precision
- Accuracy
- Classification errors
- Approximate number of false negatives

Overall accuracy is not used as the only model-selection criterion.

---

# 7. Dataset Candidates

Two public datasets were evaluated during LAB02:

1. Diabetic Retinopathy Debrecen
2. Dry Bean

The comparison considered:

- Public documentation
- Number of observations
- Number and type of predictors
- Target definition
- Number of classes
- Missing values
- SVM compatibility
- Computational feasibility
- Potential target leakage

The formal comparison is documented in:

```text
docs/dataset_profile.md
```

Additional comparison evidence is located in:

```text
reports/dataset_comparison.md
```

Diabetic Retinopathy Debrecen was selected because it provides:

- A clearly defined binary target
- Numerical variables compatible with SVM
- No reported missing values
- Manageable computational requirements
- A meaningful opportunity to audit and control target leakage
- Direct compatibility with the evaluation structure established in LAB01

---

# 8. Repository Structure

```text
Exercise_01_Reproducible_SVM/
├── data/
│   ├── data.py
│   └── raw/
│       └── dataset.csv
├── docs/
│   └── dataset_profile.md
├── notebooks/
│   ├── 00_verificacion.ipynb
│   ├── 01_svm_guiada.ipynb
│   ├── U01.01_reproducible.ipynb
│   └── U01.LAB02.ipynb
├── reports/
│   ├── dataset_comparison.md
│   └── figures/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── environment.py
│   ├── models.py
│   ├── preprocessing.py
│   └── svm_pipeline.py
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_data_contract.py
│   ├── test_environment.py
│   ├── test_leakage.py
│   ├── test_models.py
│   └── test_pipeline.py
├── README.md
└── requirements.txt
```

---

# 9. Requirements

The project requires:

- Python 3.11 or later
- Git
- Jupyter Notebook or Google Colab
- Internet access for the initial dataset download

The principal Python dependencies include:

- pandas
- numpy
- scikit-learn
- matplotlib
- joblib
- pytest
- ucimlrepo

---

# 10. Reproduction Instructions

The recommended method for reproducing Exercise 01 is to use the public
submission notebook in Google Colab.

The reproducible notebook already contains the required setup cells, data
download procedure, LAB01 baseline, LAB02 adaptation, automated tests, results,
and conclusions.

The reviewer does not need to recreate the notebook manually.

## 10.1 Open the Reproducible Notebook

Open the following link in a web browser:

https://colab.research.google.com/github/pascual-francisco/INF-8239-Ciencia-de-Datos-II/blob/main/Unit_01_Advanced_Data_Analysis/Exercise_01_Reproducible_SVM/notebooks/U01.01_reproducible.ipynb

Google Colab will open the public notebook stored in the GitHub repository.

The following options may appear at the top of Google Colab:

```text
Run all
Copy to Drive
Save in GitHub to keep changes
```

To reproduce the experiment, select:

```text
Runtime > Run all
```

The reviewer does not need to select `Copy to Drive` or
`Save in GitHub to keep changes`.

Creating a personal Google Drive copy is optional and does not modify the
original repository.

## 10.2 Clone the Public Repository

The first notebook cell clones a temporary copy of the public repository into
the Google Colab virtual machine.

```bash
%%bash

# ==============================================================================
# CELL 1: CLONE THE PUBLIC PROJECT REPOSITORY
#
# Objective:
# 1. Clone the public GitHub repository into the Google Colab virtual machine.
# 2. Make the source code, tests, documentation, and configuration files
#    available for the reproducible execution of Exercise 01.
# 3. Skip cloning if the repository already exists in the current runtime.
#
# Important:
# - No Google Drive connection is required.
# - No GitHub token is required.
# - No collaborator access is required.
# - This notebook does not perform commit, tag, or push operations.
# ==============================================================================

REPO_DIR="/content/INF-8239-Ciencia-de-Datos-II"
REPO_URL="https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git"

if [ -d "$REPO_DIR/.git" ]; then
    echo "Repository already exists in the current Colab runtime."
    echo "Clone operation skipped."
    echo "Repository path: $REPO_DIR"
else
    cd /content || exit 1

    echo "Cloning the public repository..."
    git clone "$REPO_URL"

    echo "Repository cloned successfully."
    echo "Repository path: $REPO_DIR"
fi
```

Expected output in a new runtime:

```text
Cloning the public repository...
Cloning into 'INF-8239-Ciencia-de-Datos-II'...
Repository cloned successfully.
Repository path: /content/INF-8239-Ciencia-de-Datos-II
```

The repository is public, so no username, password, or GitHub token is
required.

## 10.3 Set the Project Working Directory

The second notebook cell moves the Colab session to the Exercise 01 project
directory.

```python
# ===

# 11. Reproducible Dataset Access

The dataset-access functions are implemented in:

```text
data/data.py
```

The function:

```python
download_uci_dataset()
```

performs the following operations:

1. Connects to the official UCI data-access service.
2. Retrieves dataset ID `329`.
3. Obtains the predictors and target.
4. Combines both components into one DataFrame.
5. Verifies that the downloaded dataset is not empty.
6. Creates the local raw-data directory when necessary.
7. Saves a standardized CSV copy.

The generated file is:

```text
data/raw/dataset.csv
```

The dataset-download process does not depend on Google Drive, a local Windows
directory, or private credentials.

---

# 12. Running the Notebooks

## Environment Verification

Open and execute:

```text
notebooks/00_verificacion.ipynb
```

This notebook verifies the Python environment and principal project
dependencies.

## LAB01 Baseline

Open and execute:

```text
notebooks/01_svm_guiada.ipynb
```

This notebook reproduces the original guided SVM baseline, hyperparameter
search, and evaluation workflow.

## LAB02 Adaptation

Open and execute:

```text
notebooks/U01.LAB02.ipynb
```

Execute every cell in order, starting from the environment and data-access
cells and ending with the final verification checklist.

## Google Colab

When using Google Colab:

1. Start a clean Colab runtime.
2. Clone the public GitHub repository.
3. Enter the Exercise 01 directory.
4. Install `requirements.txt`.
5. Open the required notebook.
6. Execute all cells in order.

Google Drive is not required for dataset access, modeling, testing, or report
generation.

---

# 13. Dataset Audit

LAB02 audits:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Missing-value percentages
- Unique values
- Fully duplicated rows
- Target distribution
- Numerical variables
- Categorical variables
- Potential leakage features

The reproduced dataset contains:

```text
Rows:    1,151
Columns: 20
```

This includes:

- 19 original predictors
- 1 binary target

No rows or columns are excluded solely because they reduce model performance.

---

# 14. Leakage Controls

The following variables are excluded from the predictor matrix:

```text
pre_screening
am_fm_classification
```

## Justification

### `pre_screening`

This variable contains the result of a previous retinal-abnormality
pre-screening process.

### `am_fm_classification`

This variable contains the output of a previous automated-classification
method.

Both variables may contain information closely associated with the final
target. Their inclusion could produce an overly optimistic estimate of model
performance.

The exclusions are based on semantic meaning and information availability, not
on their effect on the final metric.

After these exclusions, the model uses:

```text
17 predictors
```

---

# 15. Data Dictionary Summary

The principal variable groups include:

- `quality`: Image-quality assessment
- `ma1` to `ma6`: Microaneurysm-detection measurements at different confidence levels
- `exudate1` to `exudate8`: Normalized exudate-related measurements
- `macula_opticdisc_distance`: Normalized distance between the macula and optic disc
- `opticdisc_diameter`: Optic-disc diameter
- `pre_screening`: Previous screening result, excluded
- `am_fm_classification`: Previous automated-classification result, excluded
- `Class`: Binary target

Complete variable descriptions are available in the UCI dataset documentation
and the project dataset profile.

---

# 16. Preprocessing

All preprocessing operations are contained inside Scikit-learn pipelines.

## Numerical Variables

Numerical predictors are processed with:

```text
SimpleImputer(strategy="median")
                    ↓
StandardScaler()
```

Although the dataset contains no reported missing values, median imputation is
included to make the pipeline robust and reusable.

## Categorical Variables

The reusable preprocessing structure includes:

```text
SimpleImputer(strategy="most_frequent")
                    ↓
OneHotEncoder(handle_unknown="ignore")
```

No categorical predictors were identified in the final predictor matrix, but
the categorical pipeline remains defined for consistency and future reuse.

Keeping preprocessing inside the pipeline prevents training information from
leaking into validation or test data.

---

# 17. Train-Test Protocol

The dataset uses a reproducible stratified train-test split:

- **Training:** 80%
- **Test:** 20%
- **Random state:** `42`
- **Stratification:** Target variable

Resulting dimensions:

```text
Training predictors: (920, 17)
Test predictors:     (231, 17)
Training target:     (920,)
Test target:         (231,)
```

The baseline and SVM use exactly the same partition.

---

# 18. Baseline Model

The reference model is:

```python
DummyClassifier(strategy="most_frequent")
```

The baseline always predicts the most frequent target class.

The baseline provides a minimum reference for determining whether the SVM
learns useful patterns beyond the target-class distribution.

The baseline and SVM share:

- The same predictor matrix
- The same preprocessing
- The same training observations
- The same test observations
- The same evaluation metric

---

# 19. SVM Model

The LAB02 SVM configuration is:

```python
SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    probability=True,
    random_state=42
)
```

The complete workflow is:

```text
Predictor Matrix
       ↓
ColumnTransformer
       ↓
Numerical Preprocessing
       ↓
StandardScaler
       ↓
RBF SVM
       ↓
Binary Prediction
```

---

# 20. Evaluation Metric

The primary evaluation metric is:

```text
F1-Macro
```

F1-Macro calculates the F1-score independently for each target class and then
computes their unweighted average.

The analysis also reviews:

- Accuracy
- Precision
- Recall
- Class-specific F1-score
- Number of observations per class
- False-negative implications

Positive-class recall receives particular attention because false negatives
represent the most costly error in the defined scenario.

---

# 21. LAB02 Results

## Dummy Baseline

```text
F1-Macro: 0.3475
```

## RBF SVM

```text
F1-Macro:                0.6921
Accuracy:                0.6926
Positive-class precision: 0.7653
Positive-class recall:    0.6098
Positive-class F1-score:  0.6787
```

## Performance Improvement

The absolute F1-Macro improvement over the baseline is:

```text
0.6921 - 0.3475 = 0.3446
```

The SVM improved F1-Macro by approximately 34.46 percentage points over the
majority-class baseline.

The positive-class recall of `0.6098` indicates that approximately 60.98% of
the positive observations were detected.

Approximately 39.02% of positive observations remained undetected. Based on
the test-set support, this represents approximately 48 false negatives.

---

# 22. Automated Tests

## Dataset Contract Tests

Run:

```bash
python -m pytest tests/test_data_contract.py -v
```

Expected result:

```text
tests/test_data_contract.py::test_dataset_is_not_empty PASSED
tests/test_data_contract.py::test_required_columns_exist PASSED
tests/test_data_contract.py::test_target_has_no_missing_and_two_classes PASSED

3 passed
```

These tests verify that:

1. The dataset is not empty.
2. Required columns exist.
3. The target contains no missing values.
4. The target contains at least two classes.

## Complete Test Suite

Run:

```bash
python -m pytest -v
```

The complete test suite includes checks related to:

- Environment configuration
- Dataset access
- Dataset contract
- Leakage controls
- Model construction
- Preprocessing
- Pipeline integrity

---

# 23. Expected Reproduction Results

A successful reproduction should generate approximately:

```text
Dataset shape:               (1151, 20)
Training predictors:         (920, 17)
Test predictors:             (231, 17)
Dummy baseline F1-Macro:     0.3475
SVM F1-Macro:                0.6921
SVM accuracy:                0.6926
Positive-class recall:       0.6098
Dataset contract tests:      3 passed
```

Small timing differences may occur across operating systems, Python versions,
dependency versions, and hardware environments.

---

# 24. Reproducibility Checklist

A reproduction is considered successful when another user can:

- [ ] Clone the public repository without authentication.
- [ ] Enter the Exercise 01 directory.
- [ ] Install dependencies from `requirements.txt`.
- [ ] Execute the notebooks without mounting Google Drive.
- [ ] Download dataset ID `329` from UCI.
- [ ] Generate `data/raw/dataset.csv`.
- [ ] Confirm a dataset shape of `(1151, 20)`.
- [ ] Reproduce the target and leakage exclusions.
- [ ] Recreate the stratified train-test split.
- [ ] Train both the Dummy baseline and SVM.
- [ ] Obtain results consistent with the documented metrics.
- [ ] Execute the dataset-contract tests.
- [ ] Obtain three passing contract tests.

---

# 25. Limitations

The current experiment has several limitations:

- The dataset contains extracted numerical features instead of the original
  retinal images.
- The model was evaluated using one stratified holdout test set.
- External validation was not performed.
- The current SVM configuration was not optimized specifically for
  positive-class recall.
- A meaningful proportion of positive observations remained undetected.
- The experiment does not establish clinical effectiveness.
- Dependency and hardware differences may produce small variations in results.
- Dataset reuse conditions should be verified before redistributing the raw
  file.

---

# 26. Recommended Next Step

The next experiment should compare controlled model adaptations using the same:

- Dataset
- Target
- Leakage exclusions
- Training and test partition
- Random seed
- Primary metric
- Priority class

Potential adaptations include:

- Class weighting
- Hyperparameter optimization
- Feature selection
- Decision-threshold analysis
- Logistic Regression
- Random Forest
- Gradient Boosting
- Principal Component Analysis
- Computational-cost comparison

Any selected model should be justified using predictive performance and
computational cost rather than overall accuracy alone.

---

# 27. Conclusion

The Exercise 01 workflow successfully combined the guided LAB01 SVM baseline
with the LAB02 public-dataset adaptation. The project established a
reproducible process for selecting, downloading, auditing, preprocessing, and
modeling a publicly documented dataset.

The Diabetic Retinopathy Debrecen dataset was retrieved through the official
UCI data-access package and stored in a standardized project-relative
location. This procedure eliminates dependence on private Google Drive paths
and allows another user to reconstruct the local CSV file from the documented
public source.

The audit confirmed 1,151 observations, numerical predictors, a binary target,
and no reported missing values. The `pre_screening` and
`am_fm_classification` variables were excluded because they represent previous
screening or automated-classification outcomes that may contain information
closely associated with the target. These exclusions were based on semantic
and availability considerations rather than metric optimization.

The DummyClassifier obtained an F1-Macro score of `0.3475`, while the RBF SVM
achieved `0.6921`. The absolute improvement of `0.3446` indicates that the
retained image-derived predictors contain meaningful classification
information beyond the majority-class distribution.

The SVM achieved an accuracy of `0.6926`. For the positive class, the model
obtained a precision of `0.7653`, recall of `0.6098`, and F1-score of `0.6787`.
Although the SVM clearly outperformed the baseline, approximately 39.02% of
positive observations remained undetected. This result highlights the
importance of evaluating class-specific errors instead of selecting a model
based only on accuracy.

A subsequent experiment should investigate whether controlled model
adaptations can improve positive-class recall or preserve comparable
performance with lower computational cost. The same dataset, target,
exclusions, split, and evaluation protocol should be maintained to ensure a
fair comparison.

---

# Academic Use Disclaimer

This project is intended exclusively for academic experimentation.

The resulting model does not constitute a medical diagnosis and must not
replace evaluation by a qualified healthcare professional.
