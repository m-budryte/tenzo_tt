import pytest
from datetime import datetime, timedelta
from solution.solution import *
from pytest_fixtures import *

def test_process_sales():
    assert process_sales('transactions.csv') == {
    '10:00': 130.88,
    '11:00': 320.65,
    '12:00': 514.65,
    '13:00': 406.08,
    '14:00': 177.77,
    '15:00': 63.43,
    '16:00': 75.42,
    '17:00': 142.34,
    '18:00': 748.62,
    '19:00': 421.08,
    '21:00': 240.54,
    }
