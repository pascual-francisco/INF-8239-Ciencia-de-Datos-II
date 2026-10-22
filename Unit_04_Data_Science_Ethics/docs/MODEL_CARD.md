
# Model Card

## Model Name

Territorial Review DSS - Synthetic

## Purpose

Decision Support System (DSS) diseñado para priorizar casos sintéticos para revisión humana.

El sistema asiste la toma de decisiones, pero no reemplaza la autoridad humana.

## Intended Users

- Product Owner
- Data Scientist
- ML Engineer
- Analistas responsables de revisión

## Prohibited Uses

- Automatic intervention
- Eligibility decision
- Emergency declaration

## Dataset

Dataset sintético: territorial_risk_synthetic.csv

Distribución objetivo:

- Positivos: 55.2 %
- Negativos: 44.8 %

Grupos protegidos:

- G1: 396 observaciones
- G2: 244 observaciones

## Model Selected

Logistic Regression

## Global Metrics

- Accuracy: 0.719
- Recall: 0.717
- Precision: 0.776
- FPR: 0.279

## Fairness Assessment

### G1

- Accuracy: 0.703
- Recall: 0.653
- FPR: 0.250
- Selection Rate: 0.446

### G2

- Accuracy: 0.746
- Recall: 0.791
- FPR: 0.375
- Selection Rate: 0.678

Las diferencias observadas requieren monitoreo continuo, pero no constituyen evidencia suficiente de discriminación causal.

## Green AI

Logistic Regression:

- Training time: 0.044 s
- Model size: 3.56 KB

Decision Tree:

- Training time: 0.040 s
- Model size: 7.90 KB

La complejidad adicional del árbol no produjo mejoras significativas.

## Risks Identified

- Clasificación incorrecta de territorios.
- Sesgo sistemático.
- Dependencia excesiva de automatización.

## Governance Decision

Resultado final:

GO

Todas las puertas de desempeño, equidad, latencia y tamaño fueron aprobadas.

## Human Oversight

Las recomendaciones del sistema deben ser revisadas y aprobadas por una persona responsable antes de cualquier acción.
