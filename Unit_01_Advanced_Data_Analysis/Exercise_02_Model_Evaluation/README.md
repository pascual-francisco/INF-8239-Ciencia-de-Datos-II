# Exercise 02: Ensembles, Dimensionality Reduction, and Green AI

## INF-8239 · Data Science II

### Unit 01: Advanced Models, Dimensionality Reduction, and Green AI

---

# Overview

This project extends the supervised-classification workflow established in
Exercise 01 by incorporating ensemble models, dimensionality reduction,
computational-cost analysis, and Green AI decision-making.

The objective is to compare multiple classification approaches using the same
dataset, target definition, leakage controls, train-test partition, and
evaluation protocol established in U01.LAB02.

The analysis includes:

- Logistic Regression
- Support Vector Machines
- Random Forest
- Histogram Gradient Boosting
- Principal Component Analysis (PCA)
- t-SNE visualization
- Repeated timing measurements
- Serialized model-size analysis
- Pareto-frontier selection
- Green AI decision support

---

# Experimental Question

Which classification model provides the best trade-off between predictive
performance and computational cost for detecting signs of diabetic
retinopathy?

---

# Dataset

## Diabetic Retinopathy Debrecen

- Repository: UCI Machine Learning Repository
- Dataset ID: 329
- Instances: 1,151
- Original Predictors: 19
- Target Variable: `Class`
- Task: Binary Classification

The dataset is the same dataset used in Exercise 01 to ensure a fair and
reproducible comparison.

---

# Frozen Evaluation Protocol

The following configuration remains unchanged from Exercise 01:

- Dataset: Diabetic Retinopathy Debrecen
- Target: `Class`
- Test Size: 20%
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
