# Exercise 02: Ensembles, Dimensionality Reduction, and Green AI

## INF-8239 · Data Science II

### Unit 01: Advanced Models, Dimensionality Reduction, and Green AI

---

# Overview

This project extends the supervised classification workflow established in
Exercise 01 by incorporating ensemble learning, dimensionality reduction,
computational-cost benchmarking, and Green AI decision-making.

The objective is to compare multiple classification approaches using the same
dataset, target definition, leakage controls, train-test partition, and
evaluation protocol established in U01.LAB02.

The project evaluates predictive performance and computational efficiency to
identify models that provide the best trade-off between accuracy and cost.

---

# Experimental Question

> Which classification model provides the best trade-off between predictive
> performance and computational cost for detecting signs of diabetic
> retinopathy?

---

# Dataset

## Diabetic Retinopathy Debrecen

- Repository: UCI Machine Learning Repository
- Dataset ID: `329`
- Instances: `1,151`
- Original Predictors: `19`
- Target Variable: `Class`
- Task: Binary Classification

The same dataset used in Exercise 01 is reused to ensure a fair and
reproducible comparison.

---

# Frozen Evaluation Protocol

The following configuration remains unchanged from Exercise 01:

- Dataset: Diabetic Retinopathy Debrecen
- Target: `Class`
- Test Size: `20%`
- Random State: `42`
- Stratification: Enabled
- Primary Metric: F1-Macro
- Priority Class: Positive Class (`1`)
- Most Costly Error: False Negative

The following variables are excluded because they may introduce target
leakage:

```text
pre_screening
am_fm_classification
```

After these exclusions, the experiment uses:

```text
17 predictors
```

The train-test split remains identical to Exercise 01:

```text
Training predictors: (920, 17)
Test predictors:     (231, 17)
Training target:     (920,)
Test target:         (231,)
```

---

# Models Evaluated

The experiment compares six configurations.

| Model | Description |
|---------|-------------|
| logistic | Logistic Regression |
| svm_c1 | Support Vector Machine (C = 1) |
| svm_c10 | Support Vector Machine (C = 10) |
| rf_100 | Random Forest (100 trees) |
| rf_300 | Random Forest (300 trees) |
| boost | Histogram Gradient Boosting |

All models use the same preprocessing workflow and training-test partition.

---

# Preprocessing

Preprocessing remains consistent with Exercise 01 and is fully contained inside
Scikit-learn pipelines.

## Numerical Variables

```text
SimpleImputer(strategy="median")
                    ↓
StandardScaler()
```

## Categorical Variables

```text
SimpleImputer(strategy="most_frequent")
                    ↓
OneHotEncoder(handle_unknown="ignore")
```

This approach prevents training information from leaking into validation or
test data.

---

# PCA Evaluation

Principal Component Analysis (PCA) is evaluated to determine whether a
lower-dimensional representation can preserve predictive performance while
reducing computational cost.

The PCA experiment uses:

```python
PCA(n_components=0.95)
```

The number of retained components is reported and compared against the
equivalent non-PCA baseline.

The objective is to evaluate whether dimensionality reduction improves
efficiency without substantially degrading predictive performance.

---

# t-SNE Visualization

Two independent t-SNE projections are generated using different random seeds:

```text
Seed 42
Seed 7
```

The visualizations are used to explore class structure and embedding stability.

t-SNE is used only for exploratory analysis and does not constitute evidence
of predictive validity.

Generated figure:

```text
reports/tsne_two_seeds.png
```

---

# Green AI Methodology

Computational cost is evaluated through repeated measurements.

For every model:

1. Training is executed three times.
2. Median training time is recorded.
3. Prediction time is measured.
4. Serialized model size is calculated.

The following metrics are computed:

```text
F1-Macro
Recall-Macro
Median Training Time
Prediction Time
Serialized Model Size
```

The measurements are used as computational proxies and must not be interpreted
as direct measurements of energy consumption or carbon emissions.

---

# Pareto Frontier

A Pareto analysis is performed using:

```text
Performance = F1-Macro
Cost = Median Training Time
```

A model belongs to the Pareto frontier when no other model achieves:

- Equal or better F1-Macro
- Equal or lower training cost

while improving at least one of those dimensions.

Generated outputs:

```text
reports/green_ai_results.csv
reports/pareto.png
```

The Pareto frontier supports selecting models that balance predictive
performance and computational efficiency.

---

# Environment Registration

The notebook records:

```text
Python Version
Operating System
Processor Information
Scikit-learn Version
```

Execution times are hardware dependent and must be interpreted within the
context of the execution environment.

---

# Repository Structure

```text
Exercise_02_Model_Evaluation/
├── notebooks/
│   └── U01.LAB03.ipynb
├── reports/
│   ├── green_ai_results.csv
│   ├── pareto.png
│   ├── tsne_two_seeds.png
│   └── models/
│       ├── logistic.joblib
│       ├── svm_c1.joblib
│       ├── svm_c10.joblib
│       ├── rf_100.joblib
│       ├── rf_300.joblib
│       └── boost.joblib
├── src/
├── tests/
│   └── test_green.py
├── README.md
└── requirements.txt
```

---

# Reproduction Instructions

## Clone the Repository

```bash
git clone https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git
```

## Enter the Exercise Directory

```bash
cd INF-8239-Ciencia-de-Datos-II/Unit_01_Advanced_Data_Analysis/Exercise_02_Model_Evaluation
```

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Execute the Notebook

Open:

```text
notebooks/U01.LAB03.ipynb
```

Execute all notebook cells in order.

The notebook will:

1. Reuse the Exercise 01 dataset and protocol.
2. Train six classification models.
3. Measure fitting and inference costs.
4. Evaluate PCA.
5. Generate two t-SNE visualizations.
6. Compute the Pareto frontier.
7. Export Green AI results.
8. Execute the automated tests.

---

# Automated Tests

The project includes tests for Pareto-frontier validation.

Run:

```bash
python -m pytest tests/test_green.py -v
```

Expected result:

```text
2 passed
```

The tests verify:

1. Correct identification of dominated models.
2. Correct behavior when a single model is evaluated.

---

# Deliverables

The project generates:

```text
reports/green_ai_results.csv
reports/pareto.png
reports/tsne_two_seeds.png
reports/models/*.joblib
```

These files provide:

- Predictive performance comparisons.
- Computational-cost measurements.
- Dimensionality-reduction evidence.
- Pareto-frontier analysis.
- Green AI decision support.

---

# Expected Outcome

The final analysis will identify:

1. The highest-performing model.
2. The Pareto-optimal configurations.
3. The selected Green AI alternative.
4. The absolute F1 difference from the best model.
5. The estimated computational savings.
6. The trade-off between performance and cost.

The final recommendation must consider both predictive quality and
computational efficiency rather than predictive performance alone.

---

# Reproducibility Checklist

A reproduction is considered successful when another user can:

- [ ] Clone the public repository.
- [ ] Install the required dependencies.
- [ ] Recreate the Exercise 01 data partition.
- [ ] Train all six model configurations.
- [ ] Generate the PCA experiment.
- [ ] Generate both t-SNE visualizations.
- [ ] Measure training and inference times.
- [ ] Export the serialized models.
- [ ] Generate `green_ai_results.csv`.
- [ ] Generate the Pareto frontier figure.
- [ ] Execute `test_green.py`.
- [ ] Obtain consistent rankings and metrics.

---

# Academic Use Disclaimer

This project is intended exclusively for academic experimentation.

The resulting models do not constitute a medical diagnosis and must not replace
evaluation by a qualified healthcare professional.
