import json
from pathlib import Path
from collections import Counter

from .health import Health


FILE = Path("data/health_records.json")

def load_data():

    if not FILE.exists():
        return []

    with open(FILE) as f:
        return json.load(f)


def save_data(record):

    data = load_data()

    data.append(record)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def save_records(records):

    data = [
        {
            "name": h.name,
            "weight_kg": h.weight_kg,
            "height_m": h.height_m,
            "bmi": h.bmi,
            "category": h.category,
        }
        for h in records
    ]

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_records():

    if not FILE.exists():
        return []

    with open(FILE) as f:
        records = json.load(f)

    return [
        Health(
            r["name"],
            r["weight_kg"],
            r["height_m"]
        )
        for r in records
    ]

def get_statistics(filename: str = "data/health_records.json"):

    path = Path(filename)

    if not path.exists():
        return {
            "total_records": 0,
            "avg_bmi": 0,
            "most_common_category": None,
            "category_distribution": {},
        }

    with open(path) as f:
        data = json.load(f)

    bmis = [item["bmi"] for item in data]
    categories = [item["category"] for item in data]

    avg_bmi = round(sum(bmis) / len(bmis), 2)

    count = Counter(categories)

    most_common = count.most_common(1)[0][0]

    return {
        "total_records": len(data),
        "avg_bmi": avg_bmi,
        "most_common_category": most_common,
        "category_distribution": dict(count),
    }
