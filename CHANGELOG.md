# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-09-18

### Unit 01: Advanced Models, Dimensionality Reduction, and Green AI

#### Added
- **Repository Scaffolding:** Modular project architecture for Unit 01 (`LAB00` through `LAB03` and `Exercise_01` to `Exercise_02`).
- **Dependency Management:** Configured baseline `requirements.txt` (`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `joblib`, `pytest`).
- **VCS Rules:** Added `.gitignore` to exclude virtual environments, build artifacts, cache directories, and untracked raw data.
- **Verification Module:** Implemented baseline environment module (`src/environment.py` / `src/inf8239_u01/environment.py`) and corresponding unit tests (`tests/test_environment.py`).
- **Jupyter Verification Notebook:** Generated `notebooks/00_verificacion.ipynb` for kernel validation, interpreter tracking, and platform inspection.
- **Evidence Pipeline:** Established directory layout for visual evidence and execution artifacts (`reports/figures/` and `docs/evidence/`).

#### Validated
- Unit test suite execution verified via `pytest -q` (**1 passed**).
- Local virtual environment reproducibility and clean working tree confirmed (`git status`).
- Successful push and synchronization of baseline state with GitHub remote repository.


## 2026-09-21 - U01.LAB01

### Added
- Completed guided SVM laboratory using the Breast Cancer dataset.
- Implemented a leakage-safe SVM pipeline with StandardScaler and SVC.
- Added DummyClassifier baseline for model comparison.
- Performed hyperparameter tuning with GridSearchCV and StratifiedKFold.
- Evaluated model performance using F1-macro, ROC-AUC, and confusion matrix.
- Added reusable build_svm() function in src/inf8239_u01/models.py.
- Added pytest unit tests for model validation and pipeline structure.
- Saved cross-validation results and trained model artifacts.



## [1.0.0] - 2026-09-21

### Added
- Completed U01.LAB01 guided SVM laboratory.
