# ==============================================================================
# CELL 10: CREATE THE REUSABLE SVM MODEL MODULE
#
# Objective:
# 1. Create the src/models.py module to store the reusable
#    function responsible for building the SVM classification pipeline.
# 2. Integrate StandardScaler and SVC into a leakage-safe pipeline and
#    validate that the regularization parameter C is greater than zero.
# ==============================================================================

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def build_svm(C=1.0, gamma="scale"):
    if C <= 0:
        raise ValueError("C debe ser positivo")
    return Pipeline([
        ("scale", StandardScaler()),
        ("model", SVC(C=C, gamma=gamma, kernel="rbf", probability=True, random_state=42))
    ])
