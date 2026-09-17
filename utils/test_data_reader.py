import yaml
from pathlib import Path


# Project root folder
PROJECT_ROOT = Path(__file__).parent.parent

# Test data file path
TEST_DATA_PATH = (
    PROJECT_ROOT / "test_data" / "test_data.yaml"
)


def load_test_data():

    with open(TEST_DATA_PATH, "r") as file:
        test_data = yaml.safe_load(file)

    return test_data