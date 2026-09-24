U01.LAB02 · Documentation and Results Summary
Installation
The project requires Python and the dependencies listed in requirements.txt.

In Google Colab, the UCI data-access dependency can be installed with:

%pip install -q ucimlrepo

The main project dependencies include:

pandas
scikit-learn
matplotlib
joblib
pytest
ucimlrepo
Reproducible Dataset Access
The dataset is retrieved programmatically through the official UCI Machine Learning Repository API using dataset ID 329.

The reusable download procedure is implemented in:

data/data.py

The downloaded predictors and target are combined and saved as:

data/raw/dataset.csv

This procedure avoids using a personal Google Drive path as the only data source and allows another user to reproduce the dataset locally.

Dataset Source and License
Dataset: Diabetic Retinopathy Debrecen
Repository: UCI Machine Learning Repository
Documentation: https://archive.ics.uci.edu/dataset/329/diabetic+retinopathy+debrecen
UCI Dataset ID: 329
Authors: Bálint Antal and András Hajdu
Donation Date: November 2014
Instances: 1,151
Predictors: 19
Missing Values: None reported
License: A specific license is not explicitly displayed in the reviewed UCI metadata. Reuse and redistribution conditions should therefore be verified before publishing the raw dataset.
Unit of Analysis
Each observation represents a retinal image described through numerical features produced by image-processing and lesion-detection methods.

Target
The target variable is Class.

0: No signs of diabetic retinopathy
1: Signs of diabetic retinopathy
The experiment is a supervised binary-classification task.

Leakage Controls
The following variables were excluded from the predictor matrix:

pre_screening
am_fm_classification
These variables contain previous screening or automated-classification results that may be closely associated with the target and could produce an overoptimistic estimate of model performance.

Data Dictionary Summary
The predictors include:

quality: Image-quality assessment result.
ma1 to ma6: Microaneurysm-detection results at different confidence levels.
exudate1 to exudate8: Normalized exudate-related measurements.
macula_opticdisc_distance: Normalized distance between the macula and optic disc.
opticdisc_diameter: Optic-disc diameter.
Class: Binary target indicating the presence or absence of diabetic-retinopathy signs.
The complete variable descriptions are available in the UCI dataset documentation.

Evaluation Metric
The primary evaluation metric is F1-Macro because it assigns equal importance to both target classes.

Positive-class recall is also emphasized because false negatives represent the most costly error in this academic screening scenario.

Execution Summary
The notebook performs the following workflow:

Downloads the dataset reproducibly through the UCI API.
Saves a standardized CSV copy in data/raw/.
Audits dimensions, data types, missing values, unique values, and duplicates.
Defines the target and removes potential leakage variables.
Creates preprocessing inside a Scikit-learn pipeline.
Produces a stratified 80/20 training and test split.
Trains a DummyClassifier baseline.
Trains an RBF-kernel SVM.
Compares both models using F1-Macro.
Executes automated dataset-contract tests.
Test Results
The dataset contract was validated with three automated tests:

Dataset is not empty: Passed
Required columns exist: Passed
Target has no missing values and at least two classes: Passed
Final result: 3 passed in 0.67 seconds

Conclusion
The U01.LAB02 workflow successfully adapted the reproducible methodology established in LAB01 to a new publicly documented dataset. The Diabetic Retinopathy Debrecen dataset was retrieved through the official UCI API and stored in a standardized project-relative location. This approach avoids dependence on personal Google Drive paths and improves the reproducibility of the experiment.

The dataset audit confirmed 1,151 observations, a binary target, numerical predictors, and no missing values. Two variables, pre_screening and am_fm_classification, were excluded because both represent previous screening or automated-classification results that may contain information closely associated with the final target. Their exclusion was based on semantic and availability considerations rather than their effect on model performance.

The DummyClassifier baseline obtained an F1-Macro score of 0.3475, while the RBF SVM obtained an F1-Macro score of 0.6921. The improvement of 0.3446 demonstrates that the retained image-derived variables contain meaningful predictive information beyond the majority-class distribution.

The SVM achieved an accuracy of 0.6926. For the positive class, the model obtained a precision of 0.7653, recall of 0.6098,

Final Verification Checklist
The following verification confirms that the U01.LAB01 and U01.LAB02 guided workflows satisfy the technical and reproducibility requirements established for Exercise 01.

Dataset Selection
The selected dataset satisfies the minimum acceptance criteria.
The dataset contains more than 500 observations.
The target is observable and contains at least two classes.
The dataset source and documentation are publicly available.
Confirmation that the dataset has not been selected by another student remains pending.
Reproducible Data Access
The dataset is retrieved through the official UCI API using the ucimlrepo package.
The download process is encapsulated in data/data.py.
The standardized dataset is saved as data/raw/dataset.csv.
The download does not depend on a personal Google Drive path.
The dataset can be reproduced using its official UCI identifier, 329.
Target and Unit of Analysis
The unit of analysis is an individual retinal image represented through numerical image-derived features.
The target variable is Class.
The target contains two classes:
0: No signs of diabetic retinopathy
1: Signs of diabetic retinopathy
The target contains no missing values.
Identifiers and Leakage Controls
No patient identifier was included as a predictor.
The target was removed from the predictor matrix.
The pre_screening variable was excluded because it contains a previous screening result closely associated with the target.
The am_fm_classification variable was excluded because it contains a previous automated-classification result.
Feature exclusions were based on semantic and availability considerations rather than their effect on model performance.
Preprocessing and Modeling
Numerical and categorical predictors were identified programmatically.
Missing-value imputation was defined inside the preprocessing pipeline.
Numerical scaling was performed with StandardScaler.
Categorical encoding was included for reproducibility, although no categorical predictors were identified in the selected feature matrix.
All preprocessing operations remained inside a Scikit-learn Pipeline.
The DummyClassifier and SVM used the same stratified train-test split.
The split was reproduced using random_state=42.
The primary comparison metric was F1-Macro.
Model Results
Dummy baseline F1-Macro: 0.3475
SVM F1-Macro: 0.6921
SVM accuracy: 0.6926
Positive-class recall: 0.6098
The SVM substantially outperformed the majority-class baseline.
False negatives were identified as the principal model limitation.
Automated Tests
The dataset is not empty.
Required columns exist.
The target contains no missing values.
The target contains at least two classes.
All three dataset-contract tests passed successfully.
Test result: 3 passed in 0.67 seconds

Documentation and Version Control
The dataset profile and candidate comparison were documented.
Dataset provenance and license-verification status were recorded.
A summary data dictionary was included.
The notebook documents the complete guided workflow.
Model results and limitations were interpreted.
A conclusion of 300 to 500 words was included.
The repository contains meaningful commits for LAB01 and LAB02.
Reproducible source code, tests, and documentation are version controlled.
Final Status
U01.LAB01 and U01.LAB02 have produced the required evidence for Exercise 01.

The guided baseline, public dataset selection, reproducible data access, dataset audit, leakage controls, preprocessing pipeline, baseline comparison, SVM evaluation, automated tests, and documentation have been completed.

The only remaining administrative verification is confirmation that the selected dataset has not been assigned to another student.

Reproduction Instructions
1. Clone the Repository
git clone https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git
2. Enter the Exercise Directory
cd INF-8239-Ciencia-de-Datos-II/Unit_01_Advanced_Data_Analysis/Exercise_01_Reproducible_SVM
All subsequent commands must be executed from this directory.

3. Install the Dependencies
python -m pip install -r requirements.txt
If the UCI package is not installed, run:

python -m pip install ucimlrepo
4. Open the LAB02 Notebook
The principal LAB02 notebook is located at:

notebooks/U01.LAB02.ipynb
Open the notebook in Google Colab or Jupyter Notebook and execute all cells in order.

5. Reproduce the Dataset Download
The dataset-access functions are located at:

data/data.py
The notebook loads this module and retrieves the Diabetic Retinopathy Debrecen dataset through the official UCI API using dataset ID 329.

The resulting standardized dataset is saved as:

data/raw/dataset.csv
No personal Google Drive path is required to retrieve the dataset.

6. Run the Dataset Contract Tests
From the Exercise 01 directory, execute:

python -m pytest tests/test_data_contract.py -v
Expected result:

3 passed
7. Run the Complete Test Suite
python -m pytest -v
This command executes the available tests for:

Environment configuration
Dataset access
Dataset contract
Leakage controls
Model construction
Preprocessing
Pipeline integrity
8. Expected LAB02 Results
A successful execution should reproduce approximately:

Dataset shape:             (1151, 20)
Training predictors:       (920, 17)
Test predictors:           (231, 17)
Dummy baseline F1-Macro:   0.3475
SVM F1-Macro:              0.6921
SVM accuracy:              0.6926
Positive-class recall:     0.6098
Dataset contract tests:    3 passed
Small differences may occur when using different Python or dependency versions.
