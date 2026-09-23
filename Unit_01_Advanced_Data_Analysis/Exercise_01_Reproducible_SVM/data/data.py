# ==============================================================================
# REPRODUCIBLE DATA ACCESS
#
# Objective:
# 1. Support reproducible downloads from direct public CSV URLs.
# 2. Support reproducible access through the official UCI API.
# 3. Validate that downloaded datasets contain observations.
# 4. Save a standardized CSV copy inside the project data directory.
# ==============================================================================

from pathlib import Path

import pandas as pd


def download_csv(
    url: str,
    destination: str = "data/raw/dataset.csv"
) -> Path:
    """Download a public CSV file and save a reproducible local copy."""

    if not url.startswith(("https://", "http://")):
        raise ValueError("The source must be an HTTP(S) URL")

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)

    frame = pd.read_csv(url)

    if frame.empty:
        raise ValueError("The downloaded dataset is empty")

    frame.to_csv(path, index=False)

    return path


def download_uci_dataset(
    dataset_id: int,
    destination: str = "data/raw/dataset.csv"
) -> Path:
    """Download a UCI dataset through the official API and save it as CSV."""

    if dataset_id <= 0:
        raise ValueError("The UCI dataset ID must be positive")

    try:
        from ucimlrepo import fetch_ucirepo
    except ImportError as error:
        raise ImportError(
            "The ucimlrepo package is required. "
            "Install it with: pip install ucimlrepo"
        ) from error

    dataset = fetch_ucirepo(id=dataset_id)

    features = dataset.data.features.copy()
    targets = dataset.data.targets.copy()

    if isinstance(targets, pd.Series):
        targets = targets.to_frame()

    frame = pd.concat(
        [features, targets],
        axis=1
    )

    if frame.empty:
        raise ValueError("The downloaded UCI dataset is empty")

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)

    frame.to_csv(path, index=False)

    return path