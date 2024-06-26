import json
from pathlib import Path

BASE_PATH = Path.cwd() / "data"


def _read_json(file_name: str) -> dict:
    if not file_name.endswith(".json"):
        file_name += ".json"
    file_path = BASE_PATH / file_name
    with open(file_path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def get_schema_from_template(schema_path: str) -> dict:
    return _read_json(schema_path)
