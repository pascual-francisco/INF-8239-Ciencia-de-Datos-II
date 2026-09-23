# ==============================================================================
# DATASET CONTRACT TESTS
#
# Objective:
# 1. Verify that the dataset contains observations.
# 2. Confirm that the target and required predictor columns exist.
# 3. Verify that the target contains no missing values.
# 4. Confirm that the target contains at least two classes.
# ==============================================================================

import pandas as pd


TARGET = "Class"

REQUIRED = {
    TARGET,
    "quality",
    "ma1"
}


def load_data():
    """Load the reproducible dataset from the project data directory."""

    return pd.read_csv("data/raw/dataset.csv")


def test_dataset_is_not_empty():
    """Verify that the dataset contains observations."""

    assert not load_data().empty


def test_required_columns_exist():
    """Verify that the required dataset columns exist."""

    assert REQUIRED <= set(load_data().columns)


def test_target_has_no_missing_and_two_classes():
    """Verify that the target is complete and contains at least two classes."""

    y = load_data()[TARGET]

    assert y.notna().all()
    assert y.nunique() >= 2