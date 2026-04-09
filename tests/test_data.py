import json
from pathlib import Path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from health_app import data
from health_app.health import Health


def test_save_load_roundtrip(tmp_path):
    file = tmp_path / "records.json"
    data.FILE = file
    h = Health("Alice", 60, 1.7)
    data.save_records([h])
    loaded = data.load_records()
    assert len(loaded) == 1
    assert loaded[0].name == "Alice"


def test_get_statistics(tmp_path):
    file = tmp_path / "records.json"
    sample = [
        {"name": "A", "weight_kg": 50, "height_m": 1.6, "bmi": 19.53, "category": "Normal"},
        {"name": "B", "weight_kg": 100, "height_m": 1.7, "bmi": 34.6, "category": "Obese"},
    ]
    with open(file, "w") as f:
        json.dump(sample, f)
    stats = data.get_statistics(str(file))
    assert stats["total_records"] == 2
    assert stats["avg_bmi"] == round((19.53 + 34.6) / 2, 2)
    assert "Normal" in stats["category_distribution"]
