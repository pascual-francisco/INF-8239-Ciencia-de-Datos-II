# ==============================================================================
# MODULE — PROJECT CONFIGURATION
# Objective: Load the local environment variables and provide a centralized
# configuration object for the NLP sentiment-analysis project.
# ==============================================================================

from __future__ import annotations

# Import os to read environment variables.
import os

# Import dataclass to define an immutable configuration object.
from dataclasses import dataclass

# Import Path for operating-system-independent path management.
from pathlib import Path

# Import load_dotenv to load variables from the local .env file.
from dotenv import load_dotenv


# Define the project root directory.
# config.py is located directly inside the src directory:
# nlp_sentiment_analysis/src/config.py
ROOT = Path(__file__).resolve().parents[1]

# Define the path to the local environment configuration file.
ENV_PATH = ROOT / ".env"

# Load the environment variables defined in the local .env file.
load_dotenv(ENV_PATH)


@dataclass(frozen=True)
class Settings:
    """Store the project configuration as an immutable object."""

    # Define whether the dataset comes from a local file or public URL.
    data_source: str = os.getenv(
        "DATA_SOURCE",
        "local"
    )

    # Build the complete dataset path from the project root and the
    # relative path configured in the .env file.
    dataset_path: Path = ROOT / os.getenv(
        "DATASET_PATH",
        "data/sample/demo_text.csv"
    )

    # Store the public dataset URL when DATA_SOURCE is configured as url.
    dataset_url: str = os.getenv(
        "DATASET_URL",
        ""
    )

    # Define the column containing the input text.
    text_column: str = os.getenv(
        "TEXT_COLUMN",
        "text"
    )

    # Define the column containing the target labels.
    target_column: str = os.getenv(
        "TARGET_COLUMN",
        "label"
    )

    # Define a fixed random seed to support reproducible results.
    random_state: int = int(
        os.getenv(
            "RANDOM_STATE",
            "42"
        )
    )


# Create the centralized project configuration object.
settings = Settings()