# ==============================================================================
# SCRIPT — AUDIT THE CONFIGURED TEXT DATASET
# Objective: Load the dataset configured in .env and report its file hash,
# dimensions, missing values, empty texts, duplicates, class distribution,
# and text-length statistics.
# ==============================================================================

from __future__ import annotations

# Import the centralized project configuration.
from src.config import settings

# Import the reusable data-loading and validation functions.
from src.data import load_dataset, sha256, validate_dataframe


def main() -> None:
    """Execute the complete dataset audit."""

    # Load the dataset configured through DATASET_PATH in the .env file.
    df = load_dataset()

    # Validate the required columns and reject empty text observations.
    validate_dataframe(
        df,
        settings.text_column,
        settings.target_column
    )

    # Select the original text column.
    original_text = df[settings.text_column]

    # Create a normalized text version for auditing.
    clean_text = (
        original_text
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Count missing values in the required columns.
    missing_values = df[
        [
            settings.text_column,
            settings.target_column
        ]
    ].isna().sum()

    # Count empty or whitespace-only texts.
    empty_text_count = clean_text.eq("").sum()

    # Count additional occurrences of duplicated texts.
    duplicate_text_count = clean_text.duplicated().sum()

    # Count the number of available target classes.
    number_of_classes = df[
        settings.target_column
    ].nunique(
        dropna=True
    )

    # Calculate the number of observations in each class.
    class_counts = df[
        settings.target_column
    ].value_counts(
        dropna=False
    )

    # Calculate the proportion of observations in each class.
    class_proportions = df[
        settings.target_column
    ].value_counts(
        dropna=False,
        normalize=True
    )

    # Calculate text lengths in characters.
    text_lengths = clean_text.str.len()

    # Calculate descriptive statistics, including p50, p90, and p99.
    text_length_summary = text_lengths.describe(
        percentiles=[0.50, 0.90, 0.99]
    )

    # Display the configured dataset and its SHA-256 hash.
    print("=" * 70)
    print("DATASET FILE")
    print("=" * 70)
    print(f"Path: {settings.dataset_path}")
    print(f"SHA-256: {sha256(settings.dataset_path)}")

    # Display the dataset dimensions and columns.
    print("\n" + "=" * 70)
    print("DATASET STRUCTURE")
    print("=" * 70)
    print(f"Rows: {df.shape,}")
    print(f"Columns: {df.shape,}")
    print(f"Column names: {df.columns.tolist()}")

    # Display missing and empty values.
    print("\n" + "=" * 70)
    print("MISSING AND EMPTY VALUES")
    print("=" * 70)
    print(missing_values.to_string())
    print(f"\nEmpty or whitespace-only texts: {empty_text_count:,}")

    # Display duplicated text observations.
    print("\n" + "=" * 70)
    print("DUPLICATES")
    print("=" * 70)
    print(f"Duplicated text occurrences: {duplicate_text_count:,}")

    # Display the absolute class frequencies.
    print("\n" + "=" * 70)
    print("CLASS COUNTS")
    print("=" * 70)
    print(class_counts.to_string())

    # Display the relative class frequencies.
    print("\n" + "=" * 70)
    print("CLASS PROPORTIONS")
    print("=" * 70)
    print(class_proportions.round(4).to_string())

    # Display text-length statistics.
    print("\n" + "=" * 70)
    print("TEXT LENGTHS IN CHARACTERS")
    print("=" * 70)
    print(text_length_summary.to_string())

    # Create a list for problems that require stopping before training.
    stop_conditions = []

    # Stop when required columns contain missing values.
    if missing_values.sum() > 0:
        stop_conditions.append(
            "Missing values were detected in the required columns."
        )

    # Stop when the dataset contains empty texts.
    if empty_text_count > 0:
        stop_conditions.append(
            f"{empty_text_count:,} empty texts were detected."
        )

    # Stop when fewer than two target classes are available.
    if number_of_classes < 2:
        stop_conditions.append(
            "The dataset contains fewer than two target classes."
        )

    # Display the automated training decision.
    print("\n" + "=" * 70)
    print("AUDIT DECISION")
    print("=" * 70)

    if stop_conditions:
        print("STOP BEFORE TRAINING.")

        for condition in stop_conditions:
            print(f"- {condition}")
    else:
        print(
            "The dataset satisfies the programmed minimum requirements "
            "for model training."
        )

    # Display a duplicate warning separately.
    if duplicate_text_count > 0:
        print(
            "\nWarning: duplicated texts were detected. Verify that the "
            "same text does not appear in both training and test data."
        )


# Execute the audit only when this file is run directly.
if __name__ == "__main__":
    main()
