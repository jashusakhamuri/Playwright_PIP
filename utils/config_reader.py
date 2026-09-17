import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)

    return config