import pytest
from datetime import datetime, timedelta
from solution.solution import *

def test_compute_percentage():
    assert compute_percentage() == {
    '09:00': -30.0,
    '10:00': 38.2,
    '11:00': 15.6,
    '12:00': 12.4,
    '13:00': 18.2,
    '14:00': 41.6,
    '15:00': 69.4,
    '16:00': 35.4,
    '17:00': 37.9,
    '18:00': 8.0,
    '19:00': 15.7,
    '20:00': -66.0,
    '21:00': 27.4,
    '22:00': -59.0,
    }
