# Dataset Profile and Candidate Comparison

## Project Context

This document defines and compares two public datasets considered for the
adaptation of the LAB01 SVM pipeline. The final dataset will be selected after
evaluating documentation quality, target definition, computational feasibility,
potential data leakage, and suitability for reproducible experimentation.

---

## Candidate A: Diabetic Retinopathy Debrecen

### Dataset Profile

- Domain: Medical Image Analytics and Ophthalmology.

- Unit of Analysis: An individual retinal image represented through numerical
  features extracted using image-processing methods.

- Supported Decision: Support the preliminary identification of retinal images
  containing signs associated with diabetic retinopathy that may require
  additional professional evaluation.

- Tentative Target: Presence or absence of signs of diabetic retinopathy,
  where `1` indicates that the image contains signs of diabetic retinopathy
  and `0` indicates that no signs were identified.

- Task Type: Supervised Binary Classification.

- Most Costly Error: False Negative, because classifying an image containing
  signs of diabetic retinopathy as negative could delay referral for additional
  professional evaluation.

- End User: Ophthalmology researchers, medical-image analysts,
  screening-program teams, and clinical decision-support professionals.

- Documentation URL:
  https://archive.ics.uci.edu/dataset/329/diabetic+retinopathy+debrecen

- Download URL:
  https://archive.ics.uci.edu/static/public/329/data.csv

### Important Interpretation Note

This dataset contains numerical features extracted from retinal images rather
than the original images. Any model developed with these data is exclusively
for academic experimentation and does not constitute a medical diagnosis.

### Potential Leakage Risk

The `pre_screening` and `am_fm_classification` variables must be audited
carefully because they contain previous screening or automated-classification
results that may be closely associated with the target.

---

## Candidate B: Dry Bean

### Dataset Profile

- Domain: Agricultural Quality and Computer Vision Analytics.

- Unit of Analysis: An individual dry bean grain represented through numerical
  dimensional and shape features extracted from an image.

- Supported Decision: Support the automated identification and sorting of dry
  bean varieties using measurable geometric characteristics.

- Tentative Target: Registered dry bean variety represented by the `Class`
  variable.

- Task Type: Supervised Multiclass Classification.

- Most Costly Error: Misclassifying one registered bean variety as another,
  because incorrect classification may affect sorting, labeling, inventory
  control, product consistency, or quality decisions.

- End User: Agricultural quality analysts, food-processing personnel,
  automated sorting-system engineers, and computer-vision researchers.

- Documentation URL:
  https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

- Download URL:
  https://archive.ics.uci.edu/static/public/602/data.csv

### Important Interpretation Note

The dataset contains numerical features extracted from previously segmented
bean images. Therefore, the experiment evaluates classification using
image-derived measurements rather than directly processing the original
images.

### Potential Leakage Risk

No direct target-leakage variable is evident from the dataset documentation.
However, derived and highly correlated geometric variables must be audited
before modeling to determine whether they provide redundant information.

---

## Candidate Comparison

| Criterion | Candidate A: Diabetic Retinopathy Debrecen | Candidate B: Dry Bean |
|---|---|---|
| Source | UCI Machine Learning Repository; features derived from the Messidor retinal image set | UCI Machine Learning Repository; images collected through a computer-vision system |
| Authors | Bálint Antal and András Hajdu | Murat Koklu and Ilker Ali Özkan |
| Donation Date | November 2014 | September 2020 |
| License | Not explicitly displayed in the available UCI metadata; reuse conditions must be verified before redistribution | Not explicitly displayed in the available UCI metadata; reuse conditions must be verified before redistribution |
| Rows / Columns | 1,151 rows; 19 predictors and 1 target | 13,611 rows; 16 predictors and 1 target |
| Target and Classes | Binary target: `0` = no signs of diabetic retinopathy; `1` = signs of diabetic retinopathy | Multiclass target with 7 varieties: Seker, Barbunya, Bombay, Cali, Dermosan, Horoz, and Sira |
| Missing Values | None reported | None reported |
| Leakage Risk | Moderate: `pre_screening` and `am_fm_classification` may contain information closely associated with the target | Low preliminarily: no direct target copy is evident, but derived and correlated geometric features require auditing |
| Feature Types | Binary, integer, and continuous numerical features | Integer and continuous numerical features |
| SVM Compatibility | High; predictors are numerical and the target is binary | High; predictors are numerical and the target is naturally multiclass |
| Colab Compatibility | High; small dataset with low expected computational cost | High; moderate-sized dataset compatible with Colab CPU |
| Data Dictionary | Available in the UCI variables table | Available in the UCI variables table |
| Final Selection | Pending comparison and final justification | Pending comparison and final justification |

---

## Acceptance Criteria

| Acceptance Criterion | Candidate A | Candidate B |
|---|---|---|
| At least 500 observations | Accepted: 1,151 | Accepted: 13,611 |
| Observable target | Accepted | Accepted |
| At least two target classes | Accepted: 2 classes | Accepted: 7 classes |
| Documented public source | Accepted | Accepted |
| Academic use conditions reviewed | Pending explicit license verification | Pending explicit license verification |
| Variables available at prediction time | Requires audit of previous screening variables | Accepted preliminarily |
| Compatible with free Colab resources | Accepted | Accepted |
| No missing-value treatment required | Accepted | Accepted |
| Not selected by another student | Pending confirmation | Pending confirmation |

---

## Preliminary Assessment

Both datasets satisfy the principal technical acceptance criteria for LAB02.
They contain more than 500 observations, documented target variables, at least
two classes, numerical predictors, no reported missing values, and manageable
file sizes for Google Colab.

Candidate A offers a binary medical-image classification problem with a
meaningful false-negative cost. However, variables containing previous
screening and automated-classification results require a careful leakage audit.

Candidate B offers a larger multiclass classification problem with exclusively
numerical predictors and a lower preliminary leakage risk. It provides a
natural opportunity to adapt the LAB01 binary SVM pipeline to multiclass
classification and compare predictive performance with computational cost.

The final dataset selection will be documented after the candidate review.
