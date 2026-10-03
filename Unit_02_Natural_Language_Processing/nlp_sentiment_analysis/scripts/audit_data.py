# ==============================================================================
# SCRIPT — AUDIT THE CONFIGURED DATASET
# Objective: Load and validate the configured dataset and report its SHA-256
# hash, dimensions, missing values, duplicates, class distribution, and
# text-length statistics.
# ==============================================================================

from __future__ import annotations

# Import the project settings from src/config.py.
from src.config import settings

# Import the dataset utilities from src/data.py.
from src.data import load_dataset, sha256, validate_dataframe


def main() -> None:
    """Execute the complete dataset audit."""

    # Load the dataset configured in the local .env file.
    df = load_dataset()

    # Validate that the configured text and target columns exist.
    validate_dataframe(
        df,
        settings.text_column,
        settings.target_column
    )

    # Convert the text column to strings for duplicate and length analysis.
    text = df[settings.text_column].astype(str)

    # Display the configured dataset path.
    print("Ruta:", settings.dataset_path)

    # Calculate and display the SHA-256 hash of the dataset file.
    print("SHA-256:", sha256(settings.dataset_path))

    # Display the number of rows and columns.
    print("Filas y columnas:", df.shape)

    # Display missing values in the text and target columns.
    print(
        "Nulos:\n",
        df[
            [
                settings.text_column,
                settings.target_column
            ]
        ].isna().sum()
    )

    # Display the number of duplicated text observations.
    print(
        "Duplicados de texto:",
        text.duplicated().sum()
    )

    # Display the relative distribution of the target classes.
    print(
        "Distribución:\n",
        df[settings.target_column].value_counts(
            dropna=False,
            normalize=True
        )
    )

    # Display descriptive statistics for text lengths.
    # The output includes p50, p90, and p99.
    print(
        "Longitud de textos:\n",
        text.str.len().describe(
            percentiles=[0.50, 0.90, 0.99]
        )
    )


# Execute the audit only when this file is run directly.
if __name__ == "__main__":
    main()