import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent

def load_status_codes():
    with open(f"{base_dir}/status.json", "r") as json_file:
        data = json.load(json_file)
    return data
