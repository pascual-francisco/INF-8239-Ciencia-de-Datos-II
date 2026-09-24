# Changelog

All notable changes to this repository will be documented in this file.

## [1.4.0] - 2026-09-24



### Added
- Added Green AI benchmarking workflow for U01.LAB03.
- Added six model configurations:
  - Logistic Regression
  - SVM (C=1)
  - SVM (C=10)
  - Random Forest (100 trees)
  - Random Forest (300 trees)
  - Histogram Gradient Boosting
- Added PCA dimensionality-reduction analysis.
- Added t-SNE visualizations using two different random seeds.
- Added Pareto frontier analysis for performance-cost trade-off evaluation.
- Added serialized model size and inference-time benchmarking.
- Added automated Pareto validation tests (`tests/test_green.py`).

### Generated
- Generated `reports/green_ai_results.csv`.
- Generated `reports/figures/pareto.png`.
- Generated `reports/figures/tsne_two_seeds.png`.
- Generated serialized model artifacts under `reports/models/`.

### Documentation
- Added Green AI interpretation and model-selection discussion.
- Added execution environment registration for reproducibility.

## [1.3.0] - 2026-09-22
- Added U01.LAB03 notebook

## [1.2.0] - 2026-09-22

### Added
- Completed the U01.LAB02 dataset audit and baseline modeling workflow.
- Defined the `Class` target and removed potential leakage variables.
- Added preprocessing for numerical and categorical features.
- Compared the `DummyClassifier` baseline against the RBF SVM.
- Added automated dataset-contract tests.
- Added dataset documentation, evaluation results, and conclusions.

### Results
- Dummy baseline F1-Macro: `0.3475`
- SVM F1-Macro: `0.6921`
- SVM accuracy: `0.6926`
- Positive-class recall: `0.6098`
- Dataset contract tests: `3 passed`

### Status
- U01.LAB02 guided workflow completed.
- The justified model adaptation and final Exercise 01 comparison remain pending.

## [1.1.0] - 2026-09-22

### Added
- Started U01.LAB02 public dataset search, selection, and audit workflow.
- Created the dataset profile and documented the analytical problem.
- Compared the Diabetic Retinopathy Debrecen and Dry Bean datasets.
- Applied the dataset acceptance criteria to both candidates.
- Documented dataset sources, targets, classes, dimensions, missing values, and potential leakage risks.
- Added reproducible access to the UCI Machine Learning Repository through the `ucimlrepo` API.
- Added the reusable `download_uci_dataset()` function in `data/data.py`.
- Downloaded and standardized the Diabetic Retinopathy Debrecen dataset as `data/raw/dataset.csv`.
- Added `ucimlrepo` to the project dependencies.

### Changed
- Extended the Exercise 01 notebook to preserve LAB01 as the baseline and begin the LAB02 workflow.
- Updated the data-access process to avoid dependence on personal Google Drive paths.

### Documentation
- Added `docs/dataset_profile.md`.
- Documented the preliminary dataset-selection rationale.
- Added an academic-use disclaimer and a preliminary target-leakage assessment.

### Status
- Reproducible dataset access completed.
- Dataset schema audit, target definition, preprocessing, baseline comparison, and automated tests remain in progress.

## [1.0.0] - 2026-09-21

### Added
- Completed U01.LAB01 guided SVM laboratory using the Breast Cancer dataset.
- Implemented a leakage-safe SVM pipeline with StandardScaler and SVC.
- Added a DummyClassifier baseline for model comparison.
- Performed hyperparameter optimization using GridSearchCV and StratifiedKFold.
- Evaluated model performance using F1-Macro, ROC-AUC, classification reports, and confusion matrices.
- Added reusable build_svm() model factory in src/inf8239_u01/models.py.
- Added unit tests for model validation and pipeline integrity in tests/test_models.py.
- Exported cross-validation results and trained model artifacts.

### Deliverables
- notebooks/01_svm_guiada.ipynb
- src/inf8239_u01/models.py
- tests/test_models.py
- reports/svm_cv_results.csv
- reports/svm_best.joblib

## [0.1.0] - 2026-09-18

### Added
- Established the Unit 01 project structure (LAB00-LAB03 and Exercise_01-Exercise_02).
- Configured baseline environment dependencies in requirements.txt.
- Added .gitignore rules for virtual environments, cache directories, build artifacts, and raw datasets.
- Implemented environment verification modules and corresponding unit tests.
- Created the notebook 00_verificacion.ipynb for environment and interpreter validation.
- Established repository structure for reports, figures, and evidence generation.

### Validated
- Verified automated test execution using pytest.
- Confirmed reproducibility through a local virtual environment setup.
- Validated repository synchronization with the remote GitHub repository.
