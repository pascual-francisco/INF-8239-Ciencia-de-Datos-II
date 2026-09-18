"""Environment and dependency verification test suite."""
import importlib
import pytest

REQUIRED_MODULES = [
    "numpy",
    "pandas",
    "sklearn",
    "matplotlib",
    "seaborn",
    "joblib",
    "pytest",
]

@pytest.mark.parametrize("module_name", REQUIRED_MODULES)
def test_required_modules_importable(module_name):
    """Ensure all core packages are importable."""
    module = importlib.import_module(module_name)
    assert module is not None
