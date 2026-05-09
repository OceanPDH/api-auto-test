import os
import yaml


def load_yaml(filename):
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    filepath = os.path.join(data_dir, filename)
    with open(filepath, "r") as f:
        return yaml.safe_load(f)
    