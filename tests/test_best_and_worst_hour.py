import pytest
from solution.solution import *
from pytest_fixtures import *

example_1 = {
    "18:00": -10.0,
    "19:00": 777.78,
    "20:00": -20,
    "21:00": 174.5,
}

example_2 = {
    "11:00": 0.0,
    "13:00": 10000.0,
    "14:00": 1.0,
    "23:00": 1.0,
}

def test_best_and_worst_hour():
    assert best_and_worst_hour(example_1) == ["19:00", "20:00"]

def test_best_and_worst_hour():
    assert best_and_worst_hour(example_2) == ["13:00", "11:00"]
