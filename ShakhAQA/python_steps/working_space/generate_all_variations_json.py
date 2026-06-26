import json
import os
from itertools import product
from copy import deepcopy

# ==== SETTINGS ====

BASE_PAYLOAD = {
    "p_system_id": "11111111111",
    "p_token": "111111111111",
    "p_query_id": 1111111,
    "p_request_id": "x1",
    "p_lang": "11111",
    "p_data": {
        "DATE": "01.01.11111",
        "CL": "11111000000111111111",
        "CO": "11111000000111111113",
        "NAME": "test",
        "BANK": "11111",
        "SUMMA": 10000,
        "DOC": "111111",
        "PURPOSE": "Test"
    }
}

ALLOWED_VALUES = {
    "INN": [777777777, 32167777777777],
    "PURPOSE": [11112, 11111],
    "TYPE": [0o1, 0o2, 112, 111, 11],
    "TYPE_P": [0, 1],
    "P": [3, 2, 1, 11]

}

PARENT_KEY = "p_data"
OUT_DIR = r"D:\PythonTraining"  # change destination here
PRETTY = True

# ==== LOGIC ====

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def generate_combinations(allowed_values: dict):
    keys = list(allowed_values.keys())
    domains = [allowed_values[k] for k in keys]
    for values in product(*domains):
        yield dict(zip(keys, values))

def sanitize(value):
    """Make value safe for filenames (replace spaces, special chars)."""
    return str(value).replace(" ", "_").replace("/", "-").replace("\\", "-")

def build_filename(combo: dict):
    parts = [f"{key}_{sanitize(value)}" for key, value in combo.items()]
    return " - ".join(parts) + ".json"

def write_json(path: str, data: dict, pretty: bool = True):
    with open(path, "w", encoding="utf-8") as f:
        if pretty:
            json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

def main():
    ensure_dir(OUT_DIR)

    total = 0
    for combo in generate_combinations(ALLOWED_VALUES):
        payload = deepcopy(BASE_PAYLOAD)
        payload.setdefault(PARENT_KEY, {})
        for k, v in combo.items():
            payload[PARENT_KEY][k] = v

        filename = build_filename(combo)
        out_path = os.path.join(OUT_DIR, filename)
        write_json(out_path, payload, PRETTY)
        total += 1

    print(f"Created {total} JSON files in: {os.path.abspath(OUT_DIR)}")

if __name__ == "__main__":
    main()