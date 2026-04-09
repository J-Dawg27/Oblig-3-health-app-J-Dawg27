import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from health_app.health import Health




def test_valid_health_creation():
    h = Health("Alice", 60, 1.7)
    assert h.bmi == pytest.approx(20.76, 0.01)
    assert h.category == "Normal"


def test_invalid_input():
    with pytest.raises(ValueError):
        Health("", 60, 1.7)
    with pytest.raises(ValueError):
        Health("Bob", -5, 1.7)


def test_bmi_categorization():
    assert Health("A", 45, 1.8).category == "Underweight"
    assert Health("B", 65, 1.7).category == "Normal"
    assert Health("C", 80, 1.7).category == "Overweight"
    assert Health("D", 100, 1.7).category == "Obese"


def test_ideal_weight():
    h = Health("Eve", 60, 1.7)
    assert h.get_ideal_weight() == pytest.approx(63.6, 0.1)
